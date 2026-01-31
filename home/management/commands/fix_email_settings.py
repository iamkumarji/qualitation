from django.core.management.base import BaseCommand
from home.models import EmailSettings
from wagtail.models import Site


class Command(BaseCommand):
    help = 'Fix email settings to ensure TLS/SSL are not both enabled'

    def handle(self, *args, **options):
        try:
            # Get all email settings
            for site in Site.objects.all():
                email_settings = EmailSettings.for_site(site)

                if email_settings.use_tls and email_settings.use_ssl:
                    self.stdout.write(self.style.WARNING('Both TLS and SSL were enabled'))
                    email_settings.use_ssl = False
                    email_settings.save()
                    self.stdout.write(self.style.SUCCESS('✅ Fixed: Disabled SSL, kept TLS enabled'))
                elif not email_settings.use_tls and not email_settings.use_ssl:
                    self.stdout.write(self.style.WARNING('Neither TLS nor SSL enabled'))
                    email_settings.use_tls = True
                    email_settings.save()
                    self.stdout.write(self.style.SUCCESS('✅ Fixed: Enabled TLS (recommended for port 587)'))
                else:
                    self.stdout.write(self.style.SUCCESS('✅ Email settings are correct'))

                self.stdout.write(f'Current settings:')
                self.stdout.write(f'  - TLS: {email_settings.use_tls}')
                self.stdout.write(f'  - SSL: {email_settings.use_ssl}')
                self.stdout.write(f'  - Port: {email_settings.smtp_port}')

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {str(e)}'))
            import traceback
            traceback.print_exc()
