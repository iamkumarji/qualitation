"""
Django management command to enhance the IATF 16949 stats cards
Makes them more visually appealing with icons and improved styling
"""

from django.core.management.base import BaseCommand
from home.models import FlexiblePage
import re


class Command(BaseCommand):
    help = 'Enhance the IATF 16949 stats cards section'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('\n=== Enhancing IATF Stats Cards ===\n'))

        try:
            # Get the IATF page
            iatf_page = FlexiblePage.objects.get(slug='iatf-16949')
            content = iatf_page.body[0].value['html']

            # Find and replace the Stats Section
            old_stats_pattern = r'<!-- Stats Section with Enhanced Design -->.*?(?=<!-- What is IATF 16949 Section)'

            new_stats = '''<!-- Stats Section with Enhanced Design -->
<section style="background: linear-gradient(180deg, #ffffff 0%, #f8f9fa 100%); padding: 70px 20px; position: relative; overflow: hidden;">
    <div style="position: absolute; top: -100px; right: -100px; width: 300px; height: 300px; background: radial-gradient(circle, rgba(233,69,96,0.08) 0%, transparent 70%); border-radius: 50%;"></div>
    <div style="position: absolute; bottom: -80px; left: -80px; width: 250px; height: 250px; background: radial-gradient(circle, rgba(102,126,234,0.08) 0%, transparent 70%); border-radius: 50%;"></div>

    <div style="max-width: 1200px; margin: 0 auto; position: relative; z-index: 1;">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 35px;">

            <!-- Card 1: 70,000+ Sites -->
            <div style="background: linear-gradient(135deg, #ffffff 0%, #fff5f7 100%); padding: 40px 30px; border-radius: 25px; text-align: center; box-shadow: 0 10px 40px rgba(233,69,96,0.12); border: 2px solid #ffe5eb; transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); position: relative; overflow: hidden;" onmouseover="this.style.transform='translateY(-15px) scale(1.02)'; this.style.boxShadow='0 20px 60px rgba(233,69,96,0.25)'; this.style.borderColor='#e94560'" onmouseout="this.style.transform='translateY(0) scale(1)'; this.style.boxShadow='0 10px 40px rgba(233,69,96,0.12)'; this.style.borderColor='#ffe5eb'">
                <div style="position: absolute; top: -30px; right: -30px; width: 120px; height: 120px; background: radial-gradient(circle, rgba(233,69,96,0.1) 0%, transparent 70%); border-radius: 50%;"></div>

                <div style="background: linear-gradient(135deg, #e94560, #ff6b6b); width: 80px; height: 80px; border-radius: 20px; display: flex; align-items: center; justify-content: center; margin: 0 auto 25px; box-shadow: 0 10px 30px rgba(233,69,96,0.35); position: relative;">
                    <i class="fas fa-globe" style="color: white; font-size: 2.2rem;"></i>
                    <div style="position: absolute; top: -5px; right: -5px; background: #fff; width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
                        <i class="fas fa-check" style="color: #11998e; font-size: 0.8rem;"></i>
                    </div>
                </div>

                <div style="background: linear-gradient(135deg, #e94560, #ff6b6b); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-size: 3.5rem; font-weight: 900; margin-bottom: 12px; line-height: 1; letter-spacing: -1px;">70,000+</div>

                <div style="color: #1a1a2e; font-size: 1.1rem; font-weight: 700; margin-bottom: 8px;">Certified Sites Globally</div>

                <div style="color: #666; font-size: 0.95rem; line-height: 1.6;">Organizations worldwide maintaining IATF 16949 certification</div>
            </div>

            <!-- Card 2: IATF -->
            <div style="background: linear-gradient(135deg, #ffffff 0%, #f0f4ff 100%); padding: 40px 30px; border-radius: 25px; text-align: center; box-shadow: 0 10px 40px rgba(102,126,234,0.12); border: 2px solid #dae5ff; transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); position: relative; overflow: hidden;" onmouseover="this.style.transform='translateY(-15px) scale(1.02)'; this.style.boxShadow='0 20px 60px rgba(102,126,234,0.25)'; this.style.borderColor='#667eea'" onmouseout="this.style.transform='translateY(0) scale(1)'; this.style.boxShadow='0 10px 40px rgba(102,126,234,0.12)'; this.style.borderColor='#dae5ff'">
                <div style="position: absolute; top: -30px; right: -30px; width: 120px; height: 120px; background: radial-gradient(circle, rgba(102,126,234,0.1) 0%, transparent 70%); border-radius: 50%;"></div>

                <div style="background: linear-gradient(135deg, #667eea, #764ba2); width: 80px; height: 80px; border-radius: 20px; display: flex; align-items: center; justify-content: center; margin: 0 auto 25px; box-shadow: 0 10px 30px rgba(102,126,234,0.35); position: relative;">
                    <i class="fas fa-handshake" style="color: white; font-size: 2.2rem;"></i>
                    <div style="position: absolute; top: -5px; right: -5px; background: #fff; width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
                        <i class="fas fa-star" style="color: #fb923c; font-size: 0.8rem;"></i>
                    </div>
                </div>

                <div style="background: linear-gradient(135deg, #667eea, #764ba2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-size: 3.5rem; font-weight: 900; margin-bottom: 12px; line-height: 1; letter-spacing: -1px;">IATF</div>

                <div style="color: #1a1a2e; font-size: 1.1rem; font-weight: 700; margin-bottom: 8px;">International Automotive</div>

                <div style="color: #666; font-size: 0.95rem; line-height: 1.6;">Task Force - Global automotive quality standard body</div>
            </div>

            <!-- Card 3: ISO 9001 -->
            <div style="background: linear-gradient(135deg, #ffffff 0%, #f0fdf8 100%); padding: 40px 30px; border-radius: 25px; text-align: center; box-shadow: 0 10px 40px rgba(17,153,142,0.12); border: 2px solid #d1fae5; transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); position: relative; overflow: hidden;" onmouseover="this.style.transform='translateY(-15px) scale(1.02)'; this.style.boxShadow='0 20px 60px rgba(17,153,142,0.25)'; this.style.borderColor='#11998e'" onmouseout="this.style.transform='translateY(0) scale(1)'; this.style.boxShadow='0 10px 40px rgba(17,153,142,0.12)'; this.style.borderColor='#d1fae5'">
                <div style="position: absolute; top: -30px; right: -30px; width: 120px; height: 120px; background: radial-gradient(circle, rgba(17,153,142,0.1) 0%, transparent 70%); border-radius: 50%;"></div>

                <div style="background: linear-gradient(135deg, #11998e, #38ef7d); width: 80px; height: 80px; border-radius: 20px; display: flex; align-items: center; justify-content: center; margin: 0 auto 25px; box-shadow: 0 10px 30px rgba(17,153,142,0.35); position: relative;">
                    <i class="fas fa-layer-group" style="color: white; font-size: 2.2rem;"></i>
                    <div style="position: absolute; top: -5px; right: -5px; background: #fff; width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
                        <i class="fas fa-plus" style="color: #e94560; font-size: 0.8rem;"></i>
                    </div>
                </div>

                <div style="background: linear-gradient(135deg, #11998e, #38ef7d); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-size: 3.5rem; font-weight: 900; margin-bottom: 12px; line-height: 1; letter-spacing: -1px;">ISO 9001</div>

                <div style="color: #1a1a2e; font-size: 1.1rem; font-weight: 700; margin-bottom: 8px;">Foundation + Automotive</div>

                <div style="color: #666; font-size: 0.95rem; line-height: 1.6;">Built on ISO 9001 with additional automotive requirements</div>
            </div>

            <!-- Card 4: 3 Years -->
            <div style="background: linear-gradient(135deg, #ffffff 0%, #fdf4ff 100%); padding: 40px 30px; border-radius: 25px; text-align: center; box-shadow: 0 10px 40px rgba(168,85,247,0.12); border: 2px solid #f3e8ff; transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); position: relative; overflow: hidden;" onmouseover="this.style.transform='translateY(-15px) scale(1.02)'; this.style.boxShadow='0 20px 60px rgba(168,85,247,0.25)'; this.style.borderColor='#a855f7'" onmouseout="this.style.transform='translateY(0) scale(1)'; this.style.boxShadow='0 10px 40px rgba(168,85,247,0.12)'; this.style.borderColor='#f3e8ff'">
                <div style="position: absolute; top: -30px; right: -30px; width: 120px; height: 120px; background: radial-gradient(circle, rgba(168,85,247,0.1) 0%, transparent 70%); border-radius: 50%;"></div>

                <div style="background: linear-gradient(135deg, #a855f7, #7c3aed); width: 80px; height: 80px; border-radius: 20px; display: flex; align-items: center; justify-content: center; margin: 0 auto 25px; box-shadow: 0 10px 30px rgba(168,85,247,0.35); position: relative;">
                    <i class="fas fa-sync-alt" style="color: white; font-size: 2.2rem;"></i>
                    <div style="position: absolute; top: -5px; right: -5px; background: #fff; width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
                        <i class="fas fa-calendar-check" style="color: #667eea; font-size: 0.8rem;"></i>
                    </div>
                </div>

                <div style="background: linear-gradient(135deg, #a855f7, #7c3aed); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-size: 3.5rem; font-weight: 900; margin-bottom: 12px; line-height: 1; letter-spacing: -1px;">3 Years</div>

                <div style="color: #1a1a2e; font-size: 1.1rem; font-weight: 700; margin-bottom: 8px;">Certification Cycle</div>

                <div style="color: #666; font-size: 0.95rem; line-height: 1.6;">Renewal required every three years with annual surveillance</div>
            </div>

        </div>

        <!-- Additional Info Banner -->
        <div style="margin-top: 50px; background: linear-gradient(135deg, rgba(26,26,46,0.03) 0%, rgba(15,52,96,0.05) 100%); padding: 30px; border-radius: 20px; border: 2px dashed rgba(102,126,234,0.3); text-align: center;">
            <div style="display: flex; align-items: center; justify-content: center; gap: 15px; flex-wrap: wrap;">
                <div style="background: linear-gradient(135deg, #667eea, #764ba2); width: 50px; height: 50px; border-radius: 12px; display: flex; align-items: center; justify-content: center;">
                    <i class="fas fa-info-circle" style="color: white; font-size: 1.5rem;"></i>
                </div>
                <div style="text-align: left; max-width: 900px;">
                    <div style="color: #1a1a2e; font-weight: 700; font-size: 1.15rem; margin-bottom: 6px;">IATF 16949 Recognition</div>
                    <div style="color: #666; font-size: 1.05rem; line-height: 1.7;">This standard is recognized by all major automotive OEMs worldwide including BMW, Daimler, Ford, GM, Stellantis, Volkswagen Group, and many others. A single IATF 16949 certification eliminates the need for multiple customer-specific audits.</div>
                </div>
            </div>
        </div>
    </div>
</section>

'''

            # Replace the section
            updated_content = re.sub(old_stats_pattern, new_stats, content, flags=re.DOTALL)

            if updated_content != content:
                iatf_page.body[0].value['html'] = updated_content
                iatf_page.save_revision().publish()

                self.stdout.write(self.style.SUCCESS('✓ Stats cards enhanced successfully!'))
                self.stdout.write(self.style.SUCCESS('✓ Added icon badges to each card'))
                self.stdout.write(self.style.SUCCESS('✓ Enhanced hover effects with scale animation'))
                self.stdout.write(self.style.SUCCESS('✓ Gradient text for numbers'))
                self.stdout.write(self.style.SUCCESS('✓ Added decorative elements and badges'))
                self.stdout.write(self.style.SUCCESS('✓ Included additional info banner'))
                self.stdout.write(self.style.SUCCESS('\nView at: http://localhost:8000/iatf-16949/'))
            else:
                self.stdout.write(self.style.WARNING('Section pattern not found - no changes made'))

        except FlexiblePage.DoesNotExist:
            self.stdout.write(self.style.ERROR('✗ IATF 16949 page not found'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ Error: {e}'))
            import traceback
            traceback.print_exc()

        self.stdout.write(self.style.SUCCESS('\n=== Complete ===\n'))
