"""
Django management command to update ISO 20400 page with new content
"""

from django.core.management.base import BaseCommand
from wagtail.models import Page


class Command(BaseCommand):
    help = 'Update ISO 20400 page with new beautifully illustrated content'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('\n=== Updating ISO 20400 Page ===\n'))

        try:
            # Get the ISO 20400 page
            page = Page.objects.get(slug='iso-20400').specific

            self.stdout.write(f'Found page: {page.title}')

            # New content with beautiful illustrations
            content_html = '''
<style>
    main { padding-top: 0 !important; margin-top: 0 !important; }
</style>
<!-- Hero Section -->
<section style="background: linear-gradient(135deg, #00897b 0%, #26a69a 100%); padding: 80px 40px; margin: 0; position: relative; overflow: hidden;">
    <div style="max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: 1fr 300px; gap: 60px; align-items: center;">
        <div>
            <h1 style="color: white; font-size: 3em; margin: 0 0 20px 0; font-weight: 700; line-height: 1.2;">
                ISO 20400 Certification UK
            </h1>
            <p style="color: white; font-size: 1.3em; margin: 0 0 30px 0; line-height: 1.6; opacity: 0.95;">
                Sustainable Procurement. Make purchasing decisions that deliver environmental, social, and economic value across the supply chain.
            </p>

            <!-- Feature Tags -->
            <div style="display: flex; flex-wrap: wrap; gap: 12px; margin-bottom: 30px;">
                <span style="background: rgba(255,255,255,0.25); color: white; padding: 10px 20px; border-radius: 50px; font-weight: 600; backdrop-filter: blur(10px); display: flex; align-items: center; gap: 8px;">
                    <span style="font-size: 1.2em;">♻️</span> Responsible Sourcing
                </span>
                <span style="background: rgba(255,255,255,0.25); color: white; padding: 10px 20px; border-radius: 50px; font-weight: 600; backdrop-filter: blur(10px); display: flex; align-items: center; gap: 8px;">
                    <span style="font-size: 1.2em;">✓</span> Social Value
                </span>
                <span style="background: rgba(255,255,255,0.25); color: white; padding: 10px 20px; border-radius: 50px; font-weight: 600; backdrop-filter: blur(10px); display: flex; align-items: center; gap: 8px;">
                    <span style="font-size: 1.2em;">🌍</span> ESG Aligned
                </span>
            </div>

            <!-- CTA Buttons -->
            <div style="display: flex; gap: 15px; flex-wrap: wrap;">
                <a href="/contact/" style="background: white; color: #00897b; padding: 15px 35px; border-radius: 50px; text-decoration: none; font-weight: 700; font-size: 1.1em; display: inline-flex; align-items: center; gap: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.2); transition: transform 0.2s;">
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
                    <div style="font-size: 5em; margin-bottom: 10px;">♻️</div>
                    <div style="font-size: 2em; color: #00897b; font-weight: 700;">20400</div>
                </div>
                <!-- Decorative elements -->
                <div style="position: absolute; top: 20px; left: -20px; width: 40px; height: 40px; background: #00897b; border-radius: 50%;"></div>
                <div style="position: absolute; bottom: 40px; right: -15px; width: 30px; height: 30px; background: #26a69a; border-radius: 50%;"></div>
            </div>
        </div>
    </div>
</section>

<div style="max-width: 1200px; margin: 0 auto; padding: 40px 20px;" id="learn-more">

<div style="background: linear-gradient(135deg, #e0f2f1 0%, #b2dfdb 100%); padding: 35px; border-radius: 15px; margin: 30px 0; border-left: 5px solid #00897b;">
    <p style="font-size: 1.15em; line-height: 1.8; margin: 0; color: #1e3a5f;">
        Sustainable procurement is no longer just about choosing the cheapest supplier. For UK organisations, purchasing decisions now carry environmental, social, ethical, and reputational consequences that extend far beyond the balance sheet. From modern slavery risk to carbon reduction and social value, procurement teams are under growing pressure to demonstrate responsible decision-making. <strong>ISO 20400 provides the internationally recognised framework to do exactly that</strong>.
    </p>
</div>

<p style="font-size: 1.1em; line-height: 1.8; margin: 25px 0;">
    ISO 20400 is the global guidance standard for <strong>Sustainable Procurement</strong>. It helps organisations integrate sustainability into procurement strategy, policy, and day-to-day purchasing decisions—ensuring value for money over the whole life cycle, not just at the point of purchase.
</p>

<!-- What is ISO 20400 -->
<div style="background: #f8f9fa; padding: 40px; border-radius: 15px; margin: 40px 0;">
    <h2 style="color: #1e3a5f; margin-top: 0; margin-bottom: 25px; font-size: 2em; display: flex; align-items: center;">
        <span style="background: linear-gradient(135deg, #00897b 0%, #26a69a 100%); color: white; width: 50px; height: 50px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; margin-right: 15px; font-size: 1.2em;">♻️</span>
        What is ISO 20400?
    </h2>

    <p style="font-size: 1.05em; line-height: 1.8; margin-bottom: 20px;">
        ISO 20400 is a guidance standard published by the International Organization for Standardization. It provides practical guidance on how organisations can make procurement decisions that have positive environmental, social, and economic impacts.
    </p>

    <p style="font-size: 1.1em; font-weight: 600; color: #1e3a5f; margin: 25px 0 15px 0;">
        In plain English, ISO 20400 helps organisations:
    </p>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-top: 25px;">
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); border-top: 4px solid #00897b;">
            <div style="font-size: 2em; margin-bottom: 15px;">🛒</div>
            <strong style="color: #1e3a5f; font-size: 1.1em;">Buy Responsibly</strong>
            <p style="margin: 10px 0 0 0; line-height: 1.6;">Buy goods and services responsibly</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); border-top: 4px solid #00897b;">
            <div style="font-size: 2em; margin-bottom: 15px;">🛡️</div>
            <strong style="color: #1e3a5f; font-size: 1.1em;">Reduce Risk</strong>
            <p style="margin: 10px 0 0 0; line-height: 1.6;">Reduce supply-chain risk and reputational damage</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); border-top: 4px solid #00897b;">
            <div style="font-size: 2em; margin-bottom: 15px;">📊</div>
            <strong style="color: #1e3a5f; font-size: 1.1em;">Embed ESG</strong>
            <p style="margin: 10px 0 0 0; line-height: 1.6;">Embed ESG and social value into procurement</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); border-top: 4px solid #00897b;">
            <div style="font-size: 2em; margin-bottom: 15px;">🎯</div>
            <strong style="color: #1e3a5f; font-size: 1.1em;">Align Strategy</strong>
            <p style="margin: 10px 0 0 0; line-height: 1.6;">Align procurement with organisational strategy</p>
        </div>
    </div>

    <div style="background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%); padding: 25px; border-radius: 12px; margin-top: 30px; border-left: 5px solid #ff9800;">
        <p style="margin: 0; font-size: 1.05em; line-height: 1.7;">
            <strong>Unlike certifiable ISO standards</strong>, ISO 20400 is principles-based and flexible, making it suitable for organisations of all sizes and sectors.
        </p>
    </div>
</div>

<!-- Why ISO 20400 was created -->
<h2 style="color: #1e3a5f; margin-top: 50px; margin-bottom: 20px; font-size: 2em;">
    Why ISO 20400 was created
</h2>

<div style="background: linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%); padding: 35px; border-radius: 15px; margin: 30px 0; border-left: 5px solid #f44336;">
    <p style="font-size: 1.05em; line-height: 1.8; margin: 0 0 15px 0;">
        Traditional procurement models focused heavily on cost and speed, often overlooking long-term impacts such as environmental harm, labour exploitation, or supply-chain fragility. High-profile failures—ranging from modern slavery scandals to supplier collapses—highlighted the need for a more responsible approach.
    </p>
    <p style="font-size: 1.05em; line-height: 1.8; margin: 0;">
        ISO 20400 was developed to help organisations move from <strong>transactional buying to strategic, values-led procurement</strong>. It reframes procurement as a lever for sustainability, resilience, and long-term value creation.
    </p>
</div>

<!-- Why ISO 20400 matters for UK organisations -->
<div style="background: #e3f2fd; padding: 40px; border-radius: 15px; margin: 40px 0;">
    <h2 style="color: #1e3a5f; margin-top: 0; margin-bottom: 25px; font-size: 2em; display: flex; align-items: center;">
        <span style="background: linear-gradient(135deg, #2196f3 0%, #64b5f6 100%); color: white; width: 50px; height: 50px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; margin-right: 15px; font-size: 1.2em;">🇬🇧</span>
        Why ISO 20400 matters for UK organisations
    </h2>

    <p style="font-size: 1.05em; line-height: 1.8; margin-bottom: 20px;">
        UK organisations face increasing expectations around responsible sourcing due to:
    </p>

    <div style="display: flex; flex-wrap: wrap; gap: 15px; margin: 25px 0;">
        <span style="background: white; color: #1e3a5f; padding: 12px 24px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">The Modern Slavery Act 2015</span>
        <span style="background: white; color: #1e3a5f; padding: 12px 24px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">Public sector Social Value requirements</span>
        <span style="background: white; color: #1e3a5f; padding: 12px 24px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">Net Zero and carbon-reduction commitments</span>
        <span style="background: white; color: #1e3a5f; padding: 12px 24px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">ESG reporting and investor scrutiny</span>
        <span style="background: white; color: #1e3a5f; padding: 12px 24px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">Reputational risk linked to global supply chains</span>
    </div>

    <div style="background: white; padding: 30px; border-radius: 12px; margin-top: 25px; box-shadow: 0 4px 12px rgba(0,0,0,0.08);">
        <p style="margin: 0 0 15px 0; font-size: 1.1em; line-height: 1.8; color: #1e3a5f;">
            <strong>ISO 20400 provides a credible framework</strong> to demonstrate that sustainability is being actively considered in procurement decisions, not treated as a tick-box exercise.
        </p>
        <p style="margin: 0; font-size: 1.05em; line-height: 1.8; color: #1e3a5f;">
            For public sector bodies and contractors, ISO 20400 aligns strongly with PPN guidance, social value models, and responsible procurement expectations.
        </p>
    </div>
</div>

<!-- Who ISO 20400 is for -->
<h2 style="color: #1e3a5f; margin-top: 50px; margin-bottom: 20px; font-size: 2em;">
    Who ISO 20400 is for
</h2>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 25px; margin: 30px 0;">
    <div style="background: linear-gradient(135deg, #e8eaf6 0%, #c5cae9 100%); padding: 30px; border-radius: 12px; border-left: 5px solid #3f51b5;">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 15px; font-size: 1.3em;">🏛️ Public Sector & Local Authorities</h3>
        <p style="margin: 0; line-height: 1.7;">Embedding social value and ethical sourcing</p>
    </div>
    <div style="background: linear-gradient(135deg, #fce4ec 0%, #f8bbd0 100%); padding: 30px; border-radius: 12px; border-left: 5px solid #e91e63;">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 15px; font-size: 1.3em;">🏗️ Construction & Infrastructure</h3>
        <p style="margin: 0; line-height: 1.7;">Managing complex, high-risk supply chains</p>
    </div>
    <div style="background: linear-gradient(135deg, #e0f2f1 0%, #b2dfdb 100%); padding: 30px; border-radius: 12px; border-left: 5px solid #009688;">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 15px; font-size: 1.3em;">🏭 Manufacturing Organisations</h3>
        <p style="margin: 0; line-height: 1.7;">Responsible sourcing of raw materials</p>
    </div>
    <div style="background: linear-gradient(135deg, #fff9c4 0%, #fff59d 100%); padding: 30px; border-radius: 12px; border-left: 5px solid #fbc02d;">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 15px; font-size: 1.3em;">🏥 Healthcare & Education</h3>
        <p style="margin: 0; line-height: 1.7;">Ethical procurement under budget pressure</p>
    </div>
    <div style="background: linear-gradient(135deg, #f3e5f5 0%, #e1bee7 100%); padding: 30px; border-radius: 12px; border-left: 5px solid #9c27b0;">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 15px; font-size: 1.3em;">💼 Private Sector & SMEs</h3>
        <p style="margin: 0; line-height: 1.7;">Strengthening ESG credentials and supplier resilience</p>
    </div>
</div>

<div style="background: linear-gradient(135deg, #e0f2f1 0%, #b2dfdb 100%); padding: 25px; border-radius: 12px; margin: 30px 0; border-left: 5px solid #00897b;">
    <p style="margin: 0; font-size: 1.05em; line-height: 1.7;">
        It applies equally to <strong>strategic procurement teams and operational buyers</strong>.
    </p>
</div>

<!-- Key principles -->
<div style="background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%); padding: 45px; border-radius: 15px; margin: 50px 0; color: white;">
    <h2 style="color: white; margin-top: 0; margin-bottom: 30px; font-size: 2em; text-align: center;">
        Key Principles of ISO 20400
    </h2>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 25px;">
        <div style="background: rgba(255,255,255,0.1); padding: 25px; border-radius: 12px; backdrop-filter: blur(10px);">
            <div style="font-size: 2.5em; margin-bottom: 15px;">📋</div>
            <h3 style="color: white; margin: 0 0 10px 0; font-size: 1.2em;">Accountability</h3>
            <p style="margin: 0; opacity: 0.9; line-height: 1.6;">Organisations take responsibility for the impacts of their purchasing decisions</p>
        </div>
        <div style="background: rgba(255,255,255,0.1); padding: 25px; border-radius: 12px; backdrop-filter: blur(10px);">
            <div style="font-size: 2.5em; margin-bottom: 15px;">👁️</div>
            <h3 style="color: white; margin: 0 0 10px 0; font-size: 1.2em;">Transparency</h3>
            <p style="margin: 0; opacity: 0.9; line-height: 1.6;">Clear, open procurement processes and supplier expectations</p>
        </div>
        <div style="background: rgba(255,255,255,0.1); padding: 25px; border-radius: 12px; backdrop-filter: blur(10px);">
            <div style="font-size: 2.5em; margin-bottom: 15px;">⚖️</div>
            <h3 style="color: white; margin: 0 0 10px 0; font-size: 1.2em;">Ethical Behaviour</h3>
            <p style="margin: 0; opacity: 0.9; line-height: 1.6;">Addressing corruption, labour rights, and fair treatment</p>
        </div>
        <div style="background: rgba(255,255,255,0.1); padding: 25px; border-radius: 12px; backdrop-filter: blur(10px);">
            <div style="font-size: 2.5em; margin-bottom: 15px;">👥</div>
            <h3 style="color: white; margin: 0 0 10px 0; font-size: 1.2em;">Respect for Human Rights</h3>
            <p style="margin: 0; opacity: 0.9; line-height: 1.6;">Managing risks such as forced labour and unsafe working conditions</p>
        </div>
        <div style="background: rgba(255,255,255,0.1); padding: 25px; border-radius: 12px; backdrop-filter: blur(10px);">
            <div style="font-size: 2.5em; margin-bottom: 15px;">♻️</div>
            <h3 style="color: white; margin: 0 0 10px 0; font-size: 1.2em;">Lifecycle Thinking</h3>
            <p style="margin: 0; opacity: 0.9; line-height: 1.6;">Considering environmental and social impacts from sourcing to disposal</p>
        </div>
        <div style="background: rgba(255,255,255,0.1); padding: 25px; border-radius: 12px; backdrop-filter: blur(10px);">
            <div style="font-size: 2.5em; margin-bottom: 15px;">🤝</div>
            <h3 style="color: white; margin: 0 0 10px 0; font-size: 1.2em;">Stakeholder Engagement</h3>
            <p style="margin: 0; opacity: 0.9; line-height: 1.6;">Working with suppliers, communities, and internal teams</p>
        </div>
    </div>
</div>

<!-- Benefits section -->
<h2 style="color: #1e3a5f; margin-top: 50px; margin-bottom: 30px; font-size: 2em; text-align: center;">
    Benefits of ISO 20400
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
                Clear procurement governance and decision-making
            </li>
            <li style="margin-bottom: 15px; padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #30b566; font-size: 1.3em;">✓</span>
                Improved supplier performance and accountability
            </li>
            <li style="margin-bottom: 15px; padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #30b566; font-size: 1.3em;">✓</span>
                Reduced supply-chain disruption and risk
            </li>
            <li style="padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #30b566; font-size: 1.3em;">✓</span>
                Better alignment between procurement and organisational values
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
                Stronger ESG and sustainability credentials
            </li>
            <li style="margin-bottom: 15px; padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #2196f3; font-size: 1.3em;">✓</span>
                Enhanced reputation with customers, regulators, and investors
            </li>
            <li style="margin-bottom: 15px; padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #2196f3; font-size: 1.3em;">✓</span>
                Competitive advantage in public sector and large-contract tenders
            </li>
            <li style="padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #2196f3; font-size: 1.3em;">✓</span>
                Long-term cost savings through lifecycle value
            </li>
        </ul>
    </div>

    <!-- Legal & Compliance Benefits -->
    <div style="background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%); padding: 35px; border-radius: 15px; box-shadow: 0 6px 20px rgba(0,0,0,0.1);">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 20px; font-size: 1.5em; display: flex; align-items: center;">
            <span style="font-size: 1.5em; margin-right: 10px;">⚖️</span> Legal & Compliance
        </h3>
        <ul style="list-style: none; padding: 0; margin: 0;">
            <li style="margin-bottom: 15px; padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #ff9800; font-size: 1.3em;">✓</span>
                Supports compliance with the Modern Slavery Act
            </li>
            <li style="margin-bottom: 15px; padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #ff9800; font-size: 1.3em;">✓</span>
                Reduces exposure to ethical and reputational failures
            </li>
            <li style="padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #ff9800; font-size: 1.3em;">✓</span>
                Strengthens audit trails and governance assurance
            </li>
        </ul>
    </div>
</div>

<!-- What assessors look for -->
<div style="background: #f8f9fa; padding: 40px; border-radius: 15px; margin: 50px 0;">
    <h2 style="color: #1e3a5f; margin-top: 0; margin-bottom: 25px; font-size: 2em;">
        What assessors look for when using ISO 20400
    </h2>

    <div style="background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%); padding: 25px; border-radius: 12px; margin-bottom: 25px; border-left: 5px solid #ff9800;">
        <p style="margin: 0; font-size: 1.05em; line-height: 1.7;">
            <strong>Although ISO 20400 is not certifiable</strong>, organisations often use it for gap analysis, maturity assessments, or internal audits.
        </p>
    </div>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-top: 25px;">
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
            <h4 style="color: #1e3a5f; margin-top: 0; margin-bottom: 12px;">📋 Procurement Policy & Strategy</h4>
            <p style="margin: 0; line-height: 1.6;">Sustainability embedded at a strategic level</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
            <h4 style="color: #1e3a5f; margin-top: 0; margin-bottom: 12px;">🔍 Supplier Due Diligence</h4>
            <p style="margin: 0; line-height: 1.6;">Ethical, environmental, and social risk assessment</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
            <h4 style="color: #1e3a5f; margin-top: 0; margin-bottom: 12px;">📄 Contracting & Tendering</h4>
            <p style="margin: 0; line-height: 1.6;">Sustainability criteria included in selection</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
            <h4 style="color: #1e3a5f; margin-top: 0; margin-bottom: 12px;">📊 Performance Monitoring</h4>
            <p style="margin: 0; line-height: 1.6;">KPIs, audits, and supplier reviews</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
            <h4 style="color: #1e3a5f; margin-top: 0; margin-bottom: 12px;">🎓 Training & Awareness</h4>
            <p style="margin: 0; line-height: 1.6;">Buyers understand sustainable procurement principles</p>
        </div>
    </div>

    <div style="background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%); padding: 25px; border-radius: 12px; margin-top: 25px; border-left: 5px solid #30b566;">
        <p style="margin: 0; font-size: 1.05em; line-height: 1.7;">
            The emphasis is on <strong>decision-making quality, not paperwork volume</strong>.
        </p>
    </div>
</div>

<!-- Real-world examples -->
<h2 style="color: #1e3a5f; margin-top: 50px; margin-bottom: 30px; font-size: 2em;">
    ISO 20400 in practice (real-world examples)
</h2>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 30px; margin: 30px 0;">
    <div style="background: linear-gradient(135deg, #e8eaf6 0%, #c5cae9 100%); padding: 35px; border-radius: 15px; box-shadow: 0 6px 20px rgba(0,0,0,0.1);">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 20px; font-size: 1.4em;">
            🏛️ Public Sector Organisation
        </h3>
        <p style="margin: 0; line-height: 1.7; font-size: 1.05em;">
            A UK council uses ISO 20400 to embed social value, local sourcing, and ethical labour practices into procurement—supporting community outcomes and regulatory compliance.
        </p>
    </div>

    <div style="background: linear-gradient(135deg, #fce4ec 0%, #f8bbd0 100%); padding: 35px; border-radius: 15px; box-shadow: 0 6px 20px rgba(0,0,0,0.1);">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 20px; font-size: 1.4em;">
            🏗️ Construction Contractor
        </h3>
        <p style="margin: 0; line-height: 1.7; font-size: 1.05em;">
            A contractor applies ISO 20400 to assess high-risk suppliers, reduce environmental impact, and demonstrate responsible sourcing in major infrastructure tenders.
        </p>
    </div>
</div>

<!-- Common mistakes -->
<div style="background: linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%); padding: 40px; border-radius: 15px; margin: 50px 0;">
    <h2 style="color: #1e3a5f; margin-top: 0; margin-bottom: 25px; font-size: 2em;">
        ⚠️ Common mistakes when applying ISO 20400
    </h2>

    <div style="display: grid; gap: 20px;">
        <div style="background: white; padding: 25px; border-radius: 12px; border-left: 5px solid #f44336;">
            <h4 style="color: #1e3a5f; margin: 0 0 10px 0; font-size: 1.2em;">Treating It as a Policy-Only Exercise</h4>
            <p style="margin: 0; line-height: 1.6;">Sustainable procurement must influence real purchasing decisions.</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; border-left: 5px solid #f44336;">
            <h4 style="color: #1e3a5f; margin: 0 0 10px 0; font-size: 1.2em;">Overburdening Suppliers</h4>
            <p style="margin: 0; line-height: 1.6;">Requirements should be proportionate and risk-based.</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; border-left: 5px solid #f44336;">
            <h4 style="color: #1e3a5f; margin: 0 0 10px 0; font-size: 1.2em;">Focusing Only on Tier-1 Suppliers</h4>
            <p style="margin: 0; line-height: 1.6;">Many risks exist deeper in the supply chain.</p>
        </div>
    </div>
</div>

<!-- Integration -->
<div style="background: #f8f9fa; padding: 40px; border-radius: 15px; margin: 50px 0;">
    <h2 style="color: #1e3a5f; margin-top: 0; margin-bottom: 25px; font-size: 2em;">
        ISO 20400 and other ISO standards
    </h2>

    <p style="font-size: 1.05em; line-height: 1.8; margin-bottom: 25px;">
        ISO 20400 integrates naturally with:
    </p>

    <div style="display: flex; flex-wrap: wrap; gap: 15px; margin: 25px 0;">
        <span style="background: white; color: #1e3a5f; padding: 15px 30px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1); font-size: 1.05em;">ISO 9001 – Quality Management</span>
        <span style="background: white; color: #1e3a5f; padding: 15px 30px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1); font-size: 1.05em;">ISO 14001 – Environmental Management</span>
        <span style="background: white; color: #1e3a5f; padding: 15px 30px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1); font-size: 1.05em;">ISO 45001 – Occupational Health & Safety</span>
        <span style="background: white; color: #1e3a5f; padding: 15px 30px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1); font-size: 1.05em;">ISO 37001 – Anti-Bribery Management</span>
    </div>

    <div style="background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%); padding: 25px; border-radius: 12px; margin-top: 25px; border-left: 5px solid #30b566;">
        <p style="margin: 0; font-size: 1.05em; line-height: 1.7;">
            Together, they form a strong framework for <strong>responsible, resilient supply chains</strong>.
        </p>
    </div>
</div>

<!-- Certification -->
<div style="background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%); padding: 40px; border-radius: 15px; margin: 50px 0; border-left: 5px solid #ff9800;">
    <h2 style="color: #1e3a5f; margin-top: 0; margin-bottom: 20px; font-size: 2em;">
        Can ISO 20400 be certified in the UK?
    </h2>

    <p style="margin: 0 0 15px 0; font-size: 1.05em; line-height: 1.8;">
        <strong>No.</strong> ISO 20400 is a guidance standard, not a certifiable one. However, many UK organisations:
    </p>

    <ul style="margin: 15px 0; padding-left: 30px; line-height: 1.8;">
        <li style="margin-bottom: 10px;">Use it to benchmark procurement maturity</li>
        <li style="margin-bottom: 10px;">Reference it in ESG and sustainability reporting</li>
        <li>Integrate its principles into certifiable ISO systems</li>
    </ul>

    <p style="margin: 15px 0 0 0; font-size: 1.05em; line-height: 1.8;">
        Its value lies in <strong>credibility, structure, and consistency</strong>, not certification badges.
    </p>
</div>

<!-- Who should NOT use -->
<div style="background: linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%); padding: 40px; border-radius: 15px; margin: 50px 0; border-left: 5px solid #f44336;">
    <h2 style="color: #1e3a5f; margin-top: 0; margin-bottom: 20px; font-size: 2em;">
        Who should NOT use ISO 20400?
    </h2>

    <p style="margin: 0; font-size: 1.05em; line-height: 1.8;">
        If procurement decisions are <strong>minimal, low-risk, or entirely outsourced with no oversight</strong>, ISO 20400 may offer limited value. It also requires leadership buy-in—without it, sustainable procurement initiatives rarely succeed.
    </p>
</div>

<!-- FAQs -->
<div style="background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%); padding: 45px; border-radius: 15px; margin: 50px 0; color: white;">
    <h2 style="color: white; margin-top: 0; margin-bottom: 30px; font-size: 2em; text-align: center;">
        Frequently Asked Questions (FAQs)
    </h2>

    <div style="display: grid; gap: 25px;">
        <div style="background: rgba(255,255,255,0.1); padding: 30px; border-radius: 12px; backdrop-filter: blur(10px);">
            <h4 style="color: white; margin: 0 0 12px 0; font-size: 1.3em;">Is ISO 20400 mandatory in the UK?</h4>
            <p style="margin: 0; opacity: 0.9; line-height: 1.7; font-size: 1.05em;">No. It is voluntary, but widely regarded as best practice.</p>
        </div>

        <div style="background: rgba(255,255,255,0.1); padding: 30px; border-radius: 12px; backdrop-filter: blur(10px);">
            <h4 style="color: white; margin: 0 0 12px 0; font-size: 1.3em;">Does ISO 20400 replace social value policies?</h4>
            <p style="margin: 0; opacity: 0.9; line-height: 1.7; font-size: 1.05em;">No. It provides the framework to implement them effectively.</p>
        </div>

        <div style="background: rgba(255,255,255,0.1); padding: 30px; border-radius: 12px; backdrop-filter: blur(10px);">
            <h4 style="color: white; margin: 0 0 12px 0; font-size: 1.3em;">Is ISO 20400 suitable for SMEs?</h4>
            <p style="margin: 0; opacity: 0.9; line-height: 1.7; font-size: 1.05em;">Yes. The guidance is scalable and proportionate.</p>
        </div>

        <div style="background: rgba(255,255,255,0.1); padding: 30px; border-radius: 12px; backdrop-filter: blur(10px);">
            <h4 style="color: white; margin: 0 0 12px 0; font-size: 1.3em;">Does ISO 20400 support ESG reporting?</h4>
            <p style="margin: 0; opacity: 0.9; line-height: 1.7; font-size: 1.05em;">Yes. It provides evidence-based structure behind ESG claims.</p>
        </div>
    </div>
</div>

<!-- Call to action -->
<div style="background: linear-gradient(135deg, #00897b 0%, #26a69a 100%); padding: 50px; border-radius: 15px; margin: 50px 0; text-align: center; color: white;">
    <h2 style="color: white; margin: 0 0 20px 0; font-size: 2.2em;">
        Ready to make procurement a force for good?
    </h2>
    <p style="font-size: 1.2em; line-height: 1.8; margin: 0 0 30px 0; opacity: 0.95;">
        Qualitation has been helping UK organisations implement sustainable procurement practices for over 25 years with a 100% first-time success rate.
    </p>
    <div style="display: flex; gap: 20px; justify-content: center; flex-wrap: wrap;">
        <a href="/contact/" style="background: white; color: #00897b; padding: 15px 40px; border-radius: 50px; text-decoration: none; font-weight: 700; font-size: 1.1em; display: inline-block; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
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

            self.stdout.write(self.style.SUCCESS(f'✓ Updated ISO 20400 page'))
            self.stdout.write(self.style.SUCCESS(f'✓ URL: /{page.get_url_parts()[2]}'))
            self.stdout.write(self.style.SUCCESS('✓ Published successfully'))

        except Page.DoesNotExist:
            self.stdout.write(self.style.ERROR('✗ ISO 20400 page not found'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ Error: {e}'))
            import traceback
            traceback.print_exc()

        self.stdout.write(self.style.SUCCESS('\n=== Complete ===\n'))
