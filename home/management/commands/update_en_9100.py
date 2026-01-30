"""
Django management command to update EN 9100 page with new content
"""

from django.core.management.base import BaseCommand
from wagtail.models import Page


class Command(BaseCommand):
    help = 'Update EN 9100 page with new beautifully illustrated content'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('\n=== Updating EN 9100 Page ===\n'))

        try:
            # Get the EN 9100 page
            page = Page.objects.get(slug='en-9100').specific

            self.stdout.write(f'Found page: {page.title}')

            # New content with beautiful illustrations
            content_html = '''
<style>
    main { padding-top: 0 !important; margin-top: 0 !important; }
</style>
<!-- Hero Section -->
<section style="background: linear-gradient(135deg, #1565c0 0%, #1976d2 100%); padding: 80px 40px; margin: 0; position: relative; overflow: hidden;">
    <div style="max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: 1fr 300px; gap: 60px; align-items: center;">
        <div>
            <h1 style="color: white; font-size: 3em; margin: 0 0 20px 0; font-weight: 700; line-height: 1.2;">
                EN 9100 Certification UK
            </h1>
            <p style="color: white; font-size: 1.3em; margin: 0 0 30px 0; line-height: 1.6; opacity: 0.95;">
                Aerospace Quality Management System. Deliver safety-critical products with the precision, control, and accountability the aerospace industry demands.
            </p>

            <!-- Feature Tags -->
            <div style="display: flex; flex-wrap: wrap; gap: 12px; margin-bottom: 30px;">
                <span style="background: rgba(255,255,255,0.25); color: white; padding: 10px 20px; border-radius: 50px; font-weight: 600; backdrop-filter: blur(10px); display: flex; align-items: center; gap: 8px;">
                    <span style="font-size: 1.2em;">✈️</span> Aerospace Grade
                </span>
                <span style="background: rgba(255,255,255,0.25); color: white; padding: 10px 20px; border-radius: 50px; font-weight: 600; backdrop-filter: blur(10px); display: flex; align-items: center; gap: 8px;">
                    <span style="font-size: 1.2em;">🛡️</span> Safety Critical
                </span>
                <span style="background: rgba(255,255,255,0.25); color: white; padding: 10px 20px; border-radius: 50px; font-weight: 600; backdrop-filter: blur(10px); display: flex; align-items: center; gap: 8px;">
                    <span style="font-size: 1.2em;">🌍</span> Global Standard
                </span>
            </div>

            <!-- CTA Buttons -->
            <div style="display: flex; gap: 15px; flex-wrap: wrap;">
                <a href="/contact/" style="background: white; color: #1565c0; padding: 15px 35px; border-radius: 50px; text-decoration: none; font-weight: 700; font-size: 1.1em; display: inline-flex; align-items: center; gap: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.2); transition: transform 0.2s;">
                    <span style="font-size: 1.2em;">🚀</span> Get Certified
                </a>
                <a href="#learn-more" style="background: transparent; color: white; padding: 15px 35px; border-radius: 50px; text-decoration: none; font-weight: 700; font-size: 1.1em; display: inline-flex; align-items: center; border: 2px solid white; transition: all 0.2s;">
                    Learn More
                </a>
            </div>
        </div>

        <!-- Hero Icon -->
        <div style="display: flex; justify-content: center; align-items: center;">
            <div style="background: white; width: 250px; height: 250px; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 10px 40px rgba(0,0,0,0.2); position: relative;">
                <div style="text-align: center;">
                    <div style="font-size: 5em; margin-bottom: 10px;">✈️</div>
                    <div style="font-size: 2em; color: #1565c0; font-weight: 700;">9100</div>
                </div>
                <!-- Decorative elements -->
                <div style="position: absolute; top: 20px; left: -20px; width: 40px; height: 40px; background: #1565c0; border-radius: 50%;"></div>
                <div style="position: absolute; bottom: 40px; right: -15px; width: 30px; height: 30px; background: #1976d2; border-radius: 50%;"></div>
            </div>
        </div>
    </div>
</section>

<div style="max-width: 1200px; margin: 0 auto; padding: 40px 20px;" id="learn-more">

<div style="background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%); padding: 35px; border-radius: 15px; margin: 30px 0; border-left: 5px solid #1565c0;">
    <p style="font-size: 1.15em; line-height: 1.8; margin: 0; color: #1e3a5f;">
        For organisations operating in the aerospace and defence supply chain, quality is not just about customer satisfaction—<strong>it is about safety, airworthiness, and trust</strong>. A single failure can have catastrophic consequences. EN 9100 provides the internationally recognised framework that ensures aerospace organisations operate with the highest levels of control, consistency, and accountability.
    </p>
</div>

<p style="font-size: 1.1em; line-height: 1.8; margin: 25px 0;">
    EN 9100 is the European adoption of the aerospace quality management standard commonly known as <strong>AS/EN/JISQ 9100</strong>. It builds on ISO 9001 but adds stringent aerospace-specific requirements covering risk, configuration control, product safety, and counterfeit part prevention.
</p>

<!-- What is EN 9100 -->
<div style="background: #f8f9fa; padding: 40px; border-radius: 15px; margin: 40px 0;">
    <h2 style="color: #1e3a5f; margin-top: 0; margin-bottom: 25px; font-size: 2em; display: flex; align-items: center;">
        <span style="background: linear-gradient(135deg, #1565c0 0%, #1976d2 100%); color: white; width: 50px; height: 50px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; margin-right: 15px; font-size: 1.2em;">✈️</span>
        What is EN 9100?
    </h2>

    <p style="font-size: 1.05em; line-height: 1.8; margin-bottom: 20px;">
        EN 9100 is a quality management system (QMS) standard developed specifically for the aerospace, aviation, and defence (AAD) sector. It is based on ISO 9001 but includes additional requirements that address the unique risks and regulatory expectations of the aerospace industry.
    </p>

    <div style="background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%); padding: 25px; border-radius: 12px; margin: 25px 0; border-left: 5px solid #ff9800;">
        <p style="margin: 0; font-size: 1.05em; line-height: 1.7;">
            The standard is maintained by the <strong>International Aerospace Quality Group (IAQG)</strong> to ensure global consistency across Europe (EN), North America (AS), and Asia (JISQ).
        </p>
    </div>

    <p style="font-size: 1.1em; font-weight: 600; color: #1e3a5f; margin: 25px 0 15px 0;">
        In practical terms, EN 9100 helps organisations:
    </p>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-top: 25px;">
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); border-top: 4px solid #1565c0;">
            <div style="font-size: 2em; margin-bottom: 15px;">🛡️</div>
            <strong style="color: #1e3a5f; font-size: 1.1em;">Deliver Safe Products</strong>
            <p style="margin: 10px 0 0 0; line-height: 1.6;">Deliver safe, conforming aerospace products</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); border-top: 4px solid #1565c0;">
            <div style="font-size: 2em; margin-bottom: 15px;">⚙️</div>
            <strong style="color: #1e3a5f; font-size: 1.1em;">Control Processes</strong>
            <p style="margin: 10px 0 0 0; line-height: 1.6;">Control complex, high-risk processes</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); border-top: 4px solid #1565c0;">
            <div style="font-size: 2em; margin-bottom: 15px;">✓</div>
            <strong style="color: #1e3a5f; font-size: 1.1em;">Meet Expectations</strong>
            <p style="margin: 10px 0 0 0; line-height: 1.6;">Meet OEM and regulatory expectations</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); border-top: 4px solid #1565c0;">
            <div style="font-size: 2em; margin-bottom: 15px;">🌍</div>
            <strong style="color: #1e3a5f; font-size: 1.1em;">Access Supply Chain</strong>
            <p style="margin: 10px 0 0 0; line-height: 1.6;">Gain access to the global aerospace supply chain</p>
        </div>
    </div>
</div>

<!-- Why EN 9100 was created -->
<h2 style="color: #1e3a5f; margin-top: 50px; margin-bottom: 20px; font-size: 2em;">
    Why EN 9100 was created
</h2>

<div style="background: linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%); padding: 35px; border-radius: 15px; margin: 30px 0; border-left: 5px solid #f44336;">
    <p style="font-size: 1.05em; line-height: 1.8; margin: 0 0 15px 0;">
        Aerospace organisations historically relied on customer-specific quality requirements, resulting in duplication, inconsistency, and high audit burdens across the supply chain.
    </p>
    <p style="font-size: 1.1em; font-weight: 600; color: #1e3a5f; margin: 15px 0;">
        EN 9100 was created to:
    </p>
    <ul style="margin: 15px 0 0 0; padding-left: 25px; line-height: 1.8;">
        <li style="margin-bottom: 10px;">Harmonise aerospace quality requirements globally</li>
        <li style="margin-bottom: 10px;">Strengthen product safety and airworthiness controls</li>
        <li style="margin-bottom: 10px;">Improve supplier performance and traceability</li>
        <li>Reduce risk across complex, multi-tier supply chains</li>
    </ul>
</div>

<div style="background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%); padding: 30px; border-radius: 12px; margin: 30px 0; border-left: 5px solid #30b566;">
    <p style="margin: 0; font-size: 1.05em; line-height: 1.7;">
        The result is a <strong>single, trusted quality standard</strong> recognised by aerospace OEMs, Tier 1 suppliers, and regulators worldwide.
    </p>
</div>

<!-- Why EN 9100 matters for UK organisations -->
<div style="background: #e3f2fd; padding: 40px; border-radius: 15px; margin: 40px 0;">
    <h2 style="color: #1e3a5f; margin-top: 0; margin-bottom: 25px; font-size: 2em; display: flex; align-items: center;">
        <span style="background: linear-gradient(135deg, #2196f3 0%, #64b5f6 100%); color: white; width: 50px; height: 50px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; margin-right: 15px; font-size: 1.2em;">🇬🇧</span>
        Why EN 9100 matters for UK organisations
    </h2>

    <p style="font-size: 1.05em; line-height: 1.8; margin-bottom: 20px;">
        For UK aerospace organisations, <strong>EN 9100 is often non-negotiable</strong>. Without it, many businesses are excluded from bidding for work with:
    </p>

    <div style="display: flex; flex-wrap: wrap; gap: 15px; margin: 25px 0;">
        <span style="background: white; color: #1e3a5f; padding: 12px 24px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">Aircraft and engine manufacturers</span>
        <span style="background: white; color: #1e3a5f; padding: 12px 24px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">Defence primes</span>
        <span style="background: white; color: #1e3a5f; padding: 12px 24px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">Tier 1 and Tier 2 aerospace suppliers</span>
    </div>

    <div style="background: white; padding: 30px; border-radius: 12px; margin-top: 25px; box-shadow: 0 4px 12px rgba(0,0,0,0.08);">
        <p style="margin: 0 0 15px 0; font-size: 1.1em; line-height: 1.8; color: #1e3a5f;">
            <strong>EN 9100 certification demonstrates</strong> that your organisation meets the highest international quality and safety expectations, making it essential for export, long-term contracts, and supply-chain approval.
        </p>
        <p style="margin: 0; font-size: 1.05em; line-height: 1.8; color: #1e3a5f;">
            It also supports compliance with regulatory bodies such as the <strong>Civil Aviation Authority (CAA)</strong> and international aviation authorities.
        </p>
    </div>
</div>

<!-- Who EN 9100 is for -->
<h2 style="color: #1e3a5f; margin-top: 50px; margin-bottom: 20px; font-size: 2em;">
    Who EN 9100 is for
</h2>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 25px; margin: 30px 0;">
    <div style="background: linear-gradient(135deg, #e8eaf6 0%, #c5cae9 100%); padding: 30px; border-radius: 12px; border-left: 5px solid #3f51b5;">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 15px; font-size: 1.3em;">🏭 Aerospace Manufacturing</h3>
        <p style="margin: 0; line-height: 1.7;">Parts, assemblies, and components</p>
    </div>
    <div style="background: linear-gradient(135deg, #fce4ec 0%, #f8bbd0 100%); padding: 30px; border-radius: 12px; border-left: 5px solid #e91e63;">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 15px; font-size: 1.3em;">⚙️ Precision Engineering & Machining</h3>
        <p style="margin: 0; line-height: 1.7;">High-precision manufacturing</p>
    </div>
    <div style="background: linear-gradient(135deg, #e0f2f1 0%, #b2dfdb 100%); padding: 30px; border-radius: 12px; border-left: 5px solid #009688;">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 15px; font-size: 1.3em;">🔧 Maintenance, Repair & Overhaul (MRO)</h3>
        <p style="margin: 0; line-height: 1.7;">Service and maintenance operations</p>
    </div>
    <div style="background: linear-gradient(135deg, #fff9c4 0%, #fff59d 100%); padding: 30px; border-radius: 12px; border-left: 5px solid #fbc02d;">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 15px; font-size: 1.3em;">📐 Design & Engineering Services</h3>
        <p style="margin: 0; line-height: 1.7;">Engineering and design capabilities</p>
    </div>
    <div style="background: linear-gradient(135deg, #f3e5f5 0%, #e1bee7 100%); padding: 30px; border-radius: 12px; border-left: 5px solid #9c27b0;">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 15px; font-size: 1.3em;">📦 Stockists & Distributors</h3>
        <p style="margin: 0; line-height: 1.7;">Including traceability and counterfeit prevention</p>
    </div>
</div>

<div style="background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%); padding: 25px; border-radius: 12px; margin: 30px 0; border-left: 5px solid #1565c0;">
    <p style="margin: 0; font-size: 1.05em; line-height: 1.7;">
        It is relevant to <strong>OEMs, Tier 1, Tier 2, and Tier 3 suppliers</strong> across civil, defence, and space sectors.
    </p>
</div>

<!-- Key principles -->
<div style="background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%); padding: 45px; border-radius: 15px; margin: 50px 0; color: white;">
    <h2 style="color: white; margin-top: 0; margin-bottom: 30px; font-size: 2em; text-align: center;">
        Key Principles of EN 9100
    </h2>

    <p style="text-align: center; margin: 0 0 30px 0; opacity: 0.95; font-size: 1.1em;">
        EN 9100 includes all ISO 9001 requirements plus critical aerospace-specific controls:
    </p>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 25px;">
        <div style="background: rgba(255,255,255,0.1); padding: 25px; border-radius: 12px; backdrop-filter: blur(10px);">
            <div style="font-size: 2.5em; margin-bottom: 15px;">🛡️</div>
            <h3 style="color: white; margin: 0 0 10px 0; font-size: 1.2em;">Product Safety</h3>
            <p style="margin: 0; opacity: 0.9; line-height: 1.6;">Formal identification and management of safety-critical risks</p>
        </div>
        <div style="background: rgba(255,255,255,0.1); padding: 25px; border-radius: 12px; backdrop-filter: blur(10px);">
            <div style="font-size: 2.5em; margin-bottom: 15px;">⚠️</div>
            <h3 style="color: white; margin: 0 0 10px 0; font-size: 1.2em;">Risk Management</h3>
            <p style="margin: 0; opacity: 0.9; line-height: 1.6;">Proactive identification and mitigation of operational and supply-chain risks</p>
        </div>
        <div style="background: rgba(255,255,255,0.1); padding: 25px; border-radius: 12px; backdrop-filter: blur(10px);">
            <div style="font-size: 2.5em; margin-bottom: 15px;">📋</div>
            <h3 style="color: white; margin: 0 0 10px 0; font-size: 1.2em;">Configuration Management</h3>
            <p style="margin: 0; opacity: 0.9; line-height: 1.6;">Strict control of design, changes, and revisions</p>
        </div>
        <div style="background: rgba(255,255,255,0.1); padding: 25px; border-radius: 12px; backdrop-filter: blur(10px);">
            <div style="font-size: 2.5em; margin-bottom: 15px;">🚫</div>
            <h3 style="color: white; margin: 0 0 10px 0; font-size: 1.2em;">Counterfeit Part Prevention</h3>
            <p style="margin: 0; opacity: 0.9; line-height: 1.6;">Controls to prevent counterfeit or suspect parts entering the supply chain</p>
        </div>
        <div style="background: rgba(255,255,255,0.1); padding: 25px; border-radius: 12px; backdrop-filter: blur(10px);">
            <div style="font-size: 2.5em; margin-bottom: 15px;">🔍</div>
            <h3 style="color: white; margin: 0 0 10px 0; font-size: 1.2em;">Traceability</h3>
            <p style="margin: 0; opacity: 0.9; line-height: 1.6;">Full traceability of materials, processes, and approvals</p>
        </div>
        <div style="background: rgba(255,255,255,0.1); padding: 25px; border-radius: 12px; backdrop-filter: blur(10px);">
            <div style="font-size: 2.5em; margin-bottom: 15px;">👤</div>
            <h3 style="color: white; margin: 0 0 10px 0; font-size: 1.2em;">Human Factors Awareness</h3>
            <p style="margin: 0; opacity: 0.9; line-height: 1.6;">Managing fatigue, competence, and human error</p>
        </div>
        <div style="background: rgba(255,255,255,0.1); padding: 25px; border-radius: 12px; backdrop-filter: blur(10px);">
            <div style="font-size: 2.5em; margin-bottom: 15px;">🤝</div>
            <h3 style="color: white; margin: 0 0 10px 0; font-size: 1.2em;">Supplier Control</h3>
            <p style="margin: 0; opacity: 0.9; line-height: 1.6;">Robust approval, monitoring, and performance management</p>
        </div>
    </div>
</div>

<!-- Benefits section -->
<h2 style="color: #1e3a5f; margin-top: 50px; margin-bottom: 30px; font-size: 2em; text-align: center;">
    Benefits of EN 9100
</h2>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 30px; margin: 40px 0;">
    <!-- Internal Benefits -->
    <div style="background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%); padding: 35px; border-radius: 15px; box-shadow: 0 6px 20px rgba(0,0,0,0.1);">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 20px; font-size: 1.5em; display: flex; align-items: center;">
            <span style="font-size: 1.5em; margin-right: 10px;">🔧</span> Internal Benefits
        </h3>
        <ul style="list-style: none; padding: 0; margin: 0;">
            <li style="margin-bottom: 15px; padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #30b566; font-size: 1.3em;">✓</span>
                Improved process control and consistency
            </li>
            <li style="margin-bottom: 15px; padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #30b566; font-size: 1.3em;">✓</span>
                Reduced rework, scrap, and non-conformities
            </li>
            <li style="margin-bottom: 15px; padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #30b566; font-size: 1.3em;">✓</span>
                Clear accountability and responsibilities
            </li>
            <li style="padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #30b566; font-size: 1.3em;">✓</span>
                Stronger safety and quality culture
            </li>
        </ul>
    </div>

    <!-- Strategic Benefits -->
    <div style="background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%); padding: 35px; border-radius: 15px; box-shadow: 0 6px 20px rgba(0,0,0,0.1);">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 20px; font-size: 1.5em; display: flex; align-items: center;">
            <span style="font-size: 1.5em; margin-right: 10px;">🎯</span> Strategic Benefits
        </h3>
        <ul style="list-style: none; padding: 0; margin: 0;">
            <li style="margin-bottom: 15px; padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #2196f3; font-size: 1.3em;">✓</span>
                Access to global aerospace supply chains
            </li>
            <li style="margin-bottom: 15px; padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #2196f3; font-size: 1.3em;">✓</span>
                Preferred supplier status with OEMs
            </li>
            <li style="margin-bottom: 15px; padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #2196f3; font-size: 1.3em;">✓</span>
                Increased customer confidence and trust
            </li>
            <li style="padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #2196f3; font-size: 1.3em;">✓</span>
                Long-term contract opportunities
            </li>
        </ul>
    </div>

    <!-- Compliance & Risk Benefits -->
    <div style="background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%); padding: 35px; border-radius: 15px; box-shadow: 0 6px 20px rgba(0,0,0,0.1);">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 20px; font-size: 1.5em; display: flex; align-items: center;">
            <span style="font-size: 1.5em; margin-right: 10px;">⚖️</span> Compliance & Risk
        </h3>
        <ul style="list-style: none; padding: 0; margin: 0;">
            <li style="margin-bottom: 15px; padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #ff9800; font-size: 1.3em;">✓</span>
                Alignment with aviation regulatory expectations
            </li>
            <li style="margin-bottom: 15px; padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #ff9800; font-size: 1.3em;">✓</span>
                Reduced operational and reputational risk
            </li>
            <li style="padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #ff9800; font-size: 1.3em;">✓</span>
                Stronger defence against product liability issues
            </li>
        </ul>
    </div>
</div>

<!-- What auditors look for -->
<div style="background: #f8f9fa; padding: 40px; border-radius: 15px; margin: 50px 0;">
    <h2 style="color: #1e3a5f; margin-top: 0; margin-bottom: 25px; font-size: 2em;">
        What EN 9100 auditors actually look for
    </h2>

    <div style="background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%); padding: 25px; border-radius: 12px; margin-bottom: 25px; border-left: 5px solid #ff9800;">
        <p style="margin: 0; font-size: 1.05em; line-height: 1.7;">
            <strong>A UKAS-accredited aerospace auditor will look far beyond basic ISO 9001 compliance.</strong>
        </p>
    </div>

    <p style="font-size: 1.05em; line-height: 1.8; margin-bottom: 25px;">
        They will assess:
    </p>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-top: 25px;">
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
            <h4 style="color: #1e3a5f; margin-top: 0; margin-bottom: 12px;">⚠️ Risk & Opportunity Management</h4>
            <p style="margin: 0; line-height: 1.6;">Evidence of proactive risk control</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
            <h4 style="color: #1e3a5f; margin-top: 0; margin-bottom: 12px;">🛡️ Product Safety Controls</h4>
            <p style="margin: 0; line-height: 1.6;">Identification and escalation of safety risks</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
            <h4 style="color: #1e3a5f; margin-top: 0; margin-bottom: 12px;">📋 Configuration & Change Control</h4>
            <p style="margin: 0; line-height: 1.6;">Controlled and traceable changes</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
            <h4 style="color: #1e3a5f; margin-top: 0; margin-bottom: 12px;">🤝 Supplier Management</h4>
            <p style="margin: 0; line-height: 1.6;">Approval, monitoring, and performance data</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
            <h4 style="color: #1e3a5f; margin-top: 0; margin-bottom: 12px;">⚙️ Operational Discipline</h4>
            <p style="margin: 0; line-height: 1.6;">Adherence to procedures on the shop floor</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
            <h4 style="color: #1e3a5f; margin-top: 0; margin-bottom: 12px;">📊 Evidence of Use</h4>
            <p style="margin: 0; line-height: 1.6;">Records proving the system works in practice</p>
        </div>
    </div>

    <div style="background: linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%); padding: 25px; border-radius: 12px; margin-top: 25px; border-left: 5px solid #f44336;">
        <p style="margin: 0; font-size: 1.05em; line-height: 1.7;">
            <strong>Audits are typically more intensive and longer</strong> than ISO 9001 audits.
        </p>
    </div>
</div>

<!-- Real-world examples -->
<h2 style="color: #1e3a5f; margin-top: 50px; margin-bottom: 30px; font-size: 2em;">
    EN 9100 in practice (real-world examples)
</h2>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 30px; margin: 30px 0;">
    <div style="background: linear-gradient(135deg, #e8eaf6 0%, #c5cae9 100%); padding: 35px; border-radius: 15px; box-shadow: 0 6px 20px rgba(0,0,0,0.1);">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 20px; font-size: 1.4em;">
            ⚙️ Precision Engineering Company
        </h3>
        <p style="margin: 0; line-height: 1.7; font-size: 1.05em;">
            A UK machining firm achieves EN 9100 to become a Tier 2 supplier to an aircraft engine manufacturer. The standard strengthens traceability, inspection control, and supplier management—unlocking new long-term contracts.
        </p>
    </div>

    <div style="background: linear-gradient(135deg, #fce4ec 0%, #f8bbd0 100%); padding: 35px; border-radius: 15px; box-shadow: 0 6px 20px rgba(0,0,0,0.1);">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 20px; font-size: 1.4em;">
            🔧 Aerospace MRO Organisation
        </h3>
        <p style="margin: 0; line-height: 1.7; font-size: 1.05em;">
            An MRO provider uses EN 9100 to demonstrate compliance with strict safety, documentation, and regulatory requirements—supporting approvals from major aerospace clients.
        </p>
    </div>
</div>

<!-- Common mistakes -->
<div style="background: linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%); padding: 40px; border-radius: 15px; margin: 50px 0;">
    <h2 style="color: #1e3a5f; margin-top: 0; margin-bottom: 25px; font-size: 2em;">
        ⚠️ Common mistakes when implementing EN 9100
    </h2>

    <div style="display: grid; gap: 20px;">
        <div style="background: white; padding: 25px; border-radius: 12px; border-left: 5px solid #f44336;">
            <h4 style="color: #1e3a5f; margin: 0 0 10px 0; font-size: 1.2em;">Assuming ISO 9001 Is Enough</h4>
            <p style="margin: 0; line-height: 1.6;">EN 9100 has significantly more depth and rigour.</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; border-left: 5px solid #f44336;">
            <h4 style="color: #1e3a5f; margin: 0 0 10px 0; font-size: 1.2em;">Underestimating Cultural Change</h4>
            <p style="margin: 0; line-height: 1.6;">Aerospace quality requires discipline at every level.</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; border-left: 5px solid #f44336;">
            <h4 style="color: #1e3a5f; margin: 0 0 10px 0; font-size: 1.2em;">Weak Supplier Control</h4>
            <p style="margin: 0; line-height: 1.6;">Supply-chain failures are a major audit focus.</p>
        </div>
    </div>
</div>

<!-- Certification process -->
<div style="background: #f8f9fa; padding: 40px; border-radius: 15px; margin: 50px 0;">
    <h2 style="color: #1e3a5f; margin-top: 0; margin-bottom: 30px; font-size: 2em; text-align: center;">
        EN 9100 certification process
    </h2>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 25px;">
        <div style="background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); text-align: center;">
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px; font-size: 1.8em; font-weight: bold;">1</div>
            <h4 style="color: #1e3a5f; margin: 0 0 12px 0; font-size: 1.2em;">Stage 1: Readiness & Documentation Review</h4>
            <p style="margin: 0; line-height: 1.6;">The auditor checks that your QMS meets EN 9100 requirements</p>
        </div>
        <div style="background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); text-align: center;">
            <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); color: white; width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px; font-size: 1.8em; font-weight: bold;">2</div>
            <h4 style="color: #1e3a5f; margin: 0 0 12px 0; font-size: 1.2em;">Stage 2: Certification Audit</h4>
            <p style="margin: 0; line-height: 1.6;">A detailed on-site audit evaluates implementation, effectiveness, and compliance</p>
        </div>
        <div style="background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); text-align: center;">
            <div style="background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%); color: white; width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px; font-size: 1.8em; font-weight: bold;">3</div>
            <h4 style="color: #1e3a5f; margin: 0 0 12px 0; font-size: 1.2em;">Surveillance Audits</h4>
            <p style="margin: 0; line-height: 1.6;">Annual audits confirm ongoing conformity and improvement</p>
        </div>
        <div style="background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); text-align: center;">
            <div style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); color: white; width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px; font-size: 1.8em; font-weight: bold;">4</div>
            <h4 style="color: #1e3a5f; margin: 0 0 12px 0; font-size: 1.2em;">Recertification</h4>
            <p style="margin: 0; line-height: 1.6;">A full reassessment every three years renews certification</p>
        </div>
    </div>
</div>

<!-- Duration and cost -->
<h2 style="color: #1e3a5f; margin-top: 50px; margin-bottom: 20px; font-size: 2em;">
    How long does EN 9100 certification last?
</h2>

<p style="font-size: 1.05em; line-height: 1.8; margin: 25px 0;">
    EN 9100 certification is valid for <strong>three years</strong>, subject to successful annual surveillance audits. Failure to address major non-conformities can result in suspension or withdrawal—<strong>often with serious contractual consequences</strong>.
</p>

<h2 style="color: #1e3a5f; margin-top: 50px; margin-bottom: 20px; font-size: 2em;">
    How much does EN 9100 cost in the UK?
</h2>

<p style="font-size: 1.05em; line-height: 1.8; margin: 25px 0;">
    Costs depend on:
</p>

<ul style="font-size: 1.05em; line-height: 1.8; margin: 25px 0; padding-left: 30px;">
    <li style="margin-bottom: 10px;">Organisation size and complexity</li>
    <li style="margin-bottom: 10px;">Scope (design, manufacture, MRO, stockist)</li>
    <li>Number of sites and employees</li>
</ul>

<div style="background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%); padding: 35px; border-radius: 15px; margin: 30px 0; border-left: 5px solid #2196f3;">
    <p style="margin: 0 0 15px 0; font-size: 1.1em; font-weight: 600; color: #1e3a5f;">
        Typical costs include:
    </p>
    <ul style="margin: 0; padding-left: 25px; line-height: 1.8;">
        <li style="margin-bottom: 10px;">UKAS-accredited certification audit fees</li>
        <li style="margin-bottom: 10px;">Consultancy and gap analysis (if required)</li>
        <li>Internal resource time and training</li>
    </ul>
</div>

<p style="font-size: 1.05em; line-height: 1.8; margin: 25px 0;">
    While more demanding than ISO 9001, <strong>EN 9100 delivers significant commercial return through access to aerospace markets</strong>.
</p>

<!-- Integration -->
<div style="background: #f8f9fa; padding: 40px; border-radius: 15px; margin: 50px 0;">
    <h2 style="color: #1e3a5f; margin-top: 0; margin-bottom: 25px; font-size: 2em;">
        EN 9100 and integration with other standards
    </h2>

    <p style="font-size: 1.05em; line-height: 1.8; margin-bottom: 25px;">
        EN 9100 follows the <strong>Annex SL High-Level Structure</strong>, allowing integration with:
    </p>

    <div style="display: flex; flex-wrap: wrap; gap: 15px; margin: 25px 0;">
        <span style="background: white; color: #1e3a5f; padding: 15px 30px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1); font-size: 1.05em;">ISO 9001 – Quality</span>
        <span style="background: white; color: #1e3a5f; padding: 15px 30px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1); font-size: 1.05em;">ISO 14001 – Environmental</span>
        <span style="background: white; color: #1e3a5f; padding: 15px 30px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1); font-size: 1.05em;">ISO 45001 – Health & Safety</span>
        <span style="background: white; color: #1e3a5f; padding: 15px 30px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1); font-size: 1.05em;">ISO 27001 – Information Security</span>
    </div>

    <div style="background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%); padding: 25px; border-radius: 12px; margin-top: 25px; border-left: 5px solid #30b566;">
        <p style="margin: 0; font-size: 1.05em; line-height: 1.7;">
            Many aerospace organisations operate a fully <strong>Integrated Management System (IMS)</strong>.
        </p>
    </div>
</div>

<!-- Who should NOT implement -->
<div style="background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%); padding: 40px; border-radius: 15px; margin: 50px 0; border-left: 5px solid #ff9800;">
    <h2 style="color: #1e3a5f; margin-top: 0; margin-bottom: 20px; font-size: 2em;">
        Who should NOT implement EN 9100?
    </h2>

    <p style="margin: 0; font-size: 1.05em; line-height: 1.8;">
        If your organisation has <strong>no involvement in the aerospace or defence supply chain and no customer requirement</strong>, EN 9100 is unlikely to be appropriate. The standard demands significant commitment, discipline, and ongoing oversight.
    </p>
</div>

<!-- FAQs -->
<div style="background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%); padding: 45px; border-radius: 15px; margin: 50px 0; color: white;">
    <h2 style="color: white; margin-top: 0; margin-bottom: 30px; font-size: 2em; text-align: center;">
        Frequently Asked Questions (FAQs)
    </h2>

    <div style="display: grid; gap: 25px;">
        <div style="background: rgba(255,255,255,0.1); padding: 30px; border-radius: 12px; backdrop-filter: blur(10px);">
            <h4 style="color: white; margin: 0 0 12px 0; font-size: 1.3em;">Is EN 9100 mandatory in the UK?</h4>
            <p style="margin: 0; opacity: 0.9; line-height: 1.7; font-size: 1.05em;">No, but it is often a contractual requirement.</p>
        </div>

        <div style="background: rgba(255,255,255,0.1); padding: 30px; border-radius: 12px; backdrop-filter: blur(10px);">
            <h4 style="color: white; margin: 0 0 12px 0; font-size: 1.3em;">Is EN 9100 the same as AS 9100?</h4>
            <p style="margin: 0; opacity: 0.9; line-height: 1.7; font-size: 1.05em;">Yes. They are regional versions of the same global standard.</p>
        </div>

        <div style="background: rgba(255,255,255,0.1); padding: 30px; border-radius: 12px; backdrop-filter: blur(10px);">
            <h4 style="color: white; margin: 0 0 12px 0; font-size: 1.3em;">Can SMEs achieve EN 9100?</h4>
            <p style="margin: 0; opacity: 0.9; line-height: 1.7; font-size: 1.05em;">Yes. Many UK aerospace SMEs are EN 9100 certified.</p>
        </div>

        <div style="background: rgba(255,255,255,0.1); padding: 30px; border-radius: 12px; backdrop-filter: blur(10px);">
            <h4 style="color: white; margin: 0 0 12px 0; font-size: 1.3em;">Is EN 9100 harder than ISO 9001?</h4>
            <p style="margin: 0; opacity: 0.9; line-height: 1.7; font-size: 1.05em;">Yes. It includes additional aerospace-specific requirements and stricter auditing.</p>
        </div>
    </div>
</div>

<!-- Call to action -->
<div style="background: linear-gradient(135deg, #1565c0 0%, #1976d2 100%); padding: 50px; border-radius: 15px; margin: 50px 0; text-align: center; color: white;">
    <h2 style="color: white; margin: 0 0 20px 0; font-size: 2.2em;">
        Ready to enter the aerospace supply chain?
    </h2>
    <p style="font-size: 1.2em; line-height: 1.8; margin: 0 0 30px 0; opacity: 0.95;">
        Qualitation has been helping UK aerospace organisations achieve EN 9100 certification for over 25 years with a 100% first-time success rate.
    </p>
    <div style="display: flex; gap: 20px; justify-content: center; flex-wrap: wrap;">
        <a href="/contact/" style="background: white; color: #1565c0; padding: 15px 40px; border-radius: 50px; text-decoration: none; font-weight: 700; font-size: 1.1em; display: inline-block; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
            Get Started Today
        </a>
        <a href="tel:03456006975" style="background: rgba(255,255,255,0.2); color: white; padding: 15px 40px; border-radius: 50px; text-decoration: none; font-weight: 700; font-size: 1.1em; display: inline-block; border: 2px solid white; backdrop-filter: blur(10px);">
            📞 0345 600 6975
        </a>
    </div>
</div>

</div>
'''

            # Clear existing body content and add new HTML block
            import uuid
            new_body = [
                {
                    'type': 'html',
                    'value': {
                        'html': content_html
                    },
                    'id': str(uuid.uuid4())
                }
            ]

            # Update the page body
            page.body = new_body

            # Clear the intro field
            page.intro = ''

            # Save and publish
            page.save_revision().publish()

            self.stdout.write(self.style.SUCCESS(f'✓ Updated EN 9100 page'))
            self.stdout.write(self.style.SUCCESS(f'✓ URL: /{page.get_url_parts()[2]}'))
            self.stdout.write(self.style.SUCCESS('✓ Published successfully'))

        except Page.DoesNotExist:
            self.stdout.write(self.style.ERROR('✗ EN 9100 page not found'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ Error: {e}'))
            import traceback
            traceback.print_exc()

        self.stdout.write(self.style.SUCCESS('\n=== Complete ===\n'))
