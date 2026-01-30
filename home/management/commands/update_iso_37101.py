"""
Django management command to update ISO 37101 page with new content
"""

from django.core.management.base import BaseCommand
from wagtail.models import Page
from wagtail import blocks
from wagtail.blocks import StreamValue


class Command(BaseCommand):
    help = 'Update ISO 37101 page with new beautifully illustrated content'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('\n=== Updating ISO 37101 Page ===\n'))

        try:
            # Get the ISO 37101 page
            page = Page.objects.get(slug='iso-37101').specific

            self.stdout.write(f'Found page: {page.title}')

            # New content with beautiful illustrations
            content_html = '''
<style>
    main { padding-top: 0 !important; margin-top: 0 !important; }
</style>
<!-- Hero Section -->
<section style="background: linear-gradient(135deg, #30b566 0%, #56d882 100%); padding: 80px 40px; margin: 0; position: relative; overflow: hidden;">
    <div style="max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: 1fr 300px; gap: 60px; align-items: center;">
        <div>
            <h1 style="color: white; font-size: 3em; margin: 0 0 20px 0; font-weight: 700; line-height: 1.2;">
                ISO 37101 Certification UK
            </h1>
            <p style="color: white; font-size: 1.3em; margin: 0 0 30px 0; line-height: 1.6; opacity: 0.95;">
                Sustainable Development Management System. Demonstrate your commitment to environmental, social, and economic responsibility.
            </p>

            <!-- Feature Tags -->
            <div style="display: flex; flex-wrap: wrap; gap: 12px; margin-bottom: 30px;">
                <span style="background: rgba(255,255,255,0.25); color: white; padding: 10px 20px; border-radius: 50px; font-weight: 600; backdrop-filter: blur(10px); display: flex; align-items: center; gap: 8px;">
                    <span style="font-size: 1.2em;">🌍</span> Holistic Sustainability
                </span>
                <span style="background: rgba(255,255,255,0.25); color: white; padding: 10px 20px; border-radius: 50px; font-weight: 600; backdrop-filter: blur(10px); display: flex; align-items: center; gap: 8px;">
                    <span style="font-size: 1.2em;">✓</span> UN SDG Aligned
                </span>
                <span style="background: rgba(255,255,255,0.25); color: white; padding: 10px 20px; border-radius: 50px; font-weight: 600; backdrop-filter: blur(10px); display: flex; align-items: center; gap: 8px;">
                    <span style="font-size: 1.2em;">🇬🇧</span> UK Communities
                </span>
            </div>

            <!-- CTA Buttons -->
            <div style="display: flex; gap: 15px; flex-wrap: wrap;">
                <a href="/contact/" style="background: white; color: #30b566; padding: 15px 35px; border-radius: 50px; text-decoration: none; font-weight: 700; font-size: 1.1em; display: inline-flex; align-items: center; gap: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.2); transition: transform 0.2s;">
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
                    <div style="font-size: 5em; margin-bottom: 10px;">🌍</div>
                    <div style="font-size: 2em; color: #30b566; font-weight: 700;">37101</div>
                </div>
                <!-- Decorative elements -->
                <div style="position: absolute; top: 20px; left: -20px; width: 40px; height: 40px; background: #30b566; border-radius: 50%;"></div>
                <div style="position: absolute; bottom: 40px; right: -15px; width: 30px; height: 30px; background: #56d882; border-radius: 50%;"></div>
            </div>
        </div>
    </div>
</section>

<div style="max-width: 1200px; margin: 0 auto; padding: 40px 20px;" id="learn-more">

<div style="background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%); padding: 35px; border-radius: 15px; margin: 30px 0; border-left: 5px solid #30b566;">
    <p style="font-size: 1.15em; line-height: 1.8; margin: 0; color: #1e3a5f;">
        In a time of climate pressure, social inequality, and increasing scrutiny on how organisations contribute to society, sustainability is no longer a "nice to have." For UK organisations—especially those working with local authorities, infrastructure, housing, or the built environment—demonstrating genuine, structured commitment to sustainable development is fast becoming a strategic necessity. <strong>ISO 37101</strong> provides the internationally recognised framework to do exactly that.
    </p>
</div>

<p style="font-size: 1.1em; line-height: 1.8; margin: 25px 0;">
    ISO 37101 is the global standard for a <strong>Sustainable Development Management System (SDMS)</strong>. It helps organisations contribute meaningfully to sustainable development outcomes while balancing economic performance, social responsibility, and environmental protection. Rather than focusing on vague ESG statements, ISO 37101 turns sustainability into a measurable, managed, and continuously improving business process.
</p>

<!-- What is ISO 37101 -->
<div style="background: #f8f9fa; padding: 40px; border-radius: 15px; margin: 40px 0;">
    <h2 style="color: #1e3a5f; margin-top: 0; margin-bottom: 25px; font-size: 2em; display: flex; align-items: center;">
        <span style="background: linear-gradient(135deg, #30b566 0%, #56d882 100%); color: white; width: 50px; height: 50px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; margin-right: 15px; font-size: 1.2em;">🌍</span>
        What is ISO 37101?
    </h2>

    <p style="font-size: 1.05em; line-height: 1.8; margin-bottom: 20px;">
        ISO 37101 is a voluntary international standard published by the International Organization for Standardization. It sets out the requirements for establishing, implementing, maintaining, and continually improving a management system that supports sustainable development in communities.
    </p>

    <p style="font-size: 1.1em; font-weight: 600; color: #1e3a5f; margin: 25px 0 15px 0;">
        In practical terms, ISO 37101 helps organisations:
    </p>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-top: 25px;">
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); border-top: 4px solid #30b566;">
            <div style="font-size: 2em; margin-bottom: 15px;">🎯</div>
            <strong style="color: #1e3a5f; font-size: 1.1em;">Understand Impact</strong>
            <p style="margin: 10px 0 0 0; line-height: 1.6;">Understand their impact on society, the environment, and the economy</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); border-top: 4px solid #30b566;">
            <div style="font-size: 2em; margin-bottom: 15px;">📊</div>
            <strong style="color: #1e3a5f; font-size: 1.1em;">Align Strategy</strong>
            <p style="margin: 10px 0 0 0; line-height: 1.6;">Align their strategy with sustainability objectives</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); border-top: 4px solid #30b566;">
            <div style="font-size: 2em; margin-bottom: 15px;">🤝</div>
            <strong style="color: #1e3a5f; font-size: 1.1em;">Engage Stakeholders</strong>
            <p style="margin: 10px 0 0 0; line-height: 1.6;">Engage stakeholders effectively</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); border-top: 4px solid #30b566;">
            <div style="font-size: 2em; margin-bottom: 15px;">📈</div>
            <strong style="color: #1e3a5f; font-size: 1.1em;">Measure & Improve</strong>
            <p style="margin: 10px 0 0 0; line-height: 1.6;">Measure and improve long-term outcomes, not just short-term outputs</p>
        </div>
    </div>

    <div style="background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%); padding: 25px; border-radius: 12px; margin-top: 30px; border-left: 5px solid #ff9800;">
        <p style="margin: 0; font-size: 1.05em; line-height: 1.7;">
            <strong>Unlike environmental-only standards</strong>, ISO 37101 is holistic. It addresses governance, ethics, resilience, inclusion, wellbeing, and economic vitality alongside environmental performance.
        </p>
    </div>
</div>

<!-- Why ISO 37101 was created -->
<h2 style="color: #1e3a5f; margin-top: 50px; margin-bottom: 20px; font-size: 2em;">
    Why ISO 37101 was created
</h2>

<div style="background: linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%); padding: 35px; border-radius: 15px; margin: 30px 0; border-left: 5px solid #f44336;">
    <p style="font-size: 1.05em; line-height: 1.8; margin: 0;">
        Many sustainability initiatives fail because they are <strong>fragmented</strong>—carbon reduction plans sit in isolation, social value is treated as a procurement tick-box, and governance is reactive rather than strategic.
    </p>
</div>

<p style="font-size: 1.05em; line-height: 1.8; margin: 25px 0;">
    ISO 37101 was developed to solve this problem by introducing a <strong>management-system approach to sustainable development</strong>. It brings structure, accountability, and leadership oversight to sustainability, ensuring that policies, objectives, and actions are aligned and measurable.
</p>

<p style="font-size: 1.05em; line-height: 1.8; margin: 25px 0;">
    The standard was designed to support the <strong>UN Sustainable Development Goals (SDGs)</strong> while remaining practical and adaptable for organisations of all sizes.
</p>

<!-- Why ISO 37101 matters for UK organisations -->
<div style="background: #e3f2fd; padding: 40px; border-radius: 15px; margin: 40px 0;">
    <h2 style="color: #1e3a5f; margin-top: 0; margin-bottom: 25px; font-size: 2em; display: flex; align-items: center;">
        <span style="background: linear-gradient(135deg, #2196f3 0%, #64b5f6 100%); color: white; width: 50px; height: 50px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; margin-right: 15px; font-size: 1.2em;">🇬🇧</span>
        Why ISO 37101 matters for UK organisations
    </h2>

    <p style="font-size: 1.05em; line-height: 1.8; margin-bottom: 20px;">
        In the UK, sustainability expectations are being driven by:
    </p>

    <div style="display: flex; flex-wrap: wrap; gap: 15px; margin: 25px 0;">
        <span style="background: white; color: #1e3a5f; padding: 12px 24px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">Public sector procurement frameworks</span>
        <span style="background: white; color: #1e3a5f; padding: 12px 24px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">Planning and regeneration requirements</span>
        <span style="background: white; color: #1e3a5f; padding: 12px 24px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">Net Zero commitments</span>
        <span style="background: white; color: #1e3a5f; padding: 12px 24px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">ESG reporting and investor scrutiny</span>
        <span style="background: white; color: #1e3a5f; padding: 12px 24px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">Social Value obligations</span>
    </div>

    <div style="background: white; padding: 30px; border-radius: 12px; margin-top: 25px; box-shadow: 0 4px 12px rgba(0,0,0,0.08);">
        <p style="margin: 0; font-size: 1.1em; line-height: 1.8; color: #1e3a5f;">
            <strong>ISO 37101 provides credible evidence</strong> that your organisation is managing sustainability systematically, not superficially. For organisations working with councils, housing associations, infrastructure projects, or community-facing services, it acts as a powerful badge of trust and competence.
        </p>
    </div>
</div>

<!-- Who ISO 37101 is for -->
<h2 style="color: #1e3a5f; margin-top: 50px; margin-bottom: 20px; font-size: 2em;">
    Who ISO 37101 is for
</h2>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 25px; margin: 30px 0;">
    <div style="background: linear-gradient(135deg, #e8eaf6 0%, #c5cae9 100%); padding: 30px; border-radius: 12px; border-left: 5px solid #3f51b5;">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 15px; font-size: 1.3em;">🏛️ Local Authorities & Public Bodies</h3>
        <p style="margin: 0; line-height: 1.7;">Managing sustainable development strategies and community outcomes</p>
    </div>
    <div style="background: linear-gradient(135deg, #fce4ec 0%, #f8bbd0 100%); padding: 30px; border-radius: 12px; border-left: 5px solid #e91e63;">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 15px; font-size: 1.3em;">🏗️ Developers & Construction Firms</h3>
        <p style="margin: 0; line-height: 1.7;">Embedding sustainability into planning, delivery, and regeneration projects</p>
    </div>
    <div style="background: linear-gradient(135deg, #e0f2f1 0%, #b2dfdb 100%); padding: 30px; border-radius: 12px; border-left: 5px solid #009688;">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 15px; font-size: 1.3em;">⚡ Infrastructure & Utilities</h3>
        <p style="margin: 0; line-height: 1.7;">Balancing resilience, environmental impact, and social responsibility</p>
    </div>
    <div style="background: linear-gradient(135deg, #fff9c4 0%, #fff59d 100%); padding: 30px; border-radius: 12px; border-left: 5px solid #fbc02d;">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 15px; font-size: 1.3em;">🏘️ Housing Associations</h3>
        <p style="margin: 0; line-height: 1.7;">Addressing wellbeing, inclusion, and environmental performance</p>
    </div>
    <div style="background: linear-gradient(135deg, #f3e5f5 0%, #e1bee7 100%); padding: 30px; border-radius: 12px; border-left: 5px solid #9c27b0;">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 15px; font-size: 1.3em;">🏢 Private Organisations</h3>
        <p style="margin: 0; line-height: 1.7;">Demonstrating ESG maturity and community impact</p>
    </div>
</div>

<!-- Key principles -->
<div style="background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%); padding: 45px; border-radius: 15px; margin: 50px 0; color: white;">
    <h2 style="color: white; margin-top: 0; margin-bottom: 30px; font-size: 2em; text-align: center;">
        Key Principles of ISO 37101
    </h2>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 25px;">
        <div style="background: rgba(255,255,255,0.1); padding: 25px; border-radius: 12px; backdrop-filter: blur(10px);">
            <div style="font-size: 2.5em; margin-bottom: 15px;">🎯</div>
            <h3 style="color: white; margin: 0 0 10px 0; font-size: 1.2em;">Sustainable Development Outcomes</h3>
            <p style="margin: 0; opacity: 0.9; line-height: 1.6;">Focusing on long-term environmental, social, and economic value</p>
        </div>
        <div style="background: rgba(255,255,255,0.1); padding: 25px; border-radius: 12px; backdrop-filter: blur(10px);">
            <div style="font-size: 2.5em; margin-bottom: 15px;">🔄</div>
            <h3 style="color: white; margin: 0 0 10px 0; font-size: 1.2em;">Systems Thinking</h3>
            <p style="margin: 0; opacity: 0.9; line-height: 1.6;">Recognising that decisions in one area affect others</p>
        </div>
        <div style="background: rgba(255,255,255,0.1); padding: 25px; border-radius: 12px; backdrop-filter: blur(10px);">
            <div style="font-size: 2.5em; margin-bottom: 15px;">👥</div>
            <h3 style="color: white; margin: 0 0 10px 0; font-size: 1.2em;">Stakeholder Engagement</h3>
            <p style="margin: 0; opacity: 0.9; line-height: 1.6;">Involving communities, partners, and supply chains</p>
        </div>
        <div style="background: rgba(255,255,255,0.1); padding: 25px; border-radius: 12px; backdrop-filter: blur(10px);">
            <div style="font-size: 2.5em; margin-bottom: 15px;">👔</div>
            <h3 style="color: white; margin: 0 0 10px 0; font-size: 1.2em;">Leadership & Governance</h3>
            <p style="margin: 0; opacity: 0.9; line-height: 1.6;">Sustainability driven from the top, not as a side project</p>
        </div>
        <div style="background: rgba(255,255,255,0.1); padding: 25px; border-radius: 12px; backdrop-filter: blur(10px);">
            <div style="font-size: 2.5em; margin-bottom: 15px;">📈</div>
            <h3 style="color: white; margin: 0 0 10px 0; font-size: 1.2em;">Continuous Improvement</h3>
            <p style="margin: 0; opacity: 0.9; line-height: 1.6;">Using data, reviews, and performance indicators</p>
        </div>
    </div>
</div>

<!-- Benefits section -->
<h2 style="color: #1e3a5f; margin-top: 50px; margin-bottom: 30px; font-size: 2em; text-align: center;">
    Benefits of ISO 37101
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
                Clear sustainability objectives linked to strategy
            </li>
            <li style="margin-bottom: 15px; padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #30b566; font-size: 1.3em;">✓</span>
                Improved decision-making based on long-term impacts
            </li>
            <li style="margin-bottom: 15px; padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #30b566; font-size: 1.3em;">✓</span>
                Better coordination between departments and projects
            </li>
            <li style="padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #30b566; font-size: 1.3em;">✓</span>
                Stronger governance and accountability
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
                Enhanced credibility with public sector clients
            </li>
            <li style="margin-bottom: 15px; padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #2196f3; font-size: 1.3em;">✓</span>
                Strong alignment with ESG and Social Value
            </li>
            <li style="margin-bottom: 15px; padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #2196f3; font-size: 1.3em;">✓</span>
                Improved reputation and stakeholder trust
            </li>
            <li style="padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #2196f3; font-size: 1.3em;">✓</span>
                Support for Net Zero and resilience planning
            </li>
        </ul>
    </div>

    <!-- Compliance Benefits -->
    <div style="background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%); padding: 35px; border-radius: 15px; box-shadow: 0 6px 20px rgba(0,0,0,0.1);">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 20px; font-size: 1.5em; display: flex; align-items: center;">
            <span style="font-size: 1.5em; margin-right: 10px;">📋</span> Compliance & Procurement
        </h3>
        <ul style="list-style: none; padding: 0; margin: 0;">
            <li style="margin-bottom: 15px; padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #ff9800; font-size: 1.3em;">✓</span>
                Strong evidence for sustainability in tenders
            </li>
            <li style="margin-bottom: 15px; padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #ff9800; font-size: 1.3em;">✓</span>
                Alignment with UK procurement expectations
            </li>
            <li style="margin-bottom: 15px; padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #ff9800; font-size: 1.3em;">✓</span>
                Reduced risk of "greenwashing" accusations
            </li>
            <li style="padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #ff9800; font-size: 1.3em;">✓</span>
                Easier integration with other ISO standards
            </li>
        </ul>
    </div>
</div>

<!-- What auditors look for -->
<div style="background: #f8f9fa; padding: 40px; border-radius: 15px; margin: 50px 0;">
    <h2 style="color: #1e3a5f; margin-top: 0; margin-bottom: 25px; font-size: 2em;">
        What ISO 37101 auditors actually look for
    </h2>

    <div style="background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%); padding: 25px; border-radius: 12px; margin-bottom: 25px; border-left: 5px solid #ff9800;">
        <p style="margin: 0; font-size: 1.05em; line-height: 1.7;">
            <strong>Auditors are not judging your political views or environmental activism.</strong> They are assessing whether your management system works.
        </p>
    </div>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-top: 25px;">
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
            <h4 style="color: #1e3a5f; margin-top: 0; margin-bottom: 12px;">📍 Context Analysis</h4>
            <p style="margin: 0; line-height: 1.6;">Understanding your role and influence within the community</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
            <h4 style="color: #1e3a5f; margin-top: 0; margin-bottom: 12px;">🎯 Sustainability Objectives</h4>
            <p style="margin: 0; line-height: 1.6;">Clear, measurable, and relevant goals</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
            <h4 style="color: #1e3a5f; margin-top: 0; margin-bottom: 12px;">👥 Stakeholder Engagement</h4>
            <p style="margin: 0; line-height: 1.6;">Consultation, feedback, and communication evidence</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
            <h4 style="color: #1e3a5f; margin-top: 0; margin-bottom: 12px;">📊 Performance Monitoring</h4>
            <p style="margin: 0; line-height: 1.6;">KPIs, reports, and reviews</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
            <h4 style="color: #1e3a5f; margin-top: 0; margin-bottom: 12px;">👔 Leadership Involvement</h4>
            <p style="margin: 0; line-height: 1.6;">Evidence of senior management oversight</p>
        </div>
    </div>

    <div style="background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%); padding: 25px; border-radius: 12px; margin-top: 25px; border-left: 5px solid #30b566;">
        <p style="margin: 0; font-size: 1.05em; line-height: 1.7;">
            The focus is always on <strong>process, consistency, and improvement</strong>, not perfection.
        </p>
    </div>
</div>

<!-- Real-world examples -->
<h2 style="color: #1e3a5f; margin-top: 50px; margin-bottom: 30px; font-size: 2em;">
    ISO 37101 in practice (real-world examples)
</h2>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 30px; margin: 30px 0;">
    <div style="background: linear-gradient(135deg, #e8eaf6 0%, #c5cae9 100%); padding: 35px; border-radius: 15px; box-shadow: 0 6px 20px rgba(0,0,0,0.1);">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 20px; font-size: 1.4em;">
            🏛️ Local Authority / Regeneration Project
        </h3>
        <p style="margin: 0; line-height: 1.7; font-size: 1.05em;">
            A UK council uses ISO 37101 to manage a long-term regeneration programme. The SDMS ensures housing, transport, employment, and environmental objectives are aligned, measured, and reviewed collectively—supporting funding bids and community trust.
        </p>
    </div>

    <div style="background: linear-gradient(135deg, #fce4ec 0%, #f8bbd0 100%); padding: 35px; border-radius: 15px; box-shadow: 0 6px 20px rgba(0,0,0,0.1);">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 20px; font-size: 1.4em;">
            🏗️ Construction & Development Firm
        </h3>
        <p style="margin: 0; line-height: 1.7; font-size: 1.05em;">
            A developer applies ISO 37101 to demonstrate how projects deliver social value, reduce environmental impact, and contribute to local wellbeing—strengthening planning applications and public sector tender success.
        </p>
    </div>
</div>

<!-- Common mistakes -->
<div style="background: linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%); padding: 40px; border-radius: 15px; margin: 50px 0;">
    <h2 style="color: #1e3a5f; margin-top: 0; margin-bottom: 25px; font-size: 2em;">
        ⚠️ Common mistakes when implementing ISO 37101
    </h2>

    <div style="display: grid; gap: 20px;">
        <div style="background: white; padding: 25px; border-radius: 12px; border-left: 5px solid #f44336;">
            <h4 style="color: #1e3a5f; margin: 0 0 10px 0; font-size: 1.2em;">Treating it as a PR Exercise</h4>
            <p style="margin: 0; line-height: 1.6;">Without genuine leadership commitment, the system will fail.</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; border-left: 5px solid #f44336;">
            <h4 style="color: #1e3a5f; margin: 0 0 10px 0; font-size: 1.2em;">Trying to Measure Everything</h4>
            <p style="margin: 0; line-height: 1.6;">The standard encourages relevant indicators, not excessive bureaucracy.</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; border-left: 5px solid #f44336;">
            <h4 style="color: #1e3a5f; margin: 0 0 10px 0; font-size: 1.2em;">Ignoring Stakeholders</h4>
            <p style="margin: 0; line-height: 1.6;">Sustainable development cannot be managed in isolation from the community.</p>
        </div>
    </div>
</div>

<!-- Certification process -->
<div style="background: #f8f9fa; padding: 40px; border-radius: 15px; margin: 50px 0;">
    <h2 style="color: #1e3a5f; margin-top: 0; margin-bottom: 30px; font-size: 2em; text-align: center;">
        ISO 37101 certification process
    </h2>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 25px;">
        <div style="background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); text-align: center;">
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px; font-size: 1.8em; font-weight: bold;">1</div>
            <h4 style="color: #1e3a5f; margin: 0 0 12px 0; font-size: 1.2em;">Stage 1: Documentation Review</h4>
            <p style="margin: 0; line-height: 1.6;">The auditor checks that your SDMS is correctly designed and aligned with the standard</p>
        </div>
        <div style="background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); text-align: center;">
            <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); color: white; width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px; font-size: 1.8em; font-weight: bold;">2</div>
            <h4 style="color: #1e3a5f; margin: 0 0 12px 0; font-size: 1.2em;">Stage 2: Implementation Audit</h4>
            <p style="margin: 0; line-height: 1.6;">Verify that sustainability objectives, engagement, and monitoring are operating in practice</p>
        </div>
        <div style="background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); text-align: center;">
            <div style="background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%); color: white; width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px; font-size: 1.8em; font-weight: bold;">3</div>
            <h4 style="color: #1e3a5f; margin: 0 0 12px 0; font-size: 1.2em;">Surveillance Audits</h4>
            <p style="margin: 0; line-height: 1.6;">Annual reviews ensure the system continues to evolve and improve</p>
        </div>
        <div style="background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); text-align: center;">
            <div style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); color: white; width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px; font-size: 1.8em; font-weight: bold;">4</div>
            <h4 style="color: #1e3a5f; margin: 0 0 12px 0; font-size: 1.2em;">Recertification</h4>
            <p style="margin: 0; line-height: 1.6;">Every three years, a full reassessment renews certification</p>
        </div>
    </div>
</div>

<!-- Duration and cost -->
<h2 style="color: #1e3a5f; margin-top: 50px; margin-bottom: 20px; font-size: 2em;">
    How long does ISO 37101 certification last?
</h2>

<p style="font-size: 1.05em; line-height: 1.8; margin: 25px 0;">
    ISO 37101 certification is valid for <strong>three years</strong>, subject to successful annual surveillance audits. Failure to demonstrate ongoing improvement can result in suspension or withdrawal.
</p>

<h2 style="color: #1e3a5f; margin-top: 50px; margin-bottom: 20px; font-size: 2em;">
    How much does ISO 37101 cost in the UK?
</h2>

<p style="font-size: 1.05em; line-height: 1.8; margin: 25px 0;">
    Costs vary depending on:
</p>

<ul style="font-size: 1.05em; line-height: 1.8; margin: 25px 0; padding-left: 30px;">
    <li style="margin-bottom: 10px;">Organisation size and complexity</li>
    <li style="margin-bottom: 10px;">Scope of activities and influence</li>
    <li>Existing management systems</li>
</ul>

<div style="background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%); padding: 35px; border-radius: 15px; margin: 30px 0; border-left: 5px solid #2196f3;">
    <p style="margin: 0 0 15px 0; font-size: 1.1em; font-weight: 600; color: #1e3a5f;">
        Typical costs include:
    </p>
    <ul style="margin: 0; padding-left: 25px; line-height: 1.8;">
        <li style="margin-bottom: 10px;">Certification Audit Fees</li>
        <li style="margin-bottom: 10px;">Consultancy Support (if used)</li>
        <li>Internal Resource Time</li>
    </ul>
</div>

<p style="font-size: 1.05em; line-height: 1.8; margin: 25px 0;">
    Like ISO 27001, ISO 37101 should be viewed as an <strong>investment in long-term resilience and credibility</strong>, not just a compliance cost.
</p>

<!-- Integration -->
<div style="background: #f8f9fa; padding: 40px; border-radius: 15px; margin: 50px 0;">
    <h2 style="color: #1e3a5f; margin-top: 0; margin-bottom: 25px; font-size: 2em;">
        ISO 37101 and integration with other standards
    </h2>

    <p style="font-size: 1.05em; line-height: 1.8; margin-bottom: 25px;">
        ISO 37101 follows the same <strong>High-Level Structure (Annex SL)</strong> as ISO 9001, ISO 14001, and ISO 27001. This makes it ideal for an <strong>Integrated Management System (IMS)</strong>, allowing shared:
    </p>

    <div style="display: flex; flex-wrap: wrap; gap: 15px; margin: 25px 0;">
        <span style="background: white; color: #1e3a5f; padding: 15px 30px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1); font-size: 1.05em;">Internal audits</span>
        <span style="background: white; color: #1e3a5f; padding: 15px 30px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1); font-size: 1.05em;">Management reviews</span>
        <span style="background: white; color: #1e3a5f; padding: 15px 30px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1); font-size: 1.05em;">Document control processes</span>
    </div>

    <div style="background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%); padding: 25px; border-radius: 12px; margin-top: 25px; border-left: 5px solid #30b566;">
        <p style="margin: 0; font-size: 1.05em; line-height: 1.7;">
            This significantly <strong>reduces duplication and cost</strong>.
        </p>
    </div>
</div>

<!-- Who should NOT implement -->
<div style="background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%); padding: 40px; border-radius: 15px; margin: 50px 0; border-left: 5px solid #ff9800;">
    <h2 style="color: #1e3a5f; margin-top: 0; margin-bottom: 20px; font-size: 2em;">
        Who should NOT implement ISO 37101?
    </h2>

    <p style="margin: 0; font-size: 1.05em; line-height: 1.8;">
        If your organisation has <strong>no meaningful interaction with communities</strong>, no sustainability obligations, and no stakeholder expectations, ISO 37101 may not be appropriate. Likewise, organisations seeking a quick marketing badge without behavioural change will struggle to achieve certification.
    </p>
</div>

<!-- FAQs -->
<div style="background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%); padding: 45px; border-radius: 15px; margin: 50px 0; color: white;">
    <h2 style="color: white; margin-top: 0; margin-bottom: 30px; font-size: 2em; text-align: center;">
        Frequently Asked Questions (FAQs)
    </h2>

    <div style="display: grid; gap: 25px;">
        <div style="background: rgba(255,255,255,0.1); padding: 30px; border-radius: 12px; backdrop-filter: blur(10px);">
            <h4 style="color: white; margin: 0 0 12px 0; font-size: 1.3em;">Is ISO 37101 a legal requirement in the UK?</h4>
            <p style="margin: 0; opacity: 0.9; line-height: 1.7; font-size: 1.05em;">No. It is voluntary, but increasingly influential in procurement and funding decisions.</p>
        </div>

        <div style="background: rgba(255,255,255,0.1); padding: 30px; border-radius: 12px; backdrop-filter: blur(10px);">
            <h4 style="color: white; margin: 0 0 12px 0; font-size: 1.3em;">Is ISO 37101 the same as ISO 14001?</h4>
            <p style="margin: 0; opacity: 0.9; line-height: 1.7; font-size: 1.05em;">No. ISO 14001 focuses on environmental management. ISO 37101 covers environmental, social, economic, and governance outcomes.</p>
        </div>

        <div style="background: rgba(255,255,255,0.1); padding: 30px; border-radius: 12px; backdrop-filter: blur(10px);">
            <h4 style="color: white; margin: 0 0 12px 0; font-size: 1.3em;">Can SMEs achieve ISO 37101?</h4>
            <p style="margin: 0; opacity: 0.9; line-height: 1.7; font-size: 1.05em;">Yes. The standard is scalable and proportionate to organisational size and influence.</p>
        </div>

        <div style="background: rgba(255,255,255,0.1); padding: 30px; border-radius: 12px; backdrop-filter: blur(10px);">
            <h4 style="color: white; margin: 0 0 12px 0; font-size: 1.3em;">Does ISO 37101 support ESG reporting?</h4>
            <p style="margin: 0; opacity: 0.9; line-height: 1.7; font-size: 1.05em;">Absolutely. It provides structure and evidence behind ESG claims.</p>
        </div>
    </div>
</div>

<!-- Call to action -->
<div style="background: linear-gradient(135deg, #30b566 0%, #56d882 100%); padding: 50px; border-radius: 15px; margin: 50px 0; text-align: center; color: white;">
    <h2 style="color: white; margin: 0 0 20px 0; font-size: 2.2em;">
        Ready to demonstrate your commitment to sustainable development?
    </h2>
    <p style="font-size: 1.2em; line-height: 1.8; margin: 0 0 30px 0; opacity: 0.95;">
        Qualitation has been helping UK organisations achieve ISO certification for over 25 years with a 100% first-time success rate.
    </p>
    <div style="display: flex; gap: 20px; justify-content: center; flex-wrap: wrap;">
        <a href="/contact/" style="background: white; color: #30b566; padding: 15px 40px; border-radius: 50px; text-decoration: none; font-weight: 700; font-size: 1.1em; display: inline-block; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
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

            self.stdout.write(self.style.SUCCESS(f'✓ Updated ISO 37101 page'))
            self.stdout.write(self.style.SUCCESS(f'✓ URL: /{page.get_url_parts()[2]}'))
            self.stdout.write(self.style.SUCCESS('✓ Published successfully'))

        except Page.DoesNotExist:
            self.stdout.write(self.style.ERROR('✗ ISO 37101 page not found'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ Error: {e}'))
            import traceback
            traceback.print_exc()

        self.stdout.write(self.style.SUCCESS('\n=== Complete ===\n'))
