"""
Django management command to fix Resources page block order using SQL
"""

from django.core.management.base import BaseCommand
from django.db import connection
import json


class Command(BaseCommand):
    help = 'Reorder Resources page blocks: Explore -> Articles -> CTA'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('\n=== Fixing Resources Page Order ===\n'))

        # Get current body
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

        # Create new ordered blocks
        new_body = []

        # Block 0: Explore Our Resources (without CTA)
        explore_html = '''
<section style="background: linear-gradient(135deg, #3d7ab5 0%, #1e3a5f 100%); padding: 80px 20px; text-align: center; color: white;">
    <h1 style="font-size: 3em; margin-bottom: 20px;">ISO Resources & Guides</h1>
    <p style="font-size: 1.3em; max-width: 800px; margin: 0 auto;">
        Helpful resources, guides, and information to support your ISO certification journey.
    </p>
</section>

<section style="max-width: 1200px; margin: 60px auto; padding: 0 20px;">
    <h2 style="text-align: center; font-size: 2.5em; margin-bottom: 40px;">Explore Our Resources</h2>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 30px;">
        <div style="border-left: 4px solid #1e3a5f; padding: 20px; background: #f8f9fa;">
            <h3 style="color: #1e3a5f;">📚 ISO Standards Guide</h3>
            <p style="margin: 15px 0;">Learn about different ISO standards and which one is right for your organization.</p>
            <a href="/iso-standards/" style="color: #1e3a5f; text-decoration: none; font-weight: 600;">Explore Standards →</a>
        </div>

        <div style="border-left: 4px solid #2d5a87; padding: 20px; background: #f8f9fa;">
            <h3 style="color: #2d5a87;">❓ Frequently Asked Questions</h3>
            <p style="margin: 15px 0;">Find answers to common questions about ISO certification and our services.</p>
            <a href="/faq/" style="color: #2d5a87; text-decoration: none; font-weight: 600;">View FAQs →</a>
        </div>

        <div style="border-left: 4px solid #3d7ab5; padding: 20px; background: #f8f9fa;">
            <h3 style="color: #3d7ab5;">🎓 Training Courses</h3>
            <p style="margin: 15px 0;">Professional training courses for ISO standards and internal auditing.</p>
            <a href="/training/" style="color: #3d7ab5; text-decoration: none; font-weight: 600;">View Courses →</a>
        </div>
    </div>
</section>
'''
        new_body.append({
            'type': 'html',
            'value': {'html': explore_html},
            'id': body_data[0]['id']  # Keep the same ID
        })

        # Block 1: News & Articles (keep as is)
        new_body.append(body_data[1])

        # Block 2: Need Personalized Guidance CTA (new)
        import uuid
        cta_html = '''
<section style="max-width: 1200px; margin: 80px auto 60px; padding: 0 20px;">
    <div style="background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%); padding: 60px 40px; border-radius: 15px; text-align: center; color: white;">
        <h2 style="font-size: 2.2em; margin-bottom: 20px;">Need Personalized Guidance?</h2>
        <p style="font-size: 1.2em; margin-bottom: 30px; opacity: 0.95;">
            Our expert team is here to help. Get in touch for a free consultation.
        </p>
        <a href="/contact/" style="background: white; color: #1e3a5f; padding: 15px 40px; border-radius: 50px; text-decoration: none; font-size: 1.1em; display: inline-block; font-weight: 600;">
            Contact Us
        </a>
    </div>
</section>
'''
        new_body.append({
            'type': 'html',
            'value': {'html': cta_html},
            'id': str(uuid.uuid4())  # New unique ID
        })

        # Update the database
        new_body_json = json.dumps(new_body)

        with connection.cursor() as cursor:
            cursor.execute('''
                UPDATE home_flexiblepage
                SET body = %s
                WHERE page_ptr_id = %s
            ''', [new_body_json, page_id])

        self.stdout.write(self.style.SUCCESS('✓ Updated Resources page order:'))
        self.stdout.write(self.style.SUCCESS('  1. Explore Our Resources'))
        self.stdout.write(self.style.SUCCESS('  2. News & Articles'))
        self.stdout.write(self.style.SUCCESS('  3. Need Personalized Guidance (CTA)'))

        # Now publish the page
        from home.models import FlexiblePage
        page = FlexiblePage.objects.get(id=page_id)
        page.save_revision().publish()

        self.stdout.write(self.style.SUCCESS('✓ Page published successfully'))
        self.stdout.write(self.style.SUCCESS('\n=== Complete ===\n'))
