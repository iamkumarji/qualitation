"""
Django management command to standardize Stage 1 (Step 3) text across all certification pages
"""

from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    help = 'Standardize Stage 1 Assessment text to include "Ensuring Written Systems Meet Standard"'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('\n=== Standardizing Stage 1 / Step 3 Text ===\n'))

        # Define variations of Stage 1 text that need updating
        stage1_updates = [
            # Generic certification body reference
            (
                'Certification body reviews your documented systems to verify they meet',
                'Stage 1 Assessment: Ensuring Written Systems Meet Standard. Certification body reviews your documented systems to verify they meet'
            ),
            # For pages that might have shorter text
            (
                'Stage 1 Assessment</h3>',
                'Stage 1 Assessment: Ensuring Written Systems Meet Standard</h3>'
            ),
            # Alternative wording
            (
                'Stage 1:',
                'Stage 1: Ensuring Written Systems Meet Standard -'
            ),
            # For "Step 3"
            (
                '<h3 style="color: #FF9800; margin-bottom: 12px;">Stage 1 Assessment</h3>',
                '<h3 style="color: #FF9800; margin-bottom: 12px;">Stage 1: Ensuring Written Systems Meet Standard</h3>'
            ),
        ]

        total_updates = 0

        # Update using SQL
        with connection.cursor() as cursor:
            for old_text, new_text in stage1_updates:
                # Update FlexiblePage
                sql = """
                UPDATE home_flexiblepage
                SET body = REPLACE(body, %s, %s)
                WHERE body LIKE %s
                """
                cursor.execute(sql, [old_text, new_text, f'%{old_text}%'])
                rows_updated = cursor.rowcount
                if rows_updated > 0:
                    total_updates += rows_updated
                    self.stdout.write(f'  ✓ Updated {rows_updated} pages (pattern: Stage 1)')

                # Update HomePage
                sql = """
                UPDATE home_homepage
                SET body = REPLACE(body, %s, %s)
                WHERE body LIKE %s
                """
                cursor.execute(sql, [old_text, new_text, f'%{old_text}%'])
                rows_updated = cursor.rowcount
                if rows_updated > 0:
                    total_updates += rows_updated

        self.stdout.write(self.style.SUCCESS(f'\n=== Total updates: {total_updates} ==='))

        # Now publish all updated pages
        self.stdout.write('\n=== Publishing updated pages ===')

        from home.models import FlexiblePage, HomePage

        # Publish FlexiblePages
        for page in FlexiblePage.objects.all():
            try:
                page.save_revision().publish()
            except Exception as e:
                self.stdout.write(f'  ✗ Error publishing {page.title}: {e}')

        # Publish HomePage
        homepage = HomePage.objects.first()
        if homepage:
            try:
                homepage.save_revision().publish()
            except Exception as e:
                self.stdout.write(f'  ✗ Error publishing Home Page: {e}')

        self.stdout.write(self.style.SUCCESS('\n=== All pages published ==='))
