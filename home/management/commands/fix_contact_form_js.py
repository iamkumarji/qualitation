from django.core.management.base import BaseCommand
from wagtail.models import Page
from home.models import FlexiblePage
import json


class Command(BaseCommand):
    help = 'Fix contact form to use JavaScript for CSRF token'

    def handle(self, *args, **options):
        try:
            # Find the contact page
            contact_page = FlexiblePage.objects.filter(slug='contact').first()

            if not contact_page:
                self.stdout.write(self.style.ERROR('Contact page not found'))
                return

            # Get the body content
            body_data = contact_page.body.raw_data if hasattr(contact_page.body, 'raw_data') else contact_page.body

            # Update HTML blocks that contain forms
            updated = False
            for block in body_data:
                if block.get('type') == 'html':
                    html = block.get('value', {}).get('html', '')

                    if '<form' in html:
                        # Remove the template tag we added
                        html = html.replace('{%csrf_token %}', '').replace('{% csrf_token %}', '')

                        # Ensure correct action URL
                        html = html.replace('action="#"', 'action="/contact/submit/"')

                        # Add ID to the form if it doesn't have one
                        if 'id="contact-form"' not in html:
                            html = html.replace('<form method="post"', '<form method="post" id="contact-form"')

                        # Add script to inject CSRF token at the end
                        if '<script>' not in html or 'csrfToken' not in html:
                            csrf_script = '''
<script>
// Add CSRF token to contact form
document.addEventListener('DOMContentLoaded', function() {
    var form = document.getElementById('contact-form');
    if (form) {
        // Get CSRF token from cookie
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = cookies[i].trim();
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }

        var csrftoken = getCookie('csrftoken');

        // Create and add CSRF input
        var csrfInput = document.createElement('input');
        csrfInput.type = 'hidden';
        csrfInput.name = 'csrfmiddlewaretoken';
        csrfInput.value = csrftoken;
        form.insertBefore(csrfInput, form.firstChild);
    }
});
</script>'''
                            html += csrf_script

                        # Update the block
                        block['value']['html'] = html
                        updated = True
                        self.stdout.write(self.style.SUCCESS('Updated HTML form block with JavaScript CSRF'))

            if updated:
                # Save the page
                contact_page.body = body_data
                contact_page.save_revision().publish()
                self.stdout.write(self.style.SUCCESS('✅ Contact page updated and published!'))
                self.stdout.write(self.style.SUCCESS('The form now includes JavaScript to add CSRF token'))
            else:
                self.stdout.write(self.style.WARNING('No forms found to update'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {str(e)}'))
            import traceback
            traceback.print_exc()
