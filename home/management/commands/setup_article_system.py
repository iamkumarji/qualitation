"""
Django management command to set up the article management system
Converts existing Resources page to ArticleIndexPage and migrates articles
"""

from django.core.management.base import BaseCommand
from home.models import FlexiblePage, ArticleIndexPage, ArticlePage
from wagtail.models import Page
import datetime


class Command(BaseCommand):
    help = 'Set up article management system and migrate existing articles'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('\n=== Setting Up Article Management System ===\n'))

        try:
            # Get the home page
            home_page = Page.objects.get(slug='home')

            # Check if Resources page exists
            try:
                resources_page = FlexiblePage.objects.get(slug='resources')
                self.stdout.write(self.style.WARNING('Found existing Resources FlexiblePage'))

                # Create new ArticleIndexPage to replace it
                article_index = ArticleIndexPage(
                    title='Resources',
                    slug='resources-new',  # Temporary slug
                    show_in_menus=True,
                    intro='',
                    show_hero=True,
                    hero_title='ISO Resources & Expert Insights',
                    hero_subtitle='Stay informed with our latest insights, expert opinions, and guidance on ISO standards and quality management.',
                    show_cta=True,
                    cta_title='Need Personalized Guidance?',
                    cta_text='Our expert team is here to help. Get in touch for a free consultation.',
                    cta_button_text='Contact Us',
                    cta_button_link='/contact/',
                )

                # Add to home page
                home_page.add_child(instance=article_index)
                article_index.save_revision().publish()

                self.stdout.write(self.style.SUCCESS('✓ Created new ArticleIndexPage'))

                # Now migrate the two existing articles
                articles_data = [
                    {
                        'title': "Don't use templates to achieve an ISO Standard",
                        'slug': 'dont-use-templates-to-achieve-an-iso-standard',
                        'date': datetime.date(2020, 10, 27),
                        'intro': "Why you should not use someone else's templates to 'help' you attain an ISO Certification",
                        'gradient_start': '#667eea',
                        'gradient_end': '#764ba2',
                    },
                    {
                        'title': 'Automation is the future for ISO Standards!',
                        'slug': 'automation-is-the-future-for-iso-standards',
                        'date': datetime.date(2019, 10, 24),
                        'intro': 'Discusses how robots and automation are increasingly prevalent in manufacturing and ISO Standards implementation',
                        'gradient_start': '#4facfe',
                        'gradient_end': '#00f2fe',
                    },
                ]

                migrated_count = 0
                for article_data in articles_data:
                    # Check if the old article page exists
                    try:
                        old_article = FlexiblePage.objects.get(slug=article_data['slug'])

                        # Create new ArticlePage
                        article_page = ArticlePage(
                            title=article_data['title'],
                            slug=article_data['slug'] + '-new',  # Temporary slug
                            date=article_data['date'],
                            intro=article_data['intro'],
                            body=old_article.intro if old_article.intro else '',  # Get content from old page
                            card_gradient_start=article_data['gradient_start'],
                            card_gradient_end=article_data['gradient_end'],
                            show_in_menus=False,
                        )

                        # Add to article index
                        article_index.add_child(instance=article_page)
                        article_page.save_revision().publish()

                        self.stdout.write(self.style.SUCCESS(f'✓ Migrated article: {article_data["title"]}'))

                        # Delete old article page
                        old_article.delete()
                        self.stdout.write(self.style.SUCCESS(f'  - Deleted old page'))

                        # Update slug to remove '-new' suffix
                        article_page.slug = article_data['slug']
                        article_page.save_revision().publish()

                        migrated_count += 1

                    except FlexiblePage.DoesNotExist:
                        self.stdout.write(self.style.WARNING(f'  - Old article not found: {article_data["slug"]}'))

                # Delete old resources page
                resources_page.delete()
                self.stdout.write(self.style.SUCCESS('✓ Deleted old Resources FlexiblePage'))

                # Update ArticleIndexPage slug
                article_index.slug = 'resources'
                article_index.save_revision().publish()
                self.stdout.write(self.style.SUCCESS('✓ Updated ArticleIndexPage slug to "resources"'))

                self.stdout.write(self.style.SUCCESS(f'\n✓ Migrated {migrated_count} articles'))

            except FlexiblePage.DoesNotExist:
                # Resources page doesn't exist, create fresh ArticleIndexPage
                article_index = ArticleIndexPage(
                    title='Resources',
                    slug='resources',
                    show_in_menus=True,
                    intro='',
                    show_hero=True,
                    hero_title='ISO Resources & Expert Insights',
                    hero_subtitle='Stay informed with our latest insights, expert opinions, and guidance on ISO standards and quality management.',
                    show_cta=True,
                    cta_title='Need Personalized Guidance?',
                    cta_text='Our expert team is here to help. Get in touch for a free consultation.',
                    cta_button_text='Contact Us',
                    cta_button_link='/contact/',
                )

                home_page.add_child(instance=article_index)
                article_index.save_revision().publish()

                self.stdout.write(self.style.SUCCESS('✓ Created new ArticleIndexPage at /resources/'))

            self.stdout.write(self.style.SUCCESS('\n=== Article System Setup Complete ==='))
            self.stdout.write(self.style.SUCCESS('\nYou can now:'))
            self.stdout.write(self.style.SUCCESS('1. Go to Wagtail Admin → Pages → Resources'))
            self.stdout.write(self.style.SUCCESS('2. Click "Add child page" → Article'))
            self.stdout.write(self.style.SUCCESS('3. Fill in the article details and publish'))
            self.stdout.write(self.style.SUCCESS('4. Articles will automatically appear on the Resources page!'))
            self.stdout.write(self.style.SUCCESS('\nURL: http://localhost:8000/admin/pages/'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ Error: {e}'))
            import traceback
            traceback.print_exc()

        self.stdout.write(self.style.SUCCESS('\n=== Complete ===\n'))
