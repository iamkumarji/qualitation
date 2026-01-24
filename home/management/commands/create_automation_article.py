"""
Django management command to create the Automation article page
"""

from django.core.management.base import BaseCommand
from home.models import FlexiblePage
from wagtail.models import Page
import uuid


class Command(BaseCommand):
    help = 'Create the Automation ISO article page'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('\n=== Creating Automation Article Page ===\n'))

        try:
            # Get the home page as parent
            home_page = Page.objects.get(slug='home')

            # Check if page already exists
            if FlexiblePage.objects.filter(slug='automation-is-the-future-for-iso-standards').exists():
                self.stdout.write(self.style.WARNING('✗ Page already exists, deleting old version...'))
                old_page = FlexiblePage.objects.get(slug='automation-is-the-future-for-iso-standards')
                old_page.delete()

            # Create the article HTML content
            article_html = '''
<article style="max-width: 900px; margin: 0 auto; padding: 40px 20px;">

    <!-- Header -->
    <header style="margin-bottom: 40px; border-bottom: 3px solid #4facfe; padding-bottom: 30px;">
        <div style="color: #999; font-size: 0.95em; margin-bottom: 15px; text-transform: uppercase; letter-spacing: 1px;">
            📅 24 October 2019
        </div>
        <h1 style="font-size: 2.8em; color: #1e3a5f; margin-bottom: 20px; line-height: 1.2;">
            Automation is the future for ISO Standards!
        </h1>
    </header>

    <!-- Introduction -->
    <div style="font-size: 1.1em; line-height: 1.8; color: #333; margin-bottom: 40px;">
        <p style="margin-bottom: 20px;">
            We have all seen the headlines telling us that robots are taking over in manufacturing and we have had many
            versions of the science fiction theory that robots will take over the world – well it is coming closer!
        </p>
        <p style="margin-bottom: 20px; font-weight: 500; color: #4facfe;">
            Rest assured, I am not referring to a military takeover, nor anything detrimental at all actually!
        </p>
        <p style="margin-bottom: 20px;">
            I am referring to the fact that more and more the possibility exists to have programmes take over some of the
            grunt work behind bureaucracy and tedious repetitive daily grind. Throw in the fact that when it is hooked up
            correctly, this results in better re ordering of details, trends, nuances and patterns and you can see how these
            can be better analysed to identify more sensitive indicators to market directions, more precise spotting of
            quality issues at earlier stages and quicker response times to issues before they turn into problems, than ever before.
        </p>
    </div>

    <!-- Benefits Section -->
    <section style="background: linear-gradient(135deg, #e0f7fa 0%, #b2ebf2 100%); padding: 40px; border-radius: 15px; margin-bottom: 40px; border-left: 5px solid #4facfe;">
        <h2 style="font-size: 2em; color: #1e3a5f; margin-bottom: 25px;">
            🎯 The Impact
        </h2>
        <div style="background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
            <p style="font-size: 1.05em; line-height: 1.8; color: #333; margin-bottom: 20px;">
                What is happening is an ability to <strong>ascertain the root causes earlier</strong> – leading to prompter
                action and resulting in:
            </p>
            <ul style="list-style: none; padding: 0; margin: 0;">
                <li style="margin-bottom: 15px; padding-left: 35px; position: relative; line-height: 1.7;">
                    <span style="position: absolute; left: 0; top: 0; font-size: 1.3em; color: #f5576c;">↓</span>
                    Less downtime
                </li>
                <li style="margin-bottom: 15px; padding-left: 35px; position: relative; line-height: 1.7;">
                    <span style="position: absolute; left: 0; top: 0; font-size: 1.3em; color: #f5576c;">↓</span>
                    Less financial loss
                </li>
                <li style="margin-bottom: 25px; padding-left: 35px; position: relative; line-height: 1.7;">
                    <span style="position: absolute; left: 0; top: 0; font-size: 1.3em; color: #f5576c;">↓</span>
                    Less customer dissatisfaction
                </li>
            </ul>
            <p style="font-size: 1.05em; line-height: 1.8; color: #333; margin-bottom: 20px;">
                Alternatively, it allows us to see where we can improve further than ever before with:
            </p>
            <ul style="list-style: none; padding: 0; margin: 0;">
                <li style="margin-bottom: 15px; padding-left: 35px; position: relative; line-height: 1.7;">
                    <span style="position: absolute; left: 0; top: 0; font-size: 1.3em; color: #4facfe;">↑</span>
                    More productivity
                </li>
                <li style="margin-bottom: 15px; padding-left: 35px; position: relative; line-height: 1.7;">
                    <span style="position: absolute; left: 0; top: 0; font-size: 1.3em; color: #4facfe;">↑</span>
                    More profit
                </li>
                <li style="padding-left: 35px; position: relative; line-height: 1.7;">
                    <span style="position: absolute; left: 0; top: 0; font-size: 1.3em; color: #4facfe;">↑</span>
                    More customer and staff satisfaction
                </li>
            </ul>
        </div>
    </section>

    <!-- Revolution Section -->
    <div style="font-size: 1.1em; line-height: 1.8; color: #333; margin-bottom: 40px;">
        <h2 style="font-size: 2em; color: #1e3a5f; margin-bottom: 20px;">
            🤖 Where is This Revolution?
        </h2>
        <p style="margin-bottom: 20px;">
            Actually, it is not that new – it has been happening piecemeal in the background for a while, but it is starting
            to break through to mainstream. It is in the daily control of systems. Documentation, training, auditing and
            purchasing have experienced this already and now it is moving into development of management systems, installation
            of controls and cross checking of activities.
        </p>
        <p style="margin-bottom: 20px; padding: 20px; background: #f0f9ff; border-left: 4px solid #4facfe; border-radius: 5px;">
            <strong>Specifically, the ISO Business Management systems are getting automated.</strong> While there is still
            need for human control of the systems, the installations are becoming sufficiently automated that there will be
            a time when ISO consultancy will fall away.
        </p>
        <p style="margin-bottom: 20px; font-style: italic; color: #666;">
            Remember – this is my field – I run a network of ISO consultants – and I am predicting that our work will decline.
            I prefer to say it as I see it and note, as I certainly feel, that it is better to go with the flow. This will
            happen more and more and we should not stand in the way and expect the changes to go away!
        </p>
    </div>

    <!-- Advantages Section -->
    <section style="background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%); padding: 40px; border-radius: 15px; margin-bottom: 40px; border-left: 5px solid #66bb6a;">
        <h2 style="font-size: 2em; color: #1e3a5f; margin-bottom: 25px;">
            ✅ Advantages of Automated ISO Systems
        </h2>
        <p style="font-size: 1.05em; color: #333; margin-bottom: 25px;">
            I know of several automated ISO system programmes now – in 9001, 14001, 45001 and 27001 – with more to come.
            They offer a number of advantages:
        </p>

        <div style="background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
            <ul style="list-style: none; padding: 0; margin: 0;">
                <li style="margin-bottom: 20px; padding-left: 35px; position: relative; line-height: 1.7;">
                    <span style="position: absolute; left: 0; top: 0; font-size: 1.5em; color: #66bb6a;">✓</span>
                    They are as fast or slow to install as the organisation wants them to be
                </li>
                <li style="margin-bottom: 20px; padding-left: 35px; position: relative; line-height: 1.7;">
                    <span style="position: absolute; left: 0; top: 0; font-size: 1.5em; color: #66bb6a;">✓</span>
                    They ensure that you have everything you need to gain certification
                </li>
                <li style="margin-bottom: 20px; padding-left: 35px; position: relative; line-height: 1.7;">
                    <span style="position: absolute; left: 0; top: 0; font-size: 1.5em; color: #66bb6a;">✓</span>
                    They provide direct links between what you do and the clauses in the Standards
                </li>
                <li style="margin-bottom: 20px; padding-left: 35px; position: relative; line-height: 1.7;">
                    <span style="position: absolute; left: 0; top: 0; font-size: 1.5em; color: #66bb6a;">✓</span>
                    The auditing by the certifier is facilitated as everything is in the history logs
                </li>
                <li style="margin-bottom: 20px; padding-left: 35px; position: relative; line-height: 1.7;">
                    <span style="position: absolute; left: 0; top: 0; font-size: 1.5em; color: #66bb6a;">✓</span>
                    They can be installed without additional ISO consultants in many cases
                </li>
                <li style="margin-bottom: 20px; padding-left: 35px; position: relative; line-height: 1.7;">
                    <span style="position: absolute; left: 0; top: 0; font-size: 1.5em; color: #66bb6a;">✓</span>
                    They can be installed with less ISO consultancy in all cases
                </li>
                <li style="margin-bottom: 20px; padding-left: 35px; position: relative; line-height: 1.7;">
                    <span style="position: absolute; left: 0; top: 0; font-size: 1.5em; color: #66bb6a;">✓</span>
                    Over time your organisation will know and understand the systems far deeper
                </li>
                <li style="padding-left: 35px; position: relative; line-height: 1.7;">
                    <span style="position: absolute; left: 0; top: 0; font-size: 1.5em; color: #66bb6a;">✓</span>
                    <strong style="color: #66bb6a;">They can be up to 10 times cheaper to install than previously!</strong>
                </li>
            </ul>
        </div>
    </section>

    <!-- Disadvantages Section -->
    <section style="background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%); padding: 40px; border-radius: 15px; margin-bottom: 40px; border-left: 5px solid #ff9800;">
        <h2 style="font-size: 2em; color: #1e3a5f; margin-bottom: 25px;">
            ⚠️ Some Considerations
        </h2>
        <p style="font-size: 1.05em; color: #333; margin-bottom: 25px;">
            There are some disadvantages too:
        </p>

        <div style="background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
            <ul style="list-style: none; padding: 0; margin: 0;">
                <li style="margin-bottom: 20px; padding-left: 35px; position: relative; line-height: 1.7;">
                    <span style="position: absolute; left: 0; top: 0; font-size: 1.3em; color: #ff9800;">⚡</span>
                    If you don't know anything about ISO standards, this may be quite a learning curve – but that was going
                    to be the case anyway – it is just that you may not have an ISO consultant to hand with the automated systems
                </li>
                <li style="margin-bottom: 20px; padding-left: 35px; position: relative; line-height: 1.7;">
                    <span style="position: absolute; left: 0; top: 0; font-size: 1.3em; color: #ff9800;">⚡</span>
                    You may find that you are not sure where to stop – adding controls where they are not needed
                </li>
                <li style="padding-left: 35px; position: relative; line-height: 1.7;">
                    <span style="position: absolute; left: 0; top: 0; font-size: 1.3em; color: #ff9800;">⚡</span>
                    Combining them with existing ISO systems will be more difficult unless the existing systems shift to
                    automated set-ups as well (but that would potentially be cheaper in the long run anyway)
                </li>
            </ul>
        </div>
    </section>

    <!-- Additional Considerations -->
    <div style="font-size: 1.1em; line-height: 1.8; color: #333; margin-bottom: 40px;">
        <h2 style="font-size: 2em; color: #1e3a5f; margin-bottom: 20px;">
            💡 Other Areas of Interest
        </h2>

        <div style="background: #f8f9fa; padding: 25px; border-radius: 10px; margin-bottom: 20px; border-left: 4px solid #667eea;">
            <p style="margin: 0; line-height: 1.7;">
                <strong>Industry-Specific Standards:</strong> Those standards specific to particular industries sectors
                (aviation, automotive, medical devices, laboratory competence etc) will still require a specialist consultant
                if the organisation has never used the standard before. They are simply too complex and too uniquely focused
                to let programmes sort this kind of approach at this time (maybe not for ever, but it will be quite a while).
            </p>
        </div>

        <div style="background: #f8f9fa; padding: 25px; border-radius: 10px; margin-bottom: 20px; border-left: 4px solid #4facfe;">
            <p style="margin: 0; line-height: 1.7;">
                <strong>Revolution in Certification Auditing:</strong> Auditing of automated systems will revolutionise
                certification – with assessment visits being capable of being carried out from offsite (via cloud) – not
                every year and not for all aspects of the system, but enough that costs should come down and certifiers
                become more flexible. This is my opinion, rather than fact, but there seem to me to be enough smaller
                certifiers that will do this to improve their business reach that others will get left behind if they don't
                follow suit.
            </p>
        </div>
    </div>

    <!-- Conclusion -->
    <section style="font-size: 1.1em; line-height: 1.8; color: #333; margin-bottom: 50px;">
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 40px; border-radius: 15px; color: white;">
            <h2 style="font-size: 2em; margin-bottom: 20px; color: white;">
                The Bottom Line
            </h2>
            <p style="margin-bottom: 20px; font-size: 1.15em;">
                <strong>Automation is here to stay and early movers get a huge advantage over late-comers</strong> – namely
                that their systems will be less demanding of human time – and consequently should be more productive.
            </p>
            <p style="margin: 0; opacity: 0.95;">
                With productivity being the current focus of attention in the UK's economic markets (again), this should
                sound a very attractive proposition.
            </p>
        </div>
    </section>

    <!-- CTA Section -->
    <section style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); padding: 50px 40px; border-radius: 15px; text-align: center; color: white; box-shadow: 0 10px 30px rgba(79, 172, 254, 0.3);">
        <h3 style="font-size: 2em; margin-bottom: 20px; color: white;">
            Want to Find Out More?
        </h3>
        <p style="font-size: 1.2em; margin-bottom: 30px; opacity: 0.95;">
            Discover how automation can transform your ISO management systems
        </p>
        <div style="margin-bottom: 25px;">
            <a href="/contact/" style="background: white; color: #4facfe; padding: 15px 40px; border-radius: 50px; text-decoration: none; font-size: 1.1em; display: inline-block; font-weight: 600; margin: 10px; transition: all 0.3s ease;">
                Contact Us
            </a>
            <a href="tel:03458006975" style="background: transparent; color: white; padding: 15px 40px; border-radius: 50px; text-decoration: none; font-size: 1.1em; display: inline-block; font-weight: 600; margin: 10px; border: 2px solid white; transition: all 0.3s ease;">
                📞 0345 800 6975
            </a>
        </div>
        <p style="margin: 0; opacity: 0.9; font-size: 1.05em;">
            Contact Carl Kruger for expert guidance
        </p>
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
                title="Automation is the future for ISO Standards!",
                slug='automation-is-the-future-for-iso-standards',
                intro='Discusses how robots and automation are increasingly prevalent in manufacturing and ISO Standards implementation',
                seo_title="Automation is the future for ISO Standards | Qualitation",
                search_description='Explore how automated ISO management systems are revolutionizing certification processes, reducing costs, and improving efficiency across industries.',
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

            self.stdout.write(self.style.SUCCESS('✓ Created Automation article page'))
            self.stdout.write(self.style.SUCCESS(f'✓ URL: /automation-is-the-future-for-iso-standards/'))
            self.stdout.write(self.style.SUCCESS('✓ Page published successfully'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ Error: {e}'))
            import traceback
            traceback.print_exc()

        self.stdout.write(self.style.SUCCESS('\n=== Complete ===\n'))
