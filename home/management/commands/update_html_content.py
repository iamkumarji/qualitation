"""
Django management command to directly update HTML content in streamfield blocks
"""

from django.core.management.base import BaseCommand
from home.models import FlexiblePage, HomePage


class Command(BaseCommand):
    help = 'Update HTML content directly in streamfield blocks'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('\n=== Updating HTML Content in Pages ===\n'))

        # Define all replacements
        self.replacements = [
            ('20+ Years Experience', '25+ Years Experience'),
            ('20+ years', '25+ years'),
            ('over 20 years', 'over 25 years'),
            ('more than 20 years', 'more than 25 years'),
            ('98%', '100%'),
            ('98% success rate', '100% first-time certification success'),
            ('UKAS accredited', 'Over 25 years of 100% first time certification success'),
            ('UKAS-accredited certification support', 'Over 25 years of 100% first time certifications success!'),
            ('Government contracts', 'Government tender processes'),
            ('government contracts', 'government tender processes'),
        ]

        total_updated = 0

        # Update all FlexiblePages
        for page in FlexiblePage.objects.all():
            if self.update_page_html(page):
                total_updated += 1
                self.stdout.write(f'  ✓ Updated: {page.title}')

        # Update HomePage
        try:
            homepage = HomePage.objects.first()
            if homepage and self.update_page_html(homepage):
                total_updated += 1
                self.stdout.write(f'  ✓ Updated: Home Page')
        except Exception as e:
            self.stdout.write(f'  ! Error updating homepage: {e}')

        self.stdout.write(self.style.SUCCESS(f'\n=== Total Pages Updated: {total_updated} ===\n'))

    def update_page_html(self, page):
        """Update HTML content in all blocks of a page"""
        updated = False

        if not page.body:
            return updated

        for i, block in enumerate(page.body):
            if block.block_type == 'html':
                # Get the HTML content
                html_content = block.value.get('html', '')
                if not html_content:
                    continue

                # Convert to string if it's not already
                html_str = str(html_content)
                original_html = html_str

                # Apply all replacements
                for old_text, new_text in self.replacements:
                    html_str = html_str.replace(old_text, new_text)

                # If content changed, update it
                if html_str != original_html:
                    page.body[i].value['html'] = html_str
                    updated = True

            elif block.block_type == 'paragraph':
                # Update paragraph content
                content = block.value.get('content', '')
                if not content:
                    continue

                content_str = str(content)
                original_content = content_str

                for old_text, new_text in self.replacements:
                    content_str = content_str.replace(old_text, new_text)

                if content_str != original_content:
                    page.body[i].value['content'] = content_str
                    updated = True

            elif block.block_type == 'accordion':
                # Update accordion items
                items = block.value.get('items', [])
                for item in items:
                    if 'content' in item:
                        content_str = str(item['content'])
                        original = content_str
                        for old_text, new_text in self.replacements:
                            content_str = content_str.replace(old_text, new_text)
                        if content_str != original:
                            item['content'] = content_str
                            updated = True

                    if 'title' in item:
                        title_str = str(item['title'])
                        original = title_str
                        for old_text, new_text in self.replacements:
                            title_str = title_str.replace(old_text, new_text)
                        if title_str != original:
                            item['title'] = title_str
                            updated = True

        # Save and publish if updated
        if updated:
            page.save_revision().publish()

        return updated
