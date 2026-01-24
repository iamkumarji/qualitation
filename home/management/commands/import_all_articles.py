"""
Django management command to import all remaining articles from the collection
"""

from django.core.management.base import BaseCommand
from home.models import ArticleIndexPage, ArticlePage
import datetime


class Command(BaseCommand):
    help = 'Import all remaining articles from the Qualitation collection'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('\n=== Importing All Articles ===\n'))

        try:
            # Get the Resources/ArticleIndex page
            resources_page = ArticleIndexPage.objects.get(slug='resources')

            # Define all articles with their metadata
            # We already have: Templates (2020), Automation, ISO Standard, Trust but Verify (2019)
            # Need to add the remaining 20 articles

            articles_to_create = []

            # Remaining 2019 articles (6 more)
            articles_to_create.extend([
                {
                    'title': 'Rewarding Failure – should we?',
                    'slug': 'rewarding-failure-should-we',
                    'date': datetime.date(2019, 9, 26),
                    'intro': 'Examines uncertainty and disruption caused by failure in various contexts and organizational settings',
                    'gradient_start': '#9c27b0',
                    'gradient_end': '#e91e63',
                },
                {
                    'title': 'Why choose to automate quality first NOT volume?',
                    'slug': 'why-choose-to-automate-quality-first-not-volume',
                    'date': datetime.date(2019, 9, 23),
                    'intro': 'Explores automated systems in manufacturing, emphasizing quality prioritization over volume',
                    'gradient_start': '#ff5722',
                    'gradient_end': '#ff9800',
                },
                {
                    'title': 'Why IT is the Key to More Efficient ISO Administration',
                    'slug': 'why-it-is-the-key-to-more-efficient-iso-administration',
                    'date': datetime.date(2019, 6, 13),
                    'intro': 'Explains how automated systems reduce tedious ISO administrator workload while maintaining standards compliance',
                    'gradient_start': '#3f51b5',
                    'gradient_end': '#2196f3',
                },
                {
                    'title': 'The wide-ranging benefits of ISO IT software',
                    'slug': 'the-wide-ranging-benefits-of-iso-it-software',
                    'date': datetime.date(2019, 6, 3),
                    'intro': 'Describes how ISO software reduces administrative burden and improves organizational processes and staff motivation',
                    'gradient_start': '#00bcd4',
                    'gradient_end': '#009688',
                },
                {
                    'title': 'Why Put Quality First?',
                    'slug': 'why-put-quality-first',
                    'date': datetime.date(2019, 5, 29),
                    'intro': 'Putting quality management at the forefront of your operations by investing in internationally recognised ISO standards is vital',
                    'gradient_start': '#8bc34a',
                    'gradient_end': '#cddc39',
                },
                {
                    'title': 'Why Should Quality Matter More To Your Business?',
                    'slug': 'why-should-quality-matter-more-to-your-business',
                    'date': datetime.date(2019, 5, 21),
                    'intro': 'Emphasizes quality as essential for customer loyalty and profit growth, advocating for ISO 9001 certification',
                    'gradient_start': '#ffc107',
                    'gradient_end': '#ff9800',
                },
                {
                    'title': 'Brexit – how are ISO standards affected?',
                    'slug': 'brexit-how-are-iso-standards-affected',
                    'date': datetime.date(2019, 3, 11),
                    'intro': 'Explains that ISO infrastructure remains unchanged despite Brexit, as ISO operates independently from the UK',
                    'gradient_start': '#607d8b',
                    'gradient_end': '#455a64',
                },
            ])

            # 2018 articles (6)
            articles_to_create.extend([
                {
                    'title': 'Sustainable Business Practices with ISO 14001',
                    'slug': 'sustainable-business-practices-with-iso-14001',
                    'date': datetime.date(2018, 6, 22),
                    'intro': 'Focuses on consumer demand for ethical purchasing and manufacturer sustainability commitments through ISO 14001',
                    'gradient_start': '#4caf50',
                    'gradient_end': '#66bb6a',
                },
                {
                    'title': 'New Direction for Automotive Industry – IATF 16949 Certification',
                    'slug': 'new-direction-for-automotive-industry-iatf-16949',
                    'date': datetime.date(2018, 5, 15),
                    'intro': 'Details the transition from ISO/TS 16949 to IATF 16949 for automotive quality management systems',
                    'gradient_start': '#ff6f00',
                    'gradient_end': '#ffa726',
                },
                {
                    'title': 'Does Brexit Invalidate ISO Certification?',
                    'slug': 'does-brexit-invalidate-iso-certification',
                    'date': datetime.date(2018, 4, 16),
                    'intro': 'Clarifies that ISO certifications remain valid post-Brexit as ISO is an international organization',
                    'gradient_start': '#5c6bc0',
                    'gradient_end': '#7986cb',
                },
                {
                    'title': 'Competitors: The Greatest Threat to your Organisation?',
                    'slug': 'competitors-greatest-threat-to-organisation',
                    'date': datetime.date(2018, 3, 12),
                    'intro': 'Explains how to beat the competition through quality and ISO certification',
                    'gradient_start': '#e53935',
                    'gradient_end': '#ef5350',
                },
                {
                    'title': 'Will ISO 14001 Environmental Management become Mandatory for every UK Business?',
                    'slug': 'will-iso-14001-become-mandatory',
                    'date': datetime.date(2018, 2, 19),
                    'intro': 'Discusses the trend towards environmental accountability and the business case for ISO 14001',
                    'gradient_start': '#43a047',
                    'gradient_end': '#66bb6a',
                },
                {
                    'title': 'How to organise the ISO Training?',
                    'slug': 'how-to-organise-iso-training',
                    'date': datetime.date(2018, 1, 8),
                    'intro': 'Provides guidance on planning and delivering effective ISO training for all staff members',
                    'gradient_start': '#26a69a',
                    'gradient_end': '#4db6ac',
                },
            ])

            # 2017 articles (7)
            articles_to_create.extend([
                {
                    'title': 'How do I choose an ISO Certifier?',
                    'slug': 'how-do-i-choose-iso-certifier',
                    'date': datetime.date(2017, 12, 11),
                    'intro': 'Guidance on selecting an accredited certification body and understanding the certification process',
                    'gradient_start': '#1976d2',
                    'gradient_end': '#42a5f5',
                },
                {
                    'title': 'Mitigating Winter Hazards with the ISO 45001',
                    'slug': 'mitigating-winter-hazards-iso-45001',
                    'date': datetime.date(2017, 12, 6),
                    'intro': 'Addresses winter workplace safety challenges and how ISO 45001 helps manage seasonal risks',
                    'gradient_start': '#0097a7',
                    'gradient_end': '#00acc1',
                },
                {
                    'title': "How ISO Management Systems can drive 'Smart Maintenance'",
                    'slug': 'iso-systems-drive-smart-maintenance',
                    'date': datetime.date(2017, 11, 13),
                    'intro': 'Explains how ISO standards support data-driven maintenance optimization',
                    'gradient_start': '#00897b',
                    'gradient_end': '#26a69a',
                },
                {
                    'title': 'Disruption Caused by Security Incidents Cut by 72% with ISO 27001 certification',
                    'slug': 'security-incidents-cut-72-percent-iso-27001',
                    'date': datetime.date(2017, 11, 3),
                    'intro': 'Research showing certified organizations experience significantly less disruption from cyber security incidents',
                    'gradient_start': '#c62828',
                    'gradient_end': '#e53935',
                },
                {
                    'title': 'How to put an ISO System into Practice',
                    'slug': 'how-to-put-iso-system-into-practice',
                    'date': datetime.date(2017, 10, 19),
                    'intro': 'Practical guidance on implementing and embedding ISO management systems into daily operations',
                    'gradient_start': '#6a1b9a',
                    'gradient_end': '#8e24aa',
                },
                {
                    'title': 'The Steps Involved in Obtaining an ISO Standard',
                    'slug': 'steps-involved-obtaining-iso-standard',
                    'date': datetime.date(2017, 10, 10),
                    'intro': 'A comprehensive guide to the ISO certification process from initial discussion to certification',
                    'gradient_start': '#f57c00',
                    'gradient_end': '#fb8c00',
                },
                {
                    'title': 'Solid Foundations',
                    'slug': 'solid-foundations',
                    'date': datetime.date(2017, 9, 28),
                    'intro': 'Why investing in ISO standards creates solid foundations for sustainable business growth',
                    'gradient_start': '#5d4037',
                    'gradient_end': '#6d4c41',
                },
            ])

            created_count = 0
            for article_data in articles_to_create:
                # Check if article already exists
                if ArticlePage.objects.filter(slug=article_data['slug']).exists():
                    self.stdout.write(self.style.WARNING(f'  - Skipping (exists): {article_data["title"]}'))
                    continue

                # Create basic article (content will be added separately for each)
                article = ArticlePage(
                    title=article_data['title'],
                    slug=article_data['slug'],
                    date=article_data['date'],
                    intro=article_data['intro'],
                    body='<p>Article content coming soon. This article has been imported from the Qualitation archives.</p>',
                    author='Qualitation Team',
                    card_gradient_start=article_data['gradient_start'],
                    card_gradient_end=article_data['gradient_end'],
                    show_in_menus=False,
                )

                # Add to resources page
                resources_page.add_child(instance=article)
                article.save_revision().publish()

                created_count += 1
                self.stdout.write(self.style.SUCCESS(f'✓ Created: {article_data["title"]}'))

            self.stdout.write(self.style.SUCCESS(f'\n✓ Created {created_count} new articles'))
            self.stdout.write(self.style.SUCCESS(f'✓ Total articles now: {ArticlePage.objects.count()}'))

        except ArticleIndexPage.DoesNotExist:
            self.stdout.write(self.style.ERROR('✗ Resources page not found'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ Error: {e}'))
            import traceback
            traceback.print_exc()

        self.stdout.write(self.style.SUCCESS('\n=== Complete ===\n'))
        self.stdout.write(self.style.SUCCESS('Note: Articles created with placeholder content.'))
        self.stdout.write(self.style.SUCCESS('Full content will be added in subsequent commands.'))
