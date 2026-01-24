"""
Django management command to add news articles to Resources page
"""

from django.core.management.base import BaseCommand
from home.models import FlexiblePage


class Command(BaseCommand):
    help = 'Add news articles section to Resources page'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('\n=== Adding Articles to Resources Page ===\n'))

        try:
            page = FlexiblePage.objects.get(slug='resources')

            # Create the articles HTML block
            articles_html = '''
<section style="max-width: 1200px; margin: 80px auto 60px; padding: 0 20px;">
    <h2 style="text-align: center; font-size: 2.5em; margin-bottom: 20px; color: #1e3a5f;">News & Articles</h2>
    <p style="text-align: center; font-size: 1.2em; color: #666; margin-bottom: 50px; max-width: 800px; margin-left: auto; margin-right: auto;">
        Stay informed with our latest insights, expert opinions, and guidance on ISO standards and quality management.
    </p>

    <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(350px, 1fr)); gap: 30px;">

        <!-- Article 1 -->
        <article style="border: 1px solid #e0e0e0; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.08); transition: transform 0.3s ease, box-shadow 0.3s ease; background: white;">
            <div style="padding: 30px;">
                <div style="color: #999; font-size: 0.9em; margin-bottom: 10px;">27 October 2020</div>
                <h3 style="color: #1e3a5f; margin-bottom: 15px; font-size: 1.4em;">Don't use templates to achieve an ISO Standard</h3>
                <p style="color: #666; line-height: 1.6; margin-bottom: 20px;">Why you should not use someone else's templates to 'help' you attain an ISO Certification</p>
                <a href="https://qualitation.co.uk/dont-use-templates-to-achieve-an-iso-standard" target="_blank" rel="noopener noreferrer" style="color: #1e3a5f; text-decoration: none; font-weight: 600; display: inline-flex; align-items: center; gap: 5px;">
                    Read Article →
                </a>
            </div>
        </article>

        <!-- Article 2 -->
        <article style="border: 1px solid #e0e0e0; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.08); transition: transform 0.3s ease, box-shadow 0.3s ease; background: white;">
            <div style="padding: 30px;">
                <div style="color: #999; font-size: 0.9em; margin-bottom: 10px;">24 October 2019</div>
                <h3 style="color: #1e3a5f; margin-bottom: 15px; font-size: 1.4em;">Automation is the future for ISO Standards!</h3>
                <p style="color: #666; line-height: 1.6; margin-bottom: 20px;">Discusses how robots and automation are increasingly prevalent in manufacturing and ISO Standards implementation</p>
                <a href="https://qualitation.co.uk/automation-is-the-future-for-iso-standards" target="_blank" rel="noopener noreferrer" style="color: #1e3a5f; text-decoration: none; font-weight: 600; display: inline-flex; align-items: center; gap: 5px;">
                    Read Article →
                </a>
            </div>
        </article>

        <!-- Article 3 -->
        <article style="border: 1px solid #e0e0e0; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.08); transition: transform 0.3s ease, box-shadow 0.3s ease; background: white;">
            <div style="padding: 30px;">
                <div style="color: #999; font-size: 0.9em; margin-bottom: 10px;">8 October 2019</div>
                <h3 style="color: #1e3a5f; margin-bottom: 15px; font-size: 1.4em;">What is an ISO Standard for?</h3>
                <p style="color: #666; line-height: 1.6; margin-bottom: 20px;">Everyone wants to buy good quality goods and services for a realistic value. Explores how ISO Standards help organizations optimize quality</p>
                <a href="https://qualitation.co.uk/what-is-an-iso-standard-for" target="_blank" rel="noopener noreferrer" style="color: #1e3a5f; text-decoration: none; font-weight: 600; display: inline-flex; align-items: center; gap: 5px;">
                    Read Article →
                </a>
            </div>
        </article>

        <!-- Article 4 -->
        <article style="border: 1px solid #e0e0e0; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.08); transition: transform 0.3s ease, box-shadow 0.3s ease; background: white;">
            <div style="padding: 30px;">
                <div style="color: #999; font-size: 0.9em; margin-bottom: 10px;">30 September 2019</div>
                <h3 style="color: #1e3a5f; margin-bottom: 15px; font-size: 1.4em;">Trust but Verify</h3>
                <p style="color: #666; line-height: 1.6; margin-bottom: 20px;">Addresses verification across complex supply chains where products become components in larger offerings</p>
                <a href="https://qualitation.co.uk/trust-but-verify" target="_blank" rel="noopener noreferrer" style="color: #1e3a5f; text-decoration: none; font-weight: 600; display: inline-flex; align-items: center; gap: 5px;">
                    Read Article →
                </a>
            </div>
        </article>

        <!-- Article 5 -->
        <article style="border: 1px solid #e0e0e0; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.08); transition: transform 0.3s ease, box-shadow 0.3s ease; background: white;">
            <div style="padding: 30px;">
                <div style="color: #999; font-size: 0.9em; margin-bottom: 10px;">26 September 2019</div>
                <h3 style="color: #1e3a5f; margin-bottom: 15px; font-size: 1.4em;">Rewarding Failure – should we?</h3>
                <p style="color: #666; line-height: 1.6; margin-bottom: 20px;">Examines uncertainty and disruption caused by failure in various contexts and organizational settings</p>
                <a href="https://qualitation.co.uk/rewarding-failure-should-we" target="_blank" rel="noopener noreferrer" style="color: #1e3a5f; text-decoration: none; font-weight: 600; display: inline-flex; align-items: center; gap: 5px;">
                    Read Article →
                </a>
            </div>
        </article>

        <!-- Article 6 -->
        <article style="border: 1px solid #e0e0e0; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.08); transition: transform 0.3s ease, box-shadow 0.3s ease; background: white;">
            <div style="padding: 30px;">
                <div style="color: #999; font-size: 0.9em; margin-bottom: 10px;">23 September 2019</div>
                <h3 style="color: #1e3a5f; margin-bottom: 15px; font-size: 1.4em;">Why choose to automate quality first NOT volume?</h3>
                <p style="color: #666; line-height: 1.6; margin-bottom: 20px;">Explores automated systems in manufacturing, emphasizing quality prioritization over volume</p>
                <a href="https://qualitation.co.uk/why-choose-to-automate-quality-first-not-volume" target="_blank" rel="noopener noreferrer" style="color: #1e3a5f; text-decoration: none; font-weight: 600; display: inline-flex; align-items: center; gap: 5px;">
                    Read Article →
                </a>
            </div>
        </article>

        <!-- Article 7 -->
        <article style="border: 1px solid #e0e0e0; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.08); transition: transform 0.3s ease, box-shadow 0.3s ease; background: white;">
            <div style="padding: 30px;">
                <div style="color: #999; font-size: 0.9em; margin-bottom: 10px;">13 June 2019</div>
                <h3 style="color: #1e3a5f; margin-bottom: 15px; font-size: 1.4em;">Why IT is the Key to More Efficient ISO Administration</h3>
                <p style="color: #666; line-height: 1.6; margin-bottom: 20px;">Explains how automated systems reduce tedious ISO administrator workload while maintaining standards compliance</p>
                <a href="https://qualitation.co.uk/why-it-is-the-key-to-more-efficient-iso-administration" target="_blank" rel="noopener noreferrer" style="color: #1e3a5f; text-decoration: none; font-weight: 600; display: inline-flex; align-items: center; gap: 5px;">
                    Read Article →
                </a>
            </div>
        </article>

        <!-- Article 8 -->
        <article style="border: 1px solid #e0e0e0; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.08); transition: transform 0.3s ease, box-shadow 0.3s ease; background: white;">
            <div style="padding: 30px;">
                <div style="color: #999; font-size: 0.9em; margin-bottom: 10px;">3 June 2019</div>
                <h3 style="color: #1e3a5f; margin-bottom: 15px; font-size: 1.4em;">The wide-ranging benefits of ISO IT software</h3>
                <p style="color: #666; line-height: 1.6; margin-bottom: 20px;">Describes how ISO software reduces administrative burden and improves organizational processes and staff motivation</p>
                <a href="https://qualitation.co.uk/the-wide-ranging-benefits-of-iso-it-software" target="_blank" rel="noopener noreferrer" style="color: #1e3a5f; text-decoration: none; font-weight: 600; display: inline-flex; align-items: center; gap: 5px;">
                    Read Article →
                </a>
            </div>
        </article>

        <!-- Article 9 -->
        <article style="border: 1px solid #e0e0e0; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.08); transition: transform 0.3s ease, box-shadow 0.3s ease; background: white;">
            <div style="padding: 30px;">
                <div style="color: #999; font-size: 0.9em; margin-bottom: 10px;">29 May 2019</div>
                <h3 style="color: #1e3a5f; margin-bottom: 15px; font-size: 1.4em;">Why Put Quality First?</h3>
                <p style="color: #666; line-height: 1.6; margin-bottom: 20px;">Putting quality management at the forefront of your operations by investing in internationally recognised ISO standards is vital</p>
                <a href="https://qualitation.co.uk/why-put-quality-first" target="_blank" rel="noopener noreferrer" style="color: #1e3a5f; text-decoration: none; font-weight: 600; display: inline-flex; align-items: center; gap: 5px;">
                    Read Article →
                </a>
            </div>
        </article>

        <!-- Article 10 -->
        <article style="border: 1px solid #e0e0e0; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.08); transition: transform 0.3s ease, box-shadow 0.3s ease; background: white;">
            <div style="padding: 30px;">
                <div style="color: #999; font-size: 0.9em; margin-bottom: 10px;">21 May 2019</div>
                <h3 style="color: #1e3a5f; margin-bottom: 15px; font-size: 1.4em;">Why Should Quality Matter More To Your Business?</h3>
                <p style="color: #666; line-height: 1.6; margin-bottom: 20px;">Emphasizes quality as essential for customer loyalty and profit growth, advocating for ISO 9001 certification</p>
                <a href="https://qualitation.co.uk/why-should-quality-matter-more-to-your-business" target="_blank" rel="noopener noreferrer" style="color: #1e3a5f; text-decoration: none; font-weight: 600; display: inline-flex; align-items: center; gap: 5px;">
                    Read Article →
                </a>
            </div>
        </article>

        <!-- Article 11 -->
        <article style="border: 1px solid #e0e0e0; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.08); transition: transform 0.3s ease, box-shadow 0.3s ease; background: white;">
            <div style="padding: 30px;">
                <div style="color: #999; font-size: 0.9em; margin-bottom: 10px;">11 March 2019</div>
                <h3 style="color: #1e3a5f; margin-bottom: 15px; font-size: 1.4em;">Brexit – how are ISO standards affected?</h3>
                <p style="color: #666; line-height: 1.6; margin-bottom: 20px;">Explains that ISO infrastructure remains unchanged despite Brexit, as ISO operates independently from the UK</p>
                <a href="https://qualitation.co.uk/brexit-how-are-iso-standards-affected" target="_blank" rel="noopener noreferrer" style="color: #1e3a5f; text-decoration: none; font-weight: 600; display: inline-flex; align-items: center; gap: 5px;">
                    Read Article →
                </a>
            </div>
        </article>

        <!-- Article 12 -->
        <article style="border: 1px solid #e0e0e0; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.08); transition: transform 0.3s ease, box-shadow 0.3s ease; background: white;">
            <div style="padding: 30px;">
                <div style="color: #999; font-size: 0.9em; margin-bottom: 10px;">22 June 2018</div>
                <h3 style="color: #1e3a5f; margin-bottom: 15px; font-size: 1.4em;">Sustainable Business Practices with ISO 14001</h3>
                <p style="color: #666; line-height: 1.6; margin-bottom: 20px;">Focuses on consumer demand for ethical purchasing and manufacturer sustainability commitments through ISO 14001</p>
                <a href="https://qualitation.co.uk/sustainable-business-practices-with-iso-14001" target="_blank" rel="noopener noreferrer" style="color: #1e3a5f; text-decoration: none; font-weight: 600; display: inline-flex; align-items: center; gap: 5px;">
                    Read Article →
                </a>
            </div>
        </article>

    </div>
</section>

<style>
article:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 15px rgba(0,0,0,0.15) !important;
}
</style>
'''

            # Add the articles block to the page
            # The page currently has 1 block, we'll append the new articles section
            page.body.append(('html', {'html': articles_html}))

            # Save and publish
            page.save_revision().publish()

            self.stdout.write(self.style.SUCCESS('✓ Added 12 news articles to Resources page'))
            self.stdout.write(self.style.SUCCESS('✓ Page published successfully'))

        except FlexiblePage.DoesNotExist:
            self.stdout.write(self.style.ERROR('✗ Resources page not found'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ Error: {e}'))

        self.stdout.write(self.style.SUCCESS('\n=== Complete ===\n'))
