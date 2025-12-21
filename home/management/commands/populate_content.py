"""
Django management command to populate the Qualitation website with content.
Updated with complete content from Qualitation_Complete_Website_Content.docx
"""

from django.core.management.base import BaseCommand
from wagtail.models import Page, Site
from home.models import (
    HomePage, FlexiblePage, HeaderMenu, HeaderTopLink, HeaderMainLink,
    HeaderISOStandard, HeaderISODropdownItem, FooterMenu, FooterColumn,
    FooterLink, SiteMenuSettings, FooterSettings
)


class Command(BaseCommand):
    help = 'Populate the Qualitation website with content'

    def create_flexible_page(self, parent, title, slug, intro="", body_content=None):
        """Helper function to create a FlexiblePage"""
        existing = FlexiblePage.objects.filter(slug=slug).first()
        if existing:
            self.stdout.write(f"  - Page '{title}' already exists, updating...")
            existing.title = title
            existing.intro = intro
            if body_content:
                existing.body = body_content
            existing.save_revision().publish()
            return existing

        page = FlexiblePage(
            title=title,
            slug=slug,
            intro=intro,
            body=body_content or []
        )
        parent.add_child(instance=page)
        page.save_revision().publish()
        self.stdout.write(f"  - Created page: {title}")
        return page

    def populate_homepage(self):
        """Update the homepage with Qualitation content"""
        self.stdout.write("\n=== Updating Homepage ===")

        homepage = HomePage.objects.first()
        if not homepage:
            self.stdout.write(self.style.ERROR("ERROR: No homepage found!"))
            return None

        homepage.body = [
            # Hero Carousel Section
            ('carousel', {
                'slides': [
                    {
                        'slide_type': 'image',
                        'heading': 'ISO Certification Consultants',
                        'description': 'The British Quality Centre - Expert ISO consultancy with 100% first-time certification success rate across 25+ years.',
                        'button_text': 'Request a Quote',
                        'button_link': '/contact/',
                        'text_position': 'center',
                    },
                    {
                        'slide_type': 'image',
                        'heading': '100% First-Time Pass Rate',
                        'description': '25+ years of helping businesses achieve ISO certification. 20+ expert consultants operating UK-wide.',
                        'button_text': 'Our Services',
                        'button_link': '/iso-services/',
                        'text_position': 'center',
                    },
                    {
                        'slide_type': 'image',
                        'heading': 'ISO 9001, 14001, 45001 & More',
                        'description': 'Quality, Environmental, Health & Safety management systems. Expert guidance for all major ISO standards.',
                        'button_text': 'View Standards',
                        'button_link': '/iso-standards/',
                        'text_position': 'center',
                    },
                    {
                        'slide_type': 'image',
                        'heading': 'Professional Training Courses',
                        'description': 'Foundation, Internal Auditor and Lead Auditor courses delivered by industry specialists.',
                        'button_text': 'Training Courses',
                        'button_link': '/training/',
                        'text_position': 'center',
                    },
                ],
                'autoplay': True,
                'autoplay_speed': 5000,
                'transition_effect': 'fade',
                'show_dots': True,
                'show_arrows': True,
            }),

            # Introduction Section
            ('paragraph', {
                'content': '''<h2 style="text-align:center;">Your Partner in ISO Certification</h2>
                <p style="text-align:center; max-width:800px; margin:0 auto;">Qualitation (trading name of Oxford Quality Centre Ltd) is an ISO consultancy established in 1998. We boast a <strong>100% first-time certification success rate</strong> across 25+ years of operation with 20+ consultants operating UK-wide. Academic research shows ISO certified organisations are more efficient, successful, and profitable.</p>''',
                'alignment': 'center',
            }),

            # Services Cards - ISO Standards
            ('service_cards', {
                'heading': 'Our ISO Certification Services',
                'subheading': '<p>Comprehensive consultancy for all major ISO management system standards</p>',
                'cards': [
                    {
                        'title': 'ISO 9001',
                        'description': 'Quality Management System - Over 2.1 million companies certified across 170 countries worldwide.',
                        'icon': 'fa-certificate',
                        'link': None,
                    },
                    {
                        'title': 'ISO 14001',
                        'description': 'Environmental Management System - The second most popular standard globally for sustainability.',
                        'icon': 'fa-leaf',
                        'link': None,
                    },
                    {
                        'title': 'ISO 27001',
                        'description': 'Information Security Management - Ensure data is controlled and kept safe.',
                        'icon': 'fa-shield-alt',
                        'link': None,
                    },
                    {
                        'title': 'ISO 45001',
                        'description': 'Health & Safety Management - Protect your workforce with formalised safety documentation.',
                        'icon': 'fa-hard-hat',
                        'link': None,
                    },
                    {
                        'title': 'AS9100 Series',
                        'description': 'Aerospace Quality Management - For Aviation, Space and Defence industries.',
                        'icon': 'fa-plane',
                        'link': None,
                    },
                    {
                        'title': 'IATF 16949',
                        'description': 'Automotive Quality - Essential for automotive industry suppliers.',
                        'icon': 'fa-car',
                        'link': None,
                    },
                ],
            }),

            # Why Choose Qualitation
            ('heading', {
                'text': 'Why Choose Qualitation?',
                'level': 'h2',
                'alignment': 'center',
            }),
            ('columns', {
                'columns': [
                    {'content': '<h4>100% Success Rate</h4><p>25+ years of first-time certification success. We work with you until you succeed.</p>'},
                    {'content': '<h4>20+ Expert Consultants</h4><p>Nationwide network of qualified Qualitators with real industry experience.</p>'},
                    {'content': '<h4>Established 1998</h4><p>Trusted ISO consultancy with proven track record across all major standards.</p>'},
                ],
            }),

            # How It Works - Beautiful Process Steps
            ('html', {
                'html': '''
<section class="process-section">
    <div class="process-container">
        <h2 style="text-align: center; font-size: 2.5rem; font-weight: 800; margin-bottom: 1rem; color: #1e293b;">Our Three-Stage Guaranteed Process</h2>
        <p style="text-align: center; font-size: 1.1rem; color: #64748b; max-width: 700px; margin: 0 auto 2rem;">20+ years of 100% first-time pass rate with our proven certification process</p>

        <div class="process-steps">
            <div class="process-step">
                <div class="step-number">1</div>
                <div class="step-content">
                    <h3 class="step-title">Design & Create</h3>
                    <p class="step-description">Discussions between your team and Qualitator. Minimal disruption with maximum effect, keeping existing procedures where possible.</p>
                </div>
            </div>

            <div class="process-step">
                <div class="step-number">2</div>
                <div class="step-content">
                    <h3 class="step-title">Install & Stage 1</h3>
                    <p class="step-description">Systems drawn up, awareness training provided. Stage 1 assessment by certifiers checking systems match ISO requirements.</p>
                </div>
            </div>

            <div class="process-step">
                <div class="step-number">3</div>
                <div class="step-content">
                    <h3 class="step-title">Certification</h3>
                    <p class="step-description">Procedures used, records kept. Internal Audit training, Management Review guidance. Stage 2 assessment and certificate issued.</p>
                </div>
            </div>

            <div class="process-step">
                <div class="step-number">4</div>
                <div class="step-content">
                    <h3 class="step-title">Internal Audits</h3>
                    <p class="step-description">Periodic reviews of all procedures. Focus on finding improvements, not a witch-hunt. Training provided for your auditors.</p>
                </div>
            </div>

            <div class="process-step">
                <div class="step-number">5</div>
                <div class="step-content">
                    <h3 class="step-title">Ongoing Support</h3>
                    <p class="step-description">Management reviews, surveillance audits, and continuous improvement support to maintain certification.</p>
                </div>
            </div>
        </div>
    </div>
</section>
''',
            }),

            # Testimonials Slider
            ('testimonial_slider', {
                'heading': 'What Our Clients Say',
                'subheading': 'Trusted by organisations across the UK',
                'testimonials': [
                    {
                        'quote': 'The BSi auditor was impressed with how prepared we were and advised that this was the first instance she had seen in 2 years where there had not been a single non-conformance at either stage 1 or stage 2 audits.',
                        'author': 'Chantal Watling',
                        'author_title': 'Quality Manager, Wolfram',
                        'rating': 5,
                    },
                    {
                        'quote': 'Your experience in the aerospace industry proved very useful and made a significant contribution to our efforts to achieve certification.',
                        'author': 'AirTanker Services Ltd',
                        'author_title': 'Aerospace Client',
                        'rating': 5,
                    },
                    {
                        'quote': 'Following Qualitation\'s work, the UK Accreditation Service (UKAS) assessor said our quality manual was one of the best they\'d ever seen.',
                        'author': 'Mark Craven',
                        'author_title': 'Director, Control Plant',
                        'rating': 5,
                    },
                    {
                        'quote': 'I\'ve worked with Geoff over a number of years and greatly value his integrity and pragmatic approach to helping companies achieve better results.',
                        'author': 'Ian Walker Ltd',
                        'author_title': 'Business Client',
                        'rating': 5,
                    },
                    {
                        'quote': 'The integrity was never in question, he was easy to get on with and his expert guidance was always well thought through.',
                        'author': 'Gary Nevison',
                        'author_title': 'Business Client',
                        'rating': 5,
                    },
                ],
                'autoplay': True,
                'autoplay_speed': 5000,
            }),

            # FAQ Section
            ('heading', {
                'text': 'Frequently Asked Questions',
                'level': 'h2',
                'alignment': 'center',
            }),
            ('accordion', {
                'items': [
                    {
                        'title': 'What is an ISO standard?',
                        'content': '<p>An ISO standard is a set of requirements that any organisation can adopt voluntarily. These requirements have been developed by a network of international experts to represent the current consensus on best practice in specific areas of business operation.</p>',
                    },
                    {
                        'title': 'How long does ISO certification take?',
                        'content': '<p>This depends on the complexity of your operations and which standard(s) you are seeking. A small company seeking ISO 9001 might achieve certification in 2-3 months. Larger organisations or those seeking multiple standards may take 6-12 months.</p>',
                    },
                    {
                        'title': 'How much does ISO certification cost?',
                        'content': '<p>Costs vary based on scope, number of standards, personnel/sites, installation method, and timeframe. Simple organisations may need 5-8 consultant days, while complex organisations may need 100+ days. Qualitation provides transparent pricing: day rate × number of days.</p>',
                    },
                    {
                        'title': 'What is a certification body?',
                        'content': '<p>The Certification Body (CB) assesses systems against ISO standard criteria. CBs should be UKAS-accredited, aligning with the official ISO structure. Non-UKAS accredited bodies are not recommended.</p>',
                    },
                    {
                        'title': 'How long is ISO certification valid?',
                        'content': '<p>After obtaining UKAS-accredited certification, it\'s valid for about a year (possibly 14 months) before needing re-assessment. Annual surveillance audits are also typically required.</p>',
                    },
                    {
                        'title': 'Can I implement ISO myself?',
                        'content': '<p>Yes, but self-implementation takes more time and lacks consultant insights. Consultants offer efficiency, experience, fresh perspectives, and timely readiness for certification assessments.</p>',
                    },
                ],
            }),

            # CTA Section
            ('hero', {
                'heading': 'Ready to Get Started?',
                'subheading': '<p>Contact us today for a free, no-obligation consultation. We\'ll discuss your requirements and provide a clear proposal for achieving ISO certification.</p>',
                'cta_text': 'Request a Quote',
                'cta_link': None,
                'secondary_cta_text': 'Call 0345 600 6975',
                'secondary_cta_link': 'tel:03456006975',
            }),

            # Contact Form
            ('contact_form', {
                'heading': 'Get in Touch',
                'subheading': 'Fill in the form below and we\'ll get back to you within 24 hours',
                'background_color': 'light-blue',
            }),
        ]

        homepage.save_revision().publish()
        self.stdout.write(self.style.SUCCESS("  - Homepage updated with Qualitation content"))
        return homepage

    def create_pages(self):
        """Create all the content pages"""
        self.stdout.write("\n=== Creating Content Pages ===")

        homepage = HomePage.objects.first()
        if not homepage:
            self.stdout.write(self.style.ERROR("ERROR: No homepage found!"))
            return

        # ==================== ABOUT US PAGE ====================
        about_page = self.create_flexible_page(
            parent=homepage,
            title="About Us",
            slug="about-us",
            intro="",
            body_content=[
                ('heading', {'text': 'About Qualitation', 'level': 'h1', 'alignment': 'center'}),
                ('paragraph', {
                    'content': '''<p style="text-align:center; font-size:1.2em; max-width:800px; margin:0 auto 2rem;">The British Quality Centre - Established 1998</p>''',
                    'alignment': 'center',
                }),
                ('paragraph', {
                    'content': '''<p>Qualitation (trading name of Oxford Quality Centre Ltd) is an ISO consultancy established in 1998. The company boasts a <strong>100% first-time certification success rate</strong> across 25+ years of operation with 20+ consultants operating UK-wide.</p>

                    <p>Academic research shows ISO 9001 certified organisations are more efficient, successful, and profitable. We help businesses achieve these benefits through expert guidance and practical implementation.</p>''',
                    'alignment': 'left',
                }),
                ('heading', {'text': 'Company Details', 'level': 'h2', 'alignment': 'left'}),
                ('columns', {
                    'columns': [
                        {'content': '''<h4>Registration</h4>
                            <p><strong>Company No:</strong> 08265550<br>
                            (England and Wales)</p>
                            <p><strong>Director:</strong> Carl Kruger</p>'''},
                        {'content': '''<h4>Contact</h4>
                            <p><strong>Phone:</strong> 0345 600 6975</p>
                            <p><strong>Email:</strong> enquiries@qualitation.co.uk</p>'''},
                        {'content': '''<h4>Address</h4>
                            <p>66 Elms Drive<br>
                            Oxford, OX3 0NL</p>'''},
                    ],
                }),
                ('heading', {'text': 'Our Qualitators', 'level': 'h2', 'alignment': 'left'}),
                ('paragraph', {
                    'content': '''<p>We call our consultants "Qualitators" - experts who are passionate about quality and helping organisations succeed. Our nationwide network brings:</p>
                    <ul>
                        <li>Real industry experience across multiple sectors</li>
                        <li>Professional qualifications (Lead Auditor, IRCA registered)</li>
                        <li>A practical, no-nonsense approach to implementation</li>
                        <li>Commitment to your success - we have a 100% first-time pass rate</li>
                    </ul>''',
                    'alignment': 'left',
                }),
                ('contact_form', {
                    'heading': 'Work With Us',
                    'subheading': 'Contact us to discuss your ISO certification needs',
                    'background_color': 'light-blue',
                }),
            ]
        )

        # ==================== CONTACT PAGE ====================
        contact_page = self.create_flexible_page(
            parent=homepage,
            title="Contact Us",
            slug="contact",
            intro="",
            body_content=[
                ('heading', {'text': 'Contact Qualitation', 'level': 'h1', 'alignment': 'center'}),
                ('paragraph', {
                    'content': '''<p style="text-align: center; font-size: 1.2em;">Get in touch with our team to discuss your ISO certification requirements.<br>We offer a free, no-obligation consultation to understand your needs.</p>''',
                    'alignment': 'center',
                }),
                ('columns', {
                    'columns': [
                        {'content': '''<h3>Phone</h3>
                            <p><strong style="font-size:1.3em;">0345 600 6975</strong></p>
                            <p>Monday - Friday: 9am - 5pm</p>'''},
                        {'content': '''<h3>Email</h3>
                            <p><strong>enquiries@qualitation.co.uk</strong></p>
                            <p>We respond within 24 hours</p>'''},
                        {'content': '''<h3>Address</h3>
                            <p>66 Elms Drive<br>Oxford, OX3 0NL</p>
                            <p>Consultants available UK-wide</p>'''},
                    ],
                }),
                ('contact_form', {
                    'heading': 'Send Us a Message',
                    'subheading': 'Fill in the form below and we\'ll get back to you shortly',
                    'background_color': 'white',
                }),
            ]
        )

        # ==================== ISO SERVICES PARENT PAGE ====================
        iso_services_page = self.create_flexible_page(
            parent=homepage,
            title="ISO Services",
            slug="iso-services",
            intro="",
            body_content=[
                ('heading', {'text': 'Our ISO Consultancy Services', 'level': 'h1', 'alignment': 'center'}),
                ('paragraph', {
                    'content': '''<p style="text-align:center; max-width:800px; margin:0 auto;">From initial advice through to certification and ongoing support, Qualitation provides comprehensive ISO consultancy services.</p>''',
                    'alignment': 'center',
                }),
                ('service_cards', {
                    'heading': '',
                    'subheading': '',
                    'cards': [
                        {'title': 'Advice & Assessment', 'description': 'Deciding if ISO is right for you. Understanding costs, benefits, and requirements.', 'icon': 'fa-lightbulb'},
                        {'title': 'Design & Installation', 'description': 'Three-stage guaranteed certification process with 100% first-time pass rate.', 'icon': 'fa-cogs'},
                        {'title': 'Internal Audit Assistance', 'description': 'Audit training and support for your team. Supervised audits available.', 'icon': 'fa-clipboard-check'},
                        {'title': 'Management Reviews', 'description': 'Guidance on ISO-required management review meetings and continuous improvement.', 'icon': 'fa-users'},
                        {'title': 'Rescue Service', 'description': 'Emergency assistance when you find yourself in a fix with certification.', 'icon': 'fa-life-ring'},
                        {'title': 'Pre & Post Assessment', 'description': 'Reviews before certification and assistance with non-conformances.', 'icon': 'fa-search'},
                    ],
                }),
            ]
        )

        # ==================== ISO STANDARDS PARENT PAGE ====================
        iso_standards_page = self.create_flexible_page(
            parent=homepage,
            title="ISO Standards",
            slug="iso-standards",
            intro="",
            body_content=[
                ('heading', {'text': 'ISO Certification Standards', 'level': 'h1', 'alignment': 'center'}),
                ('paragraph', {
                    'content': '''<p style="text-align:center; max-width:800px; margin:0 auto;">ISO (International Organization for Standardization) is an independent, non-governmental body with 162 national standards organisations as members. We provide expert consultancy for all major standards.</p>''',
                    'alignment': 'center',
                }),
                ('service_cards', {
                    'heading': 'Quality+ Standards',
                    'subheading': '<p>The core management system standards</p>',
                    'cards': [
                        {'title': 'ISO 9001', 'description': 'Quality Management - Over 2.1 million companies certified in 170 countries.', 'icon': 'fa-certificate'},
                        {'title': 'ISO 14001', 'description': 'Environmental Management - The second most popular standard globally.', 'icon': 'fa-leaf'},
                        {'title': 'ISO 45001', 'description': 'Health & Safety Management - Replaces OHSAS 18001.', 'icon': 'fa-hard-hat'},
                        {'title': 'ISO 27001', 'description': 'Information Security - Ensures data is controlled and kept safe.', 'icon': 'fa-shield-alt'},
                    ],
                }),
                ('service_cards', {
                    'heading': 'Industry-Specific Standards',
                    'subheading': '<p>Specialist standards for regulated industries</p>',
                    'cards': [
                        {'title': 'AS9100 Series', 'description': 'Aerospace - Manufacturing, Maintenance & Distribution standards.', 'icon': 'fa-plane'},
                        {'title': 'IATF 16949', 'description': 'Automotive - Essential for automotive industry suppliers.', 'icon': 'fa-car'},
                        {'title': 'ISO 13485', 'description': 'Medical Devices - Supports CE marking for EU sales.', 'icon': 'fa-medkit'},
                        {'title': 'ISO 17025', 'description': 'Laboratory Competence - For scientific research settings.', 'icon': 'fa-flask'},
                    ],
                }),
            ]
        )

        # ==================== ISO 9001 PAGE ====================
        iso9001_page = self.create_flexible_page(
            parent=iso_standards_page,
            title="ISO 9001 Quality Management",
            slug="iso-9001",
            intro="",
            body_content=[
                ('hero', {
                    'heading': 'ISO 9001 Quality Management System',
                    'subheading': '<p>Over 2.1 million companies certified across 170 countries. The world\'s most recognised quality management standard.</p>',
                    'cta_text': 'Get a Quote',
                    'secondary_cta_text': 'Call Us',
                    'secondary_cta_link': 'tel:03456006975',
                }),
                ('heading', {'text': 'What is ISO 9001?', 'level': 'h2', 'alignment': 'left'}),
                ('paragraph', {
                    'content': '''<p>ISO 9001 is the internationally recognised Quality Management System standard. Academic research shows ISO 9001 certified organisations are more efficient, successful, and profitable.</p>''',
                    'alignment': 'left',
                }),
                ('heading', {'text': 'Benefits of ISO 9001', 'level': 'h2', 'alignment': 'left'}),
                ('columns', {
                    'columns': [
                        {'content': '''<h4>Internal Benefits</h4>
                            <ul>
                                <li>Process optimisation for quality assurance</li>
                                <li>Enhanced collaboration and problem-solving</li>
                                <li>Elevated staff morale</li>
                                <li>Alignment with organisational goals</li>
                            </ul>'''},
                        {'content': '''<h4>Strategic Benefits</h4>
                            <ul>
                                <li>Strategic procedure control</li>
                                <li>Empowered staff and loyalty</li>
                                <li>Client advocacy and retention</li>
                                <li>Industry acknowledgement of excellence</li>
                            </ul>'''},
                        {'content': '''<h4>Compliance Benefits</h4>
                            <ul>
                                <li>Mandatory in specific sectors</li>
                                <li>Industry prerequisite (aviation/aerospace)</li>
                                <li>Reduced oversight from authorities</li>
                                <li>UK Government contract requirements</li>
                            </ul>'''},
                    ],
                }),
                ('heading', {'text': 'Certification Process', 'level': 'h2', 'alignment': 'left'}),
                ('paragraph', {
                    'content': '''<ol>
                        <li><strong>Initiation</strong> - Free assessment discussion to understand your systems</li>
                        <li><strong>Collaborative Development</strong> - Design and create your QMS with minimal disruption</li>
                        <li><strong>Stage 1 Assessment</strong> - Certifiers check systems as written meet ISO requirements</li>
                        <li><strong>Stage 2 Evaluation</strong> - Verify systems as used through records review</li>
                    </ol>''',
                    'alignment': 'left',
                }),
                ('accordion', {
                    'items': [
                        {'title': 'Can ISO 9001 be integrated with other standards?', 'content': '<p>Yes, it can be integrated with ISO 14001, ISO 45001, and other standards to create a unified management system (Quality+).</p>'},
                        {'title': 'Is there a size requirement?', 'content': '<p>No, ISO 9001 is valid for all organisation sizes, from single-person setups to multinationals.</p>'},
                        {'title': 'How long is certification valid?', 'content': '<p>Certification is valid for about a year (possibly 14 months) before re-assessment. Annual surveillance audits are required.</p>'},
                        {'title': 'What is a UKAS-accredited certification body?', 'content': '<p>UKAS (UK Accreditation Service) accredits certification bodies to ensure they meet international standards. Always choose UKAS-accredited certification.</p>'},
                    ],
                }),
                ('contact_form', {'heading': 'Get Started with ISO 9001', 'subheading': 'Request a free consultation', 'background_color': 'light-blue'}),
            ]
        )

        # ==================== ISO 14001 PAGE ====================
        iso14001_page = self.create_flexible_page(
            parent=iso_standards_page,
            title="ISO 14001 Environmental Management",
            slug="iso-14001",
            intro="",
            body_content=[
                ('hero', {
                    'heading': 'ISO 14001 Environmental Management System',
                    'subheading': '<p>The second most popular ISO standard globally. Demonstrate your commitment to sustainability.</p>',
                    'cta_text': 'Get a Quote',
                    'secondary_cta_text': 'Call Us',
                    'secondary_cta_link': 'tel:03456006975',
                }),
                ('heading', {'text': 'Make an Impact While Reducing Yours', 'level': 'h2', 'alignment': 'left'}),
                ('paragraph', {
                    'content': '''<p>ISO 14001 covers environmental management and monitoring across all operational areas: procurement, storage, distribution, product development, production, manufacturing, and marketing.</p>
                    <p>BSI reports that <strong>60% of companies measure increased customer trust</strong> after achieving ISO 14001 certification.</p>''',
                    'alignment': 'left',
                }),
                ('heading', {'text': 'Required Registers', 'level': 'h2', 'alignment': 'left'}),
                ('columns', {
                    'columns': [
                        {'content': '''<h4>Legal Register</h4>
                            <p>Documentation of all environmental legislation affecting your business operations.</p>'''},
                        {'content': '''<h4>Environmental Impacts Register</h4>
                            <p>Potential impacts of your activities including climate change considerations and how they are addressed.</p>'''},
                    ],
                }),
                ('heading', {'text': 'Benefits', 'level': 'h2', 'alignment': 'left'}),
                ('paragraph', {
                    'content': '''<ul>
                        <li>Increased brand advocacy</li>
                        <li>Enhanced reputation</li>
                        <li>Improved employee engagement</li>
                        <li>Increased sales through environmental credentials</li>
                        <li>Competitive advantage in tenders</li>
                    </ul>''',
                    'alignment': 'left',
                }),
                ('contact_form', {'heading': 'Get Started with ISO 14001', 'subheading': 'Request a free consultation', 'background_color': 'light-blue'}),
            ]
        )

        # ==================== ISO 45001 PAGE ====================
        iso45001_page = self.create_flexible_page(
            parent=iso_standards_page,
            title="ISO 45001 Health & Safety",
            slug="iso-45001",
            intro="",
            body_content=[
                ('hero', {
                    'heading': 'ISO 45001 Health & Safety Management',
                    'subheading': '<p>The international standard for occupational health and safety. Replaces OHSAS 18001.</p>',
                    'cta_text': 'Get a Quote',
                    'secondary_cta_text': 'Call Us',
                    'secondary_cta_link': 'tel:03456006975',
                }),
                ('heading', {'text': 'Look After Your People', 'level': 'h2', 'alignment': 'left'}),
                ('paragraph', {
                    'content': '''<p>ISO 45001 covers all workplace risks including desk injuries, stair accidents, road incidents, and hazardous materials. It formalises your approach to health and safety using thorough documentation, verified by a third party.</p>''',
                    'alignment': 'left',
                }),
                ('heading', {'text': 'Required Registers', 'level': 'h2', 'alignment': 'left'}),
                ('columns', {
                    'columns': [
                        {'content': '''<h4>Legal Register</h4>
                            <p>Document outlining current health and safety laws applicable to your operations.</p>'''},
                        {'content': '''<h4>Risk & Hazard Register</h4>
                            <p>Ledger detailing risks and hazards for each team member and role.</p>'''},
                    ],
                }),
                ('heading', {'text': 'Benefits', 'level': 'h2', 'alignment': 'left'}),
                ('paragraph', {
                    'content': '''<ul>
                        <li>Efficient documentation verified by third party</li>
                        <li>Compliance with changing laws</li>
                        <li>Protection of your workforce</li>
                        <li>Reduced workplace incidents</li>
                        <li>Improved employee confidence and morale</li>
                    </ul>''',
                    'alignment': 'left',
                }),
                ('contact_form', {'heading': 'Get Started with ISO 45001', 'subheading': 'Request a free consultation', 'background_color': 'light-blue'}),
            ]
        )

        # ==================== ISO 27001 PAGE ====================
        iso27001_page = self.create_flexible_page(
            parent=iso_standards_page,
            title="ISO 27001 Information Security",
            slug="iso-27001",
            intro="",
            body_content=[
                ('hero', {
                    'heading': 'ISO 27001 Information Security Management',
                    'subheading': '<p>Ensure your data is controlled and kept safe with the leading information security standard.</p>',
                    'cta_text': 'Get a Quote',
                    'secondary_cta_text': 'Call Us',
                    'secondary_cta_link': 'tel:03456006975',
                }),
                ('heading', {'text': 'Ensuring Data is Secure', 'level': 'h2', 'alignment': 'left'}),
                ('paragraph', {
                    'content': '''<p>ISO 27001 is the specification for an Information Security Management System (ISMS). It ensures data held by companies is controlled and kept safe, especially individual-related data.</p>''',
                    'alignment': 'left',
                }),
                ('heading', {'text': 'Coverage Areas', 'level': 'h2', 'alignment': 'left'}),
                ('columns', {
                    'columns': [
                        {'content': '''<h4>Physical Damage</h4>
                            <p>Water, fire, and environmental threats to data storage.</p>'''},
                        {'content': '''<h4>Electronic Damage</h4>
                            <p>Hacking, viruses, and electronic failures.</p>'''},
                    ],
                }),
                ('columns', {
                    'columns': [
                        {'content': '''<h4>Inappropriate Release</h4>
                            <p>Accidental or malicious data breaches.</p>'''},
                        {'content': '''<h4>Data Loss</h4>
                            <p>Backups, copies, theft, and mislaid data.</p>'''},
                    ],
                }),
                ('heading', {'text': 'Management Requirements', 'level': 'h2', 'alignment': 'left'}),
                ('paragraph', {
                    'content': '''<ul>
                        <li>Systematically examine information security risks</li>
                        <li>Assess threats, vulnerabilities and impacts</li>
                        <li>Determine framework for best practice</li>
                        <li>Protect customer and staff information</li>
                    </ul>
                    <p><strong>GDPR:</strong> ISO 27001 is a strong step in dealing with GDPR legislation.</p>
                    <p><strong>27k1 ISMS:</strong> We offer a cloud-based programme for SMEs from £110/month.</p>''',
                    'alignment': 'left',
                }),
                ('contact_form', {'heading': 'Get Started with ISO 27001', 'subheading': 'Request a free consultation', 'background_color': 'light-blue'}),
            ]
        )

        # ==================== AEROSPACE STANDARDS PAGE ====================
        aerospace_page = self.create_flexible_page(
            parent=iso_standards_page,
            title="Aerospace Standards",
            slug="aerospace",
            intro="",
            body_content=[
                ('hero', {
                    'heading': 'Aviation, Space & Defence Standards',
                    'subheading': '<p>AS9100, AS9110 & AS9120 - Quality management for heavily regulated sectors where lives are at stake.</p>',
                    'cta_text': 'Get a Quote',
                    'secondary_cta_text': 'Call Us',
                    'secondary_cta_link': 'tel:03456006975',
                }),
                ('paragraph', {
                    'content': '''<p>The AS series are standards specific to Aviation, Space and Defence industries. All AS standards incorporate ISO 9001 but are adapted for these sectors with additional focus on risk management and quality.</p>''',
                    'alignment': 'left',
                }),
                ('heading', {'text': 'AS9100 - Aerospace Manufacturing', 'level': 'h2', 'alignment': 'left'}),
                ('paragraph', {
                    'content': '''<p>For manufacturing in Aviation, Space and Defence. Ensures products meet customer and industry requirements.</p>
                    <ul>
                        <li>Clear instructions for each manufacturing stage (skills, tools, calibrations, materials)</li>
                        <li>Ability to trace equipment through supply chain</li>
                        <li>Permits third party audits and assessment</li>
                        <li>Enhanced knowledge through continuous improvement</li>
                        <li>Improved efficiency minimising waste</li>
                    </ul>''',
                    'alignment': 'left',
                }),
                ('heading', {'text': 'AS9110 - Aerospace Maintenance', 'level': 'h2', 'alignment': 'left'}),
                ('paragraph', {
                    'content': '''<p>Maintenance element for aerospace. Vital because aerospace products last decades.</p>
                    <ul>
                        <li>Reduction in risk of faults during maintenance</li>
                        <li>Reduction in undetected faults from maintenance process</li>
                        <li>Improved performance against competitors</li>
                        <li>Staff trained to operate correctly = improved morale</li>
                    </ul>''',
                    'alignment': 'left',
                }),
                ('heading', {'text': 'AS9120 - Aerospace Distribution', 'level': 'h2', 'alignment': 'left'}),
                ('paragraph', {
                    'content': '''<p>For stocking and distribution of aerospace components (gauges, gaskets, fasteners, wings, landing gear, navigational arrays). Adds 100+ extra requirements to AS9100.</p>
                    <p><strong>Applicable to:</strong> Companies buying/selling parts, assemblers, warehousing aerospace components. NOT for repairers or reworkers.</p>''',
                    'alignment': 'left',
                }),
                ('contact_form', {'heading': 'Get Started with AS Standards', 'subheading': 'Request a free consultation', 'background_color': 'light-blue'}),
            ]
        )

        # ==================== AUTOMOTIVE IATF 16949 PAGE ====================
        automotive_page = self.create_flexible_page(
            parent=iso_standards_page,
            title="IATF 16949 Automotive",
            slug="iatf-16949",
            intro="",
            body_content=[
                ('hero', {
                    'heading': 'IATF 16949 Automotive Quality',
                    'subheading': '<p>The automotive industry quality management standard. Essential for automotive suppliers.</p>',
                    'cta_text': 'Get a Quote',
                    'secondary_cta_text': 'Call Us',
                    'secondary_cta_link': 'tel:03456006975',
                }),
                ('paragraph', {
                    'content': '''<p>IATF 16949 (formerly ISO/TS 16949) was developed from ISO 9001 and adapted for the Automotive industry by key industry players. Now managed by the International Automotive Task Force (IATF).</p>
                    <p><strong>Scope:</strong> Design, development, production, installation, and service of automotive-related products. Suppliers are effectively obliged to get this standard for long-term industry participation.</p>''',
                    'alignment': 'left',
                }),
                ('heading', {'text': 'Key Requirements', 'level': 'h2', 'alignment': 'left'}),
                ('paragraph', {
                    'content': '''<ul>
                        <li>Customer feedback monitoring</li>
                        <li>Working with sub-contractors</li>
                        <li>Regular management reviews</li>
                        <li>Supply chain efficiencies</li>
                        <li>Order processing and reliability</li>
                    </ul>''',
                    'alignment': 'left',
                }),
                ('contact_form', {'heading': 'Get Started with IATF 16949', 'subheading': 'Request a free consultation', 'background_color': 'light-blue'}),
            ]
        )

        # ==================== MEDICAL DEVICES PAGE ====================
        medical_page = self.create_flexible_page(
            parent=iso_standards_page,
            title="Medical Device Standards",
            slug="medical-devices",
            intro="",
            body_content=[
                ('hero', {
                    'heading': 'Medical Device & Laboratory Standards',
                    'subheading': '<p>ISO 13485, ISO 17025, ISO 15189 and CE Marking for regulated medical and laboratory environments.</p>',
                    'cta_text': 'Get a Quote',
                    'secondary_cta_text': 'Call Us',
                    'secondary_cta_link': 'tel:03456006975',
                }),
                ('heading', {'text': 'ISO 13485 - Medical Devices', 'level': 'h2', 'alignment': 'left'}),
                ('paragraph', {
                    'content': '''<p>For businesses providing medical devices and related services – design, development, production, installation, servicing. <strong>Supports CE marking for EU medical device sales.</strong></p>
                    <ul>
                        <li>Framework for customer feedback</li>
                        <li>React to feedback appropriately</li>
                        <li>Regular management review</li>
                        <li>In-house operations satisfy customer needs</li>
                    </ul>''',
                    'alignment': 'left',
                }),
                ('heading', {'text': 'ISO 17025 - Laboratory Competence', 'level': 'h2', 'alignment': 'left'}),
                ('paragraph', {
                    'content': '''<p>For scientific research settings, universities, research centres, governments, regulators, inspection bodies, product certification organisations.</p>
                    <p><strong>Benefits:</strong> Demonstrate competent operation and valid results, globally recognised, only assessed by UKAS in UK.</p>''',
                    'alignment': 'left',
                }),
                ('heading', {'text': 'ISO 15189 - Medical Laboratory Competence', 'level': 'h2', 'alignment': 'left'}),
                ('paragraph', {
                    'content': '''<p>Based on ISO 17025 with additional requirements for medical laboratory environments. Relevant to toxicology, haematology, genetics, pathology.</p>''',
                    'alignment': 'left',
                }),
                ('heading', {'text': 'CE Marking for Medical Devices', 'level': 'h2', 'alignment': 'left'}),
                ('paragraph', {
                    'content': '''<p>CE Marking indicates healthcare appliances meet legislative requirements. <strong>Legal requirement for sale of many medical devices within EU.</strong> Based on ISO 13485 certification.</p>''',
                    'alignment': 'left',
                }),
                ('contact_form', {'heading': 'Get Started with Medical Standards', 'subheading': 'Request a free consultation', 'background_color': 'light-blue'}),
            ]
        )

        # ==================== CYBER ESSENTIALS PAGE ====================
        cyber_page = self.create_flexible_page(
            parent=iso_standards_page,
            title="Cyber Essentials",
            slug="cyber-essentials",
            intro="",
            body_content=[
                ('hero', {
                    'heading': 'Cyber Essentials',
                    'subheading': '<p>Government-backed cyber security certification. A good first step for GDPR compliance.</p>',
                    'cta_text': 'Get a Quote',
                    'secondary_cta_text': 'Call Us',
                    'secondary_cta_link': 'tel:03456006975',
                }),
                ('paragraph', {
                    'content': '''<p>Cyber Essentials was developed by Government with industry. It is NOT an ISO standard but covers some ISO 27001 material. Suitable where full ISO 27001 is overkill and a good first step for GDPR compliance.</p>''',
                    'alignment': 'left',
                }),
                ('heading', {'text': 'Five Key Controls', 'level': 'h2', 'alignment': 'left'}),
                ('paragraph', {
                    'content': '''<ol>
                        <li><strong>Boundary Firewalls and Internet Gateways</strong> - Protecting your network perimeter</li>
                        <li><strong>Secure Configuration</strong> - Configuring systems securely</li>
                        <li><strong>Access Control</strong> - Managing user access appropriately</li>
                        <li><strong>Malware Protection</strong> - Defending against malicious software</li>
                        <li><strong>Patch Management</strong> - Keeping software up to date</li>
                    </ol>''',
                    'alignment': 'left',
                }),
                ('contact_form', {'heading': 'Get Cyber Essentials Certified', 'subheading': 'Request a free consultation', 'background_color': 'light-blue'}),
            ]
        )

        # ==================== QUALITY+ PAGE ====================
        qualityplus_page = self.create_flexible_page(
            parent=homepage,
            title="Quality+",
            slug="quality-plus",
            intro="",
            body_content=[
                ('hero', {
                    'heading': 'Quality+ Integrated Management System',
                    'subheading': '<p>ISO 9001 + ISO 14001 + ISO 45001 combined into one efficient management system.</p>',
                    'cta_text': 'Get a Quote',
                    'secondary_cta_text': 'Learn More',
                    'secondary_cta_link': '#benefits',
                }),
                ('heading', {'text': 'What is Quality+?', 'level': 'h2', 'alignment': 'left'}),
                ('paragraph', {
                    'content': '''<p>Quality+ links ISO 9001 Quality Management to ISO 14001 Environmental and ISO 45001 Health & Safety in an Integrated Management System (IMS).</p>
                    <p>Instead of maintaining three separate systems, Quality+ allows you to manage quality, environment, and health & safety through one unified approach - reducing duplication and streamlining processes.</p>''',
                    'alignment': 'left',
                }),
                ('heading', {'text': 'Benefits', 'level': 'h2', 'alignment': 'left'}),
                ('columns', {
                    'columns': [
                        {'content': '''<h4>Efficiency</h4><p>Single management system, single set of procedures, single internal audit programme.</p>'''},
                        {'content': '''<h4>Cost Savings</h4><p>Reduced documentation, fewer audit days, streamlined training requirements.</p>'''},
                        {'content': '''<h4>Simplicity</h4><p>One management review, one improvement plan, one system to maintain.</p>'''},
                    ],
                }),
                ('contact_form', {'heading': 'Get Started with Quality+', 'subheading': 'Discuss an integrated management system for your organisation', 'background_color': 'light-blue'}),
            ]
        )

        # ==================== GROWTH & EFFICIENCY PAGE ====================
        growth_page = self.create_flexible_page(
            parent=homepage,
            title="Growth & Efficiency",
            slug="growth-efficiency",
            intro="",
            body_content=[
                ('heading', {'text': 'Growth & Efficiency Consultancy', 'level': 'h1', 'alignment': 'center'}),
                ('paragraph', {
                    'content': '''<p style="text-align:center; max-width:800px; margin:0 auto;">Areas of consultancy that build on existing systems to enhance performance, returns, effectiveness and enjoyment while undertaking day-to-day operations.</p>''',
                    'alignment': 'center',
                }),
                ('service_cards', {
                    'heading': '',
                    'subheading': '',
                    'cards': [
                        {'title': 'Lean Management', 'description': 'Continuous improvement through ongoing small changes with compounding impact.', 'icon': 'fa-stream'},
                        {'title': 'Six Sigma', 'description': 'Improve processes by decreasing variability and increasing performance.', 'icon': 'fa-chart-line'},
                        {'title': 'Team Building', 'description': 'Optimise results by recognising different roles people are suited for.', 'icon': 'fa-users'},
                        {'title': 'Productivity', 'description': 'Improve the relationship between resource use and output levels.', 'icon': 'fa-tachometer-alt'},
                        {'title': 'Psychological Testing', 'description': 'Determine capabilities and best role placement for team members.', 'icon': 'fa-brain'},
                        {'title': 'Change Management', 'description': 'Tools and techniques for managing smooth organisational transitions.', 'icon': 'fa-exchange-alt'},
                    ],
                }),
            ]
        )

        # ==================== LEAN MANAGEMENT PAGE ====================
        lean_page = self.create_flexible_page(
            parent=growth_page,
            title="Lean Management",
            slug="lean-management",
            intro="",
            body_content=[
                ('heading', {'text': 'Lean Management', 'level': 'h1', 'alignment': 'center'}),
                ('paragraph', {
                    'content': '''<p>Lean Management is continuous improvement through ongoing small changes. Each aspect is reviewed periodically to determine what can be improved for better results - more efficient, more effective, with less resource use. Small changes have a ripple effect with compounding impact over time.</p>''',
                    'alignment': 'left',
                }),
                ('heading', {'text': 'Five Key Areas', 'level': 'h2', 'alignment': 'left'}),
                ('columns', {
                    'columns': [
                        {'content': '''<h4>Customer Value</h4><p>Understanding what the customer seeks to enhance value.</p>'''},
                        {'content': '''<h4>Value Stream</h4><p>Product life cycle from sourcing to disposal - understanding value at each step.</p>'''},
                    ],
                }),
                ('columns', {
                    'columns': [
                        {'content': '''<h4>Flow</h4><p>Resources used and wastes derived - minimise wastes.</p>'''},
                        {'content': '''<h4>Pull</h4><p>Production made to order not schedule (Just-In-Time).</p>'''},
                    ],
                }),
                ('paragraph', {
                    'content': '''<h4>Perfection</h4><p>Each stage carried out as perfectly as possible - striving for zero defects.</p>''',
                    'alignment': 'left',
                }),
                ('contact_form', {'heading': 'Get Started with Lean', 'subheading': 'Contact us to discuss lean management', 'background_color': 'light-blue'}),
            ]
        )

        # ==================== SIX SIGMA PAGE ====================
        sixsigma_page = self.create_flexible_page(
            parent=growth_page,
            title="Six Sigma",
            slug="six-sigma",
            intro="",
            body_content=[
                ('heading', {'text': 'Six Sigma (6σ)', 'level': 'h1', 'alignment': 'center'}),
                ('paragraph', {
                    'content': '''<p>Six Sigma is a methodology for improving processes by decreasing variability and increasing performance. At 6 sigma level, an organisation controls 99.9999% of production perfectly.</p>''',
                    'alignment': 'left',
                }),
                ('heading', {'text': 'What Six Sigma Drives', 'level': 'h2', 'alignment': 'left'}),
                ('paragraph', {
                    'content': '''<ul>
                        <li>Defect reduction</li>
                        <li>Quality enhancement</li>
                        <li>Staff morale improvement</li>
                        <li>Increased profits</li>
                        <li>Higher customer satisfaction</li>
                    </ul>''',
                    'alignment': 'left',
                }),
                ('heading', {'text': 'Belt Training System', 'level': 'h2', 'alignment': 'left'}),
                ('paragraph', {
                    'content': '''<p>Training progresses through colored 'belts' to become Black Belts. You cannot attain the next belt until actual project completion. This benefits both the organisation (continuous improvement) and staff (externally recognised qualification).</p>''',
                    'alignment': 'left',
                }),
                ('contact_form', {'heading': 'Get Started with Six Sigma', 'subheading': 'Contact us to discuss Six Sigma training', 'background_color': 'light-blue'}),
            ]
        )

        # ==================== TRAINING COURSES PAGE ====================
        training_page = self.create_flexible_page(
            parent=homepage,
            title="Training Courses",
            slug="training",
            intro="",
            body_content=[
                ('heading', {'text': 'ISO Training Courses', 'level': 'h1', 'alignment': 'center'}),
                ('paragraph', {
                    'content': '''<p style="text-align:center;">Courses provided by specialists in each field. Can be held at your organisation, at training locations, or at suitable venues around the country.</p>''',
                    'alignment': 'center',
                }),
                ('heading', {'text': 'ISO 9001 Quality Management', 'level': 'h3', 'alignment': 'left'}),
                ('paragraph', {
                    'content': '''<ul>
                        <li>1 day ISO 9001:2015 Foundation Course</li>
                        <li>2 day ISO 9001:2015 Internal Auditing Course</li>
                        <li>5 day ISO 9001:2015 IRCA Lead Auditor Course</li>
                    </ul>''',
                    'alignment': 'left',
                }),
                ('heading', {'text': 'ISO 14001 Environment', 'level': 'h3', 'alignment': 'left'}),
                ('paragraph', {
                    'content': '''<ul>
                        <li>1 day ISO 14001:2015 Foundation Course</li>
                        <li>2 day ISO 14001:2015 Internal Auditing Course</li>
                    </ul>''',
                    'alignment': 'left',
                }),
                ('heading', {'text': 'ISO 45001 Health & Safety', 'level': 'h3', 'alignment': 'left'}),
                ('paragraph', {
                    'content': '''<ul>
                        <li>1 day ISO 45001 Foundation Course</li>
                        <li>2 day ISO 45001 Internal Auditor Course</li>
                        <li>2 day ISO 45001 Auditor Transition Course</li>
                        <li>3 day ISO 45001 Auditor Conversion Course</li>
                        <li>5 day ISO 45001 Lead Auditor Course</li>
                    </ul>''',
                    'alignment': 'left',
                }),
                ('heading', {'text': 'ISO 27001 Information Security', 'level': 'h3', 'alignment': 'left'}),
                ('paragraph', {
                    'content': '''<ul>
                        <li>Data Security Basic Awareness Webinar (FREE)</li>
                        <li>Data Security Modular Awareness Programme</li>
                        <li>1 day ISO 27001 Foundation Course</li>
                        <li>2 day ISO 27001 Internal Auditing Course</li>
                    </ul>''',
                    'alignment': 'left',
                }),
                ('heading', {'text': 'IATF 16949 Automotive', 'level': 'h3', 'alignment': 'left'}),
                ('paragraph', {
                    'content': '''<ul>
                        <li>1 day ISO 16949 Foundation Course</li>
                        <li>2 day ISO 16949 IATF Transition Course</li>
                        <li>3 day ISO 16949 IATF Internal Auditor Course</li>
                    </ul>''',
                    'alignment': 'left',
                }),
                ('heading', {'text': 'AS 9100 Aerospace Quality', 'level': 'h3', 'alignment': 'left'}),
                ('paragraph', {
                    'content': '''<ul>
                        <li>1 day AS9100:2016 Foundation Course</li>
                        <li>2 day AS9100:2016 Internal Auditor Course</li>
                    </ul>''',
                    'alignment': 'left',
                }),
                ('heading', {'text': 'Business Improvement', 'level': 'h3', 'alignment': 'left'}),
                ('paragraph', {
                    'content': '''<ul>
                        <li>Advanced Product Quality Planning Course (APQP)</li>
                        <li>Production Part Approval Process Course (PPAP)</li>
                        <li>8D Problem Solving Course</li>
                        <li>5S Workplace Organisation Course</li>
                        <li>Process FMEA Course</li>
                        <li>Measurement Systems Analysis Course (MSA)</li>
                        <li>Use of Minitab Software Course</li>
                    </ul>''',
                    'alignment': 'left',
                }),
                ('contact_form', {'heading': 'Book a Training Course', 'subheading': 'Contact us to discuss your training requirements', 'background_color': 'light-blue'}),
            ]
        )

        # ==================== FAQ PAGE ====================
        faq_page = self.create_flexible_page(
            parent=homepage,
            title="Frequently Asked Questions",
            slug="faq",
            intro="",
            body_content=[
                ('heading', {'text': 'Frequently Asked Questions', 'level': 'h1', 'alignment': 'center'}),
                ('accordion', {
                    'items': [
                        {'title': 'What is an ISO standard?', 'content': '<p>An ISO standard is a set of requirements that any organisation can adopt voluntarily. These requirements have been developed by a network of international experts to represent the current consensus on best practice in specific areas of business operation.</p>'},
                        {'title': 'What is an ISO certified company?', 'content': '<p>When a company is certified (or registered) to an ISO standard, this means they have been independently assessed and found to be compliant with the requirements of the standard. Certification is provided by accredited third-party certification bodies.</p>'},
                        {'title': 'How long does ISO certification take?', 'content': '<p>This depends on the complexity of your operations and which standard(s) you are seeking. A small company seeking ISO 9001 might achieve certification in 2-3 months. Larger organisations or those seeking multiple standards may take 6-12 months.</p>'},
                        {'title': 'How much does ISO certification cost?', 'content': '<p>Costs vary based on scope, number of standards, personnel/sites, installation method, and timeframe. Simple organisations may need 5-8 consultant days, while complex organisations may need 100+ days. Qualitation provides transparent pricing: day rate × number of days.</p>'},
                        {'title': 'Can I implement ISO myself?', 'content': '<p>Yes, but self-implementation takes more time and lacks consultant insights. Consultants offer efficiency, experience, fresh perspectives, and timely readiness for certification assessments.</p>'},
                        {'title': 'What is a certification body?', 'content': '<p>The Certification Body (CB) assesses systems against ISO standard criteria. CBs should be UKAS-accredited, aligning with the official ISO structure. Non-UKAS accredited bodies are not recommended.</p>'},
                        {'title': 'How long is ISO certification valid?', 'content': '<p>After obtaining UKAS-accredited certification, it\'s valid for about a year (possibly 14 months) before needing re-assessment. Annual surveillance audits are also typically required.</p>'},
                    ],
                }),
            ]
        )

        self.stdout.write(self.style.SUCCESS("\n  All pages created successfully!"))
        return homepage

    def setup_header_menu(self):
        """Create and configure the header menu"""
        self.stdout.write("\n=== Setting Up Header Menu ===")

        header_menu = HeaderMenu.objects.first()
        if not header_menu:
            header_menu = HeaderMenu.objects.create(
                title="Main Header Menu",
                phone_number="0345 600 6975",
                show_price_badge=False,
                show_quote_button=True,
                quote_button_text="Request a Quote",
                quote_button_link="/contact/",
                show_portal_button=True,
                portal_button_text="Client Portal",
                portal_button_link="/admin/",
            )
        else:
            header_menu.phone_number = "0345 600 6975"
            header_menu.save()

        header_menu.top_links.all().delete()
        header_menu.main_links.all().delete()
        header_menu.iso_standards.all().delete()

        top_links = [
            ("About Us", "/about-us/"),
            ("ISO Services", "/iso-services/"),
            ("Training", "/training/"),
            ("Contact", "/contact/"),
        ]
        for i, (title, url) in enumerate(top_links):
            HeaderTopLink.objects.create(menu=header_menu, title=title, link_url=url, sort_order=i)

        main_links = [
            ("ISO Standards", "/iso-standards/"),
            ("Quality+", "/quality-plus/"),
            ("Growth & Efficiency", "/growth-efficiency/"),
            ("FAQ", "/faq/"),
        ]
        for i, (title, url) in enumerate(main_links):
            HeaderMainLink.objects.create(menu=header_menu, title=title, link_url=url, sort_order=i)

        iso_standards = [
            ("ISO 9001", "/iso-standards/iso-9001/"),
            ("ISO 14001", "/iso-standards/iso-14001/"),
            ("ISO 27001", "/iso-standards/iso-27001/"),
            ("ISO 45001", "/iso-standards/iso-45001/"),
            ("Aerospace", "/iso-standards/aerospace/"),
            ("IATF 16949", "/iso-standards/iatf-16949/"),
        ]
        for i, (title, url) in enumerate(iso_standards):
            HeaderISOStandard.objects.create(menu=header_menu, title=title, link_url=url, sort_order=i)

        site = Site.objects.get(is_default_site=True)
        menu_settings, _ = SiteMenuSettings.objects.get_or_create(site=site)
        menu_settings.header_menu = header_menu
        menu_settings.save()

        self.stdout.write(self.style.SUCCESS("  - Header menu configured"))

    def setup_footer(self):
        """Setup footer"""
        self.stdout.write("\n=== Setting Up Footer ===")

        footer_menu = FooterMenu.objects.first()
        if not footer_menu:
            footer_menu = FooterMenu.objects.create(title="Main Footer Menu")

        footer_menu.footer_columns.all().delete()

        col1 = FooterColumn.objects.create(footer_menu=footer_menu, title="ISO Standards", sort_order=0)
        for i, (title, url) in enumerate([
            ("ISO 9001 Quality", "/iso-standards/iso-9001/"),
            ("ISO 14001 Environment", "/iso-standards/iso-14001/"),
            ("ISO 27001 Security", "/iso-standards/iso-27001/"),
            ("ISO 45001 Health & Safety", "/iso-standards/iso-45001/"),
            ("Aerospace Standards", "/iso-standards/aerospace/"),
        ]):
            FooterLink.objects.create(column=col1, title=title, link_url=url, sort_order=i)

        col2 = FooterColumn.objects.create(footer_menu=footer_menu, title="Services", sort_order=1)
        for i, (title, url) in enumerate([
            ("ISO Services", "/iso-services/"),
            ("Training Courses", "/training/"),
            ("Quality+", "/quality-plus/"),
            ("Growth & Efficiency", "/growth-efficiency/"),
        ]):
            FooterLink.objects.create(column=col2, title=title, link_url=url, sort_order=i)

        col3 = FooterColumn.objects.create(footer_menu=footer_menu, title="Company", sort_order=2)
        for i, (title, url) in enumerate([
            ("About Us", "/about-us/"),
            ("Contact", "/contact/"),
            ("FAQ", "/faq/"),
        ]):
            FooterLink.objects.create(column=col3, title=title, link_url=url, sort_order=i)

        site = Site.objects.get(is_default_site=True)
        footer_settings, _ = FooterSettings.objects.get_or_create(site=site)
        footer_settings.footer_menu = footer_menu
        footer_settings.phone = "0345 600 6975"
        footer_settings.email = "enquiries@qualitation.co.uk"
        footer_settings.address = "66 Elms Drive, Oxford, OX3 0NL"
        footer_settings.copyright_text = "© 2025 Qualitation (Oxford Quality Centre Ltd). Company No. 08265550 (England & Wales)"
        footer_settings.save()

        menu_settings, _ = SiteMenuSettings.objects.get_or_create(site=site)
        menu_settings.footer_menu = footer_menu
        menu_settings.save()

        self.stdout.write(self.style.SUCCESS("  - Footer configured"))

    def handle(self, *args, **options):
        self.stdout.write("=" * 60)
        self.stdout.write("  QUALITATION WEBSITE CONTENT POPULATION")
        self.stdout.write("=" * 60)

        self.populate_homepage()
        self.create_pages()
        self.setup_header_menu()
        self.setup_footer()

        self.stdout.write("\n" + "=" * 60)
        self.stdout.write(self.style.SUCCESS("  CONTENT POPULATION COMPLETE!"))
        self.stdout.write("=" * 60)
