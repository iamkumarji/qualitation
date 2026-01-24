"""
Django management command to bulk update content using direct database access
"""

from django.core.management.base import BaseCommand
from home.models import FlexiblePage, HomePage
from django.db import connection


class Command(BaseCommand):
    help = 'Bulk update content using direct database queries'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('\n=== Bulk Content Update ===\n'))

        # Define replacements
        replacements = [
            ('20+ Years Experience', '25+ Years Experience'),
            ('20+ years', '25+ years'),
            ('over 20 years', 'over 25 years'),
            ('Years Experience: 20+', 'Years Experience: 25+'),
            ('98%', '100%'),
            ('98% success rate', '100% first-time certification success'),
            ('UKAS-accredited certification support', 'Over 25 years of 100% first time certifications success!'),
           ('Government contracts', 'Government tender processes'),
            ('government contracts', 'government tender processes'),
        ]

        # Update using SQL - safer for StreamFields
        with connection.cursor() as cursor:
            for old_text, new_text in replacements:
                # Update the body field in home_flexiblepage
                sql = """
                UPDATE home_flexiblepage
                SET body = REPLACE(body, %s, %s)
                WHERE body LIKE %s
                """
                cursor.execute(sql, [old_text, new_text, f'%{old_text}%'])
                rows_updated = cursor.rowcount
                if rows_updated > 0:
                    self.stdout.write(f'  ✓ Replaced "{old_text}" → "{new_text}" in {rows_updated} FlexiblePages')

                # Update the body field in home_homepage
                sql = """
                UPDATE home_homepage
                SET body = REPLACE(body, %s, %s)
                WHERE body LIKE %s
                """
                cursor.execute(sql, [old_text, new_text, f'%{old_text}%'])
                rows_updated = cursor.rowcount
                if rows_updated > 0:
                    self.stdout.write(f'  ✓ Replaced "{old_text}" → "{new_text}" in {rows_updated} HomePages')

        self.stdout.write(self.style.SUCCESS('\n=== Update Complete ==='))
        self.stdout.write('\nNote: You may need to create new revisions in Wagtail admin for these pages to be fully published.')
