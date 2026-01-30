"""
Django management command to update ISO 19011 page with new content
"""

from django.core.management.base import BaseCommand
from wagtail.models import Page


class Command(BaseCommand):
    help = 'Update ISO 19011 page with new beautifully illustrated content'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('\n=== Updating ISO 19011 Page ===\n'))

        try:
            # Get the ISO 19011 page
            page = Page.objects.get(slug='iso-19011').specific

            self.stdout.write(f'Found page: {page.title}')

            # New content with beautiful illustrations
            content_html = '''
<style>
    main { padding-top: 0 !important; margin-top: 0 !important; }
</style>
<!-- Hero Section -->
<section style="background: linear-gradient(135deg, #5e35b1 0%, #7e57c2 100%); padding: 80px 40px; margin: 0; position: relative; overflow: hidden;">
    <div style="max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: 1fr 300px; gap: 60px; align-items: center;">
        <div>
            <h1 style="color: white; font-size: 3em; margin: 0 0 20px 0; font-weight: 700; line-height: 1.2;">
                ISO 19011 Certification UK
            </h1>
            <p style="color: white; font-size: 1.3em; margin: 0 0 30px 0; line-height: 1.6; opacity: 0.95;">
                Guidelines for Auditing Management Systems. Transform internal audits into strategic tools for improvement, risk management, and certification readiness.
            </p>

            <!-- Feature Tags -->
            <div style="display: flex; flex-wrap: wrap; gap: 12px; margin-bottom: 30px;">
                <span style="background: rgba(255,255,255,0.25); color: white; padding: 10px 20px; border-radius: 50px; font-weight: 600; backdrop-filter: blur(10px); display: flex; align-items: center; gap: 8px;">
                    <span style="font-size: 1.2em;">📋</span> Best Practice
                </span>
                <span style="background: rgba(255,255,255,0.25); color: white; padding: 10px 20px; border-radius: 50px; font-weight: 600; backdrop-filter: blur(10px); display: flex; align-items: center; gap: 8px;">
                    <span style="font-size: 1.2em;">✓</span> Risk-Based
                </span>
                <span style="background: rgba(255,255,255,0.25); color: white; padding: 10px 20px; border-radius: 50px; font-weight: 600; backdrop-filter: blur(10px); display: flex; align-items: center; gap: 8px;">
                    <span style="font-size: 1.2em;">🔄</span> Integrated Audits
                </span>
            </div>

            <!-- CTA Buttons -->
            <div style="display: flex; gap: 15px; flex-wrap: wrap;">
                <a href="/contact/" style="background: white; color: #5e35b1; padding: 15px 35px; border-radius: 50px; text-decoration: none; font-weight: 700; font-size: 1.1em; display: inline-flex; align-items: center; gap: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.2); transition: transform 0.2s;">
                    <span style="font-size: 1.2em;">🚀</span> Get Started
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
                    <div style="font-size: 5em; margin-bottom: 10px;">📋</div>
                    <div style="font-size: 2em; color: #5e35b1; font-weight: 700;">19011</div>
                </div>
                <!-- Decorative elements -->
                <div style="position: absolute; top: 20px; left: -20px; width: 40px; height: 40px; background: #5e35b1; border-radius: 50%;"></div>
                <div style="position: absolute; bottom: 40px; right: -15px; width: 30px; height: 30px; background: #7e57c2; border-radius: 50%;"></div>
            </div>
        </div>
    </div>
</section>

<div style="max-width: 1200px; margin: 0 auto; padding: 40px 20px;" id="learn-more">

<div style="background: linear-gradient(135deg, #ede7f6 0%, #d1c4e9 100%); padding: 35px; border-radius: 15px; margin: 30px 0; border-left: 5px solid #5e35b1;">
    <p style="font-size: 1.15em; line-height: 1.8; margin: 0; color: #1e3a5f;">
        Effective internal auditing is the backbone of any successful ISO management system. Without structured, competent audits, organisations risk treating standards as paperwork exercises rather than tools for real improvement. <strong>ISO 19011 provides the internationally recognised guidance that ensures audits add value, identify risk, and support continual improvement—not just compliance</strong>.
    </p>
</div>

<p style="font-size: 1.1em; line-height: 1.8; margin: 25px 0;">
    ISO 19011 is the global guideline standard for <strong>auditing management systems</strong>. It sets out best practice for planning, conducting, reporting, and improving internal and supplier audits across all ISO standards, including quality, environmental, health & safety, information security, and more.
</p>

<!-- What is ISO 19011 -->
<div style="background: #f8f9fa; padding: 40px; border-radius: 15px; margin: 40px 0;">
    <h2 style="color: #1e3a5f; margin-top: 0; margin-bottom: 25px; font-size: 2em; display: flex; align-items: center;">
        <span style="background: linear-gradient(135deg, #5e35b1 0%, #7e57c2 100%); color: white; width: 50px; height: 50px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; margin-right: 15px; font-size: 1.2em;">📋</span>
        What is ISO 19011?
    </h2>

    <p style="font-size: 1.05em; line-height: 1.8; margin-bottom: 20px;">
        ISO 19011 is a guidance standard published by the International Organization for Standardization. It provides comprehensive guidance on auditing management systems, rather than specifying requirements for certification.
    </p>

    <p style="font-size: 1.1em; font-weight: 600; color: #1e3a5f; margin: 25px 0 15px 0;">
        In plain English, ISO 19011 explains:
    </p>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-top: 25px;">
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); border-top: 4px solid #5e35b1;">
            <div style="font-size: 2em; margin-bottom: 15px;">📅</div>
            <strong style="color: #1e3a5f; font-size: 1.1em;">Audit Programme</strong>
            <p style="margin: 10px 0 0 0; line-height: 1.6;">How to design and manage an effective audit programme</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); border-top: 4px solid #5e35b1;">
            <div style="font-size: 2em; margin-bottom: 15px;">🎯</div>
            <strong style="color: #1e3a5f; font-size: 1.1em;">Conduct Audits</strong>
            <p style="margin: 10px 0 0 0; line-height: 1.6;">How to conduct audits consistently and professionally</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); border-top: 4px solid #5e35b1;">
            <div style="font-size: 2em; margin-bottom: 15px;">👤</div>
            <strong style="color: #1e3a5f; font-size: 1.1em;">Auditor Competence</strong>
            <p style="margin: 10px 0 0 0; line-height: 1.6;">What competence auditors need</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); border-top: 4px solid #5e35b1;">
            <div style="font-size: 2em; margin-bottom: 15px;">📈</div>
            <strong style="color: #1e3a5f; font-size: 1.1em;">Drive Improvement</strong>
            <p style="margin: 10px 0 0 0; line-height: 1.6;">How audits should drive improvement, not fear or blame</p>
        </div>
    </div>

    <div style="background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%); padding: 25px; border-radius: 12px; margin-top: 30px; border-left: 5px solid #30b566;">
        <p style="margin: 0; font-size: 1.05em; line-height: 1.7;">
            It applies to <strong>internal audits, second-party (supplier) audits, and integrated audits</strong> covering multiple standards.
        </p>
    </div>
</div>

<!-- Why ISO 19011 was created -->
<h2 style="color: #1e3a5f; margin-top: 50px; margin-bottom: 20px; font-size: 2em;">
    Why ISO 19011 was created
</h2>

<div style="background: linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%); padding: 35px; border-radius: 15px; margin: 30px 0; border-left: 5px solid #f44336;">
    <p style="font-size: 1.05em; line-height: 1.8; margin: 0 0 15px 0;">
        Before ISO 19011, organisations often audited each ISO standard differently, leading to inconsistent results, duplicated effort, and low-value audits focused on checklist compliance.
    </p>
    <p style="font-size: 1.1em; font-weight: 600; color: #1e3a5f; margin: 15px 0;">
        ISO 19011 was developed to:
    </p>
    <ul style="margin: 15px 0 0 0; padding-left: 25px; line-height: 1.8;">
        <li style="margin-bottom: 10px;">Standardise good auditing practice</li>
        <li style="margin-bottom: 10px;">Promote risk-based and objective auditing</li>
        <li style="margin-bottom: 10px;">Encourage a professional, evidence-based approach</li>
        <li>Support integrated management systems</li>
    </ul>
</div>

<div style="background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%); padding: 30px; border-radius: 12px; margin: 30px 0; border-left: 5px solid #2196f3;">
    <p style="margin: 0; font-size: 1.05em; line-height: 1.7;">
        The standard shifts auditing from a <strong>box-ticking activity to a strategic management tool</strong>.
    </p>
</div>

<!-- Why ISO 19011 matters for UK organisations -->
<div style="background: #e3f2fd; padding: 40px; border-radius: 15px; margin: 40px 0;">
    <h2 style="color: #1e3a5f; margin-top: 0; margin-bottom: 25px; font-size: 2em; display: flex; align-items: center;">
        <span style="background: linear-gradient(135deg, #2196f3 0%, #64b5f6 100%); color: white; width: 50px; height: 50px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; margin-right: 15px; font-size: 1.2em;">🇬🇧</span>
        Why ISO 19011 matters for UK organisations
    </h2>

    <p style="font-size: 1.05em; line-height: 1.8; margin-bottom: 20px;">
        In the UK, internal audits are a mandatory requirement of almost every certifiable ISO standard, including:
    </p>

    <div style="display: flex; flex-wrap: wrap; gap: 15px; margin: 25px 0;">
        <span style="background: white; color: #1e3a5f; padding: 12px 24px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">ISO 9001 (Quality)</span>
        <span style="background: white; color: #1e3a5f; padding: 12px 24px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">ISO 14001 (Environment)</span>
        <span style="background: white; color: #1e3a5f; padding: 12px 24px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">ISO 45001 (Health & Safety)</span>
        <span style="background: white; color: #1e3a5f; padding: 12px 24px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">ISO 27001 (Information Security)</span>
    </div>

    <div style="background: white; padding: 30px; border-radius: 12px; margin-top: 25px; box-shadow: 0 4px 12px rgba(0,0,0,0.08);">
        <p style="margin: 0 0 15px 0; font-size: 1.1em; line-height: 1.8; color: #1e3a5f;">
            <strong>ISO 19011 provides the accepted framework</strong> for meeting those audit requirements. UKAS-accredited certification bodies expect internal audits to follow ISO 19011 principles—even though the standard itself is not certifiable.
        </p>
        <p style="margin: 0; font-size: 1.05em; line-height: 1.8; color: #1e3a5f;">
            When audits are weak, certification audits expose gaps quickly. ISO 19011 helps ensure organisations are <strong>audit-ready all year round</strong>, not just before an external visit.
        </p>
    </div>
</div>

<!-- Who ISO 19011 is for -->
<h2 style="color: #1e3a5f; margin-top: 50px; margin-bottom: 20px; font-size: 2em;">
    Who ISO 19011 is for
</h2>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 25px; margin: 30px 0;">
    <div style="background: linear-gradient(135deg, #e8eaf6 0%, #c5cae9 100%); padding: 30px; border-radius: 12px; border-left: 5px solid #3f51b5;">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 15px; font-size: 1.3em;">✓ Organisations with ISO certification</h3>
        <p style="margin: 0; line-height: 1.7;">Ensuring audits meet best practice</p>
    </div>
    <div style="background: linear-gradient(135deg, #fce4ec 0%, #f8bbd0 100%); padding: 30px; border-radius: 12px; border-left: 5px solid #e91e63;">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 15px; font-size: 1.3em;">👤 Internal Auditors</h3>
        <p style="margin: 0; line-height: 1.7;">Improving competence and confidence</p>
    </div>
    <div style="background: linear-gradient(135deg, #e0f2f1 0%, #b2dfdb 100%); padding: 30px; border-radius: 12px; border-left: 5px solid #009688;">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 15px; font-size: 1.3em;">📋 Quality, H&S, and Compliance Managers</h3>
        <p style="margin: 0; line-height: 1.7;">Managing audit programmes</p>
    </div>
    <div style="background: linear-gradient(135deg, #fff9c4 0%, #fff59d 100%); padding: 30px; border-radius: 12px; border-left: 5px solid #fbc02d;">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 15px; font-size: 1.3em;">🎓 Consultants and Auditors</h3>
        <p style="margin: 0; line-height: 1.7;">Applying a consistent methodology</p>
    </div>
    <div style="background: linear-gradient(135deg, #f3e5f5 0%, #e1bee7 100%); padding: 30px; border-radius: 12px; border-left: 5px solid #9c27b0;">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 15px; font-size: 1.3em;">🔄 Integrated Management Systems (IMS)</h3>
        <p style="margin: 0; line-height: 1.7;">Organisations with multiple ISO standards</p>
    </div>
</div>

<div style="background: linear-gradient(135deg, #ede7f6 0%, #d1c4e9 100%); padding: 25px; border-radius: 12px; margin: 30px 0; border-left: 5px solid #5e35b1;">
    <p style="margin: 0; font-size: 1.05em; line-height: 1.7;">
        It applies equally to <strong>SMEs and large, multi-site organisations</strong>.
    </p>
</div>

<!-- Key principles -->
<div style="background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%); padding: 45px; border-radius: 15px; margin: 50px 0; color: white;">
    <h2 style="color: white; margin-top: 0; margin-bottom: 30px; font-size: 2em; text-align: center;">
        Key Principles of ISO 19011
    </h2>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 25px;">
        <div style="background: rgba(255,255,255,0.1); padding: 25px; border-radius: 12px; backdrop-filter: blur(10px);">
            <div style="font-size: 2.5em; margin-bottom: 15px;">🤝</div>
            <h3 style="color: white; margin: 0 0 10px 0; font-size: 1.2em;">Integrity</h3>
            <p style="margin: 0; opacity: 0.9; line-height: 1.6;">Auditors act ethically and professionally</p>
        </div>
        <div style="background: rgba(255,255,255,0.1); padding: 25px; border-radius: 12px; backdrop-filter: blur(10px);">
            <div style="font-size: 2.5em; margin-bottom: 15px;">⚖️</div>
            <h3 style="color: white; margin: 0 0 10px 0; font-size: 1.2em;">Fair Presentation</h3>
            <p style="margin: 0; opacity: 0.9; line-height: 1.6;">Findings are accurate, objective, and evidence-based</p>
        </div>
        <div style="background: rgba(255,255,255,0.1); padding: 25px; border-radius: 12px; backdrop-filter: blur(10px);">
            <div style="font-size: 2.5em; margin-bottom: 15px;">🎯</div>
            <h3 style="color: white; margin: 0 0 10px 0; font-size: 1.2em;">Due Professional Care</h3>
            <p style="margin: 0; opacity: 0.9; line-height: 1.6;">Audits are conducted competently and diligently</p>
        </div>
        <div style="background: rgba(255,255,255,0.1); padding: 25px; border-radius: 12px; backdrop-filter: blur(10px);">
            <div style="font-size: 2.5em; margin-bottom: 15px;">🔒</div>
            <h3 style="color: white; margin: 0 0 10px 0; font-size: 1.2em;">Confidentiality</h3>
            <p style="margin: 0; opacity: 0.9; line-height: 1.6;">Information is protected and used responsibly</p>
        </div>
        <div style="background: rgba(255,255,255,0.1); padding: 25px; border-radius: 12px; backdrop-filter: blur(10px);">
            <div style="font-size: 2.5em; margin-bottom: 15px;">🔍</div>
            <h3 style="color: white; margin: 0 0 10px 0; font-size: 1.2em;">Independence</h3>
            <p style="margin: 0; opacity: 0.9; line-height: 1.6;">Auditors remain impartial and unbiased</p>
        </div>
        <div style="background: rgba(255,255,255,0.1); padding: 25px; border-radius: 12px; backdrop-filter: blur(10px);">
            <div style="font-size: 2.5em; margin-bottom: 15px;">📊</div>
            <h3 style="color: white; margin: 0 0 10px 0; font-size: 1.2em;">Evidence-Based Approach</h3>
            <p style="margin: 0; opacity: 0.9; line-height: 1.6;">Conclusions are supported by verifiable information</p>
        </div>
        <div style="background: rgba(255,255,255,0.1); padding: 25px; border-radius: 12px; backdrop-filter: blur(10px);">
            <div style="font-size: 2.5em; margin-bottom: 15px;">⚠️</div>
            <h3 style="color: white; margin: 0 0 10px 0; font-size: 1.2em;">Risk-Based Approach</h3>
            <p style="margin: 0; opacity: 0.9; line-height: 1.6;">Audit focus is aligned to organisational risk and priorities</p>
        </div>
    </div>
</div>

<!-- Benefits section -->
<h2 style="color: #1e3a5f; margin-top: 50px; margin-bottom: 30px; font-size: 2em; text-align: center;">
    Benefits of applying ISO 19011
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
                Consistent, reliable audit outcomes
            </li>
            <li style="margin-bottom: 15px; padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #30b566; font-size: 1.3em;">✓</span>
                Improved identification of risks and weaknesses
            </li>
            <li style="margin-bottom: 15px; padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #30b566; font-size: 1.3em;">✓</span>
                More confident and competent internal auditors
            </li>
            <li style="padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #30b566; font-size: 1.3em;">✓</span>
                Reduced last-minute panic before certification audits
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
                Audits that support business objectives
            </li>
            <li style="margin-bottom: 15px; padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #2196f3; font-size: 1.3em;">✓</span>
                Stronger management oversight and decision-making
            </li>
            <li style="margin-bottom: 15px; padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #2196f3; font-size: 1.3em;">✓</span>
                Better integration across multiple ISO standards
            </li>
            <li style="padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #2196f3; font-size: 1.3em;">✓</span>
                Improved culture of accountability and improvement
            </li>
        </ul>
    </div>

    <!-- Certification & Compliance Benefits -->
    <div style="background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%); padding: 35px; border-radius: 15px; box-shadow: 0 6px 20px rgba(0,0,0,0.1);">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 20px; font-size: 1.5em; display: flex; align-items: center;">
            <span style="font-size: 1.5em; margin-right: 10px;">✓</span> Certification & Compliance
        </h3>
        <ul style="list-style: none; padding: 0; margin: 0;">
            <li style="margin-bottom: 15px; padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #ff9800; font-size: 1.3em;">✓</span>
                Fewer non-conformities during external audits
            </li>
            <li style="margin-bottom: 15px; padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #ff9800; font-size: 1.3em;">✓</span>
                Stronger evidence of continual improvement
            </li>
            <li style="padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #ff9800; font-size: 1.3em;">✓</span>
                Increased credibility with certification bodies
            </li>
        </ul>
    </div>
</div>

<!-- What auditors look for -->
<div style="background: #f8f9fa; padding: 40px; border-radius: 15px; margin: 50px 0;">
    <h2 style="color: #1e3a5f; margin-top: 0; margin-bottom: 25px; font-size: 2em;">
        What auditors look for in ISO 19011-aligned audits
    </h2>

    <p style="font-size: 1.05em; line-height: 1.8; margin-bottom: 25px;">
        Certification auditors typically assess whether your internal audits:
    </p>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-top: 25px;">
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
            <h4 style="color: #1e3a5f; margin-top: 0; margin-bottom: 12px;">⚠️ Risk-Based Planning</h4>
            <p style="margin: 0; line-height: 1.6;">Are planned based on risk, not convenience</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
            <h4 style="color: #1e3a5f; margin-top: 0; margin-bottom: 12px;">🎯 Full Scope</h4>
            <p style="margin: 0; line-height: 1.6;">Cover the full scope of the management system</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
            <h4 style="color: #1e3a5f; margin-top: 0; margin-bottom: 12px;">👤 Competent Auditors</h4>
            <p style="margin: 0; line-height: 1.6;">Are conducted by competent, independent auditors</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
            <h4 style="color: #1e3a5f; margin-top: 0; margin-bottom: 12px;">📊 Meaningful Findings</h4>
            <p style="margin: 0; line-height: 1.6;">Generate meaningful findings and improvement actions</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
            <h4 style="color: #1e3a5f; margin-top: 0; margin-bottom: 12px;">👔 Management Review</h4>
            <p style="margin: 0; line-height: 1.6;">Are reviewed by top management</p>
        </div>
    </div>

    <div style="background: linear-gradient(135deg, #ede7f6 0%, #d1c4e9 100%); padding: 25px; border-radius: 12px; margin-top: 25px; border-left: 5px solid #5e35b1;">
        <p style="margin: 0; font-size: 1.05em; line-height: 1.7;">
            They will often <strong>sample audit reports, programmes, and auditor competence records</strong>.
        </p>
    </div>
</div>

<!-- Real-world examples -->
<h2 style="color: #1e3a5f; margin-top: 50px; margin-bottom: 30px; font-size: 2em;">
    ISO 19011 in practice (real-world examples)
</h2>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 30px; margin: 30px 0;">
    <div style="background: linear-gradient(135deg, #e8eaf6 0%, #c5cae9 100%); padding: 35px; border-radius: 15px; box-shadow: 0 6px 20px rgba(0,0,0,0.1);">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 20px; font-size: 1.4em;">
            🔄 Integrated Management System (IMS)
        </h3>
        <p style="margin: 0; line-height: 1.7; font-size: 1.05em;">
            A UK SME with ISO 9001, ISO 14001, and ISO 45001 uses ISO 19011 to run a single integrated audit programme—saving time while improving audit quality.
        </p>
    </div>

    <div style="background: linear-gradient(135deg, #fce4ec 0%, #f8bbd0 100%); padding: 35px; border-radius: 15px; box-shadow: 0 6px 20px rgba(0,0,0,0.1);">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 20px; font-size: 1.4em;">
            🤝 Supplier Audits
        </h3>
        <p style="margin: 0; line-height: 1.7; font-size: 1.05em;">
            An organisation applies ISO 19011 principles to second-party audits, strengthening supply-chain assurance and reducing risk.
        </p>
    </div>
</div>

<!-- Common mistakes -->
<div style="background: linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%); padding: 40px; border-radius: 15px; margin: 50px 0;">
    <h2 style="color: #1e3a5f; margin-top: 0; margin-bottom: 25px; font-size: 2em;">
        ⚠️ Common mistakes when applying ISO 19011
    </h2>

    <div style="display: grid; gap: 20px;">
        <div style="background: white; padding: 25px; border-radius: 12px; border-left: 5px solid #f44336;">
            <h4 style="color: #1e3a5f; margin: 0 0 10px 0; font-size: 1.2em;">Treating Audits as Policing Exercises</h4>
            <p style="margin: 0; line-height: 1.6;">Audits should support improvement, not create fear.</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; border-left: 5px solid #f44336;">
            <h4 style="color: #1e3a5f; margin: 0 0 10px 0; font-size: 1.2em;">Using Untrained Auditors</h4>
            <p style="margin: 0; line-height: 1.6;">Competence is critical and must be demonstrable.</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; border-left: 5px solid #f44336;">
            <h4 style="color: #1e3a5f; margin: 0 0 10px 0; font-size: 1.2em;">Auditing to Checklists Only</h4>
            <p style="margin: 0; line-height: 1.6;">ISO 19011 promotes process and risk-based auditing.</p>
        </div>
    </div>
</div>

<!-- Integration -->
<div style="background: #f8f9fa; padding: 40px; border-radius: 15px; margin: 50px 0;">
    <h2 style="color: #1e3a5f; margin-top: 0; margin-bottom: 25px; font-size: 2em;">
        ISO 19011 and other ISO standards
    </h2>

    <p style="font-size: 1.05em; line-height: 1.8; margin-bottom: 25px;">
        ISO 19011 underpins auditing requirements across almost all ISO management system standards, including:
    </p>

    <div style="display: flex; flex-wrap: wrap; gap: 15px; margin: 25px 0;">
        <span style="background: white; color: #1e3a5f; padding: 15px 30px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1); font-size: 1.05em;">ISO 9001 – Quality</span>
        <span style="background: white; color: #1e3a5f; padding: 15px 30px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1); font-size: 1.05em;">ISO 14001 – Environmental</span>
        <span style="background: white; color: #1e3a5f; padding: 15px 30px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1); font-size: 1.05em;">ISO 45001 – Occupational Health & Safety</span>
        <span style="background: white; color: #1e3a5f; padding: 15px 30px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1); font-size: 1.05em;">ISO 27001 – Information Security</span>
        <span style="background: white; color: #1e3a5f; padding: 15px 30px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1); font-size: 1.05em;">ISO 22301 – Business Continuity</span>
    </div>

    <div style="background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%); padding: 25px; border-radius: 12px; margin-top: 25px; border-left: 5px solid #30b566;">
        <p style="margin: 0; font-size: 1.05em; line-height: 1.7;">
            It is the <strong>common thread that ensures audits remain consistent, effective, and value-driven</strong>.
        </p>
    </div>
</div>

<!-- Certification -->
<div style="background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%); padding: 40px; border-radius: 15px; margin: 50px 0; border-left: 5px solid #ff9800;">
    <h2 style="color: #1e3a5f; margin-top: 0; margin-bottom: 20px; font-size: 2em;">
        Can ISO 19011 be certified in the UK?
    </h2>

    <p style="margin: 0 0 15px 0; font-size: 1.05em; line-height: 1.8;">
        <strong>No.</strong> ISO 19011 is a guidance standard, not a certifiable one. However, it is widely recognised by UKAS-accredited certification bodies as best practice for internal and supplier auditing.
    </p>

    <p style="margin: 15px 0 0 0; font-size: 1.05em; line-height: 1.8;">
        Organisations often demonstrate compliance with ISO 19011 through:
    </p>

    <ul style="margin: 15px 0; padding-left: 30px; line-height: 1.8;">
        <li style="margin-bottom: 10px;">Internal audit procedures</li>
        <li style="margin-bottom: 10px;">Auditor training records</li>
        <li>Audit programmes and reports</li>
    </ul>
</div>

<!-- Who should NOT use -->
<div style="background: linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%); padding: 40px; border-radius: 15px; margin: 50px 0; border-left: 5px solid #f44336;">
    <h2 style="color: #1e3a5f; margin-top: 0; margin-bottom: 20px; font-size: 2em;">
        Who should NOT use ISO 19011?
    </h2>

    <p style="margin: 0; font-size: 1.05em; line-height: 1.8;">
        Any organisation running an ISO management system should use ISO 19011. The only time it may not apply is where <strong>no formal auditing activity exists</strong>, which would already be a non-conformity under most ISO standards.
    </p>
</div>

<!-- FAQs -->
<div style="background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%); padding: 45px; border-radius: 15px; margin: 50px 0; color: white;">
    <h2 style="color: white; margin-top: 0; margin-bottom: 30px; font-size: 2em; text-align: center;">
        Frequently Asked Questions (FAQs)
    </h2>

    <div style="display: grid; gap: 25px;">
        <div style="background: rgba(255,255,255,0.1); padding: 30px; border-radius: 12px; backdrop-filter: blur(10px);">
            <h4 style="color: white; margin: 0 0 12px 0; font-size: 1.3em;">Is ISO 19011 mandatory in the UK?</h4>
            <p style="margin: 0; opacity: 0.9; line-height: 1.7; font-size: 1.05em;">No, but its principles are expected in internal audits.</p>
        </div>

        <div style="background: rgba(255,255,255,0.1); padding: 30px; border-radius: 12px; backdrop-filter: blur(10px);">
            <h4 style="color: white; margin: 0 0 12px 0; font-size: 1.3em;">Does ISO 19011 replace ISO 9001 audit requirements?</h4>
            <p style="margin: 0; opacity: 0.9; line-height: 1.7; font-size: 1.05em;">No. It supports and explains how to meet them effectively.</p>
        </div>

        <div style="background: rgba(255,255,255,0.1); padding: 30px; border-radius: 12px; backdrop-filter: blur(10px);">
            <h4 style="color: white; margin: 0 0 12px 0; font-size: 1.3em;">Can small businesses apply ISO 19011?</h4>
            <p style="margin: 0; opacity: 0.9; line-height: 1.7; font-size: 1.05em;">Yes. The guidance is scalable and proportionate.</p>
        </div>

        <div style="background: rgba(255,255,255,0.1); padding: 30px; border-radius: 12px; backdrop-filter: blur(10px);">
            <h4 style="color: white; margin: 0 0 12px 0; font-size: 1.3em;">Does ISO 19011 apply to supplier audits?</h4>
            <p style="margin: 0; opacity: 0.9; line-height: 1.7; font-size: 1.05em;">Yes. It covers second-party audits as well.</p>
        </div>
    </div>
</div>

<!-- Call to action -->
<div style="background: linear-gradient(135deg, #5e35b1 0%, #7e57c2 100%); padding: 50px; border-radius: 15px; margin: 50px 0; text-align: center; color: white;">
    <h2 style="color: white; margin: 0 0 20px 0; font-size: 2.2em;">
        Ready to transform your internal audits?
    </h2>
    <p style="font-size: 1.2em; line-height: 1.8; margin: 0 0 30px 0; opacity: 0.95;">
        Qualitation has been training auditors and supporting ISO management systems for over 25 years with a 100% first-time certification success rate.
    </p>
    <div style="display: flex; gap: 20px; justify-content: center; flex-wrap: wrap;">
        <a href="/contact/" style="background: white; color: #5e35b1; padding: 15px 40px; border-radius: 50px; text-decoration: none; font-weight: 700; font-size: 1.1em; display: inline-block; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
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

            self.stdout.write(self.style.SUCCESS(f'✓ Updated ISO 19011 page'))
            self.stdout.write(self.style.SUCCESS(f'✓ URL: /{page.get_url_parts()[2]}'))
            self.stdout.write(self.style.SUCCESS('✓ Published successfully'))

        except Page.DoesNotExist:
            self.stdout.write(self.style.ERROR('✗ ISO 19011 page not found'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ Error: {e}'))
            import traceback
            traceback.print_exc()

        self.stdout.write(self.style.SUCCESS('\n=== Complete ===\n'))
