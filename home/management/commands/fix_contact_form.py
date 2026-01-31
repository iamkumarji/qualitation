from django.core.management.base import BaseCommand
from wagtail.models import Page
from home.models import FlexiblePage
import json


class Command(BaseCommand):
    help = 'Fix contact form in HTML block to include CSRF token and correct action'

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

                    if '<form' in html and 'action="#"' in html:
                        # Replace action="#" with action="/contact/submit/"
                        html = html.replace('action="#"', 'action="/contact/submit/"')

                        # Add CSRF token after <form method="post"
                        if '<form method="post"' in html and '{% csrf_token %}' not in html:
                            html = html.replace(
                                '<form method="post" action="/contact/submit/"',
                                '<form method="post" action="/contact/submit/">{% csrf_token %}'
                            )

                        # Update the block
                        block['value']['html'] = html
                        updated = True
                        self.stdout.write(self.style.SUCCESS('Updated HTML form block'))

            if updated:
                # Save the page
                contact_page.body = body_data
                contact_page.save_revision().publish()
                self.stdout.write(self.style.SUCCESS('✅ Contact page updated and published!'))
                self.stdout.write(self.style.SUCCESS('The form now has:'))
                self.stdout.write(self.style.SUCCESS('  - CSRF token'))
                self.stdout.write(self.style.SUCCESS('  - Correct action URL: /contact/submit/'))
            else:
                self.stdout.write(self.style.WARNING('No forms found to update'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {str(e)}'))
            import traceback
            traceback.print_exc()
