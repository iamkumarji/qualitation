"""
Django management command to update remaining content based on search results
"""

from django.core.management.base import BaseCommand
from home.models import FlexiblePage, HomePage


class Command(BaseCommand):
    help = 'Update remaining content that was missed in first pass'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('\n=== Updating Remaining Content ===\n'))

        self.update_about_us()
        self.update_faq_page()
        self.update_iso_17020()
        self.update_iso_17025()
        self.update_iso_20000()
        self.update_iso_37301()
        self.update_cyber_essentials()
        self.update_all_pages_comprehensive()

        self.stdout.write(self.style.SUCCESS('\n=== All Updates Complete ===\n'))

    def replace_in_streamfield(self, page, old_text, new_text, case_sensitive=False):
        """Replace text in all streamfield blocks"""
        updated = False

        if not page.body:
            return updated

        for i, block in enumerate(page.body):
            block_data = dict(block.value)

            # Convert all values to strings and check/replace
            for key, value in block_data.items():
                if isinstance(value, (str, type(None))):
                    continue

                value_str = str(value)
                if case_sensitive:
                    if old_text in value_str:
                        new_value_str = value_str.replace(old_text, new_text)
                        page.body[i].value[key] = new_value_str
                        updated = True
                else:
                    if old_text.lower() in value_str.lower():
                        # Case-insensitive replace
                        import re
                        pattern = re.compile(re.escape(old_text), re.IGNORECASE)
                        new_value_str = pattern.sub(new_text, value_str)
                        page.body[i].value[key] = new_value_str
                        updated = True

        return updated

    def update_about_us(self):
        """Update About Us page"""
        self.stdout.write('\n--- Updating About Us Page ---')

        try:
            page = FlexiblePage.objects.get(slug='about-us')

            replacements = [
                ('20+ years', '25+ years'),
                ('over 20 years', 'over 25 years'),
                ('more than 20 years', 'more than 25 years'),
            ]

            updated = False
            for old_text, new_text in replacements:
                if self.replace_in_streamfield(page, old_text, new_text):
                    updated = True

            if updated:
                page.save_revision().publish()
                self.stdout.write(f'  ✓ Updated About Us page')
            else:
                self.stdout.write(f'  - No changes needed')

        except FlexiblePage.DoesNotExist:
            self.stdout.write(f'  ✗ About Us page not found')

    def update_faq_page(self):
        """Update FAQ page"""
        self.stdout.write('\n--- Updating FAQ Page ---')

        try:
            page = FlexiblePage.objects.get(slug='faq')

            replacements = [
                ('UKAS accredited', 'Over 25 years of 100% first time certification success'),
                ('UKAS-accredited', 'Over 25 years of 100% first time certification success'),
                ('98%', '100%'),
                ('20+ years', '25+ years'),
            ]

            updated = False
            for old_text, new_text in replacements:
                if self.replace_in_streamfield(page, old_text, new_text):
                    updated = True

            if updated:
                page.save_revision().publish()
                self.stdout.write(f'  ✓ Updated FAQ page')
            else:
                self.stdout.write(f'  - No changes needed')

        except FlexiblePage.DoesNotExist:
            self.stdout.write(f'  ✗ FAQ page not found')

    def update_iso_17020(self):
        """Update ISO 17020 page"""
        self.stdout.write('\n--- Updating ISO 17020 Page ---')

        try:
            page = FlexiblePage.objects.get(slug='iso-iec-17020-inspection-body')

            replacements = [
                ('UKAS accredited', 'Over 25 years of 100% first time accreditation success'),
                ('UKAS-accredited', 'Over 25 years of 100% first time accreditation success'),
                ('98%', '100%'),
                ('20+ years', '25+ years'),
            ]

            updated = False
            for old_text, new_text in replacements:
                if self.replace_in_streamfield(page, old_text, new_text):
                    updated = True

            if updated:
                page.save_revision().publish()
                self.stdout.write(f'  ✓ Updated ISO 17020 page')
            else:
                self.stdout.write(f'  - No changes needed')

        except FlexiblePage.DoesNotExist:
            self.stdout.write(f'  ✗ ISO 17020 page not found')

    def update_iso_17025(self):
        """Update ISO 17025 page"""
        self.stdout.write('\n--- Updating ISO 17025 Page (Additional) ---')

        try:
            page = FlexiblePage.objects.get(slug='iso-iec-17025-laboratory-competence')

            replacements = [
                ('UKAS accredited', 'Over 25 years of 100% first time accreditation success'),
                ('UKAS-accredited', 'Over 25 years of 100% first time accreditation success'),
                ('98%', '100%'),
                ('20+ years', '25+ years'),
            ]

            updated = False
            for old_text, new_text in replacements:
                if self.replace_in_streamfield(page, old_text, new_text):
                    updated = True

            if updated:
                page.save_revision().publish()
                self.stdout.write(f'  ✓ Updated ISO 17025 page')
            else:
                self.stdout.write(f'  - No changes needed')

        except FlexiblePage.DoesNotExist:
            self.stdout.write(f'  ✗ ISO 17025 page not found')

    def update_iso_20000(self):
        """Update ISO 20000 page"""
        self.stdout.write('\n--- Updating ISO 20000 Page (Additional) ---')

        try:
            page = FlexiblePage.objects.get(slug='iso-20000')

            replacements = [
                ('UKAS accredited', 'Globally Recognised'),
                ('UKAS-accredited', 'Globally Recognised'),
                ('98%', '100%'),
                ('20+ years', '25+ years'),
            ]

            updated = False
            for old_text, new_text in replacements:
                if self.replace_in_streamfield(page, old_text, new_text):
                    updated = True

            if updated:
                page.save_revision().publish()
                self.stdout.write(f'  ✓ Updated ISO 20000 page')
            else:
                self.stdout.write(f'  - No changes needed')

        except FlexiblePage.DoesNotExist:
            self.stdout.write(f'  ✗ ISO 20000 page not found')

    def update_iso_37301(self):
        """Update ISO 37301 page"""
        self.stdout.write('\n--- Updating ISO 37301 Page ---')

        try:
            page = FlexiblePage.objects.get(slug='iso-37301-compliance-management')

            replacements = [
                ('UKAS accredited', 'Globally Recognised'),
                ('UKAS-accredited', 'Globally Recognised'),
                ('98%', '100%'),
                ('20+ years', '25+ years'),
            ]

            updated = False
            for old_text, new_text in replacements:
                if self.replace_in_streamfield(page, old_text, new_text):
                    updated = True

            if updated:
                page.save_revision().publish()
                self.stdout.write(f'  ✓ Updated ISO 37301 page')
            else:
                self.stdout.write(f'  - No changes needed')

        except FlexiblePage.DoesNotExist:
            self.stdout.write(f'  ✗ ISO 37301 page not found')

    def update_cyber_essentials(self):
        """Update Cyber Essentials page"""
        self.stdout.write('\n--- Updating Cyber Essentials Page (Additional) ---')

        try:
            page = FlexiblePage.objects.get(slug='cyber-essentials')

            replacements = [
                ('Government contracts', 'Government tender processes'),
                ('government contracts', 'government tender processes'),
                ('98%', '100%'),
                ('20+ years', '25+ years'),
            ]

            updated = False
            for old_text, new_text in replacements:
                if self.replace_in_streamfield(page, old_text, new_text):
                    updated = True

            if updated:
                page.save_revision().publish()
                self.stdout.write(f'  ✓ Updated Cyber Essentials page')
            else:
                self.stdout.write(f'  - No changes needed')

        except FlexiblePage.DoesNotExist:
            self.stdout.write(f'  ✗ Cyber Essentials page not found')

    def update_all_pages_comprehensive(self):
        """Do a comprehensive sweep of all pages for any missed content"""
        self.stdout.write('\n--- Comprehensive Sweep of All Pages ---')

        replacements = [
            ('98%', '100%'),
            ('20+ years', '25+ years'),
            ('over 20 years', 'over 25 years'),
            ('Years Experience: 20+', 'Years Experience: 25+'),
            ('20+ Years Experience', '25+ Years Experience'),
        ]

        updated_pages = []
        for page in FlexiblePage.objects.all():
            page_updated = False
            for old_text, new_text in replacements:
                if self.replace_in_streamfield(page, old_text, new_text):
                    page_updated = True

            if page_updated:
                page.save_revision().publish()
                updated_pages.append(page.title)

        if updated_pages:
            for title in updated_pages:
                self.stdout.write(f'  ✓ Updated: {title}')
        else:
            self.stdout.write(f'  - No additional pages needed updates')
