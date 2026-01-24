"""
Django management command to create the Templates article page
"""

from django.core.management.base import BaseCommand
from home.models import FlexiblePage
from wagtail.models import Page
import uuid


class Command(BaseCommand):
    help = 'Create the Templates ISO article page'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('\n=== Creating Templates Article Page ===\n'))

        try:
            # Get the home page as parent
            home_page = Page.objects.get(slug='home')

            # Check if page already exists
            if FlexiblePage.objects.filter(slug='dont-use-templates-to-achieve-an-iso-standard').exists():
                self.stdout.write(self.style.WARNING('✗ Page already exists, deleting old version...'))
                old_page = FlexiblePage.objects.get(slug='dont-use-templates-to-achieve-an-iso-standard')
                old_page.delete()

            # Create the article HTML content
            article_html = '''
<article style="max-width: 900px; margin: 0 auto; padding: 40px 20px;">

    <!-- Header -->
    <header style="margin-bottom: 40px; border-bottom: 3px solid #667eea; padding-bottom: 30px;">
        <div style="color: #999; font-size: 0.95em; margin-bottom: 15px; text-transform: uppercase; letter-spacing: 1px;">
            📅 27 October 2020
        </div>
        <h1 style="font-size: 2.8em; color: #1e3a5f; margin-bottom: 20px; line-height: 1.2;">
            Don't use templates to achieve ISO standards!
        </h1>
    </header>

    <!-- Introduction -->
    <div style="font-size: 1.1em; line-height: 1.8; color: #333; margin-bottom: 40px;">
        <p style="margin-bottom: 20px;">
            I was recently contacted out of the blue and asked to help complete some ISO templates that they had attached.
            I read the attachments they sent and I could see why they were having difficulty working out how to complete the templates.
        </p>
        <p style="margin-bottom: 20px;">
            The templates were not very well structured and were out of date – some were dated over 10 years ago, or they
            referred to versions of the standard that have been replaced at least once if not twice by now etc.
        </p>
        <p style="margin-bottom: 20px; font-weight: 500; color: #f5576c;">
            I replied expressing the hope they had not paid for them as it was my opinion that they would be spending far
            more of your time fitting them to their organisation than if they had started from scratch.
        </p>
    </div>

    <!-- Problem Section -->
    <section style="background: linear-gradient(135deg, #fff5f5 0%, #ffe5e5 100%); padding: 40px; border-radius: 15px; margin-bottom: 40px; border-left: 5px solid #f5576c;">
        <h2 style="font-size: 2em; color: #1e3a5f; margin-bottom: 25px;">
            ❌ So what are the problems with using a template?
        </h2>
        <p style="font-size: 1.05em; color: #333; margin-bottom: 25px; line-height: 1.7;">
            While a template will allow you to get the standard certified initially, it is useless for several reasons:
        </p>

        <div style="background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
            <ul style="list-style: none; padding: 0; margin: 0;">
                <li style="margin-bottom: 25px; padding-left: 35px; position: relative; line-height: 1.7;">
                    <span style="position: absolute; left: 0; top: 0; font-size: 1.5em; color: #f5576c;">•</span>
                    It does not relate to your organisation (being generic) so no-one reading it (ie your staff) will
                    understand what it is about – so how can the staff follow it
                </li>
                <li style="margin-bottom: 25px; padding-left: 35px; position: relative; line-height: 1.7;">
                    <span style="position: absolute; left: 0; top: 0; font-size: 1.5em; color: #f5576c;">•</span>
                    By the time you/someone in your team has adjusted the clauses so that it does relate to your organisation,
                    they might as well have started from scratch.
                </li>
                <li style="margin-bottom: 25px; padding-left: 35px; position: relative; line-height: 1.7;">
                    <span style="position: absolute; left: 0; top: 0; font-size: 1.5em; color: #f5576c;">•</span>
                    The templates will not detail the way you will actually be working (so you have to run it as an extra
                    task in parallel to your own controls that you already use – ie extra work)
                </li>
                <li style="padding-left: 35px; position: relative; line-height: 1.7;">
                    <span style="position: absolute; left: 0; top: 0; font-size: 1.5em; color: #f5576c;">•</span>
                    <strong>It will not help you to achieve the goals you are getting the standard for:</strong>
                    <ul style="margin-top: 15px; list-style: none; padding: 0;">
                        <li style="margin-bottom: 12px; padding-left: 25px; position: relative;">
                            <span style="position: absolute; left: 0; color: #999;">→</span>
                            If you want the standard to improve your operations: it won't – as the templates do not relate
                            to your operations without totally rewriting them
                        </li>
                        <li style="margin-bottom: 12px; padding-left: 25px; position: relative;">
                            <span style="position: absolute; left: 0; color: #999;">→</span>
                            If you want the standard to meet tender requirements – you might have certification, but so will
                            all others applying and if any of them actually have a proper system supporting it, they will be
                            better than you and you will not get the tender anyway
                        </li>
                        <li style="padding-left: 25px; position: relative;">
                            <span style="position: absolute; left: 0; color: #999;">→</span>
                            If you want the standard to improve your staff capabilities – it won't as they will recognise
                            that you have cut corners plus they will likely be confused by the fact there seem to be 2 parallel
                            systems one of which they don't recognise
                        </li>
                    </ul>
                </li>
            </ul>
        </div>
    </section>

    <!-- Solution Section -->
    <section style="background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%); padding: 40px; border-radius: 15px; margin-bottom: 40px; border-left: 5px solid #667eea;">
        <h2 style="font-size: 2em; color: #1e3a5f; margin-bottom: 25px;">
            ✅ So what does a good Management System achieve?
        </h2>

        <div style="background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
            <p style="font-size: 1.05em; color: #333; margin-bottom: 25px; font-weight: 500;">
                A good control system:
            </p>
            <ul style="list-style: none; padding: 0; margin: 0;">
                <li style="margin-bottom: 20px; padding-left: 35px; position: relative; line-height: 1.7;">
                    <span style="position: absolute; left: 0; top: 0; font-size: 1.5em; color: #667eea;">✓</span>
                    reduces the time you spend on the system,
                </li>
                <li style="margin-bottom: 20px; padding-left: 35px; position: relative; line-height: 1.7;">
                    <span style="position: absolute; left: 0; top: 0; font-size: 1.5em; color: #667eea;">✓</span>
                    matches what you do already as much as possible,
                </li>
                <li style="margin-bottom: 20px; padding-left: 35px; position: relative; line-height: 1.7;">
                    <span style="position: absolute; left: 0; top: 0; font-size: 1.5em; color: #667eea;">✓</span>
                    its within your normal procedures so you don't have extra work,
                </li>
                <li style="margin-bottom: 20px; padding-left: 35px; position: relative; line-height: 1.7;">
                    <span style="position: absolute; left: 0; top: 0; font-size: 1.5em; color: #667eea;">✓</span>
                    is understood and used by everyone in the organisation,
                </li>
                <li style="margin-bottom: 20px; padding-left: 35px; position: relative; line-height: 1.7;">
                    <span style="position: absolute; left: 0; top: 0; font-size: 1.5em; color: #667eea;">✓</span>
                    the improvements continue to develop year by year for ever,
                </li>
                <li style="padding-left: 35px; position: relative; line-height: 1.7;">
                    <span style="position: absolute; left: 0; top: 0; font-size: 1.5em; color: #667eea;">✓</span>
                    the financial return and profitability improve too.
                </li>
            </ul>
        </div>

        <div style="margin-top: 30px; padding: 25px; background: white; border-radius: 10px; border-left: 4px solid #4facfe;">
            <p style="font-size: 1.05em; line-height: 1.7; color: #333; margin: 0;">
                <strong style="color: #1e3a5f;">Finally, and often most importantly,</strong> because you have business
                systems that achieve this, your organisation becomes one that others want to work with – so you will win
                tenders as well.
            </p>
        </div>
    </section>

    <!-- Conclusion -->
    <section style="font-size: 1.1em; line-height: 1.8; color: #333; margin-bottom: 50px;">
        <h2 style="font-size: 1.8em; color: #1e3a5f; margin-bottom: 20px;">
            The Bottom Line
        </h2>
        <p style="margin-bottom: 20px; font-weight: 500; color: #f5576c; font-size: 1.15em;">
            From a cost efficiency point of view, I would never recommend that anyone use templates.
        </p>
        <p style="margin-bottom: 20px;">
            You can choose whoever you like as a consultant, but even if they are bad, they will be better than using
            most templates that I have ever seen.
        </p>
        <p>
            <strong>So contact us to have a free, no obligation conversation about how to take things forwards.</strong>
            It will cost you to get a consultant in. But it will cost you if you use templates as that will be totally
            wasted money. With any reasonable consultant you will get systems that match what you do in a way that
            following them is easy.
        </p>
    </section>

    <!-- CTA Section -->
    <section style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 50px 40px; border-radius: 15px; text-align: center; color: white; box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);">
        <h3 style="font-size: 2em; margin-bottom: 20px; color: white;">
            Ready to Build a Proper ISO System?
        </h3>
        <p style="font-size: 1.2em; margin-bottom: 30px; opacity: 0.95;">
            Get a free, no-obligation consultation with our expert team
        </p>
        <div style="margin-bottom: 25px;">
            <a href="/contact/" style="background: white; color: #667eea; padding: 15px 40px; border-radius: 50px; text-decoration: none; font-size: 1.1em; display: inline-block; font-weight: 600; margin: 10px; transition: all 0.3s ease;">
                Contact Us
            </a>
            <a href="tel:03456006975" style="background: transparent; color: white; padding: 15px 40px; border-radius: 50px; text-decoration: none; font-size: 1.1em; display: inline-block; font-weight: 600; margin: 10px; border: 2px solid white; transition: all 0.3s ease;">
                📞 0345 600 6975
            </a>
        </div>
        <a href="mailto:carl.kruger@qualitation.co.uk" style="color: white; opacity: 0.9; text-decoration: underline; font-size: 1.05em;">
            carl.kruger@qualitation.co.uk
        </a>
    </section>

</article>

<style>
    article a:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
</style>
'''

            # Create the page
            page = FlexiblePage(
                title="Don't use templates to achieve an ISO Standard",
                slug='dont-use-templates-to-achieve-an-iso-standard',
                intro='Why you should not use someone else\'s templates to \'help\' you attain an ISO Certification',
                seo_title="Don't use templates to achieve ISO standards | Qualitation",
                search_description='Learn why using ISO templates is counterproductive and how a properly tailored management system delivers real business value and competitive advantage.',
                show_in_menus=False,
                body=[
                    {
                        'type': 'html',
                        'value': {'html': article_html},
                        'id': str(uuid.uuid4())
                    }
                ]
            )

            # Add to home page
            home_page.add_child(instance=page)

            # Save and publish
            page.save_revision().publish()

            self.stdout.write(self.style.SUCCESS('✓ Created Templates article page'))
            self.stdout.write(self.style.SUCCESS(f'✓ URL: /dont-use-templates-to-achieve-an-iso-standard/'))
            self.stdout.write(self.style.SUCCESS('✓ Page published successfully'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ Error: {e}'))
            import traceback
            traceback.print_exc()

        self.stdout.write(self.style.SUCCESS('\n=== Complete ===\n'))
