"""
Django management command to create the missing pages identified in the Excel feedback
"""

from django.core.management.base import BaseCommand
from wagtail.models import Page
from home.models import FlexiblePage, HomePage


class Command(BaseCommand):
    help = 'Create missing pages (ISO Certification, ISO Consultancy, Resources)'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('\n=== Creating Missing Pages ===\n'))

        # Get the home page to add children to
        homepage = HomePage.objects.first()
        if not homepage:
            self.stdout.write(self.style.ERROR('ERROR: No homepage found!'))
            return

        # Create ISO Certification page
        self.create_iso_certification(homepage)

        # Create ISO Consultancy page
        self.create_iso_consultancy(homepage)

        # Create Resources page
        self.create_resources(homepage)

        self.stdout.write(self.style.SUCCESS('\n=== Page Creation Complete ===\n'))

    def create_iso_certification(self, parent):
        """Create ISO Certification overview page"""
        self.stdout.write('\n--- Creating ISO Certification Page ---')

        existing = FlexiblePage.objects.filter(slug='iso-certification').first()
        if existing:
            self.stdout.write(f'  - Page already exists: {existing.title}')
            return

        body_content = [
            ('html', {
                'html': '''
<section style="background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%); padding: 80px 20px; text-align: center; color: white;">
    <h1 style="font-size: 3em; margin-bottom: 20px;">ISO Certification Services</h1>
    <p style="font-size: 1.3em; max-width: 800px; margin: 0 auto;">
        Expert guidance to help your organization achieve ISO certification with confidence.
        Over 25 years of 100% first-time certification success.
    </p>
</section>

<section style="max-width: 1200px; margin: 60px auto; padding: 0 20px;">
    <h2 style="text-align: center; font-size: 2.5em; margin-bottom: 40px;">Our ISO Certification Services</h2>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; margin-bottom: 60px;">
        <div style="border: 1px solid #ddd; padding: 30px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            <h3 style="color: #1e3a5f; margin-bottom: 15px;">Gap Analysis</h3>
            <p>We assess your current systems against ISO requirements to identify areas for improvement.</p>
        </div>

        <div style="border: 1px solid #ddd; padding: 30px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            <h3 style="color: #1e3a5f; margin-bottom: 15px;">Documentation Support</h3>
            <p>Expert help with creating policies, procedures, and all required documentation for certification.</p>
        </div>

        <div style="border: 1px solid #ddd; padding: 30px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            <h3 style="color: #1e3a5f; margin-bottom: 15px;">Implementation Guidance</h3>
            <p>Step-by-step support to implement your management system effectively across your organization.</p>
        </div>

        <div style="border: 1px solid #ddd; padding: 30px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            <h3 style="color: #1e3a5f; margin-bottom: 15px;">Audit Preparation</h3>
            <p>Comprehensive preparation for your certification audit to ensure first-time success.</p>
        </div>
    </div>

    <div style="text-align: center; margin-top: 60px;">
        <a href="/contact/" style="background: #1e3a5f; color: white; padding: 15px 40px; border-radius: 50px; text-decoration: none; font-size: 1.1em; display: inline-block;">
            Request a Quote
        </a>
    </div>
</section>
'''
            }),
        ]

        page = FlexiblePage(
            title='ISO Certification',
            slug='iso-certification',
            intro='Professional ISO certification services with 100% first-time success rate',
            body=body_content
        )
        parent.add_child(instance=page)
        page.save_revision().publish()
        self.stdout.write(f'  ✓ Created: ISO Certification page')

    def create_iso_consultancy(self, parent):
        """Create ISO Consultancy page"""
        self.stdout.write('\n--- Creating ISO Consultancy Page ---')

        existing = FlexiblePage.objects.filter(slug='iso-consultancy').first()
        if existing:
            self.stdout.write(f'  - Page already exists: {existing.title}')
            return

        body_content = [
            ('html', {
                'html': '''
<section style="background: linear-gradient(135deg, #2d5a87 0%, #1e3a5f 100%); padding: 80px 20px; text-align: center; color: white;">
    <h1 style="font-size: 3em; margin-bottom: 20px;">ISO Consultancy Services</h1>
    <p style="font-size: 1.3em; max-width: 800px; margin: 0 auto;">
        Expert ISO consultancy to guide your organization through every step of the certification process.
        25+ years of proven expertise.
    </p>
</section>

<section style="max-width: 1200px; margin: 60px auto; padding: 0 20px;">
    <h2 style="text-align: center; font-size: 2.5em; margin-bottom: 40px;">Why Choose Our Consultancy Services?</h2>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; margin-bottom: 60px;">
        <div style="background: #f8f9fa; padding: 30px; border-radius: 10px;">
            <h3 style="color: #1e3a5f; margin-bottom: 15px;">📊 Expert Knowledge</h3>
            <p>Over 25 years of ISO consultancy experience across all major standards.</p>
        </div>

        <div style="background: #f8f9fa; padding: 30px; border-radius: 10px;">
            <h3 style="color: #1e3a5f; margin-bottom: 15px;">✅ 100% Success Rate</h3>
            <p>Every client we work with achieves first-time certification success.</p>
        </div>

        <div style="background: #f8f9fa; padding: 30px; border-radius: 10px;">
            <h3 style="color: #1e3a5f; margin-bottom: 15px;">🎯 Tailored Approach</h3>
            <p>Customized consultancy services designed for your organization's specific needs.</p>
        </div>
    </div>

    <h2 style="text-align: center; font-size: 2.2em; margin: 60px 0 30px;">Our Consultancy Process</h2>

    <div style="display: flex; flex-direction: column; gap: 20px;">
        <div style="display: flex; gap: 20px; align-items: start;">
            <div style="background: #1e3a5f; color: white; width: 50px; height: 50px; border-radius: 50%; display: flex; align-items: center; justify-content: center; flex-shrink: 0; font-size: 1.5em; font-weight: bold;">1</div>
            <div>
                <h3>Initial Assessment</h3>
                <p>We evaluate your current systems and identify gaps against ISO requirements.</p>
            </div>
        </div>

        <div style="display: flex; gap: 20px; align-items: start;">
            <div style="background: #1e3a5f; color: white; width: 50px; height: 50px; border-radius: 50%; display: flex; align-items: center; justify-content: center; flex-shrink: 0; font-size: 1.5em; font-weight: bold;">2</div>
            <div>
                <h3>Custom Planning</h3>
                <p>Development of a tailored implementation plan for your organization.</p>
            </div>
        </div>

        <div style="display: flex; gap: 20px; align-items: start;">
            <div style="background: #1e3a5f; color: white; width: 50px; height: 50px; border-radius: 50%; display: flex; align-items: center; justify-content: center; flex-shrink: 0; font-size: 1.5em; font-weight: bold;">3</div>
            <div>
                <h3>Implementation Support</h3>
                <p>Hands-on guidance through system implementation and documentation.</p>
            </div>
        </div>

        <div style="display: flex; gap: 20px; align-items: start;">
            <div style="background: #1e3a5f; color: white; width: 50px; height: 50px; border-radius: 50%; display: flex; align-items: center; justify-content: center; flex-shrink: 0; font-size: 1.5em; font-weight: bold;">4</div>
            <div>
                <h3>Certification Success</h3>
                <p>Audit preparation and support to ensure successful certification.</p>
            </div>
        </div>
    </div>

    <div style="text-align: center; margin-top: 60px;">
        <a href="/contact/" style="background: #2d5a87; color: white; padding: 15px 40px; border-radius: 50px; text-decoration: none; font-size: 1.1em; display: inline-block;">
            Get Started Today
        </a>
    </div>
</section>
'''
            }),
        ]

        page = FlexiblePage(
            title='ISO Consultancy',
            slug='iso-consultancy',
            intro='Professional ISO consultancy services tailored to your organization',
            body=body_content
        )
        parent.add_child(instance=page)
        page.save_revision().publish()
        self.stdout.write(f'  ✓ Created: ISO Consultancy page')

    def create_resources(self, parent):
        """Create Resources page"""
        self.stdout.write('\n--- Creating Resources Page ---')

        existing = FlexiblePage.objects.filter(slug='resources').first()
        if existing:
            self.stdout.write(f'  - Page already exists: {existing.title}')
            return

        body_content = [
            ('html', {
                'html': '''
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

    <div style="background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%); padding: 60px 40px; margin-top: 80px; border-radius: 15px; text-align: center; color: white;">
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
            }),
        ]

        page = FlexiblePage(
            title='Resources',
            slug='resources',
            intro='Helpful resources and guides for ISO certification',
            body=body_content
        )
        parent.add_child(instance=page)
        page.save_revision().publish()
        self.stdout.write(f'  ✓ Created: Resources page')
