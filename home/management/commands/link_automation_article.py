"""
Django management command to update Resources page to link to local Automation article
"""

from django.core.management.base import BaseCommand
from django.db import connection
import json


class Command(BaseCommand):
    help = 'Update Resources page to link to local Automation article instead of external URL'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('\n=== Updating Resources Page Automation Article Link ===\n'))

        try:
            # Get the Resources page body
            with connection.cursor() as cursor:
                cursor.execute('''
                    SELECT fp.body, p.id
                    FROM home_flexiblepage fp
                    JOIN wagtailcore_page p ON fp.page_ptr_id = p.id
                    WHERE p.slug = 'resources'
                ''')
                result = cursor.fetchone()
                if not result:
                    self.stdout.write(self.style.ERROR('✗ Resources page not found'))
                    return

                body_json, page_id = result

            # Parse the JSON
            body_data = json.loads(body_json)

            # Find the HTML block containing the articles (should be first block)
            for block in body_data:
                if block['type'] == 'html':
                    html_content = block['value']['html']

                    # Replace the external link with our local article link
                    old_link = 'https://qualitation.co.uk/automation-is-the-future-for-iso-standards'
                    new_link = '/automation-is-the-future-for-iso-standards/'

                    if old_link in html_content:
                        html_content = html_content.replace(old_link, new_link)

                        # Also update target and rel attributes for internal link
                        # Remove target="_blank" and rel="noopener noreferrer" for internal links
                        html_content = html_content.replace(
                            f'<a href="{new_link}" target="_blank" rel="noopener noreferrer"',
                            f'<a href="{new_link}"'
                        )

                        block['value']['html'] = html_content

                        self.stdout.write(self.style.SUCCESS('✓ Updated Automation article link to local page'))
                        break

            # Update the database
            new_body_json = json.dumps(body_data)

            with connection.cursor() as cursor:
                cursor.execute('''
                    UPDATE home_flexiblepage
                    SET body = %s
                    WHERE page_ptr_id = %s
                ''', [new_body_json, page_id])

            # Publish the page
            from home.models import FlexiblePage
            page = FlexiblePage.objects.get(id=page_id)
            page.save_revision().publish()

            self.stdout.write(self.style.SUCCESS('✓ Resources page updated and published'))
            self.stdout.write(self.style.SUCCESS('✓ Article 2 now links to: /automation-is-the-future-for-iso-standards/'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ Error: {e}'))
            import traceback
            traceback.print_exc()

        self.stdout.write(self.style.SUCCESS('\n=== Complete ===\n'))
