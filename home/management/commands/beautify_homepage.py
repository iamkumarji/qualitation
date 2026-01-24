"""
Django management command to beautify the homepage
Enhances visual design with modern styling, animations, and effects
"""

from django.core.management.base import BaseCommand
from home.models import HomePage


class Command(BaseCommand):
    help = 'Beautify the homepage with modern design enhancements'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('\n=== Beautifying Homepage ===\n'))

        try:
            # Get the homepage
            home_page = HomePage.objects.first()

            if not home_page:
                self.stdout.write(self.style.ERROR('✗ Homepage not found'))
                return

            # We'll enhance specific blocks
            for i, block in enumerate(home_page.body):
                block_type = block.block_type

                if block_type == 'html':
                    html_content = block.value.get('html', '') if hasattr(block.value, 'get') else str(block.value)

                    # Enhance Stats Section
                    if 'stats-section' in html_content and 'stats-card' not in html_content:
                        self.stdout.write(f'Enhancing stats section in block {i}...')
                        html_content = self.enhance_stats_section(html_content)
                        block.value['html'] = html_content

                    # Enhance Service Cards
                    elif 'service-card' in html_content and 'Our ISO Certification Services' in html_content:
                        self.stdout.write(f'Enhancing service cards in block {i}...')
                        html_content = self.enhance_service_cards(html_content)
                        block.value['html'] = html_content

                    # Enhance Why Choose Section
                    elif 'why-card' in html_content and 'Why Choose Qualitation' in html_content:
                        self.stdout.write(f'Enhancing why choose section in block {i}...')
                        html_content = self.enhance_why_section(html_content)
                        block.value['html'] = html_content

                    # Enhance Testimonials
                    elif 'testimonial-card' in html_content:
                        self.stdout.write(f'Enhancing testimonials in block {i}...')
                        html_content = self.enhance_testimonials(html_content)
                        block.value['html'] = html_content

                    # Enhance CTA Section
                    elif 'Ready to Get ISO Certified' in html_content:
                        self.stdout.write(f'Enhancing CTA section in block {i}...')
                        html_content = self.enhance_cta_section(html_content)
                        block.value['html'] = html_content

            # Save changes
            home_page.save_revision().publish()

            self.stdout.write(self.style.SUCCESS('\n✓ Homepage beautified successfully!'))
            self.stdout.write(self.style.SUCCESS('✓ Enhanced stats section'))
            self.stdout.write(self.style.SUCCESS('✓ Enhanced service cards'))
            self.stdout.write(self.style.SUCCESS('✓ Enhanced why choose section'))
            self.stdout.write(self.style.SUCCESS('✓ Enhanced testimonials'))
            self.stdout.write(self.style.SUCCESS('✓ Enhanced CTA section'))
            self.stdout.write(self.style.SUCCESS('\nView at: http://localhost:8000/'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ Error: {e}'))
            import traceback
            traceback.print_exc()

        self.stdout.write(self.style.SUCCESS('\n=== Complete ===\n'))

    def enhance_stats_section(self, html_content):
        """Enhance the stats section with modern card design"""
        import re

        # Find and replace the stats section
        old_stats = re.search(r'<style>.*?\.stats-section.*?</style>.*?<section class="stats-section">.*?</section>', html_content, re.DOTALL)

        if old_stats:
            new_stats = '''<style>
.stats-section {
    background: linear-gradient(135deg, #0066cc 0%, #004999 100%);
    padding: 90px 20px;
    position: relative;
    overflow: hidden;
}
.stats-section::before {
    content: '';
    position: absolute;
    top: -50%;
    right: -20%;
    width: 500px;
    height: 500px;
    background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
    border-radius: 50%;
    animation: float 20s ease-in-out infinite;
}
.stats-section::after {
    content: '';
    position: absolute;
    bottom: -30%;
    left: -10%;
    width: 400px;
    height: 400px;
    background: radial-gradient(circle, rgba(255,255,255,0.08) 0%, transparent 70%);
    border-radius: 50%;
    animation: float 15s ease-in-out infinite reverse;
}
@keyframes float {
    0%, 100% { transform: translateY(0px) scale(1); }
    50% { transform: translateY(-30px) scale(1.05); }
}
.stats-container {
    max-width: 1200px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 35px;
    position: relative;
    z-index: 1;
}
.stats-card {
    background: rgba(255, 255, 255, 0.12);
    backdrop-filter: blur(10px);
    padding: 45px 30px;
    border-radius: 25px;
    text-align: center;
    border: 2px solid rgba(255, 255, 255, 0.15);
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    position: relative;
    overflow: hidden;
}
.stats-card::before {
    content: '';
    position: absolute;
    top: -100%;
    left: -100%;
    width: 300%;
    height: 300%;
    background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 50%);
    transition: all 0.6s;
}
.stats-card:hover::before {
    top: -50%;
    left: -50%;
}
.stats-card:hover {
    transform: translateY(-15px) scale(1.03);
    background: rgba(255, 255, 255, 0.18);
    border-color: rgba(255, 255, 255, 0.3);
    box-shadow: 0 25px 60px rgba(0, 0, 0, 0.3);
}
.stats-icon {
    width: 85px;
    height: 85px;
    background: linear-gradient(135deg, rgba(255,255,255,0.25), rgba(255,255,255,0.15));
    border-radius: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 25px;
    font-size: 2.5rem;
    color: white;
    position: relative;
    z-index: 1;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
}
.stats-card:hover .stats-icon {
    transform: rotateY(360deg);
    transition: transform 0.6s;
}
.stats-number {
    font-size: 3.8rem;
    font-weight: 900;
    color: white;
    margin-bottom: 12px;
    line-height: 1;
    position: relative;
    z-index: 1;
    text-shadow: 0 4px 15px rgba(0,0,0,0.3);
}
.stats-label {
    font-size: 1.15rem;
    color: rgba(255, 255, 255, 0.95);
    font-weight: 600;
    position: relative;
    z-index: 1;
    line-height: 1.4;
}
@media (max-width: 768px) {
    .stats-container {
        grid-template-columns: repeat(2, 1fr);
        gap: 25px;
    }
}
</style>

<section class="stats-section">
    <div class="stats-container">
        <div class="stats-card">
            <div class="stats-icon">
                <i class="fas fa-trophy"></i>
            </div>
            <div class="stats-number">100%</div>
            <div class="stats-label">First-Time<br>Certification Success</div>
        </div>
        <div class="stats-card">
            <div class="stats-icon">
                <i class="fas fa-users"></i>
            </div>
            <div class="stats-number">500+</div>
            <div class="stats-label">UK Organisations<br>Certified</div>
        </div>
        <div class="stats-card">
            <div class="stats-icon">
                <i class="fas fa-calendar-check"></i>
            </div>
            <div class="stats-number">25+</div>
            <div class="stats-label">Years ISO<br>Consultancy Experience</div>
        </div>
        <div class="stats-card">
            <div class="stats-icon">
                <i class="fas fa-award"></i>
            </div>
            <div class="stats-number">14</div>
            <div class="stats-label">ISO Standards<br>We Support</div>
        </div>
    </div>
</section>'''

            html_content = html_content.replace(old_stats.group(0), new_stats)

        return html_content

    def enhance_service_cards(self, html_content):
        """Enhance service cards with better styling"""
        import re

        # Add enhanced styles for service cards
        service_style = '''<style>
.service-card {
    background: white;
    border-radius: 20px;
    padding: 35px 28px;
    text-align: center;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    border: 2px solid #f0f4f8;
    position: relative;
    overflow: hidden;
}
.service-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, var(--card-color), var(--card-color-light));
    transform: scaleX(0);
    transition: transform 0.4s;
}
.service-card:hover::before {
    transform: scaleX(1);
}
.service-card:hover {
    transform: translateY(-12px) scale(1.02);
    box-shadow: 0 20px 50px rgba(0, 102, 204, 0.18);
    border-color: var(--card-color);
}
.service-icon-wrapper {
    position: relative;
    width: 90px;
    height: 90px;
    margin: 0 auto 25px;
}
.service-icon-bg {
    position: absolute;
    width: 100%;
    height: 100%;
    border-radius: 18px;
    opacity: 0.1;
    transform: rotate(45deg);
}
.service-icon {
    position: relative;
    width: 100%;
    height: 100%;
    border-radius: 18px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 2.2rem;
    color: white;
    box-shadow: 0 10px 30px rgba(0, 102, 204, 0.25);
    transition: all 0.4s;
}
.service-card:hover .service-icon {
    transform: scale(1.1) rotate(5deg);
    box-shadow: 0 15px 40px rgba(0, 102, 204, 0.35);
}
.service-title {
    font-size: 1.35rem;
    font-weight: 700;
    color: #1e3a5f;
    margin-bottom: 12px;
}
.service-desc {
    font-size: 1.02rem;
    color: #64748b;
    line-height: 1.6;
}
</style>'''

        # Insert style before the services section
        if '<h2>Our ISO Certification Services</h2>' in html_content and 'service-card::before' not in html_content:
            html_content = html_content.replace(
                '<h2>Our ISO Certification Services</h2>',
                service_style + '\n<h2>Our ISO Certification Services</h2>'
            )

        return html_content

    def enhance_why_section(self, html_content):
        """Enhance why choose section"""
        import re

        why_style = '''<style>
.why-card {
    background: white;
    border-radius: 22px;
    padding: 40px 30px;
    text-align: center;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    border: 2px solid #f0f4f8;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.06);
}
.why-card:hover {
    transform: translateY(-15px);
    box-shadow: 0 25px 60px rgba(0, 102, 204, 0.15);
    border-color: #0066cc;
}
.why-illustration {
    width: 120px;
    height: 120px;
    margin: 0 auto 25px;
    transition: transform 0.4s;
}
.why-card:hover .why-illustration {
    transform: scale(1.1) rotate(5deg);
}
.why-card h3 {
    font-size: 1.5rem;
    color: #1e3a5f;
    margin-bottom: 15px;
    font-weight: 700;
}
.why-card p {
    font-size: 1.05rem;
    color: #64748b;
    line-height: 1.7;
}
</style>'''

        if 'Why Choose Qualitation' in html_content and 'why-card:hover' not in html_content:
            html_content = html_content.replace(
                '<h2>Why Choose Qualitation?</h2>',
                why_style + '\n<h2>Why Choose Qualitation?</h2>'
            )

        return html_content

    def enhance_testimonials(self, html_content):
        """Enhance testimonial cards"""
        testimonial_style = '''<style>
.testimonial-card {
    background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
    border-radius: 22px;
    padding: 40px 35px;
    border: 2px solid #e5e7eb;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    position: relative;
    overflow: hidden;
}
.testimonial-card::before {
    content: '"';
    position: absolute;
    top: 20px;
    right: 30px;
    font-size: 120px;
    color: rgba(0, 102, 204, 0.05);
    font-family: Georgia, serif;
    line-height: 1;
}
.testimonial-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 20px 50px rgba(0, 102, 204, 0.15);
    border-color: #0066cc;
}
.testimonial-stars {
    color: #fbbf24;
    font-size: 1.3rem;
    margin-bottom: 20px;
    text-shadow: 0 2px 4px rgba(251, 191, 36, 0.3);
}
.testimonial-text {
    font-size: 1.08rem;
    color: #475569;
    line-height: 1.8;
    margin-bottom: 25px;
    font-style: italic;
}
.testimonial-avatar {
    width: 55px;
    height: 55px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-weight: 700;
    font-size: 1.2rem;
    box-shadow: 0 6px 20px rgba(0, 102, 204, 0.3);
}
</style>'''

        if 'testimonial-card' in html_content and 'testimonial-card::before' not in html_content:
            html_content = html_content.replace(
                '<h2>What Our Clients Say</h2>',
                testimonial_style + '\n<h2>What Our Clients Say</h2>'
            )

        return html_content

    def enhance_cta_section(self, html_content):
        """Enhance CTA section"""
        import re

        # Find the CTA section and enhance it
        if 'Ready to Get ISO Certified' in html_content:
            # Add enhanced styles
            cta_style = '''<style>
.cta-section {
    background: linear-gradient(135deg, #1e3a5f 0%, #0f172a 100%);
    padding: 90px 20px;
    text-align: center;
    position: relative;
    overflow: hidden;
}
.cta-section::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -20%;
    width: 600px;
    height: 600px;
    background: radial-gradient(circle, rgba(255,255,255,0.08) 0%, transparent 70%);
    border-radius: 50%;
}
.cta-section h2 {
    font-size: 3rem;
    color: white;
    margin-bottom: 20px;
    font-weight: 800;
    position: relative;
    z-index: 1;
}
.cta-section p {
    font-size: 1.3rem;
    color: rgba(255, 255, 255, 0.9);
    margin-bottom: 40px;
    position: relative;
    z-index: 1;
}
.cta-btn {
    display: inline-flex;
    align-items: center;
    gap: 12px;
    padding: 18px 40px;
    border-radius: 50px;
    font-size: 1.15rem;
    font-weight: 700;
    text-decoration: none;
    transition: all 0.3s;
    position: relative;
    z-index: 1;
}
.cta-btn-primary {
    background: linear-gradient(135deg, #0066cc, #3b82f6);
    color: white;
    box-shadow: 0 10px 30px rgba(0, 102, 204, 0.4);
}
.cta-btn-primary:hover {
    transform: translateY(-5px) scale(1.05);
    box-shadow: 0 20px 50px rgba(0, 102, 204, 0.5);
}
.cta-btn-secondary {
    background: rgba(255, 255, 255, 0.15);
    color: white;
    border: 2px solid rgba(255, 255, 255, 0.3);
    backdrop-filter: blur(10px);
}
.cta-btn-secondary:hover {
    background: rgba(255, 255, 255, 0.25);
    transform: translateY(-5px);
}
</style>'''

            if 'cta-section::before' not in html_content:
                html_content = html_content.replace(
                    '<h2>Ready to Get ISO Certified?</h2>',
                    cta_style + '\n<h2>Ready to Get ISO Certified?</h2>'
                )

        return html_content
