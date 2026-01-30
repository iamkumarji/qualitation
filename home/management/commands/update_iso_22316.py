"""
Django management command to update ISO 22316 page with new content
"""

from django.core.management.base import BaseCommand
from wagtail.models import Page


class Command(BaseCommand):
    help = 'Update ISO 22316 page with new beautifully illustrated content'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('\n=== Updating ISO 22316 Page ===\n'))

        try:
            # Get the ISO 22316 page
            page = Page.objects.get(slug='iso-22316').specific

            self.stdout.write(f'Found page: {page.title}')

            # New content with beautiful illustrations
            content_html = '''
<style>
    main { padding-top: 0 !important; margin-top: 0 !important; }
</style>
<!-- Hero Section -->
<section style="background: linear-gradient(135deg, #ff6b6b 0%, #ee5a6f 100%); padding: 80px 40px; margin: 0; position: relative; overflow: hidden;">
    <div style="max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: 1fr 300px; gap: 60px; align-items: center;">
        <div>
            <h1 style="color: white; font-size: 3em; margin: 0 0 20px 0; font-weight: 700; line-height: 1.2;">
                ISO 22316 Certification UK
            </h1>
            <p style="color: white; font-size: 1.3em; margin: 0 0 30px 0; line-height: 1.6; opacity: 0.95;">
                Organisational Resilience Management. Build the capability to anticipate, adapt, and thrive through disruption.
            </p>

            <!-- Feature Tags -->
            <div style="display: flex; flex-wrap: wrap; gap: 12px; margin-bottom: 30px;">
                <span style="background: rgba(255,255,255,0.25); color: white; padding: 10px 20px; border-radius: 50px; font-weight: 600; backdrop-filter: blur(10px); display: flex; align-items: center; gap: 8px;">
                    <span style="font-size: 1.2em;">🛡️</span> Strategic Resilience
                </span>
                <span style="background: rgba(255,255,255,0.25); color: white; padding: 10px 20px; border-radius: 50px; font-weight: 600; backdrop-filter: blur(10px); display: flex; align-items: center; gap: 8px;">
                    <span style="font-size: 1.2em;">🎯</span> Leadership-Led
                </span>
                <span style="background: rgba(255,255,255,0.25); color: white; padding: 10px 20px; border-radius: 50px; font-weight: 600; backdrop-filter: blur(10px); display: flex; align-items: center; gap: 8px;">
                    <span style="font-size: 1.2em;">🔄</span> Adaptive Capacity
                </span>
            </div>

            <!-- CTA Buttons -->
            <div style="display: flex; gap: 15px; flex-wrap: wrap;">
                <a href="/contact/" style="background: white; color: #ff6b6b; padding: 15px 35px; border-radius: 50px; text-decoration: none; font-weight: 700; font-size: 1.1em; display: inline-flex; align-items: center; gap: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.2); transition: transform 0.2s;">
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
                    <div style="font-size: 5em; margin-bottom: 10px;">🛡️</div>
                    <div style="font-size: 2em; color: #ff6b6b; font-weight: 700;">22316</div>
                </div>
                <!-- Decorative elements -->
                <div style="position: absolute; top: 20px; left: -20px; width: 40px; height: 40px; background: #ff6b6b; border-radius: 50%;"></div>
                <div style="position: absolute; bottom: 40px; right: -15px; width: 30px; height: 30px; background: #ee5a6f; border-radius: 50%;"></div>
            </div>
        </div>
    </div>
</section>

<div style="max-width: 1200px; margin: 0 auto; padding: 40px 20px;" id="learn-more">

<div style="background: linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%); padding: 35px; border-radius: 15px; margin: 30px 0; border-left: 5px solid #ff6b6b;">
    <p style="font-size: 1.15em; line-height: 1.8; margin: 0; color: #1e3a5f;">
        In an increasingly volatile world—marked by cyber incidents, supply chain disruption, workforce instability, and economic uncertainty—UK organisations can no longer rely on traditional business continuity plans alone. <strong>Resilience today is about anticipation, adaptation, and long-term survival</strong>, not just recovery. ISO 22316 provides the strategic framework to embed resilience into the very fabric of how your organisation operates.
    </p>
</div>

<p style="font-size: 1.1em; line-height: 1.8; margin: 25px 0;">
    ISO 22316 is the international guidance standard for <strong>Organisational Resilience</strong>. It helps organisations strengthen their ability to absorb shocks, adapt to change, and continue to achieve objectives—no matter what disruption they face. Rather than focusing on single threats, ISO 22316 takes a whole-organisation view of resilience, spanning leadership, culture, governance, people, and strategy.
</p>

<!-- What is ISO 22316 -->
<div style="background: #f8f9fa; padding: 40px; border-radius: 15px; margin: 40px 0;">
    <h2 style="color: #1e3a5f; margin-top: 0; margin-bottom: 25px; font-size: 2em; display: flex; align-items: center;">
        <span style="background: linear-gradient(135deg, #ff6b6b 0%, #ee5a6f 100%); color: white; width: 50px; height: 50px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; margin-right: 15px; font-size: 1.2em;">🛡️</span>
        What is ISO 22316?
    </h2>

    <p style="font-size: 1.05em; line-height: 1.8; margin-bottom: 20px;">
        ISO 22316 is a guidance standard published by the International Organization for Standardization. It provides a structured framework to help organisations build, enhance, and review organisational resilience.
    </p>

    <p style="font-size: 1.1em; font-weight: 600; color: #1e3a5f; margin: 25px 0 15px 0;">
        In plain English, ISO 22316 helps you answer critical questions such as:
    </p>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-top: 25px;">
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); border-top: 4px solid #ff6b6b;">
            <div style="font-size: 2em; margin-bottom: 15px;">🔮</div>
            <strong style="color: #1e3a5f; font-size: 1.1em;">Anticipate Disruption</strong>
            <p style="margin: 10px 0 0 0; line-height: 1.6;">How well can we anticipate disruption?</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); border-top: 4px solid #ff6b6b;">
            <div style="font-size: 2em; margin-bottom: 15px;">👥</div>
            <strong style="color: #1e3a5f; font-size: 1.1em;">Prepared Leadership</strong>
            <p style="margin: 10px 0 0 0; line-height: 1.6;">Are our leaders and people equipped to respond to uncertainty?</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); border-top: 4px solid #ff6b6b;">
            <div style="font-size: 2em; margin-bottom: 15px;">🎯</div>
            <strong style="color: #1e3a5f; font-size: 1.1em;">Adapt Strategy</strong>
            <p style="margin: 10px 0 0 0; line-height: 1.6;">Can we adapt our strategy under pressure?</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); border-top: 4px solid #ff6b6b;">
            <div style="font-size: 2em; margin-bottom: 15px;">⚙️</div>
            <strong style="color: #1e3a5f; font-size: 1.1em;">Continue Functioning</strong>
            <p style="margin: 10px 0 0 0; line-height: 1.6;">Will our organisation still function if key assumptions fail?</p>
        </div>
    </div>

    <div style="background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%); padding: 25px; border-radius: 12px; margin-top: 30px; border-left: 5px solid #ff9800;">
        <p style="margin: 0; font-size: 1.05em; line-height: 1.7;">
            <strong>Unlike ISO 22301 (Business Continuity)</strong>, ISO 22316 is strategic rather than procedural. It does not prescribe plans or checklists; instead, it focuses on building the capabilities and behaviours that make organisations resilient over the long term.
        </p>
    </div>
</div>

<!-- Why ISO 22316 was created -->
<h2 style="color: #1e3a5f; margin-top: 50px; margin-bottom: 20px; font-size: 2em;">
    Why ISO 22316 was created
</h2>

<div style="background: linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%); padding: 35px; border-radius: 15px; margin: 30px 0; border-left: 5px solid #f44336;">
    <p style="font-size: 1.05em; line-height: 1.8; margin: 0 0 15px 0;">
        Many organisations discovered during major crises—such as COVID-19, cyber-attacks, or global supply chain failures—that <strong>having documented plans was not enough</strong>. Plans failed because leadership, culture, decision-making, and communication were not resilient.
    </p>
    <p style="font-size: 1.05em; line-height: 1.8; margin: 0;">
        ISO 22316 was created to address this gap. It shifts resilience from a siloed compliance activity into a <strong>leadership-led management discipline</strong>. The standard recognises that resilience emerges from how an organisation is governed, how it learns, and how it adapts—not just how it recovers.
    </p>
</div>

<!-- Why ISO 22316 matters for UK organisations -->
<div style="background: #e3f2fd; padding: 40px; border-radius: 15px; margin: 40px 0;">
    <h2 style="color: #1e3a5f; margin-top: 0; margin-bottom: 25px; font-size: 2em; display: flex; align-items: center;">
        <span style="background: linear-gradient(135deg, #2196f3 0%, #64b5f6 100%); color: white; width: 50px; height: 50px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; margin-right: 15px; font-size: 1.2em;">🇬🇧</span>
        Why ISO 22316 matters for UK organisations
    </h2>

    <p style="font-size: 1.05em; line-height: 1.8; margin-bottom: 20px;">
        UK organisations operate in an environment of:
    </p>

    <div style="display: flex; flex-wrap: wrap; gap: 15px; margin: 25px 0;">
        <span style="background: white; color: #1e3a5f; padding: 12px 24px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">Economic uncertainty and inflationary pressure</span>
        <span style="background: white; color: #1e3a5f; padding: 12px 24px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">Increasing cyber and data risks</span>
        <span style="background: white; color: #1e3a5f; padding: 12px 24px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">Workforce shortages and skills gaps</span>
        <span style="background: white; color: #1e3a5f; padding: 12px 24px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">Regulatory change and political uncertainty</span>
        <span style="background: white; color: #1e3a5f; padding: 12px 24px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">Complex, globalised supply chains</span>
    </div>

    <div style="background: white; padding: 30px; border-radius: 12px; margin-top: 25px; box-shadow: 0 4px 12px rgba(0,0,0,0.08);">
        <p style="margin: 0; font-size: 1.1em; line-height: 1.8; color: #1e3a5f;">
            <strong>ISO 22316 provides a credible framework</strong> for demonstrating that resilience is being actively managed at board level. It is particularly valuable for organisations subject to regulatory scrutiny, public accountability, or critical service delivery expectations.
        </p>
    </div>
</div>

<!-- Who ISO 22316 is for -->
<h2 style="color: #1e3a5f; margin-top: 50px; margin-bottom: 20px; font-size: 2em;">
    Who ISO 22316 is for
</h2>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 25px; margin: 30px 0;">
    <div style="background: linear-gradient(135deg, #e8eaf6 0%, #c5cae9 100%); padding: 30px; border-radius: 12px; border-left: 5px solid #3f51b5;">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 15px; font-size: 1.3em;">🏛️ Public Sector & Local Authorities</h3>
        <p style="margin: 0; line-height: 1.7;">Maintaining essential services under pressure</p>
    </div>
    <div style="background: linear-gradient(135deg, #fce4ec 0%, #f8bbd0 100%); padding: 30px; border-radius: 12px; border-left: 5px solid #e91e63;">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 15px; font-size: 1.3em;">⚡ Critical Infrastructure & Utilities</h3>
        <p style="margin: 0; line-height: 1.7;">Managing systemic and cascading risks</p>
    </div>
    <div style="background: linear-gradient(135deg, #e0f2f1 0%, #b2dfdb 100%); padding: 30px; border-radius: 12px; border-left: 5px solid #009688;">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 15px; font-size: 1.3em;">💼 Financial & Professional Services</h3>
        <p style="margin: 0; line-height: 1.7;">Meeting governance and risk expectations</p>
    </div>
    <div style="background: linear-gradient(135deg, #fff9c4 0%, #fff59d 100%); padding: 30px; border-radius: 12px; border-left: 5px solid #fbc02d;">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 15px; font-size: 1.3em;">🏥 Healthcare & Education</h3>
        <p style="margin: 0; line-height: 1.7;">Sustaining operations during prolonged disruption</p>
    </div>
    <div style="background: linear-gradient(135deg, #f3e5f5 0%, #e1bee7 100%); padding: 30px; border-radius: 12px; border-left: 5px solid #9c27b0;">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 15px; font-size: 1.3em;">🚀 Growing SMEs</h3>
        <p style="margin: 0; line-height: 1.7;">Building resilience early to support sustainable growth</p>
    </div>
</div>

<!-- Key principles -->
<div style="background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%); padding: 45px; border-radius: 15px; margin: 50px 0; color: white;">
    <h2 style="color: white; margin-top: 0; margin-bottom: 30px; font-size: 2em; text-align: center;">
        Key Principles of ISO 22316
    </h2>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 25px;">
        <div style="background: rgba(255,255,255,0.1); padding: 25px; border-radius: 12px; backdrop-filter: blur(10px);">
            <div style="font-size: 2.5em; margin-bottom: 15px;">👔</div>
            <h3 style="color: white; margin: 0 0 10px 0; font-size: 1.2em;">Leadership & Culture</h3>
            <p style="margin: 0; opacity: 0.9; line-height: 1.6;">Resilience starts with leadership behaviours, decision-making, and organisational values</p>
        </div>
        <div style="background: rgba(255,255,255,0.1); padding: 25px; border-radius: 12px; backdrop-filter: blur(10px);">
            <div style="font-size: 2.5em; margin-bottom: 15px;">🎯</div>
            <h3 style="color: white; margin: 0 0 10px 0; font-size: 1.2em;">Shared Purpose</h3>
            <p style="margin: 0; opacity: 0.9; line-height: 1.6;">A clear mission and objectives help organisations stay focused during disruption</p>
        </div>
        <div style="background: rgba(255,255,255,0.1); padding: 25px; border-radius: 12px; backdrop-filter: blur(10px);">
            <div style="font-size: 2.5em; margin-bottom: 15px;">👁️</div>
            <h3 style="color: white; margin: 0 0 10px 0; font-size: 1.2em;">Situational Awareness</h3>
            <p style="margin: 0; opacity: 0.9; line-height: 1.6;">Understanding internal and external risks, trends, and weak signals</p>
        </div>
        <div style="background: rgba(255,255,255,0.1); padding: 25px; border-radius: 12px; backdrop-filter: blur(10px);">
            <div style="font-size: 2.5em; margin-bottom: 15px;">⚖️</div>
            <h3 style="color: white; margin: 0 0 10px 0; font-size: 1.2em;">Effective Governance</h3>
            <p style="margin: 0; opacity: 0.9; line-height: 1.6;">Clear accountability, risk ownership, and oversight at senior levels</p>
        </div>
        <div style="background: rgba(255,255,255,0.1); padding: 25px; border-radius: 12px; backdrop-filter: blur(10px);">
            <div style="font-size: 2.5em; margin-bottom: 15px;">🔄</div>
            <h3 style="color: white; margin: 0 0 10px 0; font-size: 1.2em;">Adaptive Capacity</h3>
            <p style="margin: 0; opacity: 0.9; line-height: 1.6;">The ability to change structures, strategies, and priorities quickly</p>
        </div>
        <div style="background: rgba(255,255,255,0.1); padding: 25px; border-radius: 12px; backdrop-filter: blur(10px);">
            <div style="font-size: 2.5em; margin-bottom: 15px;">📚</div>
            <h3 style="color: white; margin: 0 0 10px 0; font-size: 1.2em;">Continuous Learning</h3>
            <p style="margin: 0; opacity: 0.9; line-height: 1.6;">Learning from incidents, near-misses, and change</p>
        </div>
    </div>
</div>

<!-- Benefits section -->
<h2 style="color: #1e3a5f; margin-top: 50px; margin-bottom: 30px; font-size: 2em; text-align: center;">
    Benefits of ISO 22316
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
                Stronger leadership decision-making under pressure
            </li>
            <li style="margin-bottom: 15px; padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #30b566; font-size: 1.3em;">✓</span>
                Improved cross-functional collaboration
            </li>
            <li style="margin-bottom: 15px; padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #30b566; font-size: 1.3em;">✓</span>
                Enhanced staff confidence and engagement
            </li>
            <li style="padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #30b566; font-size: 1.3em;">✓</span>
                Reduced impact of disruption
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
                Greater long-term stability and sustainability
            </li>
            <li style="margin-bottom: 15px; padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #2196f3; font-size: 1.3em;">✓</span>
                Improved board-level governance and assurance
            </li>
            <li style="margin-bottom: 15px; padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #2196f3; font-size: 1.3em;">✓</span>
                Stronger reputation with stakeholders and regulators
            </li>
            <li style="padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #2196f3; font-size: 1.3em;">✓</span>
                Better alignment between risk, strategy, and performance
            </li>
        </ul>
    </div>

    <!-- Risk & Compliance Benefits -->
    <div style="background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%); padding: 35px; border-radius: 15px; box-shadow: 0 6px 20px rgba(0,0,0,0.1);">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 20px; font-size: 1.5em; display: flex; align-items: center;">
            <span style="font-size: 1.5em; margin-right: 10px;">📋</span> Risk & Compliance
        </h3>
        <ul style="list-style: none; padding: 0; margin: 0;">
            <li style="margin-bottom: 15px; padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #ff9800; font-size: 1.3em;">✓</span>
                Complements ISO 22301, ISO 27001, and ISO 9001
            </li>
            <li style="margin-bottom: 15px; padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #ff9800; font-size: 1.3em;">✓</span>
                Supports regulatory expectations around operational resilience
            </li>
            <li style="padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #ff9800; font-size: 1.3em;">✓</span>
                Provides evidence of proactive risk management
            </li>
        </ul>
    </div>
</div>

<!-- What assessors look for -->
<div style="background: #f8f9fa; padding: 40px; border-radius: 15px; margin: 50px 0;">
    <h2 style="color: #1e3a5f; margin-top: 0; margin-bottom: 25px; font-size: 2em;">
        What assessors look for when using ISO 22316
    </h2>

    <div style="background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%); padding: 25px; border-radius: 12px; margin-bottom: 25px; border-left: 5px solid #ff9800;">
        <p style="margin: 0; font-size: 1.05em; line-height: 1.7;">
            <strong>While ISO 22316 is not a certifiable standard on its own</strong>, it is often used as a benchmark for maturity assessments or integrated into existing management systems.
        </p>
    </div>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-top: 25px;">
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
            <h4 style="color: #1e3a5f; margin-top: 0; margin-bottom: 12px;">👔 Leadership Commitment</h4>
            <p style="margin: 0; line-height: 1.6;">Evidence of leadership commitment to resilience</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
            <h4 style="color: #1e3a5f; margin-top: 0; margin-bottom: 12px;">🎯 Clear Purpose</h4>
            <p style="margin: 0; line-height: 1.6;">Clear understanding of organisational purpose and priorities</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
            <h4 style="color: #1e3a5f; margin-top: 0; margin-bottom: 12px;">📊 Risk Monitoring</h4>
            <p style="margin: 0; line-height: 1.6;">Mechanisms for monitoring emerging risks</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
            <h4 style="color: #1e3a5f; margin-top: 0; margin-bottom: 12px;">🔗 Integration</h4>
            <p style="margin: 0; line-height: 1.6;">Integration of resilience into strategy and governance</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
            <h4 style="color: #1e3a5f; margin-top: 0; margin-bottom: 12px;">📚 Learning Evidence</h4>
            <p style="margin: 0; line-height: 1.6;">Evidence of learning and adaptation</p>
        </div>
    </div>

    <div style="background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%); padding: 25px; border-radius: 12px; margin-top: 25px; border-left: 5px solid #30b566;">
        <p style="margin: 0; font-size: 1.05em; line-height: 1.7;">
            The focus is always on <strong>capability and behaviour</strong>, not documentation alone.
        </p>
    </div>
</div>

<!-- Real-world examples -->
<h2 style="color: #1e3a5f; margin-top: 50px; margin-bottom: 30px; font-size: 2em;">
    ISO 22316 in practice (real-world examples)
</h2>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 30px; margin: 30px 0;">
    <div style="background: linear-gradient(135deg, #e8eaf6 0%, #c5cae9 100%); padding: 35px; border-radius: 15px; box-shadow: 0 6px 20px rgba(0,0,0,0.1);">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 20px; font-size: 1.4em;">
            🏛️ Public Sector Organisation
        </h3>
        <p style="margin: 0; line-height: 1.7; font-size: 1.05em;">
            A UK public body uses ISO 22316 to strengthen its response to prolonged service disruption. Leadership workshops, governance reviews, and scenario planning improve decision-making during crises.
        </p>
    </div>

    <div style="background: linear-gradient(135deg, #fce4ec 0%, #f8bbd0 100%); padding: 35px; border-radius: 15px; box-shadow: 0 6px 20px rgba(0,0,0,0.1);">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 20px; font-size: 1.4em;">
            💼 Financial Services Firm
        </h3>
        <p style="margin: 0; line-height: 1.7; font-size: 1.05em;">
            A regulated firm applies ISO 22316 alongside ISO 22301 to demonstrate operational resilience to regulators—linking business continuity, cyber security, and strategic risk into one coherent framework.
        </p>
    </div>
</div>

<!-- Common mistakes -->
<div style="background: linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%); padding: 40px; border-radius: 15px; margin: 50px 0;">
    <h2 style="color: #1e3a5f; margin-top: 0; margin-bottom: 25px; font-size: 2em;">
        ⚠️ Common mistakes when applying ISO 22316
    </h2>

    <div style="display: grid; gap: 20px;">
        <div style="background: white; padding: 25px; border-radius: 12px; border-left: 5px solid #f44336;">
            <h4 style="color: #1e3a5f; margin: 0 0 10px 0; font-size: 1.2em;">Confusing Resilience with Business Continuity</h4>
            <p style="margin: 0; line-height: 1.6;">Resilience is broader—it includes culture, leadership, and adaptability.</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; border-left: 5px solid #f44336;">
            <h4 style="color: #1e3a5f; margin: 0 0 10px 0; font-size: 1.2em;">Limiting Ownership to Risk Teams</h4>
            <p style="margin: 0; line-height: 1.6;">True resilience must be owned by senior leadership and embedded across the organisation.</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; border-left: 5px solid #f44336;">
            <h4 style="color: #1e3a5f; margin: 0 0 10px 0; font-size: 1.2em;">Overcomplicating the Framework</h4>
            <p style="margin: 0; line-height: 1.6;">ISO 22316 is principles-based and should be applied proportionately.</p>
        </div>
    </div>
</div>

<!-- Integration -->
<div style="background: #f8f9fa; padding: 40px; border-radius: 15px; margin: 50px 0;">
    <h2 style="color: #1e3a5f; margin-top: 0; margin-bottom: 25px; font-size: 2em;">
        ISO 22316 and other ISO standards
    </h2>

    <p style="font-size: 1.05em; line-height: 1.8; margin-bottom: 25px;">
        ISO 22316 integrates naturally with:
    </p>

    <div style="display: flex; flex-wrap: wrap; gap: 15px; margin: 25px 0;">
        <span style="background: white; color: #1e3a5f; padding: 15px 30px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1); font-size: 1.05em;">ISO 22301 – Business Continuity</span>
        <span style="background: white; color: #1e3a5f; padding: 15px 30px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1); font-size: 1.05em;">ISO 27001 – Information Security</span>
        <span style="background: white; color: #1e3a5f; padding: 15px 30px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1); font-size: 1.05em;">ISO 9001 – Quality Management</span>
        <span style="background: white; color: #1e3a5f; padding: 15px 30px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1); font-size: 1.05em;">ISO 14001 – Environmental Management</span>
    </div>

    <div style="background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%); padding: 25px; border-radius: 12px; margin-top: 25px; border-left: 5px solid #30b566;">
        <p style="margin: 0; font-size: 1.05em; line-height: 1.7;">
            Together, these standards form a strong foundation for an <strong>Integrated Management System (IMS)</strong> that supports both compliance and resilience.
        </p>
    </div>
</div>

<!-- Certification -->
<div style="background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%); padding: 40px; border-radius: 15px; margin: 50px 0; border-left: 5px solid #ff9800;">
    <h2 style="color: #1e3a5f; margin-top: 0; margin-bottom: 20px; font-size: 2em;">
        Can ISO 22316 be certified in the UK?
    </h2>

    <p style="margin: 0 0 15px 0; font-size: 1.05em; line-height: 1.8;">
        ISO 22316 itself is a <strong>guidance standard</strong>, not a certifiable one. However, many UK organisations:
    </p>

    <ul style="margin: 15px 0; padding-left: 30px; line-height: 1.8;">
        <li style="margin-bottom: 10px;">Use it to assess and improve resilience maturity</li>
        <li style="margin-bottom: 10px;">Integrate its principles into ISO 22301 or ISO 9001 systems</li>
        <li>Use it as evidence of good governance and leadership</li>
    </ul>

    <p style="margin: 15px 0 0 0; font-size: 1.05em; line-height: 1.8;">
        Certification bodies and regulators increasingly recognise ISO 22316 as <strong>best practice for organisational resilience</strong>.
    </p>
</div>

<!-- Who should NOT use -->
<div style="background: linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%); padding: 40px; border-radius: 15px; margin: 50px 0; border-left: 5px solid #f44336;">
    <h2 style="color: #1e3a5f; margin-top: 0; margin-bottom: 20px; font-size: 2em;">
        Who should NOT use ISO 22316?
    </h2>

    <p style="margin: 0; font-size: 1.05em; line-height: 1.8;">
        If an organisation is only seeking a <strong>quick certificate or checklist solution</strong>, ISO 22316 may not meet expectations. The standard requires reflection, leadership engagement, and cultural change—not just documentation.
    </p>
</div>

<!-- FAQs -->
<div style="background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%); padding: 45px; border-radius: 15px; margin: 50px 0; color: white;">
    <h2 style="color: white; margin-top: 0; margin-bottom: 30px; font-size: 2em; text-align: center;">
        Frequently Asked Questions (FAQs)
    </h2>

    <div style="display: grid; gap: 25px;">
        <div style="background: rgba(255,255,255,0.1); padding: 30px; border-radius: 12px; backdrop-filter: blur(10px);">
            <h4 style="color: white; margin: 0 0 12px 0; font-size: 1.3em;">Is ISO 22316 mandatory in the UK?</h4>
            <p style="margin: 0; opacity: 0.9; line-height: 1.7; font-size: 1.05em;">No. It is voluntary, but widely regarded as best practice for organisational resilience.</p>
        </div>

        <div style="background: rgba(255,255,255,0.1); padding: 30px; border-radius: 12px; backdrop-filter: blur(10px);">
            <h4 style="color: white; margin: 0 0 12px 0; font-size: 1.3em;">Is ISO 22316 the same as ISO 22301?</h4>
            <p style="margin: 0; opacity: 0.9; line-height: 1.7; font-size: 1.05em;">No. ISO 22301 focuses on business continuity plans. ISO 22316 focuses on strategic resilience capabilities.</p>
        </div>

        <div style="background: rgba(255,255,255,0.1); padding: 30px; border-radius: 12px; backdrop-filter: blur(10px);">
            <h4 style="color: white; margin: 0 0 12px 0; font-size: 1.3em;">Can SMEs use ISO 22316?</h4>
            <p style="margin: 0; opacity: 0.9; line-height: 1.7; font-size: 1.05em;">Yes. The principles are scalable and highly relevant to growing organisations.</p>
        </div>

        <div style="background: rgba(255,255,255,0.1); padding: 30px; border-radius: 12px; backdrop-filter: blur(10px);">
            <h4 style="color: white; margin: 0 0 12px 0; font-size: 1.3em;">Does ISO 22316 help with regulators?</h4>
            <p style="margin: 0; opacity: 0.9; line-height: 1.7; font-size: 1.05em;">Yes. It supports governance, risk management, and operational resilience expectations.</p>
        </div>
    </div>
</div>

<!-- Call to action -->
<div style="background: linear-gradient(135deg, #ff6b6b 0%, #ee5a6f 100%); padding: 50px; border-radius: 15px; margin: 50px 0; text-align: center; color: white;">
    <h2 style="color: white; margin: 0 0 20px 0; font-size: 2.2em;">
        Ready to build genuine organisational resilience?
    </h2>
    <p style="font-size: 1.2em; line-height: 1.8; margin: 0 0 30px 0; opacity: 0.95;">
        Qualitation has been helping UK organisations strengthen resilience and achieve ISO certification for over 25 years with a 100% first-time success rate.
    </p>
    <div style="display: flex; gap: 20px; justify-content: center; flex-wrap: wrap;">
        <a href="/contact/" style="background: white; color: #ff6b6b; padding: 15px 40px; border-radius: 50px; text-decoration: none; font-weight: 700; font-size: 1.1em; display: inline-block; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
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

            self.stdout.write(self.style.SUCCESS(f'✓ Updated ISO 22316 page'))
            self.stdout.write(self.style.SUCCESS(f'✓ URL: /{page.get_url_parts()[2]}'))
            self.stdout.write(self.style.SUCCESS('✓ Published successfully'))

        except Page.DoesNotExist:
            self.stdout.write(self.style.ERROR('✗ ISO 22316 page not found'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ Error: {e}'))
            import traceback
            traceback.print_exc()

        self.stdout.write(self.style.SUCCESS('\n=== Complete ===\n'))
