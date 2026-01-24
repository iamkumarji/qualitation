"""
Django management command to beautify the IATF 16949 page
Enhances visual design while preserving all existing content
"""

from django.core.management.base import BaseCommand
from home.models import FlexiblePage


class Command(BaseCommand):
    help = 'Beautify the IATF 16949 page with enhanced visual design'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('\n=== Beautifying IATF 16949 Page ===\n'))

        try:
            # Get the IATF page
            iatf_page = FlexiblePage.objects.get(slug='iatf-16949')

            # Get current content
            current_html = iatf_page.body[0].value['html']

            self.stdout.write(f'Current content length: {len(current_html)} characters')

            # Enhanced version with better visual design
            enhanced_html = '''
<!-- Hero Section with Enhanced Gradient and Animation -->
<section style="background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%); padding: 100px 20px; text-align: center; position: relative; overflow: hidden;">
    <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; opacity: 0.08;">
        <svg viewBox="0 0 800 400" style="width: 100%; height: 100%;">
            <circle cx="100" cy="200" r="80" fill="none" stroke="white" stroke-width="2">
                <animate attributeName="r" values="80;90;80" dur="4s" repeatCount="indefinite"/>
            </circle>
            <circle cx="100" cy="200" r="60" fill="none" stroke="white" stroke-width="1">
                <animate attributeName="r" values="60;70;60" dur="3s" repeatCount="indefinite"/>
            </circle>
            <circle cx="100" cy="200" r="40" fill="none" stroke="white" stroke-width="1"/>
            <circle cx="400" cy="200" r="100" fill="none" stroke="white" stroke-width="2">
                <animate attributeName="r" values="100;110;100" dur="5s" repeatCount="indefinite"/>
            </circle>
            <circle cx="700" cy="200" r="70" fill="none" stroke="white" stroke-width="2">
                <animate attributeName="r" values="70;80;70" dur="3.5s" repeatCount="indefinite"/>
            </circle>
            <line x1="180" y1="200" x2="300" y2="200" stroke="white" stroke-width="1"/>
            <line x1="500" y1="200" x2="630" y2="200" stroke="white" stroke-width="1"/>
        </svg>
    </div>
    <div style="max-width: 900px; margin: 0 auto; position: relative; z-index: 1;">
        <div style="margin-bottom: 30px; animation: fadeInDown 1s ease-out;">
            <svg viewBox="0 0 120 120" style="width: 120px; height: 120px; filter: drop-shadow(0 10px 20px rgba(233,69,96,0.3));">
                <defs>
                    <linearGradient id="autoGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" style="stop-color:#e94560"/>
                        <stop offset="100%" style="stop-color:#ff6b6b"/>
                    </linearGradient>
                </defs>
                <path d="M25 70 L30 55 L45 45 L75 45 L90 55 L95 70 L95 80 L25 80 Z" fill="none" stroke="url(#autoGrad)" stroke-width="3"/>
                <circle cx="40" cy="80" r="10" fill="none" stroke="#e94560" stroke-width="3"/>
                <circle cx="80" cy="80" r="10" fill="none" stroke="#e94560" stroke-width="3"/>
                <circle cx="60" cy="30" r="15" fill="none" stroke="#e94560" stroke-width="2"/>
                <path d="M60 15 L60 20 M60 40 L60 45 M45 30 L50 30 M70 30 L75 30 M49 19 L52 22 M68 38 L71 41 M49 41 L52 38 M68 22 L71 19" stroke="#e94560" stroke-width="2" stroke-linecap="round"/>
                <circle cx="60" cy="30" r="6" fill="#e94560"/>
            </svg>
        </div>
        <div style="display: inline-block; background: rgba(233,69,96,0.2); border: 1px solid rgba(233,69,96,0.4); padding: 8px 20px; border-radius: 50px; margin-bottom: 25px; backdrop-filter: blur(10px);">
            <span style="color: #ff6b6b; font-size: 0.9rem; font-weight: 600; letter-spacing: 1px;">AUTOMOTIVE QUALITY STANDARD</span>
        </div>
        <h1 style="color: #ffffff; font-size: 3.2rem; font-weight: 800; margin-bottom: 25px; text-shadow: 2px 4px 8px rgba(0,0,0,0.4); line-height: 1.2;">
            IATF 16949 Automotive Quality Management
        </h1>
        <p style="color: #e0e0e0; font-size: 1.4rem; line-height: 1.9; margin-bottom: 40px; max-width: 750px; margin-left: auto; margin-right: auto;">
            The globally recognised Quality Management System standard for the automotive industry. Essential for UK suppliers to access OEM and Tier 1 supply chains worldwide.
        </p>
        <div style="display: flex; gap: 15px; justify-content: center; flex-wrap: wrap;">
            <a href="/contact/" style="display: inline-flex; align-items: center; gap: 10px; background: linear-gradient(135deg, #e94560, #ff6b6b); color: #ffffff; padding: 16px 40px; text-decoration: none; border-radius: 50px; font-weight: 700; font-size: 1.1rem; box-shadow: 0 10px 30px rgba(233,69,96,0.4); transition: all 0.3s;" onmouseover="this.style.transform='translateY(-3px)'; this.style.boxShadow='0 15px 40px rgba(233,69,96,0.5)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 10px 30px rgba(233,69,96,0.4)'">
                <i class="fas fa-rocket"></i> Start IATF 16949 Certification
            </a>
            <a href="#core-tools" style="display: inline-flex; align-items: center; gap: 10px; background: rgba(255,255,255,0.1); border: 2px solid rgba(255,255,255,0.3); color: #ffffff; padding: 14px 35px; text-decoration: none; border-radius: 50px; font-weight: 600; font-size: 1.1rem; backdrop-filter: blur(10px); transition: all 0.3s;" onmouseover="this.style.background='rgba(255,255,255,0.2)'" onmouseout="this.style.background='rgba(255,255,255,0.1)'">
                <i class="fas fa-tools"></i> Learn About Core Tools
            </a>
        </div>
    </div>
</section>

<style>
@keyframes fadeInDown {
    from {
        opacity: 0;
        transform: translateY(-20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
</style>

<!-- Stats Section with Enhanced Design -->
<section style="background: #ffffff; padding: 60px 20px; box-shadow: 0 -5px 20px rgba(0,0,0,0.05);">
    <div style="max-width: 1100px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 40px; text-align: center;">
        <div style="padding: 30px 20px; background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%); border-radius: 20px; box-shadow: 0 8px 25px rgba(0,0,0,0.06); transition: all 0.3s;" onmouseover="this.style.transform='translateY(-8px)'; this.style.boxShadow='0 15px 35px rgba(0,0,0,0.1)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 8px 25px rgba(0,0,0,0.06)'">
            <div style="background: linear-gradient(135deg, #e94560, #ff6b6b); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-size: 3.2rem; font-weight: 800; margin-bottom: 10px;">70,000+</div>
            <div style="color: #666; font-size: 1.05rem; font-weight: 500;">Certified Sites Globally</div>
        </div>
        <div style="padding: 30px 20px; background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%); border-radius: 20px; box-shadow: 0 8px 25px rgba(0,0,0,0.06); transition: all 0.3s;" onmouseover="this.style.transform='translateY(-8px)'; this.style.boxShadow='0 15px 35px rgba(0,0,0,0.1)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 8px 25px rgba(0,0,0,0.06)'">
            <div style="background: linear-gradient(135deg, #667eea, #764ba2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-size: 3.2rem; font-weight: 800; margin-bottom: 10px;">IATF</div>
            <div style="color: #666; font-size: 1.05rem; font-weight: 500;">International Automotive Task Force</div>
        </div>
        <div style="padding: 30px 20px; background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%); border-radius: 20px; box-shadow: 0 8px 25px rgba(0,0,0,0.06); transition: all 0.3s;" onmouseover="this.style.transform='translateY(-8px)'; this.style.boxShadow='0 15px 35px rgba(0,0,0,0.1)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 8px 25px rgba(0,0,0,0.06)'">
            <div style="background: linear-gradient(135deg, #11998e, #38ef7d); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-size: 3.2rem; font-weight: 800; margin-bottom: 10px;">ISO 9001</div>
            <div style="color: #666; font-size: 1.05rem; font-weight: 500;">Foundation + Automotive Requirements</div>
        </div>
        <div style="padding: 30px 20px; background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%); border-radius: 20px; box-shadow: 0 8px 25px rgba(0,0,0,0.06); transition: all 0.3s;" onmouseover="this.style.transform='translateY(-8px)'; this.style.boxShadow='0 15px 35px rgba(0,0,0,0.1)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 8px 25px rgba(0,0,0,0.06)'">
            <div style="background: linear-gradient(135deg, #f093fb, #f5576c); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-size: 3.2rem; font-weight: 800; margin-bottom: 10px;">3 Years</div>
            <div style="color: #666; font-size: 1.05rem; font-weight: 500;">Certification Cycle</div>
        </div>
    </div>
</section>

<!-- What is IATF 16949 Section with Enhanced Layout -->
<section style="background: linear-gradient(180deg, #f8f9fa 0%, #ffffff 100%); padding: 80px 20px;">
    <div style="max-width: 1200px; margin: 0 auto;">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 60px; align-items: center;">
            <div>
                <div style="display: inline-block; background: linear-gradient(135deg, #e94560, #ff6b6b); padding: 8px 20px; border-radius: 50px; margin-bottom: 20px;">
                    <span style="color: white; font-size: 0.85rem; font-weight: 700; letter-spacing: 1px;">ABOUT THE STANDARD</span>
                </div>
                <h2 style="color: #1a1a2e; font-size: 2.6rem; margin-bottom: 30px; font-weight: 800; line-height: 1.3;">What is IATF 16949?</h2>
                <p style="color: #555; font-size: 1.15rem; line-height: 1.9; margin-bottom: 25px;">
                    IATF 16949 is an international quality management standard for organisations that design, develop, manufacture, install, or service automotive-related products. It replaced ISO/TS 16949 and is maintained by the International Automotive Task Force.
                </p>
                <p style="color: #555; font-size: 1.15rem; line-height: 1.9; margin-bottom: 25px;">
                    The standard builds on ISO 9001 but includes additional automotive-specific requirements focused on product safety, traceability, risk management, supplier quality assurance, defect prevention, and process control.
                </p>
                <p style="color: #555; font-size: 1.15rem; line-height: 1.9; margin-bottom: 30px;">
                    For UK automotive suppliers, IATF 16949 certification is often mandatory to access OEM and Tier 1 supply chains, maintaining credibility in European and global markets post-Brexit.
                </p>
                <div style="background: linear-gradient(135deg, #fff5f7, #ffffff); border-left: 4px solid #e94560; padding: 25px; border-radius: 12px;">
                    <div style="display: flex; align-items: start; gap: 15px;">
                        <div style="background: linear-gradient(135deg, #e94560, #ff6b6b); width: 50px; height: 50px; border-radius: 12px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                            <i class="fas fa-lightbulb" style="color: white; font-size: 1.5rem;"></i>
                        </div>
                        <div>
                            <div style="color: #1a1a2e; font-weight: 700; font-size: 1.1rem; margin-bottom: 8px;">Did You Know?</div>
                            <div style="color: #666; font-size: 1rem; line-height: 1.7;">IATF 16949 certification demonstrates your commitment to automotive quality excellence and is recognized by major OEMs worldwide including BMW, Ford, GM, and Volkswagen.</div>
                        </div>
                    </div>
                </div>
            </div>
            <div style="text-align: center;">
                <div style="background: white; padding: 40px; border-radius: 25px; box-shadow: 0 15px 50px rgba(0,0,0,0.08);">
                    <svg viewBox="0 0 300 280" style="max-width: 100%; height: auto;">
                        <rect x="50" y="40" width="200" height="200" rx="15" fill="#f8f9fa" stroke="#1a1a2e" stroke-width="3"/>
                        <text x="150" y="70" text-anchor="middle" fill="#1a1a2e" font-size="14" font-weight="bold">IATF 16949 STRUCTURE</text>

                        <rect x="70" y="90" width="160" height="45" rx="8" fill="linear-gradient(135deg, #1a1a2e, #0f3460)"/>
                        <rect x="70" y="90" width="160" height="45" rx="8" fill="#1a1a2e"/>
                        <text x="150" y="118" text-anchor="middle" fill="white" font-size="12" font-weight="600">ISO 9001 Foundation</text>

                        <path d="M 150 135 L 150 145" stroke="#e94560" stroke-width="2" marker-end="url(#arrowred)"/>

                        <rect x="70" y="145" width="160" height="45" rx="8" fill="#e94560"/>
                        <text x="150" y="165" text-anchor="middle" fill="white" font-size="11" font-weight="600">Automotive-Specific</text>
                        <text x="150" y="180" text-anchor="middle" fill="white" font-size="11" font-weight="600">Requirements</text>

                        <path d="M 150 190 L 150 200" stroke="#667eea" stroke-width="2" marker-end="url(#arrowblue)"/>

                        <rect x="70" y="200" width="160" height="45" rx="8" fill="#16213e"/>
                        <text x="150" y="220" text-anchor="middle" fill="white" font-size="11" font-weight="600">Customer-Specific</text>
                        <text x="150" y="235" text-anchor="middle" fill="white" font-size="11" font-weight="600">Requirements</text>

                        <defs>
                            <marker id="arrowred" markerWidth="10" markerHeight="10" refX="5" refY="3" orient="auto" markerUnits="strokeWidth">
                                <path d="M0,0 L0,6 L9,3 z" fill="#e94560" />
                            </marker>
                            <marker id="arrowblue" markerWidth="10" markerHeight="10" refX="5" refY="3" orient="auto" markerUnits="strokeWidth">
                                <path d="M0,0 L0,6 L9,3 z" fill="#667eea" />
                            </marker>
                        </defs>
                    </svg>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Key Principles Section with Enhanced Cards -->
<section style="background: white; padding: 80px 20px;">
    <div style="max-width: 1200px; margin: 0 auto;">
        <div style="text-align: center; margin-bottom: 60px;">
            <div style="display: inline-block; background: linear-gradient(135deg, #667eea, #764ba2); padding: 8px 20px; border-radius: 50px; margin-bottom: 20px;">
                <span style="color: white; font-size: 0.85rem; font-weight: 700; letter-spacing: 1px;">CORE PRINCIPLES</span>
            </div>
            <h2 style="color: #1a1a2e; font-size: 2.6rem; margin-bottom: 20px; font-weight: 800;">Key Principles of IATF 16949</h2>
            <p style="color: #666; font-size: 1.2rem; max-width: 700px; margin: 0 auto;">Six fundamental principles that drive automotive quality excellence</p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 35px;">
            <!-- Defect Prevention -->
            <div style="background: linear-gradient(135deg, #fff5f7 0%, #ffffff 100%); padding: 35px; border-radius: 20px; border: 2px solid #ffe5eb; transition: all 0.3s; box-shadow: 0 5px 20px rgba(233,69,96,0.08);" onmouseover="this.style.transform='translateY(-8px)'; this.style.borderColor='#e94560'; this.style.boxShadow='0 15px 40px rgba(233,69,96,0.15)'" onmouseout="this.style.transform='translateY(0)'; this.style.borderColor='#ffe5eb'; this.style.boxShadow='0 5px 20px rgba(233,69,96,0.08)'">
                <div style="background: linear-gradient(135deg, #e94560, #ff6b6b); width: 60px; height: 60px; border-radius: 15px; display: flex; align-items: center; justify-content: center; margin-bottom: 20px; box-shadow: 0 8px 20px rgba(233,69,96,0.3);">
                    <i class="fas fa-shield-alt" style="color: white; font-size: 1.8rem;"></i>
                </div>
                <h3 style="color: #1a1a2e; font-size: 1.4rem; margin-bottom: 15px; font-weight: 700;">Defect Prevention</h3>
                <p style="color: #666; font-size: 1.05rem; line-height: 1.8; margin: 0;">Focuses on preventing defects rather than detecting them through robust process design, FMEA, control plans, and preventive actions.</p>
            </div>

            <!-- Product Safety -->
            <div style="background: linear-gradient(135deg, #f0f4ff 0%, #ffffff 100%); padding: 35px; border-radius: 20px; border: 2px solid #dae5ff; transition: all 0.3s; box-shadow: 0 5px 20px rgba(102,126,234,0.08);" onmouseover="this.style.transform='translateY(-8px)'; this.style.borderColor='#667eea'; this.style.boxShadow='0 15px 40px rgba(102,126,234,0.15)'" onmouseout="this.style.transform='translateY(0)'; this.style.borderColor='#dae5ff'; this.style.boxShadow='0 5px 20px rgba(102,126,234,0.08)'">
                <div style="background: linear-gradient(135deg, #667eea, #764ba2); width: 60px; height: 60px; border-radius: 15px; display: flex; align-items: center; justify-content: center; margin-bottom: 20px; box-shadow: 0 8px 20px rgba(102,126,234,0.3);">
                    <i class="fas fa-user-shield" style="color: white; font-size: 1.8rem;"></i>
                </div>
                <h3 style="color: #1a1a2e; font-size: 1.4rem; margin-bottom: 15px; font-weight: 700;">Product Safety</h3>
                <p style="color: #666; font-size: 1.05rem; line-height: 1.8; margin: 0;">Emphasizes identification and management of safety-related products and manufacturing processes with stringent controls and documentation.</p>
            </div>

            <!-- Process Approach -->
            <div style="background: linear-gradient(135deg, #f0fdf8 0%, #ffffff 100%); padding: 35px; border-radius: 20px; border: 2px solid #d1fae5; transition: all 0.3s; box-shadow: 0 5px 20px rgba(17,153,142,0.08);" onmouseover="this.style.transform='translateY(-8px)'; this.style.borderColor='#11998e'; this.style.boxShadow='0 15px 40px rgba(17,153,142,0.15)'" onmouseout="this.style.transform='translateY(0)'; this.style.borderColor='#d1fae5'; this.style.boxShadow='0 5px 20px rgba(17,153,142,0.08)'">
                <div style="background: linear-gradient(135deg, #11998e, #38ef7d); width: 60px; height: 60px; border-radius: 15px; display: flex; align-items: center; justify-content: center; margin-bottom: 20px; box-shadow: 0 8px 20px rgba(17,153,142,0.3);">
                    <i class="fas fa-project-diagram" style="color: white; font-size: 1.8rem;"></i>
                </div>
                <h3 style="color: #1a1a2e; font-size: 1.4rem; margin-bottom: 15px; font-weight: 700;">Process Approach</h3>
                <p style="color: #666; font-size: 1.05rem; line-height: 1.8; margin: 0;">Managing activities and resources as processes to achieve desired results consistently and efficiently throughout the value stream.</p>
            </div>

            <!-- Continual Improvement -->
            <div style="background: linear-gradient(135deg, #fffbf0 0%, #ffffff 100%); padding: 35px; border-radius: 20px; border: 2px solid #fef3c7; transition: all 0.3s; box-shadow: 0 5px 20px rgba(251,146,60,0.08);" onmouseover="this.style.transform='translateY(-8px)'; this.style.borderColor='#fb923c'; this.style.boxShadow='0 15px 40px rgba(251,146,60,0.15)'" onmouseout="this.style.transform='translateY(0)'; this.style.borderColor='#fef3c7'; this.style.boxShadow='0 5px 20px rgba(251,146,60,0.08)'">
                <div style="background: linear-gradient(135deg, #fb923c, #f97316); width: 60px; height: 60px; border-radius: 15px; display: flex; align-items: center; justify-content: center; margin-bottom: 20px; box-shadow: 0 8px 20px rgba(251,146,60,0.3);">
                    <i class="fas fa-chart-line" style="color: white; font-size: 1.8rem;"></i>
                </div>
                <h3 style="color: #1a1a2e; font-size: 1.4rem; margin-bottom: 15px; font-weight: 700;">Continual Improvement</h3>
                <p style="color: #666; font-size: 1.05rem; line-height: 1.8; margin: 0;">Systematic approach to continuous enhancement using methodologies like Lean, Six Sigma, Kaizen, and lessons learned from internal/external sources.</p>
            </div>

            <!-- Supplier Management -->
            <div style="background: linear-gradient(135deg, #fdf4ff 0%, #ffffff 100%); padding: 35px; border-radius: 20px; border: 2px solid #f3e8ff; transition: all 0.3s; box-shadow: 0 5px 20px rgba(168,85,247,0.08);" onmouseover="this.style.transform='translateY(-8px)'; this.style.borderColor='#a855f7'; this.style.boxShadow='0 15px 40px rgba(168,85,247,0.15)'" onmouseout="this.style.transform='translateY(0)'; this.style.borderColor='#f3e8ff'; this.style.boxShadow='0 5px 20px rgba(168,85,247,0.08)'">
                <div style="background: linear-gradient(135deg, #a855f7, #7c3aed); width: 60px; height: 60px; border-radius: 15px; display: flex; align-items: center; justify-content: center; margin-bottom: 20px; box-shadow: 0 8px 20px rgba(168,85,247,0.3);">
                    <i class="fas fa-handshake" style="color: white; font-size: 1.8rem;"></i>
                </div>
                <h3 style="color: #1a1a2e; font-size: 1.4rem; margin-bottom: 15px; font-weight: 700;">Supplier Management</h3>
                <p style="color: #666; font-size: 1.05rem; line-height: 1.8; margin: 0;">Comprehensive supplier selection, monitoring, and development to ensure supply chain quality meets automotive industry requirements.</p>
            </div>

            <!-- Risk-Based Thinking -->
            <div style="background: linear-gradient(135deg, #f0fdfa 0%, #ffffff 100%); padding: 35px; border-radius: 20px; border: 2px solid #ccfbf1; transition: all 0.3s; box-shadow: 0 5px 20px rgba(20,184,166,0.08);" onmouseover="this.style.transform='translateY(-8px)'; this.style.borderColor='#14b8a6'; this.style.boxShadow='0 15px 40px rgba(20,184,166,0.15)'" onmouseout="this.style.transform='translateY(0)'; this.style.borderColor='#ccfbf1'; this.style.boxShadow='0 5px 20px rgba(20,184,166,0.08)'">
                <div style="background: linear-gradient(135deg, #14b8a6, #0d9488); width: 60px; height: 60px; border-radius: 15px; display: flex; align-items: center; justify-content: center; margin-bottom: 20px; box-shadow: 0 8px 20px rgba(20,184,166,0.3);">
                    <i class="fas fa-brain" style="color: white; font-size: 1.8rem;"></i>
                </div>
                <h3 style="color: #1a1a2e; font-size: 1.4rem; margin-bottom: 15px; font-weight: 700;">Risk-Based Thinking</h3>
                <p style="color: #666; font-size: 1.05rem; line-height: 1.8; margin: 0;">Proactive identification and mitigation of risks and opportunities throughout all processes to prevent issues before they occur.</p>
            </div>
        </div>
    </div>
</section>

<!-- Core Tools Section with Dark Background -->
<section id="core-tools" style="background: linear-gradient(135deg, #1a1a2e 0%, #0f3460 100%); padding: 90px 20px; position: relative; overflow: hidden;">
    <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; opacity: 0.03;">
        <div style="position: absolute; top: 20%; left: 10%; width: 300px; height: 300px; background: white; border-radius: 50%; filter: blur(100px);"></div>
        <div style="position: absolute; bottom: 20%; right: 10%; width: 350px; height: 350px; background: #e94560; border-radius: 50%; filter: blur(120px);"></div>
    </div>

    <div style="max-width: 1200px; margin: 0 auto; position: relative; z-index: 1;">
        <div style="text-align: center; margin-bottom: 60px;">
            <div style="display: inline-block; background: rgba(233,69,96,0.2); border: 1px solid rgba(233,69,96,0.4); padding: 8px 20px; border-radius: 50px; margin-bottom: 20px; backdrop-filter: blur(10px);">
                <span style="color: #ff6b6b; font-size: 0.85rem; font-weight: 700; letter-spacing: 1px;">ESSENTIAL METHODOLOGIES</span>
            </div>
            <h2 style="color: #ffffff; font-size: 2.6rem; margin-bottom: 20px; font-weight: 800;">IATF 16949 Core Tools</h2>
            <p style="color: rgba(255,255,255,0.8); font-size: 1.2rem; max-width: 800px; margin: 0 auto;">Six fundamental tools that automotive suppliers must master for effective quality management</p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 35px;">
            <!-- APQP -->
            <div style="background: rgba(255,255,255,0.08); backdrop-filter: blur(10px); padding: 40px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.1); transition: all 0.3s;" onmouseover="this.style.background='rgba(255,255,255,0.12)'; this.style.borderColor='rgba(233,69,96,0.4)'; this.style.transform='translateY(-5px)'" onmouseout="this.style.background='rgba(255,255,255,0.08)'; this.style.borderColor='rgba(255,255,255,0.1)'; this.style.transform='translateY(0)'">
                <div style="display: flex; align-items: center; gap: 20px; margin-bottom: 20px;">
                    <div style="background: linear-gradient(135deg, #e94560, #ff6b6b); width: 65px; height: 65px; border-radius: 15px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; box-shadow: 0 8px 25px rgba(233,69,96,0.4);">
                        <i class="fas fa-tasks" style="color: white; font-size: 2rem;"></i>
                    </div>
                    <h3 style="color: #ffffff; font-size: 1.5rem; margin: 0; font-weight: 700; line-height: 1.3;">APQP</h3>
                </div>
                <div style="color: #e94560; font-weight: 600; font-size: 1rem; margin-bottom: 15px; letter-spacing: 0.5px;">Advanced Product Quality Planning</div>
                <p style="color: rgba(255,255,255,0.85); font-size: 1.05rem; line-height: 1.8; margin: 0;">Structured methodology for developing products and processes, ensuring quality is built-in from concept through launch and beyond.</p>
            </div>

            <!-- PPAP -->
            <div style="background: rgba(255,255,255,0.08); backdrop-filter: blur(10px); padding: 40px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.1); transition: all 0.3s;" onmouseover="this.style.background='rgba(255,255,255,0.12)'; this.style.borderColor='rgba(233,69,96,0.4)'; this.style.transform='translateY(-5px)'" onmouseout="this.style.background='rgba(255,255,255,0.08)'; this.style.borderColor='rgba(255,255,255,0.1)'; this.style.transform='translateY(0)'">
                <div style="display: flex; align-items: center; gap: 20px; margin-bottom: 20px;">
                    <div style="background: linear-gradient(135deg, #667eea, #764ba2); width: 65px; height: 65px; border-radius: 15px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; box-shadow: 0 8px 25px rgba(102,126,234,0.4);">
                        <i class="fas fa-check-double" style="color: white; font-size: 2rem;"></i>
                    </div>
                    <h3 style="color: #ffffff; font-size: 1.5rem; margin: 0; font-weight: 700; line-height: 1.3;">PPAP</h3>
                </div>
                <div style="color: #667eea; font-weight: 600; font-size: 1rem; margin-bottom: 15px; letter-spacing: 0.5px;">Production Part Approval Process</div>
                <p style="color: rgba(255,255,255,0.85); font-size: 1.05rem; line-height: 1.8; margin: 0;">Demonstrates that manufacturing processes can consistently produce parts meeting customer specifications and requirements.</p>
            </div>

            <!-- FMEA -->
            <div style="background: rgba(255,255,255,0.08); backdrop-filter: blur(10px); padding: 40px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.1); transition: all 0.3s;" onmouseover="this.style.background='rgba(255,255,255,0.12)'; this.style.borderColor='rgba(233,69,96,0.4)'; this.style.transform='translateY(-5px)'" onmouseout="this.style.background='rgba(255,255,255,0.08)'; this.style.borderColor='rgba(255,255,255,0.1)'; this.style.transform='translateY(0)'">
                <div style="display: flex; align-items: center; gap: 20px; margin-bottom: 20px;">
                    <div style="background: linear-gradient(135deg, #11998e, #38ef7d); width: 65px; height: 65px; border-radius: 15px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; box-shadow: 0 8px 25px rgba(17,153,142,0.4);">
                        <i class="fas fa-exclamation-triangle" style="color: white; font-size: 2rem;"></i>
                    </div>
                    <h3 style="color: #ffffff; font-size: 1.5rem; margin: 0; font-weight: 700; line-height: 1.3;">FMEA</h3>
                </div>
                <div style="color: #38ef7d; font-weight: 600; font-size: 1rem; margin-bottom: 15px; letter-spacing: 0.5px;">Failure Mode and Effects Analysis</div>
                <p style="color: rgba(255,255,255,0.85); font-size: 1.05rem; line-height: 1.8; margin: 0;">Systematic approach to identify potential failures, assess risk, and implement preventive actions before problems occur.</p>
            </div>

            <!-- MSA -->
            <div style="background: rgba(255,255,255,0.08); backdrop-filter: blur(10px); padding: 40px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.1); transition: all 0.3s;" onmouseover="this.style.background='rgba(255,255,255,0.12)'; this.style.borderColor='rgba(233,69,96,0.4)'; this.style.transform='translateY(-5px)'" onmouseout="this.style.background='rgba(255,255,255,0.08)'; this.style.borderColor='rgba(255,255,255,0.1)'; this.style.transform='translateY(0)'">
                <div style="display: flex; align-items: center; gap: 20px; margin-bottom: 20px;">
                    <div style="background: linear-gradient(135deg, #fb923c, #f97316); width: 65px; height: 65px; border-radius: 15px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; box-shadow: 0 8px 25px rgba(251,146,60,0.4);">
                        <i class="fas fa-ruler-combined" style="color: white; font-size: 2rem;"></i>
                    </div>
                    <h3 style="color: #ffffff; font-size: 1.5rem; margin: 0; font-weight: 700; line-height: 1.3;">MSA</h3>
                </div>
                <div style="color: #fb923c; font-weight: 600; font-size: 1rem; margin-bottom: 15px; letter-spacing: 0.5px;">Measurement Systems Analysis</div>
                <p style="color: rgba(255,255,255,0.85); font-size: 1.05rem; line-height: 1.8; margin: 0;">Evaluates measurement system variation and ensures measurement processes are capable and reliable for decision-making.</p>
            </div>

            <!-- SPC -->
            <div style="background: rgba(255,255,255,0.08); backdrop-filter: blur(10px); padding: 40px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.1); transition: all 0.3s;" onmouseover="this.style.background='rgba(255,255,255,0.12)'; this.style.borderColor='rgba(233,69,96,0.4)'; this.style.transform='translateY(-5px)'" onmouseout="this.style.background='rgba(255,255,255,0.08)'; this.style.borderColor='rgba(255,255,255,0.1)'; this.style.transform='translateY(0)'">
                <div style="display: flex; align-items: center; gap: 20px; margin-bottom: 20px;">
                    <div style="background: linear-gradient(135deg, #a855f7, #7c3aed); width: 65px; height: 65px; border-radius: 15px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; box-shadow: 0 8px 25px rgba(168,85,247,0.4);">
                        <i class="fas fa-chart-bar" style="color: white; font-size: 2rem;"></i>
                    </div>
                    <h3 style="color: #ffffff; font-size: 1.5rem; margin: 0; font-weight: 700; line-height: 1.3;">SPC</h3>
                </div>
                <div style="color: #a855f7; font-weight: 600; font-size: 1rem; margin-bottom: 15px; letter-spacing: 0.5px;">Statistical Process Control</div>
                <p style="color: rgba(255,255,255,0.85); font-size: 1.05rem; line-height: 1.8; margin: 0;">Uses statistical methods to monitor and control processes, detecting variation and preventing defects proactively.</p>
            </div>

            <!-- Control Plans -->
            <div style="background: rgba(255,255,255,0.08); backdrop-filter: blur(10px); padding: 40px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.1); transition: all 0.3s;" onmouseover="this.style.background='rgba(255,255,255,0.12)'; this.style.borderColor='rgba(233,69,96,0.4)'; this.style.transform='translateY(-5px)'" onmouseout="this.style.background='rgba(255,255,255,0.08)'; this.style.borderColor='rgba(255,255,255,0.1)'; this.style.transform='translateY(0)'">
                <div style="display: flex; align-items: center; gap: 20px; margin-bottom: 20px;">
                    <div style="background: linear-gradient(135deg, #14b8a6, #0d9488); width: 65px; height: 65px; border-radius: 15px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; box-shadow: 0 8px 25px rgba(20,184,166,0.4);">
                        <i class="fas fa-clipboard-list" style="color: white; font-size: 2rem;"></i>
                    </div>
                    <h3 style="color: #ffffff; font-size: 1.5rem; margin: 0; font-weight: 700; line-height: 1.3;">Control Plans</h3>
                </div>
                <div style="color: #14b8a6; font-weight: 600; font-size: 1rem; margin-bottom: 15px; letter-spacing: 0.5px;">Process Control Planning</div>
                <p style="color: rgba(255,255,255,0.85); font-size: 1.05rem; line-height: 1.8; margin: 0;">Documents process controls, measurement methods, and reaction plans to ensure consistent product quality throughout production.</p>
            </div>
        </div>

        <div style="background: rgba(233,69,96,0.1); border: 1px solid rgba(233,69,96,0.3); padding: 30px; border-radius: 15px; margin-top: 50px; backdrop-filter: blur(10px);">
            <div style="display: flex; align-items: start; gap: 20px;">
                <div style="background: linear-gradient(135deg, #e94560, #ff6b6b); width: 55px; height: 55px; border-radius: 12px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                    <i class="fas fa-info-circle" style="color: white; font-size: 1.6rem;"></i>
                </div>
                <div>
                    <div style="color: white; font-weight: 700; font-size: 1.2rem; margin-bottom: 10px;">Core Tools Training</div>
                    <div style="color: rgba(255,255,255,0.9); font-size: 1.05rem; line-height: 1.7;">Qualitation provides comprehensive training on all IATF 16949 core tools. Our expert instructors bring real-world automotive experience and will help your team master these essential methodologies.</div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Benefits Section -->
<section style="background: linear-gradient(180deg, #ffffff 0%, #f8f9fa 100%); padding: 80px 20px;">
    <div style="max-width: 1200px; margin: 0 auto;">
        <div style="text-align: center; margin-bottom: 60px;">
            <div style="display: inline-block; background: linear-gradient(135deg, #11998e, #38ef7d); padding: 8px 20px; border-radius: 50px; margin-bottom: 20px;">
                <span style="color: white; font-size: 0.85rem; font-weight: 700; letter-spacing: 1px;">WHY GET CERTIFIED</span>
            </div>
            <h2 style="color: #1a1a2e; font-size: 2.6rem; margin-bottom: 20px; font-weight: 800;">Benefits of IATF 16949 Certification</h2>
            <p style="color: #666; font-size: 1.2rem; max-width: 750px; margin: 0 auto;">Strategic advantages that extend beyond compliance to drive business success</p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 35px;">
            <div style="background: white; padding: 35px; border-radius: 20px; box-shadow: 0 8px 30px rgba(0,0,0,0.06); border-left: 5px solid #e94560; transition: all 0.3s;" onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 15px 40px rgba(0,0,0,0.1)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 8px 30px rgba(0,0,0,0.06)'">
                <div style="background: linear-gradient(135deg, #fff5f7, #ffe5eb); width: 70px; height: 70px; border-radius: 15px; display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
                    <i class="fas fa-link" style="color: #e94560; font-size: 2rem;"></i>
                </div>
                <h3 style="color: #1a1a2e; font-size: 1.3rem; margin-bottom: 15px; font-weight: 700;">Supply Chain Access</h3>
                <p style="color: #666; font-size: 1.05rem; line-height: 1.8; margin: 0;">Mandatory requirement for supplying to major OEMs and Tier 1 automotive manufacturers globally. Opens doors to international markets.</p>
            </div>

            <div style="background: white; padding: 35px; border-radius: 20px; box-shadow: 0 8px 30px rgba(0,0,0,0.06); border-left: 5px solid #667eea; transition: all 0.3s;" onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 15px 40px rgba(0,0,0,0.1)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 8px 30px rgba(0,0,0,0.06)'">
                <div style="background: linear-gradient(135deg, #f0f4ff, #dae5ff); width: 70px; height: 70px; border-radius: 15px; display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
                    <i class="fas fa-chart-line" style="color: #667eea; font-size: 2rem;"></i>
                </div>
                <h3 style="color: #1a1a2e; font-size: 1.3rem; margin-bottom: 15px; font-weight: 700;">Reduced Defects & Waste</h3>
                <p style="color: #666; font-size: 1.05rem; line-height: 1.8; margin: 0;">Systematic defect prevention and process control reduce scrap, rework, warranty claims, and customer complaints significantly.</p>
            </div>

            <div style="background: white; padding: 35px; border-radius: 20px; box-shadow: 0 8px 30px rgba(0,0,0,0.06); border-left: 5px solid #11998e; transition: all 0.3s;" onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 15px 40px rgba(0,0,0,0.1)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 8px 30px rgba(0,0,0,0.06)'">
                <div style="background: linear-gradient(135deg, #f0fdf8, #d1fae5); width: 70px; height: 70px; border-radius: 15px; display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
                    <i class="fas fa-globe" style="color: #11998e; font-size: 2rem;"></i>
                </div>
                <h3 style="color: #1a1a2e; font-size: 1.3rem; margin-bottom: 15px; font-weight: 700;">Global Recognition</h3>
                <p style="color: #666; font-size: 1.05rem; line-height: 1.8; margin: 0;">Single certification recognized worldwide eliminates multiple customer-specific audits and streamlines international business.</p>
            </div>

            <div style="background: white; padding: 35px; border-radius: 20px; box-shadow: 0 8px 30px rgba(0,0,0,0.06); border-left: 5px solid #fb923c; transition: all 0.3s;" onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 15px 40px rgba(0,0,0,0.1)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 8px 30px rgba(0,0,0,0.06)'">
                <div style="background: linear-gradient(135deg, #fffbf0, #fef3c7); width: 70px; height: 70px; border-radius: 15px; display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
                    <i class="fas fa-cogs" style="color: #fb923c; font-size: 2rem;"></i>
                </div>
                <h3 style="color: #1a1a2e; font-size: 1.3rem; margin-bottom: 15px; font-weight: 700;">Improved Process Control</h3>
                <p style="color: #666; font-size: 1.05rem; line-height: 1.8; margin: 0;">Robust control plans, SPC, and documentation ensure consistent quality output and faster problem resolution when issues arise.</p>
            </div>

            <div style="background: white; padding: 35px; border-radius: 20px; box-shadow: 0 8px 30px rgba(0,0,0,0.06); border-left: 5px solid #a855f7; transition: all 0.3s;" onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 15px 40px rgba(0,0,0,0.1)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 8px 30px rgba(0,0,0,0.06)'">
                <div style="background: linear-gradient(135deg, #fdf4ff, #f3e8ff); width: 70px; height: 70px; border-radius: 15px; display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
                    <i class="fas fa-pound-sign" style="color: #a855f7; font-size: 2rem;"></i>
                </div>
                <h3 style="color: #1a1a2e; font-size: 1.3rem; margin-bottom: 15px; font-weight: 700;">Cost Reduction</h3>
                <p style="color: #666; font-size: 1.05rem; line-height: 1.8; margin: 0;">Lower operational costs through waste reduction, improved efficiency, fewer customer returns, and optimized supplier relationships.</p>
            </div>

            <div style="background: white; padding: 35px; border-radius: 20px; box-shadow: 0 8px 30px rgba(0,0,0,0.06); border-left: 5px solid #14b8a6; transition: all 0.3s;" onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 15px 40px rgba(0,0,0,0.1)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 8px 30px rgba(0,0,0,0.06)'">
                <div style="background: linear-gradient(135deg, #f0fdfa, #ccfbf1); width: 70px; height: 70px; border-radius: 15px; display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
                    <i class="fas fa-users-cog" style="color: #14b8a6; font-size: 2rem;"></i>
                </div>
                <h3 style="color: #1a1a2e; font-size: 1.3rem; margin-bottom: 15px; font-weight: 700;">Employee Engagement</h3>
                <p style="color: #666; font-size: 1.05rem; line-height: 1.8; margin: 0;">Clear processes, training, and involvement in improvement activities increase workforce competency and job satisfaction.</p>
            </div>
        </div>
    </div>
</section>

<!-- Who Needs IATF Section -->
<section style="background: white; padding: 80px 20px;">
    <div style="max-width: 1100px; margin: 0 auto;">
        <div style="text-align: center; margin-bottom: 60px;">
            <div style="display: inline-block; background: linear-gradient(135deg, #e94560, #ff6b6b); padding: 8px 20px; border-radius: 50px; margin-bottom: 20px;">
                <span style="color: white; font-size: 0.85rem; font-weight: 700; letter-spacing: 1px;">TARGET ORGANIZATIONS</span>
            </div>
            <h2 style="color: #1a1a2e; font-size: 2.6rem; margin-bottom: 20px; font-weight: 800;">Who Needs IATF 16949?</h2>
            <p style="color: #666; font-size: 1.2rem; max-width: 800px; margin: 0 auto;">IATF 16949 is applicable to any organization in the automotive supply chain</p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; margin-bottom: 50px;">
            <div style="background: linear-gradient(135deg, #fff5f7 0%, #ffffff 100%); padding: 30px; border-radius: 20px; border: 2px solid #ffe5eb;">
                <div style="color: #e94560; font-size: 2.5rem; margin-bottom: 15px;">
                    <i class="fas fa-industry"></i>
                </div>
                <h3 style="color: #1a1a2e; font-size: 1.3rem; margin-bottom: 15px; font-weight: 700;">Component Manufacturers</h3>
                <p style="color: #666; font-size: 1.05rem; line-height: 1.7; margin-bottom: 15px;">Suppliers producing automotive components, parts, and assemblies</p>
                <ul style="color: #666; font-size: 0.95rem; margin: 0; padding-left: 20px;">
                    <li style="margin-bottom: 8px;">Engine components</li>
                    <li style="margin-bottom: 8px;">Electrical systems</li>
                    <li style="margin-bottom: 8px;">Chassis parts</li>
                    <li>Interior/exterior trim</li>
                </ul>
            </div>

            <div style="background: linear-gradient(135deg, #f0f4ff 0%, #ffffff 100%); padding: 30px; border-radius: 20px; border: 2px solid #dae5ff;">
                <div style="color: #667eea; font-size: 2.5rem; margin-bottom: 15px;">
                    <i class="fas fa-box"></i>
                </div>
                <h3 style="color: #1a1a2e; font-size: 1.3rem; margin-bottom: 15px; font-weight: 700;">Material Suppliers</h3>
                <p style="color: #666; font-size: 1.05rem; line-height: 1.7; margin-bottom: 15px;">Organizations providing raw materials and consumables</p>
                <ul style="color: #666; font-size: 0.95rem; margin: 0; padding-left: 20px;">
                    <li style="margin-bottom: 8px;">Steel and aluminum</li>
                    <li style="margin-bottom: 8px;">Plastics and polymers</li>
                    <li style="margin-bottom: 8px;">Electronics</li>
                    <li>Fasteners and hardware</li>
                </ul>
            </div>

            <div style="background: linear-gradient(135deg, #f0fdf8 0%, #ffffff 100%); padding: 30px; border-radius: 20px; border: 2px solid #d1fae5;">
                <div style="color: #11998e; font-size: 2.5rem; margin-bottom: 15px;">
                    <i class="fas fa-tools"></i>
                </div>
                <h3 style="color: #1a1a2e; font-size: 1.3rem; margin-bottom: 15px; font-weight: 700;">Service Providers</h3>
                <p style="color: #666; font-size: 1.05rem; line-height: 1.7; margin-bottom: 15px;">Support services embedded in the manufacturing process</p>
                <ul style="color: #666; font-size: 0.95rem; margin: 0; padding-left: 20px;">
                    <li style="margin-bottom: 8px;">Heat treatment</li>
                    <li style="margin-bottom: 8px;">Surface finishing</li>
                    <li style="margin-bottom: 8px;">Testing services</li>
                    <li>Calibration labs</li>
                </ul>
            </div>
        </div>

        <div style="background: linear-gradient(135deg, #fffbf0, #ffffff); border-left: 5px solid #fb923c; padding: 30px; border-radius: 15px;">
            <div style="display: flex; align-items: start; gap: 20px;">
                <div style="background: linear-gradient(135deg, #fb923c, #f97316); width: 55px; height: 55px; border-radius: 12px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                    <i class="fas fa-exclamation-circle" style="color: white; font-size: 1.5rem;"></i>
                </div>
                <div>
                    <div style="color: #1a1a2e; font-weight: 700; font-size: 1.2rem; margin-bottom: 10px;">Important Note</div>
                    <div style="color: #666; font-size: 1.05rem; line-height: 1.7;">IATF 16949 cannot be applied in isolation – organizations must first be certified to ISO 9001:2015, as IATF 16949 is a supplement that adds automotive-specific requirements to the ISO 9001 foundation.</div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Certification Journey Section -->
<section style="background: #f8f9fa; padding: 80px 20px;">
    <div style="max-width: 1100px; margin: 0 auto;">
        <div style="text-align: center; margin-bottom: 60px;">
            <div style="display: inline-block; background: linear-gradient(135deg, #667eea, #764ba2); padding: 8px 20px; border-radius: 50px; margin-bottom: 20px;">
                <span style="color: white; font-size: 0.85rem; font-weight: 700; letter-spacing: 1px;">YOUR PATH TO CERTIFICATION</span>
            </div>
            <h2 style="color: #1a1a2e; font-size: 2.6rem; margin-bottom: 20px; font-weight: 800;">The Certification Journey</h2>
            <p style="color: #666; font-size: 1.2rem; max-width: 750px; margin: 0 auto;">A proven step-by-step process to achieve IATF 16949 certification</p>
        </div>

        <div style="position: relative; padding: 0 20px;">
            <!-- Timeline connector -->
            <div style="position: absolute; left: 50%; top: 80px; bottom: 80px; width: 3px; background: linear-gradient(180deg, #e94560, #667eea, #11998e, #fb923c); transform: translateX(-50%); border-radius: 10px; display: none; @media (min-width: 768px) { display: block; }"></div>

            <div style="display: flex; flex-direction: column; gap: 40px;">
                <!-- Step 1 -->
                <div style="display: grid; grid-template-columns: 1fr auto 1fr; gap: 30px; align-items: center;">
                    <div style="background: white; padding: 30px; border-radius: 20px; box-shadow: 0 8px 25px rgba(233,69,96,0.1); border: 2px solid #ffe5eb;">
                        <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 15px;">
                            <div style="background: linear-gradient(135deg, #e94560, #ff6b6b); width: 50px; height: 50px; border-radius: 12px; display: flex; align-items: center; justify-content: center; color: white; font-weight: 800; font-size: 1.3rem; flex-shrink: 0;">1</div>
                            <h3 style="color: #1a1a2e; font-size: 1.3rem; margin: 0; font-weight: 700;">Initial Gap Analysis</h3>
                        </div>
                        <p style="color: #666; font-size: 1.05rem; line-height: 1.7; margin: 0;">Comprehensive assessment of your current quality system against IATF 16949 requirements to identify gaps and development needs.</p>
                    </div>
                    <div style="background: linear-gradient(135deg, #e94560, #ff6b6b); width: 20px; height: 20px; border-radius: 50%; border: 4px solid white; box-shadow: 0 0 0 2px #e94560;"></div>
                    <div></div>
                </div>

                <!-- Step 2 -->
                <div style="display: grid; grid-template-columns: 1fr auto 1fr; gap: 30px; align-items: center;">
                    <div></div>
                    <div style="background: linear-gradient(135deg, #667eea, #764ba2); width: 20px; height: 20px; border-radius: 50%; border: 4px solid white; box-shadow: 0 0 0 2px #667eea;"></div>
                    <div style="background: white; padding: 30px; border-radius: 20px; box-shadow: 0 8px 25px rgba(102,126,234,0.1); border: 2px solid #dae5ff;">
                        <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 15px;">
                            <div style="background: linear-gradient(135deg, #667eea, #764ba2); width: 50px; height: 50px; border-radius: 12px; display: flex; align-items: center; justify-content: center; color: white; font-weight: 800; font-size: 1.3rem; flex-shrink: 0;">2</div>
                            <h3 style="color: #1a1a2e; font-size: 1.3rem; margin: 0; font-weight: 700;">System Development</h3>
                        </div>
                        <p style="color: #666; font-size: 1.05rem; line-height: 1.7; margin: 0;">Build processes, procedures, core tools (APQP, FMEA, PPAP, MSA, SPC, Control Plans) and documentation to meet standard requirements.</p>
                    </div>
                </div>

                <!-- Step 3 -->
                <div style="display: grid; grid-template-columns: 1fr auto 1fr; gap: 30px; align-items: center;">
                    <div style="background: white; padding: 30px; border-radius: 20px; box-shadow: 0 8px 25px rgba(17,153,142,0.1); border: 2px solid #d1fae5;">
                        <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 15px;">
                            <div style="background: linear-gradient(135deg, #11998e, #38ef7d); width: 50px; height: 50px; border-radius: 12px; display: flex; align-items: center; justify-content: center; color: white; font-weight: 800; font-size: 1.3rem; flex-shrink: 0;">3</div>
                            <h3 style="color: #1a1a2e; font-size: 1.3rem; margin: 0; font-weight: 700;">Training & Implementation</h3>
                        </div>
                        <p style="color: #666; font-size: 1.05rem; line-height: 1.7; margin: 0;">Staff training on new processes, core tools, and requirements. Practical implementation with consultant support and monitoring.</p>
                    </div>
                    <div style="background: linear-gradient(135deg, #11998e, #38ef7d); width: 20px; height: 20px; border-radius: 50%; border: 4px solid white; box-shadow: 0 0 0 2px #11998e;"></div>
                    <div></div>
                </div>

                <!-- Step 4 -->
                <div style="display: grid; grid-template-columns: 1fr auto 1fr; gap: 30px; align-items: center;">
                    <div></div>
                    <div style="background: linear-gradient(135deg, #fb923c, #f97316); width: 20px; height: 20px; border-radius: 50%; border: 4px solid white; box-shadow: 0 0 0 2px #fb923c;"></div>
                    <div style="background: white; padding: 30px; border-radius: 20px; box-shadow: 0 8px 25px rgba(251,146,60,0.1); border: 2px solid #fef3c7;">
                        <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 15px;">
                            <div style="background: linear-gradient(135deg, #fb923c, #f97316); width: 50px; height: 50px; border-radius: 12px; display: flex; align-items: center; justify-content: center; color: white; font-weight: 800; font-size: 1.3rem; flex-shrink: 0;">4</div>
                            <h3 style="color: #1a1a2e; font-size: 1.3rem; margin: 0; font-weight: 700;">Internal Audits</h3>
                        </div>
                        <p style="color: #666; font-size: 1.05rem; line-height: 1.7; margin: 0;">Conduct comprehensive internal audits to verify system effectiveness, identify improvements, and ensure readiness for certification audit.</p>
                    </div>
                </div>

                <!-- Step 5 -->
                <div style="display: grid; grid-template-columns: 1fr auto 1fr; gap: 30px; align-items: center;">
                    <div style="background: white; padding: 30px; border-radius: 20px; box-shadow: 0 8px 25px rgba(168,85,247,0.1); border: 2px solid #f3e8ff;">
                        <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 15px;">
                            <div style="background: linear-gradient(135deg, #a855f7, #7c3aed); width: 50px; height: 50px; border-radius: 12px; display: flex; align-items: center; justify-content: center; color: white; font-weight: 800; font-size: 1.3rem; flex-shrink: 0;">5</div>
                            <h3 style="color: #1a1a2e; font-size: 1.3rem; margin: 0; font-weight: 700;">Certification Audit</h3>
                        </div>
                        <p style="color: #666; font-size: 1.05rem; line-height: 1.7; margin: 0;">Independent IATF-recognized certification body conducts Stage 1 (documentation review) and Stage 2 (on-site verification) audits.</p>
                    </div>
                    <div style="background: linear-gradient(135deg, #a855f7, #7c3aed); width: 20px; height: 20px; border-radius: 50%; border: 4px solid white; box-shadow: 0 0 0 2px #a855f7;"></div>
                    <div></div>
                </div>

                <!-- Step 6 -->
                <div style="display: grid; grid-template-columns: 1fr auto 1fr; gap: 30px; align-items: center;">
                    <div></div>
                    <div style="background: linear-gradient(135deg, #14b8a6, #0d9488); width: 20px; height: 20px; border-radius: 50%; border: 4px solid white; box-shadow: 0 0 0 2px #14b8a6;"></div>
                    <div style="background: white; padding: 30px; border-radius: 20px; box-shadow: 0 8px 25px rgba(20,184,166,0.1); border: 2px solid #ccfbf1;">
                        <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 15px;">
                            <div style="background: linear-gradient(135deg, #14b8a6, #0d9488); width: 50px; height: 50px; border-radius: 12px; display: flex; align-items: center; justify-content: center; color: white; font-weight: 800; font-size: 1.3rem; flex-shrink: 0;">6</div>
                            <h3 style="color: #1a1a2e; font-size: 1.3rem; margin: 0; font-weight: 700;">Ongoing Maintenance</h3>
                        </div>
                        <p style="color: #666; font-size: 1.05rem; line-height: 1.7; margin: 0;">Continual improvement, annual surveillance audits, and management system maintenance to ensure ongoing compliance and performance.</p>
                    </div>
                </div>
            </div>
        </div>

        <div style="background: white; padding: 35px; border-radius: 20px; margin-top: 50px; box-shadow: 0 8px 25px rgba(0,0,0,0.06);">
            <div style="display: flex; align-items: start; gap: 20px;">
                <div style="background: linear-gradient(135deg, #667eea, #764ba2); width: 55px; height: 55px; border-radius: 12px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                    <i class="fas fa-clock" style="color: white; font-size: 1.5rem;"></i>
                </div>
                <div>
                    <div style="color: #1a1a2e; font-weight: 700; font-size: 1.2rem; margin-bottom: 10px;">Timeline</div>
                    <div style="color: #666; font-size: 1.05rem; line-height: 1.7;">Typical IATF 16949 certification projects take 9-15 months from initial assessment to certification, depending on organization size, complexity, existing ISO 9001 maturity, and resource availability. Qualitation works closely with you to accelerate the journey while maintaining quality.</div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Common Mistakes Section -->
<section style="background: linear-gradient(180deg, #ffffff 0%, #f8f9fa 100%); padding: 80px 20px;">
    <div style="max-width: 1100px; margin: 0 auto;">
        <div style="text-align: center; margin-bottom: 60px;">
            <div style="display: inline-block; background: linear-gradient(135deg, #e94560, #ff6b6b); padding: 8px 20px; border-radius: 50px; margin-bottom: 20px;">
                <span style="color: white; font-size: 0.85rem; font-weight: 700; letter-spacing: 1px;">AVOID THESE PITFALLS</span>
            </div>
            <h2 style="color: #1a1a2e; font-size: 2.6rem; margin-bottom: 20px; font-weight: 800;">Common IATF 16949 Mistakes to Avoid</h2>
            <p style="color: #666; font-size: 1.2rem; max-width: 800px; margin: 0 auto;">Learn from others' experiences and sidestep these frequent certification challenges</p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 30px;">
            <div style="background: white; padding: 30px; border-radius: 20px; box-shadow: 0 8px 25px rgba(0,0,0,0.05); border-top: 4px solid #e94560;">
                <div style="color: #e94560; font-size: 2rem; margin-bottom: 15px;">
                    <i class="fas fa-file-alt"></i>
                </div>
                <h3 style="color: #1a1a2e; font-size: 1.2rem; margin-bottom: 15px; font-weight: 700;">Treating it as a Documentation Exercise</h3>
                <p style="color: #666; font-size: 1.05rem; line-height: 1.7; margin: 0;">IATF 16949 requires practical implementation, not just paperwork. Focus on embedding processes into daily operations rather than creating shelf-ware.</p>
            </div>

            <div style="background: white; padding: 30px; border-radius: 20px; box-shadow: 0 8px 25px rgba(0,0,0,0.05); border-top: 4px solid #667eea;">
                <div style="color: #667eea; font-size: 2rem; margin-bottom: 15px;">
                    <i class="fas fa-user-times"></i>
                </div>
                <h3 style="color: #1a1a2e; font-size: 1.2rem; margin-bottom: 15px; font-weight: 700;">Insufficient Training</h3>
                <p style="color: #666; font-size: 1.05rem; line-height: 1.7; margin: 0;">Failing to train staff adequately on core tools (FMEA, APQP, SPC, etc.) and new processes leads to poor implementation and audit failures.</p>
            </div>

            <div style="background: white; padding: 30px; border-radius: 20px; box-shadow: 0 8px 25px rgba(0,0,0,0.05); border-top: 4px solid #11998e;">
                <div style="color: #11998e; font-size: 2rem; margin-bottom: 15px;">
                    <i class="fas fa-users-slash"></i>
                </div>
                <h3 style="color: #1a1a2e; font-size: 1.2rem; margin-bottom: 15px; font-weight: 700;">Lack of Top Management Commitment</h3>
                <p style="color: #666; font-size: 1.05rem; line-height: 1.7; margin: 0;">Without visible leadership support, resources, and accountability, certification projects stall and quality culture doesn't develop.</p>
            </div>

            <div style="background: white; padding: 30px; border-radius: 20px; box-shadow: 0 8px 25px rgba(0,0,0,0.05); border-top: 4px solid #fb923c;">
                <div style="color: #fb923c; font-size: 2rem; margin-bottom: 15px;">
                    <i class="fas fa-truck-loading"></i>
                </div>
                <h3 style="color: #1a1a2e; font-size: 1.2rem; margin-bottom: 15px; font-weight: 700;">Ignoring Supplier Management</h3>
                <p style="color: #666; font-size: 1.05rem; line-height: 1.7; margin: 0;">Weak supplier selection, monitoring, and development processes are a major non-conformance. Supplier quality directly impacts your certification.</p>
            </div>

            <div style="background: white; padding: 30px; border-radius: 20px; box-shadow: 0 8px 25px rgba(0,0,0,0.05); border-top: 4px solid #a855f7;">
                <div style="color: #a855f7; font-size: 2rem; margin-bottom: 15px;">
                    <i class="fas fa-copy"></i>
                </div>
                <h3 style="color: #1a1a2e; font-size: 1.2rem; margin-bottom: 15px; font-weight: 700;">Copy-Paste from Templates</h3>
                <p style="color: #666; font-size: 1.05rem; line-height: 1.7; margin: 0;">Generic templates that don't reflect your actual processes are obvious during audits. Documentation must match reality.</p>
            </div>

            <div style="background: white; padding: 30px; border-radius: 20px; box-shadow: 0 8px 25px rgba(0,0,0,0.05); border-top: 4px solid #14b8a6;">
                <div style="color: #14b8a6; font-size: 2rem; margin-bottom: 15px;">
                    <i class="fas fa-shipping-fast"></i>
                </div>
                <h3 style="color: #1a1a2e; font-size: 1.2rem; margin-bottom: 15px; font-weight: 700;">Rushing the Process</h3>
                <p style="color: #666; font-size: 1.05rem; line-height: 1.7; margin: 0;">Attempting certification too quickly without allowing time for processes to embed, data to be collected, and improvements to be made.</p>
            </div>
        </div>
    </div>
</section>

<!-- FAQ Section -->
<section style="background: white; padding: 80px 20px;">
    <div style="max-width: 900px; margin: 0 auto;">
        <div style="text-align: center; margin-bottom: 60px;">
            <div style="display: inline-block; background: linear-gradient(135deg, #667eea, #764ba2); padding: 8px 20px; border-radius: 50px; margin-bottom: 20px;">
                <span style="color: white; font-size: 0.85rem; font-weight: 700; letter-spacing: 1px;">YOUR QUESTIONS ANSWERED</span>
            </div>
            <h2 style="color: #1a1a2e; font-size: 2.6rem; margin-bottom: 20px; font-weight: 800;">Frequently Asked Questions</h2>
            <p style="color: #666; font-size: 1.2rem;">Common questions about IATF 16949 certification</p>
        </div>

        <div style="display: flex; flex-direction: column; gap: 25px;">
            <div style="background: #f8f9fa; padding: 30px; border-radius: 15px; border-left: 5px solid #e94560;">
                <h3 style="color: #1a1a2e; font-size: 1.2rem; margin-bottom: 15px; font-weight: 700; display: flex; align-items: center; gap: 12px;">
                    <i class="fas fa-question-circle" style="color: #e94560;"></i>
                    Do I need ISO 9001 before IATF 16949?
                </h3>
                <p style="color: #666; font-size: 1.05rem; line-height: 1.7; margin: 0;">Yes, absolutely. IATF 16949 is not a standalone standard—it's a supplement to ISO 9001:2015. Your organization must first have ISO 9001 certification before you can pursue IATF 16949. Many organizations achieve both simultaneously if starting from scratch.</p>
            </div>

            <div style="background: #f8f9fa; padding: 30px; border-radius: 15px; border-left: 5px solid #667eea;">
                <h3 style="color: #1a1a2e; font-size: 1.2rem; margin-bottom: 15px; font-weight: 700; display: flex; align-items: center; gap: 12px;">
                    <i class="fas fa-question-circle" style="color: #667eea;"></i>
                    How long does IATF 16949 certification take?
                </h3>
                <p style="color: #666; font-size: 1.05rem; line-height: 1.7; margin: 0;">Typically 9-15 months from initial gap analysis to certification, depending on your starting point, organization size, and resource availability. If you already have mature ISO 9001 systems, the timeline can be shorter. Organizations new to quality management systems should expect closer to 12-15 months.</p>
            </div>

            <div style="background: #f8f9fa; padding: 30px; border-radius: 15px; border-left: 5px solid #11998e;">
                <h3 style="color: #1a1a2e; font-size: 1.2rem; margin-bottom: 15px; font-weight: 700; display: flex; align-items: center; gap: 12px;">
                    <i class="fas fa-question-circle" style="color: #11998e;"></i>
                    What's the difference between IATF 16949 and ISO/TS 16949?
                </h3>
                <p style="color: #666; font-size: 1.05rem; line-height: 1.7; margin: 0;">IATF 16949:2016 replaced ISO/TS 16949:2009 in October 2016. The new version aligns with ISO 9001:2015, strengthens requirements for product safety, traceability, and risk-based thinking, and includes clearer requirements for software embedded products. Organizations certified to ISO/TS 16949 had to transition to IATF 16949 by September 2018.</p>
            </div>

            <div style="background: #f8f9fa; padding: 30px; border-radius: 15px; border-left: 5px solid #fb923c;">
                <h3 style="color: #1a1a2e; font-size: 1.2rem; margin-bottom: 15px; font-weight: 700; display: flex; align-items: center; gap: 12px;">
                    <i class="fas fa-question-circle" style="color: #fb923c;"></i>
                    How much does IATF 16949 certification cost?
                </h3>
                <p style="color: #666; font-size: 1.05rem; line-height: 1.7; margin: 0;">Costs vary significantly based on organization size, complexity, current maturity, and geographic location. Typical UK costs range from £8,000-£25,000+ for consultancy, plus £3,000-£12,000+ for certification body fees over the 3-year cycle. Larger or more complex organizations will be at the higher end. Contact us for a tailored quote.</p>
            </div>

            <div style="background: #f8f9fa; padding: 30px; border-radius: 15px; border-left: 5px solid #a855f7;">
                <h3 style="color: #1a1a2e; font-size: 1.2rem; margin-bottom: 15px; font-weight: 700; display: flex; align-items: center; gap: 12px;">
                    <i class="fas fa-question-circle" style="color: #a855f7;"></i>
                    Can I get certified remotely after COVID-19?
                </h3>
                <p style="color: #666; font-size: 1.05rem; line-height: 1.7; margin: 0;">IATF certification bodies are authorized to conduct partial remote audits under specific conditions. However, Stage 2 certification audits typically still require significant on-site presence to verify manufacturing processes, controls, and shop floor practices. Consult with your chosen certification body about their current remote audit policy.</p>
            </div>

            <div style="background: #f8f9fa; padding: 30px; border-radius: 15px; border-left: 5px solid #14b8a6;">
                <h3 style="color: #1a1a2e; font-size: 1.2rem; margin-bottom: 15px; font-weight: 700; display: flex; align-items: center; gap: 12px;">
                    <i class="fas fa-question-circle" style="color: #14b8a6;"></i>
                    What happens if I fail the certification audit?
                </h3>
                <p style="color: #666; font-size: 1.05rem; line-height: 1.7; margin: 0;">Minor non-conformances require corrective action within 90 days, with evidence submitted to the auditor. Major non-conformances require immediate corrective action and often a return visit by the auditor before certification can be granted. With proper preparation and experienced consultant support, first-time certification success is achievable—Qualitation maintains a 100% first-time pass rate.</p>
            </div>
        </div>
    </div>
</section>

<!-- How Qualitation Can Help -->
<section style="background: linear-gradient(135deg, #1a1a2e 0%, #0f3460 100%); padding: 90px 20px; position: relative; overflow: hidden;">
    <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; opacity: 0.05;">
        <div style="position: absolute; top: 10%; left: 5%; width: 400px; height: 400px; background: white; border-radius: 50%; filter: blur(120px);"></div>
        <div style="position: absolute; bottom: 10%; right: 5%; width: 350px; height: 350px; background: #e94560; border-radius: 50%; filter: blur(100px);"></div>
    </div>

    <div style="max-width: 1100px; margin: 0 auto; position: relative; z-index: 1;">
        <div style="text-align: center; margin-bottom: 60px;">
            <div style="display: inline-block; background: rgba(233,69,96,0.2); border: 1px solid rgba(233,69,96,0.4); padding: 8px 20px; border-radius: 50px; margin-bottom: 20px; backdrop-filter: blur(10px);">
                <span style="color: #ff6b6b; font-size: 0.85rem; font-weight: 700; letter-spacing: 1px;">EXPERT SUPPORT</span>
            </div>
            <h2 style="color: #ffffff; font-size: 2.6rem; margin-bottom: 20px; font-weight: 800;">How Can Qualitation Consultants Help?</h2>
            <p style="color: rgba(255,255,255,0.85); font-size: 1.2rem; max-width: 800px; margin: 0 auto; line-height: 1.7;">We provide end-to-end support for your IATF 16949 certification journey with proven automotive industry expertise</p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 35px; margin-bottom: 60px;">
            <div style="background: rgba(255,255,255,0.08); backdrop-filter: blur(10px); padding: 35px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.1);">
                <div style="background: linear-gradient(135deg, #e94560, #ff6b6b); width: 65px; height: 65px; border-radius: 15px; display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
                    <i class="fas fa-search" style="color: white; font-size: 2rem;"></i>
                </div>
                <h3 style="color: white; font-size: 1.4rem; margin-bottom: 15px; font-weight: 700;">Gap Analysis & Planning</h3>
                <p style="color: rgba(255,255,255,0.85); font-size: 1.05rem; line-height: 1.8; margin: 0;">Comprehensive assessment of your current state, detailed gap analysis, and realistic project plan with milestones and resource requirements.</p>
            </div>

            <div style="background: rgba(255,255,255,0.08); backdrop-filter: blur(10px); padding: 35px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.1);">
                <div style="background: linear-gradient(135deg, #667eea, #764ba2); width: 65px; height: 65px; border-radius: 15px; display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
                    <i class="fas fa-book" style="color: white; font-size: 2rem;"></i>
                </div>
                <h3 style="color: white; font-size: 1.4rem; margin-bottom: 15px; font-weight: 700;">Documentation Development</h3>
                <p style="color: rgba(255,255,255,0.85); font-size: 1.05rem; line-height: 1.8; margin: 0;">Creation or update of quality manuals, procedures, core tools (FMEA, APQP, PPAP, Control Plans), work instructions, and forms that reflect your operations.</p>
            </div>

            <div style="background: rgba(255,255,255,0.08); backdrop-filter: blur(10px); padding: 35px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.1);">
                <div style="background: linear-gradient(135deg, #11998e, #38ef7d); width: 65px; height: 65px; border-radius: 15px; display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
                    <i class="fas fa-chalkboard-teacher" style="color: white; font-size: 2rem;"></i>
                </div>
                <h3 style="color: white; font-size: 1.4rem; margin-bottom: 15px; font-weight: 700;">Training & Coaching</h3>
                <p style="color: rgba(255,255,255,0.85); font-size: 1.05rem; line-height: 1.8; margin: 0;">Practical training on core tools, process approach, internal auditing, and standard requirements. Ongoing coaching during implementation.</p>
            </div>

            <div style="background: rgba(255,255,255,0.08); backdrop-filter: blur(10px); padding: 35px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.1);">
                <div style="background: linear-gradient(135deg, #fb923c, #f97316); width: 65px; height: 65px; border-radius: 15px; display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
                    <i class="fas fa-clipboard-check" style="color: white; font-size: 2rem;"></i>
                </div>
                <h3 style="color: white; font-size: 1.4rem; margin-bottom: 15px; font-weight: 700;">Internal Audit Support</h3>
                <p style="color: rgba(255,255,255,0.85); font-size: 1.05rem; line-height: 1.8; margin: 0;">Conduct or support internal audits to verify system effectiveness and identify issues before the certification audit.</p>
            </div>

            <div style="background: rgba(255,255,255,0.08); backdrop-filter: blur(10px); padding: 35px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.1);">
                <div style="background: linear-gradient(135deg, #a855f7, #7c3aed); width: 65px; height: 65px; border-radius: 15px; display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
                    <i class="fas fa-hands-helping" style="color: white; font-size: 2rem;"></i>
                </div>
                <h3 style="color: white; font-size: 1.4rem; margin-bottom: 15px; font-weight: 700;">Certification Audit Prep</h3>
                <p style="color: rgba(255,255,255,0.85); font-size: 1.05rem; line-height: 1.8; margin: 0;">Pre-audit readiness review, certification body selection assistance, and support during the certification audit process.</p>
            </div>

            <div style="background: rgba(255,255,255,0.08); backdrop-filter: blur(10px); padding: 35px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.1);">
                <div style="background: linear-gradient(135deg, #14b8a6, #0d9488); width: 65px; height: 65px; border-radius: 15px; display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
                    <i class="fas fa-sync-alt" style="color: white; font-size: 2rem;"></i>
                </div>
                <h3 style="color: white; font-size: 1.4rem; margin-bottom: 15px; font-weight: 700;">Post-Certification Support</h3>
                <p style="color: rgba(255,255,255,0.85); font-size: 1.05rem; line-height: 1.8; margin: 0;">Ongoing support for continual improvement, surveillance audit preparation, and system evolution as your business grows.</p>
            </div>
        </div>

        <div style="background: rgba(233,69,96,0.15); border: 2px solid rgba(233,69,96,0.3); padding: 40px; border-radius: 20px; text-align: center; backdrop-filter: blur(10px);">
            <div style="color: white; font-size: 3rem; margin-bottom: 20px;">
                <i class="fas fa-award"></i>
            </div>
            <h3 style="color: white; font-size: 2rem; margin-bottom: 15px; font-weight: 800;">100% First-Time Certification Success Rate</h3>
            <p style="color: rgba(255,255,255,0.9); font-size: 1.2rem; line-height: 1.8; margin-bottom: 25px; max-width: 800px; margin-left: auto; margin-right: auto;">With over 25 years of automotive industry experience, our consultants have helped hundreds of UK suppliers achieve IATF 16949 certification on the first attempt. We combine deep technical knowledge with practical, business-focused guidance.</p>
            <div style="display: flex; gap: 20px; justify-content: center; align-items: center; flex-wrap: wrap;">
                <div style="text-align: center;">
                    <div style="color: #ff6b6b; font-size: 2.5rem; font-weight: 800;">25+</div>
                    <div style="color: rgba(255,255,255,0.9); font-size: 1rem;">Years Experience</div>
                </div>
                <div style="color: rgba(255,255,255,0.3); font-size: 2rem;">|</div>
                <div style="text-align: center;">
                    <div style="color: #ff6b6b; font-size: 2.5rem; font-weight: 800;">100%</div>
                    <div style="color: rgba(255,255,255,0.9); font-size: 1rem;">Success Rate</div>
                </div>
                <div style="color: rgba(255,255,255,0.3); font-size: 2rem;">|</div>
                <div style="text-align: center;">
                    <div style="color: #ff6b6b; font-size: 2.5rem; font-weight: 800;">500+</div>
                    <div style="color: rgba(255,255,255,0.9); font-size: 1rem;">Certifications</div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Final CTA Section -->
<section style="background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%); padding: 90px 20px;">
    <div style="max-width: 900px; margin: 0 auto; text-align: center;">
        <div style="background: linear-gradient(135deg, #e94560, #ff6b6b); width: 100px; height: 100px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 30px; box-shadow: 0 15px 40px rgba(233,69,96,0.3);">
            <i class="fas fa-rocket" style="color: white; font-size: 3rem;"></i>
        </div>

        <h2 style="color: #1a1a2e; font-size: 2.8rem; margin-bottom: 25px; font-weight: 800;">Ready for IATF 16949 Certification?</h2>
        <p style="color: #666; font-size: 1.3rem; line-height: 1.8; margin-bottom: 40px; max-width: 700px; margin-left: auto; margin-right: auto;">
            Join hundreds of UK automotive suppliers who have successfully achieved IATF 16949 certification with Qualitation's expert guidance. Let's discuss your certification journey today.
        </p>

        <div style="display: flex; gap: 20px; justify-content: center; flex-wrap: wrap; margin-bottom: 50px;">
            <a href="/contact/" style="display: inline-flex; align-items: center; gap: 12px; background: linear-gradient(135deg, #e94560, #ff6b6b); color: white; padding: 18px 45px; text-decoration: none; border-radius: 50px; font-weight: 700; font-size: 1.2rem; box-shadow: 0 10px 30px rgba(233,69,96,0.3); transition: all 0.3s;" onmouseover="this.style.transform='translateY(-3px)'; this.style.boxShadow='0 15px 40px rgba(233,69,96,0.4)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 10px 30px rgba(233,69,96,0.3)'">
                <i class="fas fa-envelope"></i> Request Free Consultation
            </a>
            <a href="tel:03456006975" style="display: inline-flex; align-items: center; gap: 12px; background: white; border: 3px solid #e94560; color: #e94560; padding: 15px 40px; text-decoration: none; border-radius: 50px; font-weight: 700; font-size: 1.2rem; transition: all 0.3s;" onmouseover="this.style.background='#e94560'; this.style.color='white'" onmouseout="this.style.background='white'; this.style.color='#e94560'">
                <i class="fas fa-phone"></i> 0345 600 6975
            </a>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 30px; max-width: 700px; margin: 0 auto;">
            <div style="padding: 20px;">
                <div style="color: #e94560; font-size: 1.5rem; margin-bottom: 10px;">
                    <i class="fas fa-check-circle"></i>
                </div>
                <div style="color: #1a1a2e; font-weight: 600; font-size: 1.05rem; margin-bottom: 5px;">Free Initial Consultation</div>
                <div style="color: #666; font-size: 0.95rem;">No obligation discussion</div>
            </div>

            <div style="padding: 20px;">
                <div style="color: #667eea; font-size: 1.5rem; margin-bottom: 10px;">
                    <i class="fas fa-file-invoice"></i>
                </div>
                <div style="color: #1a1a2e; font-weight: 600; font-size: 1.05rem; margin-bottom: 5px;">Transparent Pricing</div>
                <div style="color: #666; font-size: 0.95rem;">Fixed-fee quotations</div>
            </div>

            <div style="padding: 20px;">
                <div style="color: #11998e; font-size: 1.5rem; margin-bottom: 10px;">
                    <i class="fas fa-handshake"></i>
                </div>
                <div style="color: #1a1a2e; font-weight: 600; font-size: 1.05rem; margin-bottom: 5px;">Proven Track Record</div>
                <div style="color: #666; font-size: 0.95rem;">100% success rate</div>
            </div>
        </div>
    </div>
</section>
'''

            # Update the page body
            iatf_page.body = [{
                'type': 'html',
                'value': {
                    'html': enhanced_html
                }
            }]

            iatf_page.save_revision().publish()

            self.stdout.write(self.style.SUCCESS('✓ IATF 16949 page beautified successfully!'))
            self.stdout.write(self.style.SUCCESS('✓ Enhanced visual design applied'))
            self.stdout.write(self.style.SUCCESS('✓ All content preserved'))
            self.stdout.write(self.style.SUCCESS('✓ Modern animations and hover effects added'))
            self.stdout.write(self.style.SUCCESS('✓ Improved color schemes and gradients'))
            self.stdout.write(self.style.SUCCESS('\nView at: http://localhost:8000/iatf-16949/'))

        except FlexiblePage.DoesNotExist:
            self.stdout.write(self.style.ERROR('✗ IATF 16949 page not found'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ Error: {e}'))
            import traceback
            traceback.print_exc()

        self.stdout.write(self.style.SUCCESS('\n=== Complete ===\n'))
