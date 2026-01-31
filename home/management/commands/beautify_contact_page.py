from django.core.management.base import BaseCommand
from wagtail.models import Page
from home.models import FlexiblePage


class Command(BaseCommand):
    help = 'Beautify contact page with hero section and content'

    def handle(self, *args, **options):
        try:
            # Find the contact page
            contact_page = FlexiblePage.objects.filter(slug='contact').first()

            if not contact_page:
                self.stdout.write(self.style.ERROR('Contact page not found'))
                return

            # Create beautiful contact page content
            body_content = [
                # Hero Section
                {
                    'type': 'html',
                    'value': {
                        'html': '''
<!-- Hero Section with Illustration -->
<section style="background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 50%, #3d7ab5 100%); padding: 80px 0; position: relative; overflow: hidden;">
    <!-- Background Pattern -->
    <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; opacity: 0.1;">
        <svg width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <pattern id="contact-grid" width="40" height="40" patternUnits="userSpaceOnUse">
                    <circle cx="20" cy="20" r="1" fill="white"/>
                </pattern>
            </defs>
            <rect width="100%" height="100%" fill="url(#contact-grid)"/>
        </svg>
    </div>

    <div style="max-width: 1200px; margin: 0 auto; padding: 0 20px; position: relative; z-index: 1;">
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 60px; align-items: center;">
            <div>
                <h1 style="color: white; font-size: 3.2em; font-weight: 700; margin-bottom: 20px; line-height: 1.2;">
                    Let's Start Your<br><span style="color: #4fd1c5;">Certification Journey</span>
                </h1>
                <p style="color: rgba(255,255,255,0.9); font-size: 1.3em; line-height: 1.7; margin-bottom: 30px;">
                    Get in touch with our expert team for a free, no-obligation consultation. We're here to guide you through every step of your ISO certification process.
                </p>
                <div style="display: flex; gap: 15px; flex-wrap: wrap;">
                    <a href="tel:03456006975" style="display: inline-flex; align-items: center; gap: 10px; background: white; color: #1e3a5f; padding: 15px 25px; border-radius: 50px; text-decoration: none; font-weight: 600; transition: all 0.3s ease; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
                        <svg width="20" height="20" fill="#1e3a5f" viewBox="0 0 24 24"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
                        03456006975
                    </a>
                    <a href="mailto:webmail@certigence.co.uk" style="display: inline-flex; align-items: center; gap: 10px; background: rgba(255,255,255,0.2); color: white; padding: 15px 25px; border-radius: 50px; text-decoration: none; font-weight: 600; backdrop-filter: blur(10px); border: 2px solid rgba(255,255,255,0.3); transition: all 0.3s ease;">
                        <svg width="20" height="20" fill="white" viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
                        Email Us
                    </a>
                </div>
            </div>

            <!-- Illustration -->
            <div style="text-align: center;">
                <svg width="100%" height="400" viewBox="0 0 500 400" xmlns="http://www.w3.org/2000/svg">
                    <!-- Decorative elements -->
                    <circle cx="250" cy="200" r="180" fill="rgba(255,255,255,0.1)"/>
                    <circle cx="250" cy="200" r="140" fill="rgba(255,255,255,0.15)"/>

                    <!-- Contact icons -->
                    <g transform="translate(250, 200)">
                        <!-- Email icon -->
                        <g transform="translate(-80, -60)">
                            <circle cx="0" cy="0" r="35" fill="white" opacity="0.9"/>
                            <path d="M-15,-10 L0,0 L15,-10 M-15,-10 L-15,10 L15,10 L15,-10" fill="none" stroke="#2563eb" stroke-width="2" stroke-linecap="round"/>
                        </g>

                        <!-- Phone icon -->
                        <g transform="translate(80, -60)">
                            <circle cx="0" cy="0" r="35" fill="white" opacity="0.9"/>
                            <path d="M-8,-12 Q-10,-10 -10,-5 L-10,5 Q-10,10 -8,12 L8,12 Q10,10 10,5 L10,-5 Q10,-10 8,-12 Z" fill="none" stroke="#10b981" stroke-width="2"/>
                            <circle cx="0" cy="8" r="2" fill="#10b981"/>
                        </g>

                        <!-- Location icon -->
                        <g transform="translate(0, 60)">
                            <circle cx="0" cy="0" r="35" fill="white" opacity="0.9"/>
                            <path d="M0,-12 Q-8,-12 -8,-4 Q-8,4 0,12 Q8,4 8,-4 Q8,-12 0,-12 Z" fill="none" stroke="#f59e0b" stroke-width="2"/>
                            <circle cx="0" cy="-4" r="3" fill="#f59e0b"/>
                        </g>
                    </g>

                    <!-- Connecting lines -->
                    <path d="M 170 140 Q 250 180 330 140" fill="none" stroke="rgba(255,255,255,0.3)" stroke-width="2" stroke-dasharray="5,5"/>
                    <path d="M 170 140 Q 200 240 250 260" fill="none" stroke="rgba(255,255,255,0.3)" stroke-width="2" stroke-dasharray="5,5"/>
                    <path d="M 330 140 Q 300 240 250 260" fill="none" stroke="rgba(255,255,255,0.3)" stroke-width="2" stroke-dasharray="5,5"/>
                </svg>
            </div>
        </div>
    </div>
</section>
                        '''
                    },
                    'id': 'hero-section'
                },

                # Why Contact Us Section
                {
                    'type': 'html',
                    'value': {
                        'html': '''
<!-- Why Contact Us Section -->
<section style="padding: 80px 20px; background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%);">
    <div style="max-width: 1200px; margin: 0 auto;">
        <div style="text-align: center; margin-bottom: 60px;">
            <h2 style="font-size: 2.5em; font-weight: 700; color: #1e293b; margin-bottom: 15px;">
                Why Contact <span style="background: linear-gradient(135deg, #2563eb, #7c3aed); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Qualitation</span>?
            </h2>
            <p style="font-size: 1.2em; color: #64748b; max-width: 700px; margin: 0 auto;">
                We're committed to making your ISO certification journey smooth and successful
            </p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 30px; margin-bottom: 40px;">
            <!-- Card 1 -->
            <div style="background: white; padding: 35px; border-radius: 16px; box-shadow: 0 4px 20px rgba(0,0,0,0.08); transition: all 0.3s ease; border-left: 4px solid #2563eb;">
                <div style="width: 60px; height: 60px; background: linear-gradient(135deg, #dbeafe, #bfdbfe); border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
                    <span style="font-size: 30px;">🎯</span>
                </div>
                <h3 style="font-size: 1.4em; font-weight: 700; color: #1e293b; margin-bottom: 12px;">Free Consultation</h3>
                <p style="color: #64748b; line-height: 1.7; margin: 0;">
                    Get expert advice tailored to your business needs with no obligation. We'll help you understand the certification process.
                </p>
            </div>

            <!-- Card 2 -->
            <div style="background: white; padding: 35px; border-radius: 16px; box-shadow: 0 4px 20px rgba(0,0,0,0.08); transition: all 0.3s ease; border-left: 4px solid #10b981;">
                <div style="width: 60px; height: 60px; background: linear-gradient(135deg, #d1fae5, #a7f3d0); border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
                    <span style="font-size: 30px;">⚡</span>
                </div>
                <h3 style="font-size: 1.4em; font-weight: 700; color: #1e293b; margin-bottom: 12px;">Fast Response</h3>
                <p style="color: #64748b; line-height: 1.7; margin: 0;">
                    We typically respond within 24 hours. Your time is valuable, and we're here when you need us.
                </p>
            </div>

            <!-- Card 3 -->
            <div style="background: white; padding: 35px; border-radius: 16px; box-shadow: 0 4px 20px rgba(0,0,0,0.08); transition: all 0.3s ease; border-left: 4px solid #f59e0b;">
                <div style="width: 60px; height: 60px; background: linear-gradient(135deg, #fef3c7, #fde68a); border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
                    <span style="font-size: 30px;">💼</span>
                </div>
                <h3 style="font-size: 1.4em; font-weight: 700; color: #1e293b; margin-bottom: 12px;">Expert Team</h3>
                <p style="color: #64748b; line-height: 1.7; margin: 0;">
                    Work with certified professionals who have helped hundreds of businesses achieve ISO certification.
                </p>
            </div>

            <!-- Card 4 -->
            <div style="background: white; padding: 35px; border-radius: 16px; box-shadow: 0 4px 20px rgba(0,0,0,0.08); transition: all 0.3s ease; border-left: 4px solid #8b5cf6;">
                <div style="width: 60px; height: 60px; background: linear-gradient(135deg, #ede9fe, #ddd6fe); border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
                    <span style="font-size: 30px;">📊</span>
                </div>
                <h3 style="font-size: 1.4em; font-weight: 700; color: #1e293b; margin-bottom: 12px;">Tailored Solutions</h3>
                <p style="color: #64748b; line-height: 1.7; margin: 0;">
                    Every business is unique. We create customized certification plans that fit your specific needs.
                </p>
            </div>

            <!-- Card 5 -->
            <div style="background: white; padding: 35px; border-radius: 16px; box-shadow: 0 4px 20px rgba(0,0,0,0.08); transition: all 0.3s ease; border-left: 4px solid #ec4899;">
                <div style="width: 60px; height: 60px; background: linear-gradient(135deg, #fce7f3, #fbcfe8); border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
                    <span style="font-size: 30px;">✅</span>
                </div>
                <h3 style="font-size: 1.4em; font-weight: 700; color: #1e293b; margin-bottom: 12px;">Proven Track Record</h3>
                <p style="color: #64748b; line-height: 1.7; margin: 0;">
                    Join hundreds of satisfied clients who've successfully achieved certification with our guidance.
                </p>
            </div>

            <!-- Card 6 -->
            <div style="background: white; padding: 35px; border-radius: 16px; box-shadow: 0 4px 20px rgba(0,0,0,0.08); transition: all 0.3s ease; border-left: 4px solid #06b6d4;">
                <div style="width: 60px; height: 60px; background: linear-gradient(135deg, #cffafe, #a5f3fc); border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
                    <span style="font-size: 30px;">🤝</span>
                </div>
                <h3 style="font-size: 1.4em; font-weight: 700; color: #1e293b; margin-bottom: 12px;">Ongoing Support</h3>
                <p style="color: #64748b; line-height: 1.7; margin: 0;">
                    We don't just help you get certified – we support you throughout your compliance journey.
                </p>
            </div>
        </div>
    </div>
</section>
                        '''
                    },
                    'id': 'why-contact-section'
                },

                # Contact Information Cards
                {
                    'type': 'html',
                    'value': {
                        'html': '''
<!-- Contact Information Cards -->
<section style="padding: 60px 20px; background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%);">
    <div style="max-width: 1200px; margin: 0 auto;">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px;">
            <!-- Phone Card -->
            <div style="background: rgba(255,255,255,0.1); backdrop-filter: blur(10px); border-radius: 16px; padding: 40px; text-align: center; border: 1px solid rgba(255,255,255,0.2);">
                <div style="width: 80px; height: 80px; background: linear-gradient(135deg, #10b981, #059669); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px;">
                    <svg width="40" height="40" fill="white" viewBox="0 0 24 24"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
                </div>
                <h3 style="color: white; font-size: 1.5em; font-weight: 600; margin-bottom: 10px;">Call Us</h3>
                <p style="color: rgba(255,255,255,0.8); margin-bottom: 15px;">Monday - Friday: 9AM - 6PM</p>
                <a href="tel:03456006975" style="color: #4fd1c5; font-size: 1.3em; font-weight: 700; text-decoration: none;">03456006975</a>
            </div>

            <!-- Email Card -->
            <div style="background: rgba(255,255,255,0.1); backdrop-filter: blur(10px); border-radius: 16px; padding: 40px; text-align: center; border: 1px solid rgba(255,255,255,0.2);">
                <div style="width: 80px; height: 80px; background: linear-gradient(135deg, #2563eb, #1d4ed8); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px;">
                    <svg width="40" height="40" fill="white" viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
                </div>
                <h3 style="color: white; font-size: 1.5em; font-weight: 600; margin-bottom: 10px;">Email Us</h3>
                <p style="color: rgba(255,255,255,0.8); margin-bottom: 15px;">We'll respond within 24 hours</p>
                <a href="mailto:webmail@certigence.co.uk" style="color: #4fd1c5; font-size: 1.1em; font-weight: 600; text-decoration: none; word-break: break-all;">webmail@certigence.co.uk</a>
            </div>

            <!-- Office Hours Card -->
            <div style="background: rgba(255,255,255,0.1); backdrop-filter: blur(10px); border-radius: 16px; padding: 40px; text-align: center; border: 1px solid rgba(255,255,255,0.2);">
                <div style="width: 80px; height: 80px; background: linear-gradient(135deg, #f59e0b, #d97706); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px;">
                    <svg width="40" height="40" fill="white" viewBox="0 0 24 24"><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm.5-13H11v6l5.25 3.15.75-1.23-4.5-2.67z"/></svg>
                </div>
                <h3 style="color: white; font-size: 1.5em; font-weight: 600; margin-bottom: 10px;">Office Hours</h3>
                <p style="color: rgba(255,255,255,0.9); margin: 10px 0 5px; font-weight: 500;">Monday - Friday</p>
                <p style="color: #4fd1c5; font-size: 1.2em; font-weight: 700; margin: 0;">9:00 AM - 6:00 PM</p>
            </div>
        </div>
    </div>
</section>
                        '''
                    },
                    'id': 'contact-info-cards'
                },

                # Contact Form Block (this is the working one)
                {
                    'type': 'contact_form',
                    'value': {
                        'heading': '📧 Send Us a Message',
                        'subheading': 'Fill out the form below and we\'ll get back to you as soon as possible.',
                        'background_color': 'white'
                    },
                    'id': 'contact-form-block'
                },

                # FAQ Section
                {
                    'type': 'accordion',
                    'value': {
                        'items': [
                            {
                                'title': 'How quickly will I receive a response?',
                                'content': '<p>We typically respond to all inquiries within 24 hours during business days. For urgent matters, please call us directly at 03456006975.</p>'
                            },
                            {
                                'title': 'Is the consultation really free?',
                                'content': '<p>Yes! We offer a completely free, no-obligation consultation to discuss your ISO certification needs. There\'s no pressure to commit to our services.</p>'
                            },
                            {
                                'title': 'What information should I include in my message?',
                                'content': '<p>Please include your company name, industry, which ISO standard you\'re interested in, and any specific questions or concerns you have. The more details you provide, the better we can assist you.</p>'
                            },
                            {
                                'title': 'Do you offer remote consultations?',
                                'content': '<p>Absolutely! We offer both in-person and remote consultations via video call, phone, or email – whatever works best for you.</p>'
                            },
                            {
                                'title': 'What happens after I submit the form?',
                                'content': '<p>You\'ll receive an immediate confirmation email. One of our ISO certification experts will then review your inquiry and reach out to you within 24 hours to discuss your needs and next steps.</p>'
                            }
                        ]
                    },
                    'id': 'faq-section'
                }
            ]

            # Save the updated content
            contact_page.body = body_content
            contact_page.save_revision().publish()

            self.stdout.write(self.style.SUCCESS('✅ Contact page beautified successfully!'))
            self.stdout.write(self.style.SUCCESS('The page now includes:'))
            self.stdout.write(self.style.SUCCESS('  - Hero section with gradient background'))
            self.stdout.write(self.style.SUCCESS('  - Why contact us section with 6 cards'))
            self.stdout.write(self.style.SUCCESS('  - Contact information cards'))
            self.stdout.write(self.style.SUCCESS('  - Working contact form'))
            self.stdout.write(self.style.SUCCESS('  - FAQ accordion section'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {str(e)}'))
            import traceback
            traceback.print_exc()
