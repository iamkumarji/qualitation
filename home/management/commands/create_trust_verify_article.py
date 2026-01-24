"""
Django management command to create the "Trust but Verify" article
"""

from django.core.management.base import BaseCommand
from home.models import ArticleIndexPage, ArticlePage
import datetime


class Command(BaseCommand):
    help = 'Create the Trust but Verify article'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('\n=== Creating Trust but Verify Article ===\n'))

        try:
            # Get the Resources/ArticleIndex page
            resources_page = ArticleIndexPage.objects.get(slug='resources')

            # Check if article already exists
            if ArticlePage.objects.filter(slug='trust-but-verify').exists():
                self.stdout.write(self.style.WARNING('Article already exists, deleting old version...'))
                old_article = ArticlePage.objects.get(slug='trust-but-verify')
                old_article.delete()

            # Article content
            article_body = '''
<div style="background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%); padding: 30px; border-radius: 15px; margin-bottom: 40px; border-left: 5px solid #ff9800;">
    <h2 style="color: #1e3a5f; margin-top: 0; margin-bottom: 15px; font-size: 1.8em;">
        Why quality cannot be left to chance and how it can be automated?
    </h2>
</div>

<p>Every organisation has its own way of operating – its own idiosyncrasies and mindsets. But despite there being many alternative routes to attaining quality products, the common themes will be the same:</p>

<div style="background: #f8f9fa; padding: 30px; border-radius: 10px; margin: 30px 0;">
    <ul style="list-style: none; padding: 0; margin: 0;">
        <li style="margin-bottom: 15px; padding-left: 35px; position: relative; line-height: 1.7;">
            <span style="position: absolute; left: 0; top: 0; font-size: 1.3em; color: #ff9800;">◆</span>
            Everything knowing what they are to do
        </li>
        <li style="margin-bottom: 15px; padding-left: 35px; position: relative; line-height: 1.7;">
            <span style="position: absolute; left: 0; top: 0; font-size: 1.3em; color: #ff9800;">◆</span>
            Those actions interleaving successfully with each other
        </li>
        <li style="margin-bottom: 15px; padding-left: 35px; position: relative; line-height: 1.7;">
            <span style="position: absolute; left: 0; top: 0; font-size: 1.3em; color: #ff9800;">◆</span>
            Checking that what should have happened actually did happen
        </li>
        <li style="margin-bottom: 15px; padding-left: 35px; position: relative; line-height: 1.7;">
            <span style="position: absolute; left: 0; top: 0; font-size: 1.3em; color: #ff9800;">◆</span>
            Ensuring that future goals are written into the procedures of the organisation to guarantee their accomplishment
        </li>
        <li style="padding-left: 35px; position: relative; line-height: 1.7;">
            <span style="position: absolute; left: 0; top: 0; font-size: 1.3em; color: #ff9800;">◆</span>
            And so on…
        </li>
    </ul>
</div>

<h2 style="color: #1e3a5f; margin-top: 50px; margin-bottom: 20px; font-size: 2em;">
    🔍 Trust but Verify
</h2>

<p style="font-size: 1.1em; font-style: italic; color: #666; margin-bottom: 25px;">
    Originally a Russian proverb that was popularised by Ronald Reagan during the Nuclear Weapons Talks
</p>

<p>One on the list that is not often recognised, but is always there, is equivalent to the "Trust but Verify" phrase.</p>

<div style="background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%); padding: 30px; border-radius: 15px; margin: 30px 0; border-left: 5px solid #2196f3;">
    <p style="margin: 0; line-height: 1.8; font-size: 1.05em;">
        This relates to the fact that <strong>"Quality"</strong> is a difficult to item to quantify – not least as each person's definition of what constitutes Quality varies somewhat from the next. Therefore, the only way that the organisation's definition can be maintained is through <strong>regular checks</strong>.
    </p>
</div>

<p>Globally accepted best practice in this area relates to the use of <strong>internal audits</strong> combined with encouraging <strong>feedback from customers, assessors and staff</strong>. When combined with Board goals and the organisational Quality definition, the result is a regime of oversight, cross-checks and tracked reactions that ensures that the organisation's activities achieve what they are intended to do.</p>

<h2 style="color: #1e3a5f; margin-top: 50px; margin-bottom: 20px; font-size: 2em;">
    🔗 Complex Supply Chains
</h2>

<p>With detailed and complex supply patterns, this becomes even more necessary. Products made by one company are components of another's offering to a third which make up the sub-components of others again – until the final product (maybe an aircraft, a satellite or a vehicle) is completed.</p>

<div style="background: white; padding: 25px; border-radius: 10px; border: 2px solid #ff9800; margin: 30px 0;">
    <p style="margin: 0; font-weight: 500; color: #1e3a5f; font-size: 1.05em;">
        The only way that the final product's quality can be maintained is by ensuring that all the individual sub-components are correctly designed, made and utilised.
    </p>
</div>

<h2 style="color: #1e3a5f; margin-top: 50px; margin-bottom: 20px; font-size: 2em;">
    ⚡ New Technologies & Challenges
</h2>

<p>With new technologies such as <strong>3D printing</strong>, <strong>novel electronics</strong> and <strong>new exotic materials</strong>, the quest for the final Quality of a product becomes vital – and more difficult as changes in the process result in feedback form other components hitherto deemed sufficient and now possibly found wanting or unnecessary.</p>

<p>In other words, such changes send ripples of iterations through the who purchasing process and the only constant is the that the resultant quality requirements must still match the needs of the final product.</p>

<div style="background: #ffebee; padding: 30px; border-radius: 15px; margin: 30px 0; border-left: 5px solid #f44336;">
    <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 15px;">
        ⚠️ The Complexity Challenge
    </h3>
    <p style="margin-bottom: 15px;">
        The issue is that this gets highly complex and the repeated checks that have to be carried out can be difficult to track – not only for the separate component and sub-assembly manufacturers, but also for the OEM at the top of the chain.
    </p>
    <p style="margin: 0;">
        However much the burden is passed down to the suppliers, the OEM has to maintain oversight over the whole process to ensure that their own products are unaffected (otherwise you get scenarios such as the <strong>Boeing 737 Max</strong>, the <strong>Hotpoint recalls</strong> and the like).
    </p>
</div>

<h2 style="color: #1e3a5f; margin-top: 50px; margin-bottom: 20px; font-size: 2em;">
    🤖 Automated Tracking Systems
</h2>

<p>Tracking programmes in business management systems can now handle the quality controls and oversights on behalf of humans. The quality checks are programmed in and the resultant continuous feed of test results allows the systems to record and react as necessary – and reverse track batch results if required as well.</p>

<div style="background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%); padding: 30px; border-radius: 15px; margin: 30px 0; border-left: 5px solid #4caf50;">
    <p style="margin: 0; font-size: 1.05em; line-height: 1.8;">
        The theory of this is not new, but the latest iterations are getting <strong>more and more capable</strong> – reducing bureaucracy, enhancing results management, improving the process efficiency and dramatically aiding raise the bottom line.
    </p>
</div>

<h2 style="color: #1e3a5f; margin-top: 50px; margin-bottom: 20px; font-size: 2em;">
    💰 Impact on the Bottom Line
</h2>

<p style="margin-bottom: 25px;">To be clear with regard to the bottom line, this happens for a range of reasons:</p>

<div style="display: grid; gap: 20px; margin: 30px 0;">
    <!-- Benefit 1 -->
    <div style="background: white; padding: 25px; border-radius: 10px; border-left: 5px solid #ff9800; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
        <h3 style="color: #ff9800; margin-top: 0; margin-bottom: 10px; font-size: 1.2em;">
            👥 Reduced Bureaucracy
        </h3>
        <p style="margin: 0; line-height: 1.7;">
            The removal of bureaucracy from the human operators will release them for work elsewhere (or release them altogether potentially)
        </p>
    </div>

    <!-- Benefit 2 -->
    <div style="background: white; padding: 25px; border-radius: 10px; border-left: 5px solid #2196f3; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
        <h3 style="color: #2196f3; margin-top: 0; margin-bottom: 10px; font-size: 1.2em;">
            🎯 Enhanced Quality Control
        </h3>
        <p style="margin: 0; line-height: 1.7;">
            The computer oversight systems can check <strong>more items, more often, more accurately</strong> so that the chances of error and low quality product getting through is exceedingly low – this raises the organisation's reputations, avoids embarrassing recalls, prevents staff having to deal with customer complaints, allows a price increase on the basis of reliability
        </p>
    </div>

    <!-- Benefit 3 -->
    <div style="background: white; padding: 25px; border-radius: 10px; border-left: 5px solid #4caf50; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
        <h3 style="color: #4caf50; margin-top: 0; margin-bottom: 10px; font-size: 1.2em;">
            📦 Reduced Material Waste
        </h3>
        <p style="margin: 0; line-height: 1.7;">
            Once the removal of "bad" product from the processing line takes place (as a result of enhanced quality checks early in the systems), this means that material usage will be reduced (materials that were going into items that have been removed as "bad" and therefore such materials had been wasted) which also means that raw material volumes stored can be reduced – both of which will reduce costs of purchase, handling and processing
        </p>
    </div>

    <!-- Benefit 4 -->
    <div style="background: white; padding: 25px; border-radius: 10px; border-left: 5px solid #9c27b0; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
        <h3 style="color: #9c27b0; margin-top: 0; margin-bottom: 10px; font-size: 1.2em;">
            ⚙️ Reduced Processing Costs
        </h3>
        <p style="margin: 0; line-height: 1.7;">
            Reduced time and costs handling wasted products that turned out to be either of no use and have to be disposed or which can be reworked but which involves further costs and handling requirements
        </p>
    </div>
</div>

<h2 style="color: #1e3a5f; margin-top: 50px; margin-bottom: 20px; font-size: 2em;">
    📊 Building on Six Sigma
</h2>

<p>None of these concepts is necessarily new – and the whole <strong>6 Sigma approach</strong> is based around the basic ideas here – but the extent to which this can now be done is different.</p>

<div style="background: #f0f7ff; padding: 30px; border-radius: 15px; margin: 30px 0;">
    <p style="margin-bottom: 15px; font-size: 1.05em;">
        <strong style="color: #1e3a5f;">Never before</strong> have the automated systems been as good or as flexible in these fields. Nor have the extremes of checking been possible either practically or from a financial viewpoint in the past.
    </p>
    <p style="margin: 0; font-size: 1.05em;">
        Now that bespoke systems can be quickly assembled from existing modules of existing programmes, the tailoring of new and evolving systems can be achieved <strong>quickly and precisely</strong> to match the organisation's own specific requirements and focus.
    </p>
</div>

<h2 style="color: #1e3a5f; margin-top: 50px; margin-bottom: 20px; font-size: 2em;">
    🚀 Ready to Transform Your Quality Systems?
</h2>

<div style="background: linear-gradient(135deg, #ff9800 0%, #f57c00 100%); padding: 40px; border-radius: 15px; margin: 40px 0; color: white; text-align: center;">
    <p style="font-size: 1.2em; margin-bottom: 25px; line-height: 1.7;">
        Want to know how this can be carried out for your own organisation?
    </p>
    <p style="font-size: 1.4em; font-weight: 600; margin-bottom: 30px;">
        Contact Carl Kruger at Qualitation
    </p>
    <div style="display: flex; gap: 15px; justify-content: center; flex-wrap: wrap;">
        <a href="/contact/" style="background: white; color: #ff9800; padding: 15px 35px; border-radius: 50px; text-decoration: none; font-weight: 600; display: inline-block; transition: all 0.3s ease;">
            Get in Touch
        </a>
        <a href="tel:03456006975" style="background: rgba(255,255,255,0.2); color: white; padding: 15px 35px; border-radius: 50px; text-decoration: none; font-weight: 600; display: inline-block; border: 2px solid white; transition: all 0.3s ease;">
            📞 0345 600 6975
        </a>
    </div>
</div>
'''

            # Create the article
            article = ArticlePage(
                title="Trust but Verify",
                slug='trust-but-verify',
                date=datetime.date(2019, 9, 30),
                intro='Addresses verification across complex supply chains where products become components in larger offerings',
                body=article_body,
                author='Qualitation Team',
                card_gradient_start='#ff9800',
                card_gradient_end='#f57c00',
                show_in_menus=False,
            )

            # Add to resources page
            resources_page.add_child(instance=article)
            article.save_revision().publish()

            self.stdout.write(self.style.SUCCESS('✓ Created Trust but Verify article'))
            self.stdout.write(self.style.SUCCESS(f'✓ URL: /resources/trust-but-verify/'))
            self.stdout.write(self.style.SUCCESS('✓ Published successfully'))

        except ArticleIndexPage.DoesNotExist:
            self.stdout.write(self.style.ERROR('✗ Resources page not found'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ Error: {e}'))
            import traceback
            traceback.print_exc()

        self.stdout.write(self.style.SUCCESS('\n=== Complete ===\n'))
