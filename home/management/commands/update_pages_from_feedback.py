"""
Django management command to update pages based on Excel feedback
Queries on Qualitation Website.xlsx - 2026-01-19
"""

from django.core.management.base import BaseCommand
from home.models import FlexiblePage, HomePage
import json


class Command(BaseCommand):
    help = 'Update pages based on Excel feedback (Queries on Qualitation Website.xlsx)'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('\n=== Starting Page Updates ===\n'))

        # Update all pages systematically
        self.update_success_rates()
        self.update_years_experience()
        self.remove_uk_from_titles()
        self.update_iso_9001_page()
        self.update_iso_14001_page()
        self.update_iso_27001_page()
        self.update_iso_22000_page()
        self.update_iatf_16949_page()
        self.update_iso_13485_page()
        self.update_contact_page()
        self.update_iso_17025_page()
        self.update_environmental_pages()
        self.update_business_continuity_pages()
        self.update_it_security_pages()
        self.update_compliance_pages()
        self.update_food_safety_pages()
        self.update_who_gmp_page()
        self.update_iso_45001_page()

        self.stdout.write(self.style.SUCCESS('\n=== Page Updates Complete ===\n'))

    def replace_in_html_block(self, html_content, old_text, new_text):
        """Helper to replace text in HTML content"""
        if isinstance(html_content, str):
            return html_content.replace(old_text, new_text)
        return html_content

    def update_page_body(self, page, replacements):
        """Update page body with text replacements"""
        updated = False
        if not page.body:
            return updated

        for i, block in enumerate(page.body):
            block_type = block.block_type
            block_value = block.value

            # Handle different block types
            if block_type == 'html' and 'html' in block_value:
                html = str(block_value['html'])
                original_html = html
                for old_text, new_text in replacements.items():
                    html = html.replace(old_text, new_text)
                if html != original_html:
                    page.body[i].value['html'] = html
                    updated = True

            elif block_type == 'paragraph' and 'content' in block_value:
                # Convert RichText to string
                content = str(block_value['content'])
                original_content = content
                for old_text, new_text in replacements.items():
                    content = content.replace(old_text, new_text)
                if content != original_content:
                    page.body[i].value['content'] = content
                    updated = True

            elif block_type == 'heading' and 'text' in block_value:
                text = str(block_value['text'])
                original_text = text
                for old_text, new_text in replacements.items():
                    text = text.replace(old_text, new_text)
                if text != original_text:
                    page.body[i].value['text'] = text
                    updated = True

            elif block_type == 'accordion' and 'items' in block_value:
                for item in block_value['items']:
                    if 'content' in item:
                        # Convert RichText to string
                        content_str = str(item['content'])
                        original = content_str
                        for old_text, new_text in replacements.items():
                            content_str = content_str.replace(old_text, new_text)
                        if content_str != original:
                            item['content'] = content_str
                            updated = True
                    if 'title' in item:
                        title_str = str(item['title'])
                        original = title_str
                        for old_text, new_text in replacements.items():
                            title_str = title_str.replace(old_text, new_text)
                        if title_str != original:
                            item['title'] = title_str
                            updated = True

        return updated

    def update_success_rates(self):
        """Update 98% to 100% across all pages"""
        self.stdout.write('\n--- Updating Success Rates (98% → 100%) ---')

        replacements = {
            '98%': '100%',
            '98% success rate': '100% first-time certification success',
            'over 98%': '100%',
        }

        pages = FlexiblePage.objects.all()
        updated_count = 0

        for page in pages:
            if self.update_page_body(page, replacements):
                page.save_revision().publish()
                updated_count += 1
                self.stdout.write(f'  ✓ Updated: {page.title}')

        self.stdout.write(f'Updated {updated_count} pages')

    def update_years_experience(self):
        """Update 20+ years to 25+ years"""
        self.stdout.write('\n--- Updating Years of Experience (20+ → 25+) ---')

        replacements = {
            '20+ years': '25+ years',
            'over 20 years': 'over 25 years',
            'more than 20 years': 'more than 25 years',
            '20 years': '25 years',
        }

        pages = FlexiblePage.objects.all()
        updated_count = 0

        for page in pages:
            if self.update_page_body(page, replacements):
                page.save_revision().publish()
                updated_count += 1
                self.stdout.write(f'  ✓ Updated: {page.title}')

        self.stdout.write(f'Updated {updated_count} pages')

    def remove_uk_from_titles(self):
        """Remove 'UK' from page titles"""
        self.stdout.write('\n--- Removing UK from Titles ---')

        pages_to_update = [
            ('iso-27001', 'ISO 27001 Certification | Information Security'),
            ('iso-22000', 'ISO 22000 Certification | Food Safety Management'),
            ('iso-13485', 'ISO 13485 Certification | Medical Device QMS'),
            ('iso-14064', 'ISO 14064 Certification | Greenhouse Gas Reporting'),
            ('iso-22301', 'ISO 22301 Certification | Business Continuity Management'),
            ('iso-27701', 'ISO 27701 Certification | Privacy Information Management'),
            ('iso-27018', 'ISO 27018 Certification | Cloud Privacy'),
            ('iso-20000', 'ISO 20000-1 Certification | IT Service Management'),
            ('cyber-essentials', 'Cyber Essentials Certification | Cyber Security'),
            ('who-gmp', 'WHO-GMP Certification | Pharmaceutical Manufacturing'),
            ('halal', 'Halal Certification'),
            ('kosher', 'Kosher Certification'),
        ]

        for slug, new_title in pages_to_update:
            try:
                page = FlexiblePage.objects.get(slug=slug)
                old_title = page.title
                page.title = new_title
                page.save_revision().publish()
                self.stdout.write(f'  ✓ Updated: {old_title} → {new_title}')
            except FlexiblePage.DoesNotExist:
                self.stdout.write(f'  ✗ Page not found: {slug}')

    def update_iso_9001_page(self):
        """Update ISO 9001 page with specific feedback"""
        self.stdout.write('\n--- Updating ISO 9001 Page ---')

        try:
            page = FlexiblePage.objects.get(slug='iso-9001')

            replacements = {
                'meeting customer needs': 'meeting your customer needs',
                '3-6 months': '1-6 months',
                'Government contracts': 'Government tender processes',
                'UKAS accredited': 'Over 25 years of 100% first time certification success',
                'UKAS-accredited': 'Over 25 years of 100% first time certification success',
            }

            if self.update_page_body(page, replacements):
                page.save_revision().publish()
                self.stdout.write(f'  ✓ Updated ISO 9001 page')
            else:
                self.stdout.write(f'  - No changes needed for ISO 9001 page')

        except FlexiblePage.DoesNotExist:
            self.stdout.write(f'  ✗ ISO 9001 page not found')

    def update_iso_14001_page(self):
        """Update ISO 14001 page"""
        self.stdout.write('\n--- Updating ISO 14001 Page ---')

        try:
            page = FlexiblePage.objects.get(slug='iso-14001')

            replacements = {
                'especially government and large corporations': 'especially governments, charities, NGOs and large corporations',
                'UKAS Accredited': 'Over 25 years of 100% first time certification success',
                'UKAS-accredited': 'Over 25 years of 100% first time certification success',
            }

            if self.update_page_body(page, replacements):
                page.save_revision().publish()
                self.stdout.write(f'  ✓ Updated ISO 14001 page')
            else:
                self.stdout.write(f'  - No changes needed for ISO 14001 page')

        except FlexiblePage.DoesNotExist:
            self.stdout.write(f'  ✗ ISO 14001 page not found')

    def update_iso_27001_page(self):
        """Update ISO 27001 page"""
        self.stdout.write('\n--- Updating ISO 27001 Page ---')

        try:
            page = FlexiblePage.objects.get(slug='iso-27001')

            replacements = {
                'UKAS Accredited': 'Over 25 years of 100% first time certification success',
                'UKAS-accredited': 'Over 25 years of 100% first time certification success',
            }

            if self.update_page_body(page, replacements):
                page.save_revision().publish()
                self.stdout.write(f'  ✓ Updated ISO 27001 page')
            else:
                self.stdout.write(f'  - No changes needed for ISO 27001 page')

        except FlexiblePage.DoesNotExist:
            self.stdout.write(f'  ✗ ISO 27001 page not found')

    def update_iso_22000_page(self):
        """Update ISO 22000 page"""
        self.stdout.write('\n--- Updating ISO 22000 Page ---')

        try:
            page = FlexiblePage.objects.get(slug='iso-22000')

            replacements = {
                'UKAS Accredited': 'Over 25 years of 100% first time certification success',
                'UKAS-accredited': 'Over 25 years of 100% first time certification success',
            }

            if self.update_page_body(page, replacements):
                page.save_revision().publish()
                self.stdout.write(f'  ✓ Updated ISO 22000 page')
            else:
                self.stdout.write(f'  - No changes needed for ISO 22000 page')

        except FlexiblePage.DoesNotExist:
            self.stdout.write(f'  ✗ ISO 22000 page not found')

    def update_iatf_16949_page(self):
        """Update IATF 16949 page"""
        self.stdout.write('\n--- Updating IATF 16949 Page ---')

        try:
            page = FlexiblePage.objects.get(slug='iatf-16949')

            replacements = {
                'UKAS Accredited': 'Over 25 years of 100% first time certification success',
                'UKAS-accredited': 'Over 25 years of 100% first time certification success',
            }

            if self.update_page_body(page, replacements):
                page.save_revision().publish()
                self.stdout.write(f'  ✓ Updated IATF 16949 page')
            else:
                self.stdout.write(f'  - No changes needed for IATF 16949 page')

        except FlexiblePage.DoesNotExist:
            self.stdout.write(f'  ✗ IATF 16949 page not found')

    def update_iso_13485_page(self):
        """Update ISO 13485 page"""
        self.stdout.write('\n--- Updating ISO 13485 Page ---')

        try:
            page = FlexiblePage.objects.get(slug='iso-13485')

            replacements = {
                'UKAS Accredited': 'Over 25 years of 100% first time certification success',
                'UKAS-accredited': 'Over 25 years of 100% first time certification success',
            }

            if self.update_page_body(page, replacements):
                page.save_revision().publish()
                self.stdout.write(f'  ✓ Updated ISO 13485 page')
            else:
                self.stdout.write(f'  - No changes needed for ISO 13485 page')

        except FlexiblePage.DoesNotExist:
            self.stdout.write(f'  ✗ ISO 13485 page not found')

    def update_contact_page(self):
        """Update Contact page"""
        self.stdout.write('\n--- Updating Contact Page ---')

        try:
            page = FlexiblePage.objects.get(slug='contact')

            replacements = {
                'UKAS-accredited certification support': 'Over 25 years of 100% first time certifications success!',
                '98% Success Rate': '100% Success Rate',
                '20+ Years Experience': '25+ Years Experience',
                '20+': '25+',
                '98%': '100%',
            }

            if self.update_page_body(page, replacements):
                page.save_revision().publish()
                self.stdout.write(f'  ✓ Updated Contact page')
            else:
                self.stdout.write(f'  - No changes needed for Contact page')

        except FlexiblePage.DoesNotExist:
            self.stdout.write(f'  ✗ Contact page not found')

    def update_iso_17025_page(self):
        """Update ISO 17025 page"""
        self.stdout.write('\n--- Updating ISO 17025 Page ---')

        try:
            page = FlexiblePage.objects.get(slug='iso-iec-17025-laboratory-competence')

            replacements = {
                'UKAS Accredited': 'Over 25 years of 100% first time accreditation success',
                '98%': '100%',
                'The certifier': 'UKAS',
            }

            if self.update_page_body(page, replacements):
                page.save_revision().publish()
                self.stdout.write(f'  ✓ Updated ISO 17025 page')
            else:
                self.stdout.write(f'  - No changes needed for ISO 17025 page')

        except FlexiblePage.DoesNotExist:
            self.stdout.write(f'  ✗ ISO 17025 page not found')

    def update_environmental_pages(self):
        """Update environmental standards pages"""
        self.stdout.write('\n--- Updating Environmental Standards Pages ---')

        pages_to_update = ['iso-14064', 'iso-14067', 'iso-45003']

        for slug in pages_to_update:
            try:
                page = FlexiblePage.objects.get(slug=slug)

                replacements = {
                    'UKAS Accredited': 'Over 25 years of 100% first time certification success',
                    'UKAS-accredited': 'Over 25 years of 100% first time certification success',
                }

                if self.update_page_body(page, replacements):
                    page.save_revision().publish()
                    self.stdout.write(f'  ✓ Updated: {page.title}')

            except FlexiblePage.DoesNotExist:
                self.stdout.write(f'  ✗ Page not found: {slug}')

    def update_business_continuity_pages(self):
        """Update business continuity pages"""
        self.stdout.write('\n--- Updating Business Continuity Pages ---')

        pages_to_update = ['iso-22301', 'iso-50001', 'iso-55001', 'iso-41001']

        for slug in pages_to_update:
            try:
                page = FlexiblePage.objects.get(slug=slug)

                replacements = {
                    'UKAS Accredited': 'Globally Recognised',
                    'UKAS-accredited': 'Globally Recognised',
                }

                if self.update_page_body(page, replacements):
                    page.save_revision().publish()
                    self.stdout.write(f'  ✓ Updated: {page.title}')

            except FlexiblePage.DoesNotExist:
                self.stdout.write(f'  ✗ Page not found: {slug}')

    def update_it_security_pages(self):
        """Update IT security pages"""
        self.stdout.write('\n--- Updating IT Security Pages ---')

        pages = [
            ('iso-27701', 'UKAS Accredited', 'Globally Recognised'),
            ('iso-27018', 'UKAS Accredited', 'Globally Recognised'),
            ('iso-20000', 'UKAS Accredited', 'Globally Recognised'),
            ('cyber-essentials', 'IASME Accredited', 'IASME Accredited Certifiers'),
        ]

        for slug, old_text, new_text in pages:
            try:
                page = FlexiblePage.objects.get(slug=slug)

                replacements = {old_text: new_text}

                if self.update_page_body(page, replacements):
                    page.save_revision().publish()
                    self.stdout.write(f'  ✓ Updated: {page.title}')

            except FlexiblePage.DoesNotExist:
                self.stdout.write(f'  ✗ Page not found: {slug}')

    def update_compliance_pages(self):
        """Update compliance pages (SOC 2, PCI DSS)"""
        self.stdout.write('\n--- Updating Compliance Pages ---')

        try:
            page = FlexiblePage.objects.get(slug='pci-dss-compliance')

            replacements = {
                'March 2024': 'March 2025',
                'mandatory from March 2024': 'mandatory from March 2025',
            }

            if self.update_page_body(page, replacements):
                page.save_revision().publish()
                self.stdout.write(f'  ✓ Updated PCI DSS page')

        except FlexiblePage.DoesNotExist:
            self.stdout.write(f'  ✗ PCI DSS page not found')

    def update_food_safety_pages(self):
        """Update food safety pages"""
        self.stdout.write('\n--- Updating Food Safety Pages ---')

        pages_to_update = ['fssc-22000', 'halal', 'kosher']

        for slug in pages_to_update:
            try:
                page = FlexiblePage.objects.get(slug=slug)

                replacements = {
                    'UKAS Accredited': 'Over 25 years of 100% first time certification success',
                    'UKAS-accredited': 'Over 25 years of 100% first time certification success',
                }

                if self.update_page_body(page, replacements):
                    page.save_revision().publish()
                    self.stdout.write(f'  ✓ Updated: {page.title}')

            except FlexiblePage.DoesNotExist:
                self.stdout.write(f'  ✗ Page not found: {slug}')

    def update_who_gmp_page(self):
        """Update WHO-GMP page"""
        self.stdout.write('\n--- Updating WHO-GMP Page ---')

        try:
            page = FlexiblePage.objects.get(slug='who-gmp')

            replacements = {
                'UKAS Accredited': 'Over 25 years of 100% first time certification success',
                'UKAS-accredited': 'Over 25 years of 100% first time certification success',
            }

            if self.update_page_body(page, replacements):
                page.save_revision().publish()
                self.stdout.write(f'  ✓ Updated WHO-GMP page')
            else:
                self.stdout.write(f'  - No changes needed for WHO-GMP page')

        except FlexiblePage.DoesNotExist:
            self.stdout.write(f'  ✗ WHO-GMP page not found')

    def update_iso_45001_page(self):
        """Update ISO 45001 page if it exists"""
        self.stdout.write('\n--- Checking ISO 45001 Page ---')

        try:
            page = FlexiblePage.objects.get(slug='iso-45001')

            replacements = {
                'UKAS Accredited': 'Over 25 years of 100% first time certification success',
                'UKAS-accredited': 'Over 25 years of 100% first time certification success',
            }

            if self.update_page_body(page, replacements):
                page.save_revision().publish()
                self.stdout.write(f'  ✓ Updated ISO 45001 page')
            else:
                self.stdout.write(f'  ✓ ISO 45001 page exists (no changes needed)')

        except FlexiblePage.DoesNotExist:
            self.stdout.write(f'  ℹ ISO 45001 page already exists')
