from django.core.management.base import BaseCommand
from wagtail.models import Page
from home.models import FlexiblePage
from wagtail.blocks import StreamValue


class Command(BaseCommand):
    help = 'Replace HTML form with proper contact_form_block'

    def handle(self, *args, **options):
        try:
            # Find the contact page
            contact_page = FlexiblePage.objects.filter(slug='contact').first()

            if not contact_page:
                self.stdout.write(self.style.ERROR('Contact page not found'))
                return

            # Get the body content
            body_data = contact_page.body.raw_data if hasattr(contact_page.body, 'raw_data') else []

            # Remove HTML blocks with forms and add contact_form block
            new_body = []
            form_found = False

            for block in body_data:
                if block.get('type') == 'html':
                    html = block.get('value', {}).get('html', '')
                    # Keep HTML blocks that don't contain forms
                    if '<form' not in html:
                        new_body.append(block)
                    else:
                        form_found = True
                        self.stdout.write(self.style.WARNING('Removing HTML form block'))
                        # Add proper contact_form block if not already added
                        if not any(b.get('type') == 'contact_form' for b in new_body):
                            contact_form_block = {
                                'type': 'contact_form',
                                'value': {
                                    'heading': 'Get in Touch',
                                    'subheading': 'Fill out the form below and we\'ll get back to you as soon as possible.',
                                    'background_color': 'light-blue'
                                },
                                'id': 'contact-form-block'
                            }
                            new_body.append(contact_form_block)
                            self.stdout.write(self.style.SUCCESS('Added proper contact_form block'))
                else:
                    new_body.append(block)

            if form_found:
                # Save the page
                contact_page.body = new_body
                contact_page.save_revision().publish()
                self.stdout.write(self.style.SUCCESS('✅ Contact page updated and published!'))
                self.stdout.write(self.style.SUCCESS('Now using proper Wagtail contact form with CSRF protection'))
            else:
                self.stdout.write(self.style.WARNING('No HTML form blocks found'))
                # Add contact form block anyway
                if not any(b.get('type') == 'contact_form' for b in new_body):
                    contact_form_block = {
                        'type': 'contact_form',
                        'value': {
                            'heading': 'Get in Touch',
                            'subheading': 'Fill out the form below and we\'ll get back to you as soon as possible.',
                            'background_color': 'light-blue'
                        },
                        'id': 'contact-form-block'
                    }
                    new_body.append(contact_form_block)
                    contact_page.body = new_body
                    contact_page.save_revision().publish()
                    self.stdout.write(self.style.SUCCESS('✅ Added contact form block'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {str(e)}'))
            import traceback
            traceback.print_exc()
