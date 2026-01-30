"""
Django management command to update ISO 39001 page with new content
"""

from django.core.management.base import BaseCommand
from wagtail.models import Page


class Command(BaseCommand):
    help = 'Update ISO 39001 page with new beautifully illustrated content'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('\n=== Updating ISO 39001 Page ===\n'))

        try:
            # Get the ISO 39001 page
            page = Page.objects.get(slug='iso-39001').specific

            self.stdout.write(f'Found page: {page.title}')

            # New content with beautiful illustrations
            content_html = '''
<style>
    main { padding-top: 0 !important; margin-top: 0 !important; }
</style>
<!-- Hero Section -->
<section style="background: linear-gradient(135deg, #ff9800 0%, #f57c00 100%); padding: 80px 40px; margin: 0; position: relative; overflow: hidden;">
    <div style="max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: 1fr 300px; gap: 60px; align-items: center;">
        <div>
            <h1 style="color: white; font-size: 3em; margin: 0 0 20px 0; font-weight: 700; line-height: 1.2;">
                ISO 39001 Certification UK
            </h1>
            <p style="color: white; font-size: 1.3em; margin: 0 0 30px 0; line-height: 1.6; opacity: 0.95;">
                Road Traffic Safety Management System. Protect lives, reduce crashes, and demonstrate systematic commitment to safe driving operations.
            </p>

            <!-- Feature Tags -->
            <div style="display: flex; flex-wrap: wrap; gap: 12px; margin-bottom: 30px;">
                <span style="background: rgba(255,255,255,0.25); color: white; padding: 10px 20px; border-radius: 50px; font-weight: 600; backdrop-filter: blur(10px); display: flex; align-items: center; gap: 8px;">
                    <span style="font-size: 1.2em;">🚗</span> Fleet Safety
                </span>
                <span style="background: rgba(255,255,255,0.25); color: white; padding: 10px 20px; border-radius: 50px; font-weight: 600; backdrop-filter: blur(10px); display: flex; align-items: center; gap: 8px;">
                    <span style="font-size: 1.2em;">✓</span> Safe System
                </span>
                <span style="background: rgba(255,255,255,0.25); color: white; padding: 10px 20px; border-radius: 50px; font-weight: 600; backdrop-filter: blur(10px); display: flex; align-items: center; gap: 8px;">
                    <span style="font-size: 1.2em;">🛡️</span> Duty of Care
                </span>
            </div>

            <!-- CTA Buttons -->
            <div style="display: flex; gap: 15px; flex-wrap: wrap;">
                <a href="/contact/" style="background: white; color: #ff9800; padding: 15px 35px; border-radius: 50px; text-decoration: none; font-weight: 700; font-size: 1.1em; display: inline-flex; align-items: center; gap: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.2); transition: transform 0.2s;">
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
                    <div style="font-size: 5em; margin-bottom: 10px;">🚗</div>
                    <div style="font-size: 2em; color: #ff9800; font-weight: 700;">39001</div>
                </div>
                <!-- Decorative elements -->
                <div style="position: absolute; top: 20px; left: -20px; width: 40px; height: 40px; background: #ff9800; border-radius: 50%;"></div>
                <div style="position: absolute; bottom: 40px; right: -15px; width: 30px; height: 30px; background: #f57c00; border-radius: 50%;"></div>
            </div>
        </div>
    </div>
</section>

<div style="max-width: 1200px; margin: 0 auto; padding: 40px 20px;" id="learn-more">

<div style="background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%); padding: 35px; border-radius: 15px; margin: 30px 0; border-left: 5px solid #ff9800;">
    <p style="font-size: 1.15em; line-height: 1.8; margin: 0; color: #1e3a5f;">
        Road traffic accidents remain one of the leading causes of serious injury and death worldwide—and the UK is no exception. For organisations that operate vehicles, manage fleets, employ drivers, or influence road use in any way, <strong>road safety is not just a moral responsibility; it is a critical business risk</strong>. ISO 39001 provides the internationally recognised framework to manage that risk systematically and effectively.
    </p>
</div>

<p style="font-size: 1.1em; line-height: 1.8; margin: 25px 0;">
    ISO 39001 is the global standard for a <strong>Road Traffic Safety (RTS) Management System</strong>. It enables organisations to reduce deaths and serious injuries related to road traffic crashes by embedding safety into leadership, operations, and culture. Rather than relying on driver training alone, ISO 39001 treats road safety as a managed organisational process.
</p>

<!-- What is ISO 39001 -->
<div style="background: #f8f9fa; padding: 40px; border-radius: 15px; margin: 40px 0;">
    <h2 style="color: #1e3a5f; margin-top: 0; margin-bottom: 25px; font-size: 2em; display: flex; align-items: center;">
        <span style="background: linear-gradient(135deg, #ff9800 0%, #f57c00 100%); color: white; width: 50px; height: 50px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; margin-right: 15px; font-size: 1.2em;">🚗</span>
        What is ISO 39001?
    </h2>

    <p style="font-size: 1.05em; line-height: 1.8; margin-bottom: 20px;">
        ISO 39001 is a voluntary international standard published by the International Organization for Standardization. It specifies the requirements for establishing, implementing, maintaining, and continually improving a Road Traffic Safety Management System.
    </p>

    <p style="font-size: 1.1em; font-weight: 600; color: #1e3a5f; margin: 25px 0 15px 0;">
        In simple terms, ISO 39001 helps organisations:
    </p>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-top: 25px;">
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); border-top: 4px solid #ff9800;">
            <div style="font-size: 2em; margin-bottom: 15px;">🎯</div>
            <strong style="color: #1e3a5f; font-size: 1.1em;">Identify Impact</strong>
            <p style="margin: 10px 0 0 0; line-height: 1.6;">Identify how their activities affect road traffic safety</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); border-top: 4px solid #ff9800;">
            <div style="font-size: 2em; margin-bottom: 15px;">📉</div>
            <strong style="color: #1e3a5f; font-size: 1.1em;">Reduce Crashes</strong>
            <p style="margin: 10px 0 0 0; line-height: 1.6;">Reduce the likelihood and severity of road traffic crashes</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); border-top: 4px solid #ff9800;">
            <div style="font-size: 2em; margin-bottom: 15px;">🛡️</div>
            <strong style="color: #1e3a5f; font-size: 1.1em;">Protect People</strong>
            <p style="margin: 10px 0 0 0; line-height: 1.6;">Protect employees, contractors, and the public</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); border-top: 4px solid #ff9800;">
            <div style="font-size: 2em; margin-bottom: 15px;">✓</div>
            <strong style="color: #1e3a5f; font-size: 1.1em;">Demonstrate Commitment</strong>
            <p style="margin: 10px 0 0 0; line-height: 1.6;">Demonstrate a structured commitment to safe driving and transport operations</p>
        </div>
    </div>

    <div style="background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%); padding: 25px; border-radius: 12px; margin-top: 30px; border-left: 5px solid #30b566;">
        <p style="margin: 0; font-size: 1.05em; line-height: 1.7;">
            The standard applies to <strong>any organisation that interacts with the road traffic system</strong>, not just transport or logistics companies.
        </p>
    </div>
</div>

<!-- Why ISO 39001 was created -->
<h2 style="color: #1e3a5f; margin-top: 50px; margin-bottom: 20px; font-size: 2em;">
    Why ISO 39001 was created
</h2>

<div style="background: linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%); padding: 35px; border-radius: 15px; margin: 30px 0; border-left: 5px solid #f44336;">
    <p style="font-size: 1.05em; line-height: 1.8; margin: 0 0 15px 0;">
        Historically, road safety was treated as an individual responsibility—blaming drivers after incidents occurred. This approach ignored systemic issues such as vehicle maintenance, scheduling pressures, route planning, and organisational culture.
    </p>
    <p style="font-size: 1.05em; line-height: 1.8; margin: 0;">
        ISO 39001 was developed to shift road safety from a reactive, blame-based model to a <strong>preventive, systems-based approach</strong>. It recognises that organisations significantly influence road risk through their policies, decisions, and operational controls.
    </p>
</div>

<div style="background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%); padding: 30px; border-radius: 12px; margin: 30px 0; border-left: 5px solid #2196f3;">
    <p style="margin: 0; font-size: 1.05em; line-height: 1.7;">
        The standard aligns with the <strong>Safe System approach</strong> to road safety, aiming to eliminate deaths and serious injuries rather than simply reduce accident statistics.
    </p>
</div>

<!-- Why ISO 39001 matters for UK organisations -->
<div style="background: #e3f2fd; padding: 40px; border-radius: 15px; margin: 40px 0;">
    <h2 style="color: #1e3a5f; margin-top: 0; margin-bottom: 25px; font-size: 2em; display: flex; align-items: center;">
        <span style="background: linear-gradient(135deg, #2196f3 0%, #64b5f6 100%); color: white; width: 50px; height: 50px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; margin-right: 15px; font-size: 1.2em;">🇬🇧</span>
        Why ISO 39001 matters for UK organisations
    </h2>

    <p style="font-size: 1.05em; line-height: 1.8; margin-bottom: 20px;">
        In the UK, work-related road incidents are a major cause of fatalities and serious injuries. Under UK health and safety law, employers have a <strong>duty of care</strong> for employees driving on work-related journeys—including grey fleet and company car drivers.
    </p>

    <p style="font-size: 1.05em; line-height: 1.8; margin-bottom: 20px;">
        ISO 39001 helps organisations demonstrate that they are taking reasonable and proportionate steps to manage road risk. It also supports:
    </p>

    <div style="display: flex; flex-wrap: wrap; gap: 15px; margin: 25px 0;">
        <span style="background: white; color: #1e3a5f; padding: 12px 24px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">Compliance with Health and Safety at Work Act</span>
        <span style="background: white; color: #1e3a5f; padding: 12px 24px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">Reduced insurance claims and premiums</span>
        <span style="background: white; color: #1e3a5f; padding: 12px 24px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">Improved driver wellbeing and morale</span>
        <span style="background: white; color: #1e3a5f; padding: 12px 24px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">Stronger corporate social responsibility (CSR)</span>
    </div>

    <div style="background: white; padding: 30px; border-radius: 12px; margin-top: 25px; box-shadow: 0 4px 12px rgba(0,0,0,0.08);">
        <p style="margin: 0; font-size: 1.1em; line-height: 1.8; color: #1e3a5f;">
            For public sector bodies and large contractors, <strong>ISO 39001 increasingly supports procurement and safety assurance expectations</strong>.
        </p>
    </div>
</div>

<!-- Who ISO 39001 is for -->
<h2 style="color: #1e3a5f; margin-top: 50px; margin-bottom: 20px; font-size: 2em;">
    Who ISO 39001 is for
</h2>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 25px; margin: 30px 0;">
    <div style="background: linear-gradient(135deg, #e8eaf6 0%, #c5cae9 100%); padding: 30px; border-radius: 12px; border-left: 5px solid #3f51b5;">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 15px; font-size: 1.3em;">🚚 Logistics & Transport</h3>
        <p style="margin: 0; line-height: 1.7;">Fleet operations and HGV safety</p>
    </div>
    <div style="background: linear-gradient(135deg, #fce4ec 0%, #f8bbd0 100%); padding: 30px; border-radius: 12px; border-left: 5px solid #e91e63;">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 15px; font-size: 1.3em;">🏗️ Construction & Utilities</h3>
        <p style="margin: 0; line-height: 1.7;">Site vehicles and contractor driving</p>
    </div>
    <div style="background: linear-gradient(135deg, #e0f2f1 0%, #b2dfdb 100%); padding: 30px; border-radius: 12px; border-left: 5px solid #009688;">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 15px; font-size: 1.3em;">🏛️ Public Sector & Authorities</h3>
        <p style="margin: 0; line-height: 1.7;">Transport planning and service delivery</p>
    </div>
    <div style="background: linear-gradient(135deg, #fff9c4 0%, #fff59d 100%); padding: 30px; border-radius: 12px; border-left: 5px solid #fbc02d;">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 15px; font-size: 1.3em;">💼 Sales & Service</h3>
        <p style="margin: 0; line-height: 1.7;">Company cars and grey fleet drivers</p>
    </div>
    <div style="background: linear-gradient(135deg, #f3e5f5 0%, #e1bee7 100%); padding: 30px; border-radius: 12px; border-left: 5px solid #9c27b0;">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 15px; font-size: 1.3em;">🚕 Taxi, Bus & Coach</h3>
        <p style="margin: 0; line-height: 1.7;">Passenger safety and service reliability</p>
    </div>
</div>

<div style="background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%); padding: 25px; border-radius: 12px; margin: 30px 0; border-left: 5px solid #ff9800;">
    <p style="margin: 0; font-size: 1.05em; line-height: 1.7;">
        <strong>Even organisations without owned vehicles</strong> can benefit if staff drive for work purposes.
    </p>
</div>

<!-- Key principles -->
<div style="background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%); padding: 45px; border-radius: 15px; margin: 50px 0; color: white;">
    <h2 style="color: white; margin-top: 0; margin-bottom: 30px; font-size: 2em; text-align: center;">
        Key Principles of ISO 39001
    </h2>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 25px;">
        <div style="background: rgba(255,255,255,0.1); padding: 25px; border-radius: 12px; backdrop-filter: blur(10px);">
            <div style="font-size: 2.5em; margin-bottom: 15px;">🛣️</div>
            <h3 style="color: white; margin: 0 0 10px 0; font-size: 1.2em;">Safe Road Use</h3>
            <p style="margin: 0; opacity: 0.9; line-height: 1.6;">Managing speed, journey planning, and driver behaviour</p>
        </div>
        <div style="background: rgba(255,255,255,0.1); padding: 25px; border-radius: 12px; backdrop-filter: blur(10px);">
            <div style="font-size: 2.5em; margin-bottom: 15px;">🚗</div>
            <h3 style="color: white; margin: 0 0 10px 0; font-size: 1.2em;">Safe Vehicles</h3>
            <p style="margin: 0; opacity: 0.9; line-height: 1.6;">Ensuring vehicles are fit for purpose, maintained, and equipped with safety features</p>
        </div>
        <div style="background: rgba(255,255,255,0.1); padding: 25px; border-radius: 12px; backdrop-filter: blur(10px);">
            <div style="font-size: 2.5em; margin-bottom: 15px;">👤</div>
            <h3 style="color: white; margin: 0 0 10px 0; font-size: 1.2em;">Safe Road Users</h3>
            <p style="margin: 0; opacity: 0.9; line-height: 1.6;">Driver competence, fitness, fatigue management, and awareness</p>
        </div>
        <div style="background: rgba(255,255,255,0.1); padding: 25px; border-radius: 12px; backdrop-filter: blur(10px);">
            <div style="font-size: 2.5em; margin-bottom: 15px;">👔</div>
            <h3 style="color: white; margin: 0 0 10px 0; font-size: 1.2em;">Leadership & Accountability</h3>
            <p style="margin: 0; opacity: 0.9; line-height: 1.6;">Road safety driven from the top, not delegated to supervisors alone</p>
        </div>
        <div style="background: rgba(255,255,255,0.1); padding: 25px; border-radius: 12px; backdrop-filter: blur(10px);">
            <div style="font-size: 2.5em; margin-bottom: 15px;">⚠️</div>
            <h3 style="color: white; margin: 0 0 10px 0; font-size: 1.2em;">Risk-Based Thinking</h3>
            <p style="margin: 0; opacity: 0.9; line-height: 1.6;">Identifying where serious injury or death could occur and prioritising controls</p>
        </div>
        <div style="background: rgba(255,255,255,0.1); padding: 25px; border-radius: 12px; backdrop-filter: blur(10px);">
            <div style="font-size: 2.5em; margin-bottom: 15px;">📈</div>
            <h3 style="color: white; margin: 0 0 10px 0; font-size: 1.2em;">Continuous Improvement</h3>
            <p style="margin: 0; opacity: 0.9; line-height: 1.6;">Using incident data, near-misses, and audits to improve performance</p>
        </div>
    </div>
</div>

<!-- Benefits section -->
<h2 style="color: #1e3a5f; margin-top: 50px; margin-bottom: 30px; font-size: 2em; text-align: center;">
    Benefits of ISO 39001
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
                Reduced accidents, injuries, and downtime
            </li>
            <li style="margin-bottom: 15px; padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #30b566; font-size: 1.3em;">✓</span>
                Clear responsibilities for fleet and driver safety
            </li>
            <li style="margin-bottom: 15px; padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #30b566; font-size: 1.3em;">✓</span>
                Improved driver awareness and engagement
            </li>
            <li style="padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #30b566; font-size: 1.3em;">✓</span>
                Lower vehicle repair and insurance costs
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
                Stronger corporate social responsibility credentials
            </li>
            <li style="margin-bottom: 15px; padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #2196f3; font-size: 1.3em;">✓</span>
                Improved reputation with clients and regulators
            </li>
            <li style="margin-bottom: 15px; padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #2196f3; font-size: 1.3em;">✓</span>
                Competitive advantage in safety-critical contracts
            </li>
            <li style="padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #2196f3; font-size: 1.3em;">✓</span>
                Demonstrable commitment to employee wellbeing
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
                Supports compliance with UK health and safety obligations
            </li>
            <li style="margin-bottom: 15px; padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #ff9800; font-size: 1.3em;">✓</span>
                Provides strong evidence of duty of care
            </li>
            <li style="padding-left: 30px; position: relative; line-height: 1.6;">
                <span style="position: absolute; left: 0; top: 0; color: #ff9800; font-size: 1.3em;">✓</span>
                Reduces exposure to prosecution and civil claims
            </li>
        </ul>
    </div>
</div>

<!-- What auditors look for -->
<div style="background: #f8f9fa; padding: 40px; border-radius: 15px; margin: 50px 0;">
    <h2 style="color: #1e3a5f; margin-top: 0; margin-bottom: 25px; font-size: 2em;">
        What ISO 39001 auditors look for
    </h2>

    <div style="background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%); padding: 25px; border-radius: 12px; margin-bottom: 25px; border-left: 5px solid #ff9800;">
        <p style="margin: 0; font-size: 1.05em; line-height: 1.7;">
            <strong>Auditors are not simply checking driving licences.</strong> They want evidence of a working management system.
        </p>
    </div>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-top: 25px;">
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
            <h4 style="color: #1e3a5f; margin-top: 0; margin-bottom: 12px;">⚠️ Road Risk Assessment</h4>
            <p style="margin: 0; line-height: 1.6;">Understanding how your activities create risk</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
            <h4 style="color: #1e3a5f; margin-top: 0; margin-bottom: 12px;">📋 Policies & Objectives</h4>
            <p style="margin: 0; line-height: 1.6;">Clear, measurable road safety goals</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
            <h4 style="color: #1e3a5f; margin-top: 0; margin-bottom: 12px;">🔧 Operational Controls</h4>
            <p style="margin: 0; line-height: 1.6;">Vehicle checks, journey planning, fatigue management</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
            <h4 style="color: #1e3a5f; margin-top: 0; margin-bottom: 12px;">📊 Incident Reporting</h4>
            <p style="margin: 0; line-height: 1.6;">Learning from accidents and near-misses</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
            <h4 style="color: #1e3a5f; margin-top: 0; margin-bottom: 12px;">📈 Monitoring & Review</h4>
            <p style="margin: 0; line-height: 1.6;">KPIs, audits, and management oversight</p>
        </div>
    </div>

    <div style="background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%); padding: 25px; border-radius: 12px; margin-top: 25px; border-left: 5px solid #30b566;">
        <p style="margin: 0; font-size: 1.05em; line-height: 1.7;">
            The emphasis is on <strong>prevention and continual improvement</strong>.
        </p>
    </div>
</div>

<!-- Real-world examples -->
<h2 style="color: #1e3a5f; margin-top: 50px; margin-bottom: 30px; font-size: 2em;">
    ISO 39001 in practice (real-world examples)
</h2>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 30px; margin: 30px 0;">
    <div style="background: linear-gradient(135deg, #e8eaf6 0%, #c5cae9 100%); padding: 35px; border-radius: 15px; box-shadow: 0 6px 20px rgba(0,0,0,0.1);">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 20px; font-size: 1.4em;">
            🚚 Logistics & Fleet Operator
        </h3>
        <p style="margin: 0; line-height: 1.7; font-size: 1.05em;">
            A UK logistics firm uses ISO 39001 to reduce collision rates by improving driver scheduling, vehicle maintenance, and telematics monitoring—resulting in fewer claims and lower insurance premiums.
        </p>
    </div>

    <div style="background: linear-gradient(135deg, #fce4ec 0%, #f8bbd0 100%); padding: 35px; border-radius: 15px; box-shadow: 0 6px 20px rgba(0,0,0,0.1);">
        <h3 style="color: #1e3a5f; margin-top: 0; margin-bottom: 20px; font-size: 1.4em;">
            🏗️ Construction Company
        </h3>
        <p style="margin: 0; line-height: 1.7; font-size: 1.05em;">
            A construction contractor applies ISO 39001 to manage road risk from site vehicles and subcontractors, strengthening compliance with health and safety requirements and improving tender success.
        </p>
    </div>
</div>

<!-- Common mistakes -->
<div style="background: linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%); padding: 40px; border-radius: 15px; margin: 50px 0;">
    <h2 style="color: #1e3a5f; margin-top: 0; margin-bottom: 25px; font-size: 2em;">
        ⚠️ Common mistakes when implementing ISO 39001
    </h2>

    <div style="display: grid; gap: 20px;">
        <div style="background: white; padding: 25px; border-radius: 12px; border-left: 5px solid #f44336;">
            <h4 style="color: #1e3a5f; margin: 0 0 10px 0; font-size: 1.2em;">Focusing Only on Drivers</h4>
            <p style="margin: 0; line-height: 1.6;">Road safety is influenced by management decisions, not just driver behaviour.</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; border-left: 5px solid #f44336;">
            <h4 style="color: #1e3a5f; margin: 0 0 10px 0; font-size: 1.2em;">Ignoring Grey Fleet Risk</h4>
            <p style="margin: 0; line-height: 1.6;">Personal vehicles used for work still fall under employer responsibility.</p>
        </div>
        <div style="background: white; padding: 25px; border-radius: 12px; border-left: 5px solid #f44336;">
            <h4 style="color: #1e3a5f; margin: 0 0 10px 0; font-size: 1.2em;">Overlooking Fatigue & Scheduling</h4>
            <p style="margin: 0; line-height: 1.6;">Time pressure is a major cause of serious incidents.</p>
        </div>
    </div>
</div>

<!-- Certification process -->
<div style="background: #f8f9fa; padding: 40px; border-radius: 15px; margin: 50px 0;">
    <h2 style="color: #1e3a5f; margin-top: 0; margin-bottom: 30px; font-size: 2em; text-align: center;">
        ISO 39001 certification process
    </h2>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 25px;">
        <div style="background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); text-align: center;">
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px; font-size: 1.8em; font-weight: bold;">1</div>
            <h4 style="color: #1e3a5f; margin: 0 0 12px 0; font-size: 1.2em;">Stage 1: System Design Review</h4>
            <p style="margin: 0; line-height: 1.6;">The auditor checks that your RTS management system meets the standard's requirements</p>
        </div>
        <div style="background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); text-align: center;">
            <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); color: white; width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px; font-size: 1.8em; font-weight: bold;">2</div>
            <h4 style="color: #1e3a5f; margin: 0 0 12px 0; font-size: 1.2em;">Stage 2: Implementation Audit</h4>
            <p style="margin: 0; line-height: 1.6;">They verify that controls are in place and working across operations</p>
        </div>
        <div style="background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); text-align: center;">
            <div style="background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%); color: white; width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px; font-size: 1.8em; font-weight: bold;">3</div>
            <h4 style="color: #1e3a5f; margin: 0 0 12px 0; font-size: 1.2em;">Surveillance Audits</h4>
            <p style="margin: 0; line-height: 1.6;">Annual audits ensure ongoing effectiveness and improvement</p>
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
    How long does ISO 39001 certification last?
</h2>

<p style="font-size: 1.05em; line-height: 1.8; margin: 25px 0;">
    ISO 39001 certification is valid for <strong>three years</strong>, subject to successful annual surveillance audits. Failure to address serious non-conformities can lead to suspension or withdrawal.
</p>

<h2 style="color: #1e3a5f; margin-top: 50px; margin-bottom: 20px; font-size: 2em;">
    How much does ISO 39001 cost in the UK?
</h2>

<p style="font-size: 1.05em; line-height: 1.8; margin: 25px 0;">
    Costs vary depending on:
</p>

<ul style="font-size: 1.05em; line-height: 1.8; margin: 25px 0; padding-left: 30px;">
    <li style="margin-bottom: 10px;">Size of fleet and operations</li>
    <li style="margin-bottom: 10px;">Number of drivers and sites</li>
    <li>Existing health and safety systems</li>
</ul>

<div style="background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%); padding: 35px; border-radius: 15px; margin: 30px 0; border-left: 5px solid #2196f3;">
    <p style="margin: 0 0 15px 0; font-size: 1.1em; font-weight: 600; color: #1e3a5f;">
        Typical costs include:
    </p>
    <ul style="margin: 0; padding-left: 25px; line-height: 1.8;">
        <li style="margin-bottom: 10px;">Certification Audit Fees</li>
        <li style="margin-bottom: 10px;">Consultancy Support (if required)</li>
        <li>Vehicle and Safety Improvements</li>
    </ul>
</div>

<p style="font-size: 1.05em; line-height: 1.8; margin: 25px 0;">
    These costs are usually <strong>outweighed by reductions in accidents, claims, and downtime</strong>.
</p>

<!-- Integration -->
<div style="background: #f8f9fa; padding: 40px; border-radius: 15px; margin: 50px 0;">
    <h2 style="color: #1e3a5f; margin-top: 0; margin-bottom: 25px; font-size: 2em;">
        ISO 39001 and integration with other standards
    </h2>

    <p style="font-size: 1.05em; line-height: 1.8; margin-bottom: 25px;">
        ISO 39001 follows the <strong>Annex SL High-Level Structure</strong>, making it easy to integrate with:
    </p>

    <div style="display: flex; flex-wrap: wrap; gap: 15px; margin: 25px 0;">
        <span style="background: white; color: #1e3a5f; padding: 15px 30px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1); font-size: 1.05em;">ISO 9001 – Quality Management</span>
        <span style="background: white; color: #1e3a5f; padding: 15px 30px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1); font-size: 1.05em;">ISO 14001 – Environmental Management</span>
        <span style="background: white; color: #1e3a5f; padding: 15px 30px; border-radius: 50px; font-weight: 600; box-shadow: 0 2px 8px rgba(0,0,0,0.1); font-size: 1.05em;">ISO 45001 – Occupational Health & Safety</span>
    </div>

    <div style="background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%); padding: 25px; border-radius: 12px; margin-top: 25px; border-left: 5px solid #30b566;">
        <p style="margin: 0; font-size: 1.05em; line-height: 1.7;">
            This allows organisations to manage road safety within a single <strong>Integrated Management System (IMS)</strong>.
        </p>
    </div>
</div>

<!-- Who should NOT implement -->
<div style="background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%); padding: 40px; border-radius: 15px; margin: 50px 0; border-left: 5px solid #ff9800;">
    <h2 style="color: #1e3a5f; margin-top: 0; margin-bottom: 20px; font-size: 2em;">
        Who should NOT implement ISO 39001?
    </h2>

    <p style="margin: 0; font-size: 1.05em; line-height: 1.8;">
        If your organisation has <strong>no employees driving for work, no fleet, and no influence over road use</strong>, ISO 39001 may not be appropriate. Similarly, organisations seeking a superficial compliance badge without leadership commitment will struggle to gain real benefit.
    </p>
</div>

<!-- FAQs -->
<div style="background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%); padding: 45px; border-radius: 15px; margin: 50px 0; color: white;">
    <h2 style="color: white; margin-top: 0; margin-bottom: 30px; font-size: 2em; text-align: center;">
        Frequently Asked Questions (FAQs)
    </h2>

    <div style="display: grid; gap: 25px;">
        <div style="background: rgba(255,255,255,0.1); padding: 30px; border-radius: 12px; backdrop-filter: blur(10px);">
            <h4 style="color: white; margin: 0 0 12px 0; font-size: 1.3em;">Is ISO 39001 a legal requirement in the UK?</h4>
            <p style="margin: 0; opacity: 0.9; line-height: 1.7; font-size: 1.05em;">No. It is voluntary, but strongly supports compliance with UK health and safety law.</p>
        </div>

        <div style="background: rgba(255,255,255,0.1); padding: 30px; border-radius: 12px; backdrop-filter: blur(10px);">
            <h4 style="color: white; margin: 0 0 12px 0; font-size: 1.3em;">Does ISO 39001 apply to company cars and grey fleet?</h4>
            <p style="margin: 0; opacity: 0.9; line-height: 1.7; font-size: 1.05em;">Yes. Any driving undertaken for work purposes is within scope.</p>
        </div>

        <div style="background: rgba(255,255,255,0.1); padding: 30px; border-radius: 12px; backdrop-filter: blur(10px);">
            <h4 style="color: white; margin: 0 0 12px 0; font-size: 1.3em;">Can small businesses achieve ISO 39001?</h4>
            <p style="margin: 0; opacity: 0.9; line-height: 1.7; font-size: 1.05em;">Yes. The standard is scalable and proportionate.</p>
        </div>

        <div style="background: rgba(255,255,255,0.1); padding: 30px; border-radius: 12px; backdrop-filter: blur(10px);">
            <h4 style="color: white; margin: 0 0 12px 0; font-size: 1.3em;">Is ISO 39001 recognised in UK procurement?</h4>
            <p style="margin: 0; opacity: 0.9; line-height: 1.7; font-size: 1.05em;">Increasingly, yes—especially for transport, construction, and public sector contracts.</p>
        </div>
    </div>
</div>

<!-- Call to action -->
<div style="background: linear-gradient(135deg, #ff9800 0%, #f57c00 100%); padding: 50px; border-radius: 15px; margin: 50px 0; text-align: center; color: white;">
    <h2 style="color: white; margin: 0 0 20px 0; font-size: 2.2em;">
        Ready to protect lives and reduce road traffic risk?
    </h2>
    <p style="font-size: 1.2em; line-height: 1.8; margin: 0 0 30px 0; opacity: 0.95;">
        Qualitation has been helping UK organisations achieve ISO certification for over 25 years with a 100% first-time success rate.
    </p>
    <div style="display: flex; gap: 20px; justify-content: center; flex-wrap: wrap;">
        <a href="/contact/" style="background: white; color: #ff9800; padding: 15px 40px; border-radius: 50px; text-decoration: none; font-weight: 700; font-size: 1.1em; display: inline-block; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
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

            self.stdout.write(self.style.SUCCESS(f'✓ Updated ISO 39001 page'))
            self.stdout.write(self.style.SUCCESS(f'✓ URL: /{page.get_url_parts()[2]}'))
            self.stdout.write(self.style.SUCCESS('✓ Published successfully'))

        except Page.DoesNotExist:
            self.stdout.write(self.style.ERROR('✗ ISO 39001 page not found'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ Error: {e}'))
            import traceback
            traceback.print_exc()

        self.stdout.write(self.style.SUCCESS('\n=== Complete ===\n'))
