"""
Django management command to create the "What is an ISO Standard for?" article
"""

from django.core.management.base import BaseCommand
from home.models import ArticleIndexPage, ArticlePage
import datetime


class Command(BaseCommand):
    help = 'Create the ISO Standard article'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('\n=== Creating ISO Standard Article ===\n'))

        try:
            # Get the Resources/ArticleIndex page
            resources_page = ArticleIndexPage.objects.get(slug='resources')

            # Check if article already exists
            if ArticlePage.objects.filter(slug='what-is-an-iso-standard-for').exists():
                self.stdout.write(self.style.WARNING('Article already exists, deleting old version...'))
                old_article = ArticlePage.objects.get(slug='what-is-an-iso-standard-for')
                old_article.delete()

            # Article content
            article_body = '''
<p style="font-size: 1.15em; font-weight: 500; color: #1e3a5f; margin-bottom: 30px;">
    Everyone wants to buy good quality goods and services for a realistic value.
</p>

<p>To supply such goods and services, requires those organisations supplying them to be:</p>

<div style="background: #f8f9fa; padding: 30px; border-radius: 10px; margin: 30px 0;">
    <ul style="list-style: none; padding: 0; margin: 0;">
        <li style="margin-bottom: 20px; padding-left: 35px; position: relative; line-height: 1.7;">
            <span style="position: absolute; left: 0; top: 0; font-size: 1.5em; color: #30b566;">✓</span>
            <strong>Efficient</strong> – making as much as possible out of as little as possible with minimal waste
        </li>
        <li style="margin-bottom: 20px; padding-left: 35px; position: relative; line-height: 1.7;">
            <span style="position: absolute; left: 0; top: 0; font-size: 1.5em; color: #30b566;">✓</span>
            <strong>Effective</strong> – co-ordinating their processes well to avoid delays
        </li>
        <li style="margin-bottom: 20px; padding-left: 35px; position: relative; line-height: 1.7;">
            <span style="position: absolute; left: 0; top: 0; font-size: 1.5em; color: #30b566;">✓</span>
            <strong>Quality-focused</strong> – ensuring that the product/service does what it is supposed to do accurately, well and repeatedly
        </li>
        <li style="padding-left: 35px; position: relative; line-height: 1.7;">
            <span style="position: absolute; left: 0; top: 0; font-size: 1.5em; color: #30b566;">✓</span>
            <strong>Productive</strong> – making more per person
        </li>
    </ul>
</div>

<p style="margin: 30px 0; font-size: 1.05em;">
    The more they succeed in meeting these goals, the more they will be seen as providing value in the form of good quality services and products – and will profit accordingly.
</p>

<h2 style="color: #1e3a5f; margin-top: 50px; margin-bottom: 20px; font-size: 2em;">
    Optimizing Performance
</h2>

<p>To optimise these goals, they need to be as good at them as possible – so they learn from what others have done before, combining ideas from here, shortcuts from there and alternatives from elsewhere (from all over the globe) to reach as high as they can in each case.</p>

<div style="background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%); padding: 30px; border-radius: 15px; margin: 30px 0; border-left: 5px solid #30b566;">
    <p style="margin: 0; font-size: 1.1em; line-height: 1.7;">
        This results in: <strong>increased profits</strong>, <strong>increased customer satisfaction</strong>,
        <strong>increased staff morale</strong>, <strong>decreased wastage</strong>, <strong>decreased risk</strong>
        and <strong>decreased problems</strong>.
    </p>
</div>

<h2 style="color: #1e3a5f; margin-top: 50px; margin-bottom: 20px; font-size: 2em;">
    So how to prove their worth?
</h2>

<p>Any organisation that wants to demonstrate that it recognises these beneficial goals and is working towards them (it is a continuous process for even the best organisations – standing still means falling behind) can use the ISO certification as proof of its actual activities in this area.</p>

<h2 style="color: #1e3a5f; margin-top: 50px; margin-bottom: 20px; font-size: 2em;">
    How does certification to an ISO standard help?
</h2>

<p>Any other organisation that wants a supplier that strives for the best, will then see such ISO certification and know that an organisation that has an ISO Standard, is one to be trusted to:</p>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin: 30px 0;">
    <div style="background: white; padding: 20px; border-radius: 10px; border-left: 4px solid #30b566; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
        <strong style="color: #30b566;">Go Further</strong>
    </div>
    <div style="background: white; padding: 20px; border-radius: 10px; border-left: 4px solid #30b566; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
        <strong style="color: #30b566;">Do Better</strong>
    </div>
    <div style="background: white; padding: 20px; border-radius: 10px; border-left: 4px solid #30b566; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
        <strong style="color: #30b566;">Last Longer</strong>
    </div>
    <div style="background: white; padding: 20px; border-radius: 10px; border-left: 4px solid #30b566; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
        <strong style="color: #30b566;">Meet Specs Better</strong>
    </div>
    <div style="background: white; padding: 20px; border-radius: 10px; border-left: 4px solid #30b566; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
        <strong style="color: #30b566;">React Faster</strong>
    </div>
    <div style="background: white; padding: 20px; border-radius: 10px; border-left: 4px solid #30b566; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
        <strong style="color: #30b566;">Be More Economic</strong>
    </div>
</div>

<p style="font-size: 1.1em; font-weight: 500; color: #30b566; margin: 30px 0;">
    Why wouldn't they choose them?
</p>

<h2 style="color: #1e3a5f; margin-top: 50px; margin-bottom: 20px; font-size: 2em;">
    So how does an ISO Standard work?
</h2>

<p>The ISO Standards provide a framework to optimise good practice in any organisation. Each procedure (usually between 8 and 15 in a typical organisation) lays out certain steps that the best organisation practice involves and ensures that they are followed.</p>

<p>The Standards, since they apply equally to any operational practice around the globe, are perforce generic in their writing, but once adapted for the specifics of each organisation, they make a blueprint for optimum operation.</p>

<div style="background: #f0f7ff; padding: 30px; border-radius: 15px; margin: 30px 0; border-left: 5px solid #2196f3;">
    <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 15px;">
        📊 ISO Standards by the Numbers
    </h3>
    <p style="margin-bottom: 15px;">
        Different ISO Standards cover a wide range of areas of interest: the most common being the <strong>ISO 9001 Quality standard</strong> with over <strong>1,000,000 organisations</strong> around the world holding a certification in this standard at any one time.
    </p>
    <p style="margin-bottom: 15px;">
        By comparison, this is over <strong>10 times the number</strong> of organisations that have the well-known Investors in Industry award.
    </p>
    <p style="margin: 0;">
        In total there are over <strong>22,000 standards</strong> currently – many covering small areas in niche markets perhaps, but all impacting on our everyday life: scaffolding erections, manufacturing processes, chemical reactions, building strengths and many others each have their ISO standard.
    </p>
</div>

<h2 style="color: #1e3a5f; margin-top: 50px; margin-bottom: 20px; font-size: 2em;">
    What is involved in getting an ISO Standard?
</h2>

<p>To get an ISO Standard requires following the principles of globally accepted good practice – of which, most modern organisations are already aware.</p>

<p>There are some regular omissions – usually involving:</p>

<ul style="margin: 20px 0; padding-left: 30px;">
    <li style="margin-bottom: 10px;">Internal audits</li>
    <li style="margin-bottom: 10px;">Tighter documentation controls</li>
    <li>Management reviews</li>
</ul>

<p>These are easily remedied and actually go a long way to making a huge difference in how the organisation moves forward from that point on. Adoption of these approaches (by changing existing procedures to take them into account) brings with it the rewards already highlighted above.</p>

<div style="background: #fff3e0; padding: 30px; border-radius: 15px; margin: 30px 0; border-left: 5px solid #ff9800;">
    <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 15px;">
        ⚡ Certification Process
    </h3>
    <p style="margin-bottom: 15px;">
        Once the ISO systems and procedures are in place, they are assessed by third party examiners (called certifiers) to ensure that all is working well.
    </p>
    <p style="margin-bottom: 15px;">
        <strong>Make sure</strong> to get the full ISO controls in place, that you use certifiers that are assessed (in the UK) by UKAS as this is the ISO accepted route – and no other.
    </p>
    <p style="margin: 0;">
        Certification is re-assessed annually so anyone seeing an ISO Certificate knows that it is current, and the organisation is operating at high levels of good practice – not just years ago when it got the first certificate, but right up to the present day.
    </p>
</div>

<h2 style="color: #1e3a5f; margin-top: 50px; margin-bottom: 20px; font-size: 2em;">
    Do ISO Standards really work – do they even pay for themselves?
</h2>

<p style="font-size: 1.1em; line-height: 1.8;">
    Much work has been carried out to determine the impact of holding an ISO Standard on the performance of the organisation – and the repeated finding is that the attaining of an ISO standard, when it is followed up correctly, is that it <strong style="color: #30b566;">more than pays for itself again and again over the years</strong>.
</p>

<p>Many organisations at the top of their market niche can look back to the beginning of their rise in ability, recognition and results, to the attainment of the ISO standard that pushed them on the way.</p>

<h2 style="color: #1e3a5f; margin-top: 50px; margin-bottom: 20px; font-size: 2em;">
    So, who really uses and believes in ISO standards?
</h2>

<p style="font-size: 1.15em; font-weight: 500; margin-bottom: 20px;">
    Who doesn't – there are a huge range of advocates:
</p>

<div style="display: flex; flex-wrap: wrap; gap: 15px; margin: 30px 0;">
    <span style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 12px 24px; border-radius: 50px; font-weight: 600;">Government</span>
    <span style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); color: white; padding: 12px 24px; border-radius: 50px; font-weight: 600;">Manufacturers</span>
    <span style="background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%); color: white; padding: 12px 24px; border-radius: 50px; font-weight: 600;">Lawyers</span>
    <span style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); color: white; padding: 12px 24px; border-radius: 50px; font-weight: 600;">Environmentalists</span>
    <span style="background: linear-gradient(135deg, #30b566 0%, #56d882 100%); color: white; padding: 12px 24px; border-radius: 50px; font-weight: 600;">Scientists</span>
</div>

<p style="margin: 30px 0;">
    All of whom value and often insist on dealing only with organisations that have ISO standards.
</p>

<h2 style="color: #1e3a5f; margin-top: 50px; margin-bottom: 20px; font-size: 2em;">
    So, what next?
</h2>

<div style="background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%); padding: 40px; border-radius: 15px; margin: 40px 0; color: white;">
    <p style="font-size: 1.15em; line-height: 1.8; margin-bottom: 20px;">
        Qualitation has been providing consultancy services in the field of ISO standards and related business management improvements for <strong>over 25 years</strong> – and in that time we have a <strong>100% record at gaining certification for our clients first time every time</strong>.
    </p>
    <div style="display: flex; gap: 15px; flex-wrap: wrap; margin-top: 25px;">
        <a href="tel:03456006975" style="background: white; color: #1e3a5f; padding: 12px 30px; border-radius: 50px; text-decoration: none; font-weight: 600; display: inline-block;">
            📞 0345 600 6975
        </a>
        <a href="/iso-standards/" style="background: rgba(255,255,255,0.2); color: white; padding: 12px 30px; border-radius: 50px; text-decoration: none; font-weight: 600; display: inline-block; border: 2px solid white;">
            View ISO Standards
        </a>
    </div>
</div>
'''

            # Create the article
            article = ArticlePage(
                title="What is an ISO Standard for?",
                slug='what-is-an-iso-standard-for',
                date=datetime.date(2019, 10, 8),
                intro='Everyone wants to buy good quality goods and services for a realistic value. Explores how ISO Standards help organizations optimize quality',
                body=article_body,
                author='Qualitation Team',
                card_gradient_start='#30b566',
                card_gradient_end='#56d882',
                show_in_menus=False,
            )

            # Add to resources page
            resources_page.add_child(instance=article)
            article.save_revision().publish()

            self.stdout.write(self.style.SUCCESS('✓ Created ISO Standard article'))
            self.stdout.write(self.style.SUCCESS(f'✓ URL: /resources/what-is-an-iso-standard-for/'))
            self.stdout.write(self.style.SUCCESS('✓ Published successfully'))

        except ArticleIndexPage.DoesNotExist:
            self.stdout.write(self.style.ERROR('✗ Resources page not found'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ Error: {e}'))
            import traceback
            traceback.print_exc()

        self.stdout.write(self.style.SUCCESS('\n=== Complete ===\n'))
