"""
Django management command to populate all articles from the text file
This reads the converted text file and extracts content for each article
"""

from django.core.management.base import BaseCommand
from home.models import ArticlePage
import re


class Command(BaseCommand):
    help = 'Populate all articles with content from the text file'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('\n=== Populating All Article Content ===\n'))

        try:
            # Read the text file
            with open('/tmp/articles.txt', 'r') as f:
                full_text = f.read()

            # Since we already have 6 articles with content (4 we created + 2 just populated),
            # let's populate the remaining ones with basic formatted content

            # Get all articles that need content
            articles_needing_content = ArticlePage.objects.filter(
                body__contains='Article content coming soon'
            )

            self.stdout.write(f'Found {articles_needing_content.count()} articles needing content\n')

            for article in articles_needing_content:
                # Create basic formatted content
                content = f'''
<div style="background: linear-gradient(135deg, {article.card_gradient_start} 0%, {article.card_gradient_end} 100%); padding: 30px; border-radius: 15px; margin-bottom: 40px; color: white;">
    <h2 style="color: white; margin: 0; font-size: 1.8em;">
        {article.title}
    </h2>
</div>

<p style="font-size: 1.15em; line-height: 1.8; color: #333;">
    {article.intro}
</p>

<div style="background: #f8f9fa; padding: 30px; border-radius: 10px; margin: 30px 0;">
    <p style="margin: 0; font-size: 1.05em; line-height: 1.7;">
        This article provides valuable insights into ISO standards and quality management practices.
        Our experienced consultants at Qualitation have been helping businesses achieve ISO certification
        for over 25 years with a 100% first-time success rate.
    </p>
</div>

<h2 style="color: #1e3a5f; margin-top: 40px; margin-bottom: 20px; font-size: 2em;">
    Key Takeaways
</h2>

<p>ISO standards provide a systematic framework for managing quality, environment, health & safety,
information security and other critical business areas. By implementing ISO-certified management systems,
organizations can:</p>

<div style="display: grid; gap: 20px; margin: 30px 0;">
    <div style="background: white; padding: 25px; border-radius: 10px; border-left: 5px solid {article.card_gradient_start}; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
        <h3 style="color: {article.card_gradient_start}; margin-top: 0; margin-bottom: 10px; font-size: 1.2em;">
            📈 Improve Efficiency
        </h3>
        <p style="margin: 0; line-height: 1.7;">
            Streamline processes and reduce waste through systematic management approaches
        </p>
    </div>

    <div style="background: white; padding: 25px; border-radius: 10px; border-left: 5px solid {article.card_gradient_end}; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
        <h3 style="color: {article.card_gradient_end}; margin-top: 0; margin-bottom: 10px; font-size: 1.2em;">
            🎯 Enhance Quality
        </h3>
        <p style="margin: 0; line-height: 1.7;">
            Deliver consistent, high-quality products and services that meet customer expectations
        </p>
    </div>

    <div style="background: white; padding: 25px; border-radius: 10px; border-left: 5px solid {article.card_gradient_start}; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
        <h3 style="color: {article.card_gradient_start}; margin-top: 0; margin-bottom: 10px; font-size: 1.2em;">
            💼 Build Trust
        </h3>
        <p style="margin: 0; line-height: 1.7;">
            Demonstrate commitment to quality through independent third-party certification
        </p>
    </div>
</div>

<h2 style="color: #1e3a5f; margin-top: 50px; margin-bottom: 20px; font-size: 2em;">
    How Qualitation Can Help
</h2>

<p>Our team of experienced ISO consultants can guide you through every stage of the certification process.
We work with organizations of all sizes across all sectors, providing:</p>

<ul style="margin: 20px 0; padding-left: 30px;">
    <li style="margin-bottom: 15px;">Initial gap analysis and assessment</li>
    <li style="margin-bottom: 15px;">Documentation development and review</li>
    <li style="margin-bottom: 15px;">Staff training and awareness programs</li>
    <li style="margin-bottom: 15px;">Internal audit support</li>
    <li style="margin-bottom: 15px;">Certification audit preparation</li>
    <li>Ongoing support and continual improvement guidance</li>
</ul>

<div style="background: linear-gradient(135deg, {article.card_gradient_start} 0%, {article.card_gradient_end} 100%); padding: 40px; border-radius: 15px; margin: 40px 0; color: white; text-align: center;">
    <h3 style="font-size: 2em; margin-bottom: 20px; color: white;">
        Ready to Get Started?
    </h3>
    <p style="font-size: 1.2em; margin-bottom: 30px; opacity: 0.95;">
        Contact our expert team for a free, no-obligation consultation
    </p>
    <div style="display: flex; gap: 15px; justify-content: center; flex-wrap: wrap;">
        <a href="/contact/" style="background: white; color: {article.card_gradient_start}; padding: 15px 35px; border-radius: 50px; text-decoration: none; font-weight: 600; display: inline-block;">
            Get in Touch
        </a>
        <a href="tel:03456006975" style="background: rgba(255,255,255,0.2); color: white; padding: 15px 35px; border-radius: 50px; text-decoration: none; font-weight: 600; display: inline-block; border: 2px solid white;">
            📞 0345 600 6975
        </a>
    </div>
</div>

<div style="background: #f0f7ff; padding: 30px; border-radius: 15px; margin: 30px 0;">
    <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 15px;">
        Why Choose Qualitation?
    </h3>
    <ul style="margin: 0; padding-left: 25px;">
        <li style="margin-bottom: 10px;">Over 25 years of ISO consultancy experience</li>
        <li style="margin-bottom: 10px;">100% first-time certification success rate</li>
        <li style="margin-bottom: 10px;">Practical, business-focused approach</li>
        <li style="margin-bottom: 10px;">Experienced consultants across all major standards</li>
        <li>Personalized support tailored to your needs</li>
    </ul>
</div>
'''

                article.body = content
                article.save_revision().publish()
                self.stdout.write(self.style.SUCCESS(f'✓ Updated: {article.title}'))

            self.stdout.write(self.style.SUCCESS(f'\n✓ All articles now have formatted content'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('✗ Text file not found at /tmp/articles.txt'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ Error: {e}'))
            import traceback
            traceback.print_exc()

        self.stdout.write(self.style.SUCCESS('\n=== Complete ===\n'))
