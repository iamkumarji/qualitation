"""
Django management command to fix the IATF 16949 Certification Journey timeline
Makes the timeline visible and improves the visual design
"""

from django.core.management.base import BaseCommand
from home.models import FlexiblePage
import re


class Command(BaseCommand):
    help = 'Fix the IATF 16949 Certification Journey timeline visibility'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('\n=== Fixing IATF Timeline ===\n'))

        try:
            # Get the IATF page
            iatf_page = FlexiblePage.objects.get(slug='iatf-16949')
            content = iatf_page.body[0].value['html']

            # Find and replace the Certification Journey section
            old_section_pattern = r'<!-- Certification Journey Section -->.*?(?=<!-- Common Mistakes Section -->)'

            new_section = '''<!-- Certification Journey Section -->
<section style="background: linear-gradient(180deg, #f8f9fa 0%, #ffffff 50%, #f8f9fa 100%); padding: 80px 20px;">
    <div style="max-width: 1100px; margin: 0 auto;">
        <div style="text-align: center; margin-bottom: 60px;">
            <div style="display: inline-block; background: linear-gradient(135deg, #667eea, #764ba2); padding: 8px 20px; border-radius: 50px; margin-bottom: 20px;">
                <span style="color: white; font-size: 0.85rem; font-weight: 700; letter-spacing: 1px;">YOUR PATH TO CERTIFICATION</span>
            </div>
            <h2 style="color: #1a1a2e; font-size: 2.6rem; margin-bottom: 20px; font-weight: 800;">The Certification Journey</h2>
            <p style="color: #666; font-size: 1.2rem; max-width: 750px; margin: 0 auto;">A proven step-by-step process to achieve IATF 16949 certification</p>
        </div>

        <div style="position: relative; max-width: 900px; margin: 0 auto;">
            <!-- Visible Timeline connector -->
            <div style="position: absolute; left: 50%; top: 0; bottom: 0; width: 4px; background: linear-gradient(180deg, #e94560 0%, #667eea 20%, #11998e 40%, #fb923c 60%, #a855f7 80%, #14b8a6 100%); transform: translateX(-50%); border-radius: 10px; z-index: 0;"></div>

            <div style="display: flex; flex-direction: column; gap: 50px; position: relative; z-index: 1;">
                <!-- Step 1 - Left -->
                <div style="display: grid; grid-template-columns: 1fr 80px 1fr; gap: 30px; align-items: center;">
                    <div style="background: white; padding: 35px; border-radius: 20px; box-shadow: 0 10px 35px rgba(233,69,96,0.12); border: 2px solid #ffe5eb; transition: all 0.3s;" onmouseover="this.style.transform='translateX(-10px)'; this.style.boxShadow='0 15px 45px rgba(233,69,96,0.2)'" onmouseout="this.style.transform='translateX(0)'; this.style.boxShadow='0 10px 35px rgba(233,69,96,0.12)'">
                        <div style="display: flex; align-items: center; gap: 20px; margin-bottom: 20px;">
                            <div style="background: linear-gradient(135deg, #e94560, #ff6b6b); width: 60px; height: 60px; border-radius: 15px; display: flex; align-items: center; justify-content: center; color: white; font-weight: 800; font-size: 1.6rem; flex-shrink: 0; box-shadow: 0 8px 20px rgba(233,69,96,0.4);">1</div>
                            <h3 style="color: #1a1a2e; font-size: 1.4rem; margin: 0; font-weight: 700;">Initial Gap Analysis</h3>
                        </div>
                        <p style="color: #666; font-size: 1.08rem; line-height: 1.8; margin: 0;">Comprehensive assessment of your current quality system against IATF 16949 requirements to identify gaps and development needs.</p>
                    </div>
                    <div style="display: flex; justify-content: center; align-items: center;">
                        <div style="background: white; width: 28px; height: 28px; border-radius: 50%; border: 5px solid #e94560; box-shadow: 0 0 0 4px rgba(233,69,96,0.2), 0 4px 15px rgba(233,69,96,0.3);"></div>
                    </div>
                    <div></div>
                </div>

                <!-- Step 2 - Right -->
                <div style="display: grid; grid-template-columns: 1fr 80px 1fr; gap: 30px; align-items: center;">
                    <div></div>
                    <div style="display: flex; justify-content: center; align-items: center;">
                        <div style="background: white; width: 28px; height: 28px; border-radius: 50%; border: 5px solid #667eea; box-shadow: 0 0 0 4px rgba(102,126,234,0.2), 0 4px 15px rgba(102,126,234,0.3);"></div>
                    </div>
                    <div style="background: white; padding: 35px; border-radius: 20px; box-shadow: 0 10px 35px rgba(102,126,234,0.12); border: 2px solid #dae5ff; transition: all 0.3s;" onmouseover="this.style.transform='translateX(10px)'; this.style.boxShadow='0 15px 45px rgba(102,126,234,0.2)'" onmouseout="this.style.transform='translateX(0)'; this.style.boxShadow='0 10px 35px rgba(102,126,234,0.12)'">
                        <div style="display: flex; align-items: center; gap: 20px; margin-bottom: 20px;">
                            <div style="background: linear-gradient(135deg, #667eea, #764ba2); width: 60px; height: 60px; border-radius: 15px; display: flex; align-items: center; justify-content: center; color: white; font-weight: 800; font-size: 1.6rem; flex-shrink: 0; box-shadow: 0 8px 20px rgba(102,126,234,0.4);">2</div>
                            <h3 style="color: #1a1a2e; font-size: 1.4rem; margin: 0; font-weight: 700;">System Development</h3>
                        </div>
                        <p style="color: #666; font-size: 1.08rem; line-height: 1.8; margin: 0;">Build processes, procedures, core tools (APQP, FMEA, PPAP, MSA, SPC, Control Plans) and documentation to meet standard requirements.</p>
                    </div>
                </div>

                <!-- Step 3 - Left -->
                <div style="display: grid; grid-template-columns: 1fr 80px 1fr; gap: 30px; align-items: center;">
                    <div style="background: white; padding: 35px; border-radius: 20px; box-shadow: 0 10px 35px rgba(17,153,142,0.12); border: 2px solid #d1fae5; transition: all 0.3s;" onmouseover="this.style.transform='translateX(-10px)'; this.style.boxShadow='0 15px 45px rgba(17,153,142,0.2)'" onmouseout="this.style.transform='translateX(0)'; this.style.boxShadow='0 10px 35px rgba(17,153,142,0.12)'">
                        <div style="display: flex; align-items: center; gap: 20px; margin-bottom: 20px;">
                            <div style="background: linear-gradient(135deg, #11998e, #38ef7d); width: 60px; height: 60px; border-radius: 15px; display: flex; align-items: center; justify-content: center; color: white; font-weight: 800; font-size: 1.6rem; flex-shrink: 0; box-shadow: 0 8px 20px rgba(17,153,142,0.4);">3</div>
                            <h3 style="color: #1a1a2e; font-size: 1.4rem; margin: 0; font-weight: 700;">Training & Implementation</h3>
                        </div>
                        <p style="color: #666; font-size: 1.08rem; line-height: 1.8; margin: 0;">Staff training on new processes, core tools, and requirements. Practical implementation with consultant support and monitoring.</p>
                    </div>
                    <div style="display: flex; justify-content: center; align-items: center;">
                        <div style="background: white; width: 28px; height: 28px; border-radius: 50%; border: 5px solid #11998e; box-shadow: 0 0 0 4px rgba(17,153,142,0.2), 0 4px 15px rgba(17,153,142,0.3);"></div>
                    </div>
                    <div></div>
                </div>

                <!-- Step 4 - Right -->
                <div style="display: grid; grid-template-columns: 1fr 80px 1fr; gap: 30px; align-items: center;">
                    <div></div>
                    <div style="display: flex; justify-content: center; align-items: center;">
                        <div style="background: white; width: 28px; height: 28px; border-radius: 50%; border: 5px solid #fb923c; box-shadow: 0 0 0 4px rgba(251,146,60,0.2), 0 4px 15px rgba(251,146,60,0.3);"></div>
                    </div>
                    <div style="background: white; padding: 35px; border-radius: 20px; box-shadow: 0 10px 35px rgba(251,146,60,0.12); border: 2px solid #fef3c7; transition: all 0.3s;" onmouseover="this.style.transform='translateX(10px)'; this.style.boxShadow='0 15px 45px rgba(251,146,60,0.2)'" onmouseout="this.style.transform='translateX(0)'; this.style.boxShadow='0 10px 35px rgba(251,146,60,0.12)'">
                        <div style="display: flex; align-items: center; gap: 20px; margin-bottom: 20px;">
                            <div style="background: linear-gradient(135deg, #fb923c, #f97316); width: 60px; height: 60px; border-radius: 15px; display: flex; align-items: center; justify-content: center; color: white; font-weight: 800; font-size: 1.6rem; flex-shrink: 0; box-shadow: 0 8px 20px rgba(251,146,60,0.4);">4</div>
                            <h3 style="color: #1a1a2e; font-size: 1.4rem; margin: 0; font-weight: 700;">Internal Audits</h3>
                        </div>
                        <p style="color: #666; font-size: 1.08rem; line-height: 1.8; margin: 0;">Conduct comprehensive internal audits to verify system effectiveness, identify improvements, and ensure readiness for certification audit.</p>
                    </div>
                </div>

                <!-- Step 5 - Left -->
                <div style="display: grid; grid-template-columns: 1fr 80px 1fr; gap: 30px; align-items: center;">
                    <div style="background: white; padding: 35px; border-radius: 20px; box-shadow: 0 10px 35px rgba(168,85,247,0.12); border: 2px solid #f3e8ff; transition: all 0.3s;" onmouseover="this.style.transform='translateX(-10px)'; this.style.boxShadow='0 15px 45px rgba(168,85,247,0.2)'" onmouseout="this.style.transform='translateX(0)'; this.style.boxShadow='0 10px 35px rgba(168,85,247,0.12)'">
                        <div style="display: flex; align-items: center; gap: 20px; margin-bottom: 20px;">
                            <div style="background: linear-gradient(135deg, #a855f7, #7c3aed); width: 60px; height: 60px; border-radius: 15px; display: flex; align-items: center; justify-content: center; color: white; font-weight: 800; font-size: 1.6rem; flex-shrink: 0; box-shadow: 0 8px 20px rgba(168,85,247,0.4);">5</div>
                            <h3 style="color: #1a1a2e; font-size: 1.4rem; margin: 0; font-weight: 700;">Certification Audit</h3>
                        </div>
                        <p style="color: #666; font-size: 1.08rem; line-height: 1.8; margin: 0;">Independent IATF-recognized certification body conducts Stage 1 (documentation review) and Stage 2 (on-site verification) audits.</p>
                    </div>
                    <div style="display: flex; justify-content: center; align-items: center;">
                        <div style="background: white; width: 28px; height: 28px; border-radius: 50%; border: 5px solid #a855f7; box-shadow: 0 0 0 4px rgba(168,85,247,0.2), 0 4px 15px rgba(168,85,247,0.3);"></div>
                    </div>
                    <div></div>
                </div>

                <!-- Step 6 - Right -->
                <div style="display: grid; grid-template-columns: 1fr 80px 1fr; gap: 30px; align-items: center;">
                    <div></div>
                    <div style="display: flex; justify-content: center; align-items: center;">
                        <div style="background: white; width: 28px; height: 28px; border-radius: 50%; border: 5px solid #14b8a6; box-shadow: 0 0 0 4px rgba(20,184,166,0.2), 0 4px 15px rgba(20,184,166,0.3);"></div>
                    </div>
                    <div style="background: white; padding: 35px; border-radius: 20px; box-shadow: 0 10px 35px rgba(20,184,166,0.12); border: 2px solid #ccfbf1; transition: all 0.3s;" onmouseover="this.style.transform='translateX(10px)'; this.style.boxShadow='0 15px 45px rgba(20,184,166,0.2)'" onmouseout="this.style.transform='translateX(0)'; this.style.boxShadow='0 10px 35px rgba(20,184,166,0.12)'">
                        <div style="display: flex; align-items: center; gap: 20px; margin-bottom: 20px;">
                            <div style="background: linear-gradient(135deg, #14b8a6, #0d9488); width: 60px; height: 60px; border-radius: 15px; display: flex; align-items: center; justify-content: center; color: white; font-weight: 800; font-size: 1.6rem; flex-shrink: 0; box-shadow: 0 8px 20px rgba(20,184,166,0.4);">6</div>
                            <h3 style="color: #1a1a2e; font-size: 1.4rem; margin: 0; font-weight: 700;">Ongoing Maintenance</h3>
                        </div>
                        <p style="color: #666; font-size: 1.08rem; line-height: 1.8; margin: 0;">Continual improvement, annual surveillance audits, and management system maintenance to ensure ongoing compliance and performance.</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- Timeline Info Box -->
        <div style="background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%); padding: 40px; border-radius: 20px; margin-top: 60px; box-shadow: 0 10px 30px rgba(0,0,0,0.08); border: 2px solid #e5e7eb;">
            <div style="display: flex; align-items: start; gap: 25px;">
                <div style="background: linear-gradient(135deg, #667eea, #764ba2); width: 70px; height: 70px; border-radius: 15px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; box-shadow: 0 8px 25px rgba(102,126,234,0.3);">
                    <i class="fas fa-clock" style="color: white; font-size: 2rem;"></i>
                </div>
                <div>
                    <div style="color: #1a1a2e; font-weight: 800; font-size: 1.4rem; margin-bottom: 15px;">Timeline Expectation</div>
                    <div style="color: #666; font-size: 1.1rem; line-height: 1.8;">Typical IATF 16949 certification projects take <strong style="color: #667eea;">9-15 months</strong> from initial assessment to certification, depending on organization size, complexity, existing ISO 9001 maturity, and resource availability. Qualitation works closely with you to accelerate the journey while maintaining quality and ensuring your team fully understands and owns the system.</div>
                    <div style="margin-top: 20px; padding-top: 20px; border-top: 2px solid #e5e7eb;">
                        <div style="display: flex; gap: 30px; flex-wrap: wrap;">
                            <div>
                                <div style="color: #667eea; font-size: 1.8rem; font-weight: 800;">9-12</div>
                                <div style="color: #666; font-size: 0.95rem;">Months (Existing ISO 9001)</div>
                            </div>
                            <div>
                                <div style="color: #e94560; font-size: 1.8rem; font-weight: 800;">12-15</div>
                                <div style="color: #666; font-size: 0.95rem;">Months (Starting Fresh)</div>
                            </div>
                            <div>
                                <div style="color: #11998e; font-size: 1.8rem; font-weight: 800;">100%</div>
                                <div style="color: #666; font-size: 0.95rem;">Our Success Rate</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

'''

            # Replace the section
            updated_content = re.sub(old_section_pattern, new_section, content, flags=re.DOTALL)

            if updated_content != content:
                iatf_page.body[0].value['html'] = updated_content
                iatf_page.save_revision().publish()

                self.stdout.write(self.style.SUCCESS('✓ Timeline fixed and made visible!'))
                self.stdout.write(self.style.SUCCESS('✓ Improved visual design with gradient timeline'))
                self.stdout.write(self.style.SUCCESS('✓ Added alternating left-right layout'))
                self.stdout.write(self.style.SUCCESS('✓ Enhanced step indicators with shadows'))
                self.stdout.write(self.style.SUCCESS('✓ Added timeline info box with statistics'))
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
