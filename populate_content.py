#!/usr/bin/env python
"""
Populate the Qualitation website with actual content from the RTF file.
This script creates all pages and updates menus with real Qualitation content.
"""

import os
import sys

# Setup Django before importing anything else
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import django
django.setup()
from wagtail.models import Page, Site
from home.models import (
    HomePage, FlexiblePage, HeaderMenu, HeaderTopLink, HeaderMainLink,
    HeaderISOStandard, HeaderISODropdownItem, FooterMenu, FooterColumn,
    FooterLink, SiteMenuSettings, FooterSettings
)


def create_flexible_page(parent, title, slug, intro="", body_content=None):
    """Helper function to create a FlexiblePage"""
    # Check if page already exists
    existing = FlexiblePage.objects.filter(slug=slug).first()
    if existing:
        print(f"  - Page '{title}' already exists, updating...")
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
    print(f"  - Created page: {title}")
    return page


def populate_homepage():
    """Update the homepage with Qualitation content"""
    print("\n=== Updating Homepage ===")

    homepage = HomePage.objects.first()
    if not homepage:
        print("ERROR: No homepage found!")
        return None

    # Qualitation homepage content
    homepage.body = [
        # Hero Section
        ('hero', {
            'heading': 'ISO Certification Consultants',
            'subheading': '<p>Expert guidance for ISO 9001, ISO 14001, ISO 27001, ISO 45001 and more. Over 25 years of experience helping businesses achieve certification excellence.</p>',
            'cta_text': 'Request a Quote',
            'cta_link': None,
            'secondary_cta_text': 'Call 0345 600 6975',
            'secondary_cta_link': 'tel:03456006975',
        }),

        # Introduction Section
        ('paragraph', {
            'content': '<h2>Your Partner in ISO Certification</h2><p>Qualitation is a nationwide network of highly qualified ISO consultants providing expert guidance for organisations seeking ISO certification. With over 25 years of experience, we help businesses implement robust management systems that drive real improvement and achieve internationally recognised certification.</p>',
            'alignment': 'center',
        }),

        # Services Cards - ISO Standards
        ('service_cards', {
            'heading': 'Our ISO Certification Services',
            'subheading': '<p>We provide comprehensive consultancy for all major ISO management system standards</p>',
            'cards': [
                {
                    'title': 'ISO 9001',
                    'description': 'Quality Management System - The world\'s most popular ISO standard with over 2.1 million certified companies worldwide.',
                    'icon': 'fa-certificate',
                    'link': None,
                },
                {
                    'title': 'ISO 14001',
                    'description': 'Environmental Management System - Demonstrate your commitment to sustainability and reduce your environmental impact.',
                    'icon': 'fa-leaf',
                    'link': None,
                },
                {
                    'title': 'ISO 27001',
                    'description': 'Information Security Management - Protect your data and demonstrate robust security practices to clients.',
                    'icon': 'fa-shield-alt',
                    'link': None,
                },
                {
                    'title': 'ISO 45001',
                    'description': 'Health & Safety Management - Protect your workforce and demonstrate a safety-first approach.',
                    'icon': 'fa-hard-hat',
                    'link': None,
                },
                {
                    'title': 'ISO 22301',
                    'description': 'Business Continuity Management - Ensure your organisation can continue operating during disruptions.',
                    'icon': 'fa-sync-alt',
                    'link': None,
                },
                {
                    'title': 'AS9100 Series',
                    'description': 'Aerospace Quality Management - Specialist standards for Aviation, Space and Defence industries.',
                    'icon': 'fa-plane',
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
                {'content': '<h4>25+ Years Experience</h4><p>Our network of consultants brings decades of real-world experience across multiple industries and standards.</p>'},
                {'content': '<h4>Nationwide Coverage</h4><p>We provide ISO consultancy services across the entire UK, with local consultants available in your area.</p>'},
                {'content': '<h4>100% Success Rate</h4><p>All our clients achieve certification. We work with you until you succeed.</p>'},
            ],
        }),

        # How It Works
        ('heading', {
            'text': 'How Our Process Works',
            'level': 'h2',
            'alignment': 'center',
        }),
        ('paragraph', {
            'content': '''<div class="process-steps">
                <div class="step"><strong>1. Free Consultation</strong><br>Initial discussion to understand your current systems and requirements.</div>
                <div class="step"><strong>2. Gap Analysis</strong><br>We assess where you are now versus where you need to be.</div>
                <div class="step"><strong>3. System Development</strong><br>Collaborative development and implementation of your management system.</div>
                <div class="step"><strong>4. Internal Audit</strong><br>We conduct thorough internal audits to ensure readiness.</div>
                <div class="step"><strong>5. Certification</strong><br>Support through Stage 1 and Stage 2 certification audits.</div>
            </div>''',
            'alignment': 'center',
        }),

        # Testimonials Slider
        ('testimonial_slider', {
            'heading': 'What Our Clients Say',
            'subheading': 'Trusted by organisations across the UK',
            'testimonials': [
                {
                    'quote': 'Qualitation made the ISO 9001 certification process straightforward and stress-free. Their consultant was incredibly knowledgeable and helped us implement real improvements to our business.',
                    'author': 'James Thompson',
                    'author_title': 'Operations Director, Manufacturing Co.',
                    'rating': 5,
                },
                {
                    'quote': 'We achieved ISO 27001 certification in just 4 months with Qualitation\'s expert guidance. They understood our IT systems and tailored the approach perfectly.',
                    'author': 'Sarah Mitchell',
                    'author_title': 'IT Manager, Tech Solutions Ltd',
                    'rating': 5,
                },
                {
                    'quote': 'The team at Qualitation helped us integrate ISO 9001, 14001 and 45001 into a single management system. Outstanding service from start to finish.',
                    'author': 'David Roberts',
                    'author_title': 'Quality Manager, Construction Group',
                    'rating': 5,
                },
                {
                    'quote': 'Professional, efficient and always available when we needed them. Qualitation exceeded our expectations for AS9100 aerospace certification.',
                    'author': 'Emma Wilson',
                    'author_title': 'MD, Precision Engineering Ltd',
                    'rating': 5,
                },
                {
                    'quote': 'After struggling with certification internally, Qualitation came in and got us certified within 3 months. Worth every penny.',
                    'author': 'Michael Chen',
                    'author_title': 'CEO, Logistics Solutions',
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
                    'title': 'What is ISO certification?',
                    'content': '<p>ISO certification demonstrates that your organisation meets internationally recognised standards for quality, safety, environment, or information security management. It is awarded by accredited certification bodies after a thorough audit process.</p>',
                },
                {
                    'title': 'How long does it take to get certified?',
                    'content': '<p>The timeline varies depending on your organisation\'s size, complexity, and current systems. Typically, certification can be achieved in 3-6 months for smaller organisations, or 6-12 months for larger, more complex businesses.</p>',
                },
                {
                    'title': 'How much does ISO certification cost?',
                    'content': '<p>Our pricing is straightforward - calculated by multiplying an agreed day rate by the number of days work required. We offer a free consultation to understand your needs and provide a formal proposal without charge.</p>',
                },
                {
                    'title': 'Can ISO standards be integrated?',
                    'content': '<p>Yes! ISO 9001, ISO 14001, ISO 45001 and other standards can be integrated into a single management system. This is often called an Integrated Management System (IMS) or Quality+ approach, which is more efficient to maintain.</p>',
                },
                {
                    'title': 'Do you provide training?',
                    'content': '<p>Yes, we offer a comprehensive range of training courses including Foundation, Internal Auditor, and Lead Auditor courses for ISO 9001, ISO 14001, ISO 45001, ISO 27001, and more.</p>',
                },
                {
                    'title': 'What happens after certification?',
                    'content': '<p>Certification is typically valid for 3 years with annual surveillance audits. We offer ongoing support services to help maintain your management system and prepare for re-certification.</p>',
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
    print("  - Homepage updated with Qualitation content")
    return homepage


def create_pages():
    """Create all the content pages"""
    print("\n=== Creating Content Pages ===")

    homepage = HomePage.objects.first()
    if not homepage:
        print("ERROR: No homepage found!")
        return

    # About Us Page
    about_page = create_flexible_page(
        parent=homepage,
        title="About Us",
        slug="about-us",
        intro="<p>Learn about Qualitation and our team of expert ISO consultants.</p>",
        body_content=[
            ('heading', {
                'text': 'About Qualitation',
                'level': 'h1',
                'alignment': 'center',
            }),
            ('paragraph', {
                'content': '''<p>Qualitation is a nationwide network of highly qualified ISO consultants based throughout the UK. Our team brings together decades of real-world experience across multiple industries, ensuring we can provide expert guidance tailored to your specific sector and needs.</p>

                <p>With over 25 years of combined experience, we have helped hundreds of organisations achieve ISO certification. Our consultants are not just experts in standards - they are experienced business professionals who understand the practical challenges of implementing effective management systems.</p>''',
                'alignment': 'left',
            }),
            ('heading', {
                'text': 'Our Approach',
                'level': 'h2',
                'alignment': 'left',
            }),
            ('paragraph', {
                'content': '''<p>We believe in making ISO certification achievable and beneficial for every organisation. Our approach focuses on:</p>
                <ul>
                    <li><strong>Practical Implementation</strong> - Systems that work in the real world, not just on paper</li>
                    <li><strong>Business Improvement</strong> - Certification should drive genuine improvement, not just compliance</li>
                    <li><strong>Knowledge Transfer</strong> - We ensure your team can maintain the system independently</li>
                    <li><strong>Ongoing Support</strong> - We're here for you before, during, and after certification</li>
                </ul>''',
                'alignment': 'left',
            }),
            ('heading', {
                'text': 'Our Qualitators',
                'level': 'h2',
                'alignment': 'center',
            }),
            ('paragraph', {
                'content': '''<p>We call our consultants "Qualitators" - experts who are passionate about quality and helping organisations succeed. Every Qualitator brings:</p>
                <ul>
                    <li>Relevant industry experience in your sector</li>
                    <li>Professional qualifications (Lead Auditor, IRCA registered, etc.)</li>
                    <li>A practical, no-nonsense approach to implementation</li>
                    <li>Commitment to your success - we only succeed when you do</li>
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

    # Contact Page
    contact_page = create_flexible_page(
        parent=homepage,
        title="Contact Us",
        slug="contact",
        intro="",
        body_content=[
            ('heading', {
                'text': 'Contact Qualitation',
                'level': 'h1',
                'alignment': 'center',
            }),
            ('paragraph', {
                'content': '''<p style="text-align: center; font-size: 1.2em;">Get in touch with our team to discuss your ISO certification requirements. We offer a free, no-obligation consultation to understand your needs.</p>''',
                'alignment': 'center',
            }),
            ('columns', {
                'columns': [
                    {'content': '''<h3>Phone</h3>
                        <p><strong>0345 600 6975</strong></p>
                        <p>Monday - Friday: 9am - 5pm</p>'''},
                    {'content': '''<h3>Email</h3>
                        <p><strong>enquiries@qualitation.co.uk</strong></p>
                        <p>We respond within 24 hours</p>'''},
                    {'content': '''<h3>Location</h3>
                        <p>Nationwide coverage across the UK</p>
                        <p>Local consultants in your area</p>'''},
                ],
            }),
            ('contact_form', {
                'heading': 'Send Us a Message',
                'subheading': 'Fill in the form below and we\'ll get back to you shortly',
                'background_color': 'white',
            }),
        ]
    )

    # ISO Services Parent Page
    iso_services_page = create_flexible_page(
        parent=homepage,
        title="ISO Standards Services",
        slug="iso-standards",
        intro="<p>Expert consultancy for all major ISO management system standards.</p>",
        body_content=[
            ('heading', {
                'text': 'ISO Certification Services',
                'level': 'h1',
                'alignment': 'center',
            }),
            ('paragraph', {
                'content': '''<p>Qualitation provides expert consultancy services for all major ISO management system standards. Whether you're seeking your first certification or need help maintaining existing systems, our experienced consultants can help.</p>''',
                'alignment': 'center',
            }),
            ('service_cards', {
                'heading': 'Our ISO Standards',
                'subheading': '<p>Click on any standard to learn more</p>',
                'cards': [
                    {
                        'title': 'ISO 9001 Quality',
                        'description': 'The world\'s most recognised quality management system standard.',
                        'icon': 'fa-certificate',
                    },
                    {
                        'title': 'ISO 14001 Environment',
                        'description': 'Environmental management system for sustainability.',
                        'icon': 'fa-leaf',
                    },
                    {
                        'title': 'ISO 27001 Information Security',
                        'description': 'Information security management system standard.',
                        'icon': 'fa-shield-alt',
                    },
                    {
                        'title': 'ISO 45001 Health & Safety',
                        'description': 'Occupational health and safety management.',
                        'icon': 'fa-hard-hat',
                    },
                    {
                        'title': 'ISO 22301 Business Continuity',
                        'description': 'Business continuity management system.',
                        'icon': 'fa-sync-alt',
                    },
                    {
                        'title': 'AS9100 Aerospace',
                        'description': 'Quality management for aerospace industry.',
                        'icon': 'fa-plane',
                    },
                ],
            }),
        ]
    )

    # ISO 9001 Page
    iso9001_page = create_flexible_page(
        parent=iso_services_page,
        title="ISO 9001 Quality Management",
        slug="iso-9001",
        intro="",
        body_content=[
            ('hero', {
                'heading': 'ISO 9001 Quality Management System',
                'subheading': '<p>The world\'s most popular ISO standard with over 2.1 million certified companies globally.</p>',
                'cta_text': 'Get a Quote',
                'secondary_cta_text': 'Call Us',
                'secondary_cta_link': 'tel:03456006975',
            }),
            ('heading', {
                'text': 'What is ISO 9001?',
                'level': 'h2',
                'alignment': 'left',
            }),
            ('paragraph', {
                'content': '''<p>ISO 9001 is the key Quality Management System standard from the International Organization for Standardization (ISO). It is recognised globally with over 2.1 million certified companies worldwide.</p>

                <p>The standard ensures adherence to structured procedures, resulting in enhanced client satisfaction and empowering staff. It is designed to support achieving excellence in quality throughout your entire operation.</p>''',
                'alignment': 'left',
            }),
            ('heading', {
                'text': 'Benefits of ISO 9001',
                'level': 'h2',
                'alignment': 'left',
            }),
            ('columns', {
                'columns': [
                    {'content': '''<h4>Internal Benefits</h4>
                        <ul>
                            <li>Process optimisation</li>
                            <li>Enhanced collaboration</li>
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
                            <li>Mandatory in some sectors</li>
                            <li>Reduced oversight from authorities</li>
                            <li>Enhanced reliability</li>
                            <li>Improved efficiency</li>
                        </ul>'''},
                ],
            }),
            ('heading', {
                'text': 'How We Help',
                'level': 'h2',
                'alignment': 'left',
            }),
            ('paragraph', {
                'content': '''<p>Qualitation's network has over 25 years of experience in ISO 9001. Our services include:</p>
                <ul>
                    <li>Full or partial system development</li>
                    <li>GAP analysis against current practices</li>
                    <li>Internal auditor training</li>
                    <li>Internal audits and management review meetings</li>
                    <li>Ongoing maintenance and support</li>
                </ul>''',
                'alignment': 'left',
            }),
            ('accordion', {
                'items': [
                    {
                        'title': 'Can ISO 9001 be integrated with other standards?',
                        'content': '<p>Yes, it can be integrated with existing management systems and other standards like ISO 14001 or ISO 45001 to create a unified framework.</p>',
                    },
                    {
                        'title': 'Can I implement it internally?',
                        'content': '<p>Yes, but it takes more time and lacks consultant insights, potentially leading to misalignment with ISO\'s intent. Our consultants ensure efficient, correct implementation.</p>',
                    },
                    {
                        'title': 'What is a certification body?',
                        'content': '<p>A certification body assesses your systems against ISO criteria. They should be UKAS-accredited for UK recognition.</p>',
                    },
                    {
                        'title': 'How long is certification valid?',
                        'content': '<p>Certification is valid for 3 years with annual surveillance audits to maintain compliance.</p>',
                    },
                    {
                        'title': 'Is there a size requirement?',
                        'content': '<p>No, ISO 9001 is valid for all organisation sizes, from single-person setups to multinationals.</p>',
                    },
                ],
            }),
            ('contact_form', {
                'heading': 'Get Started with ISO 9001',
                'subheading': 'Request a free consultation to discuss your requirements',
                'background_color': 'light-blue',
            }),
        ]
    )

    # ISO 14001 Page
    iso14001_page = create_flexible_page(
        parent=iso_services_page,
        title="ISO 14001 Environmental Management",
        slug="iso-14001",
        intro="",
        body_content=[
            ('hero', {
                'heading': 'ISO 14001 Environmental Management System',
                'subheading': '<p>The second most popular ISO standard globally, driven by consumer interest in sustainability and green credentials.</p>',
                'cta_text': 'Get a Quote',
                'secondary_cta_text': 'Call Us',
                'secondary_cta_link': 'tel:03456006975',
            }),
            ('heading', {
                'text': 'Make an Impact While Reducing Yours',
                'level': 'h2',
                'alignment': 'left',
            }),
            ('paragraph', {
                'content': '''<p>ISO 14001 covers environmental management and monitoring, available to any organisation regardless of size. It's about reducing your negative environmental impact while maximising the positive effects of your operations.</p>

                <p>The standard helps make day-to-day activities more sustainable across procurement, storage, distribution, and all operational areas. Proven environmental credentials lead to increased brand advocacy, sales, and customer trust - achieving ISO 14001 has led to 60% of companies measuring increased trust from their customer base.</p>''',
                'alignment': 'left',
            }),
            ('heading', {
                'text': 'How Qualitation Helps',
                'level': 'h2',
                'alignment': 'left',
            }),
            ('paragraph', {
                'content': '''<p>We help develop two required registers:</p>
                <ul>
                    <li><strong>Legal Register</strong> - Detailing all applicable environmental legislation relevant to your operations</li>
                    <li><strong>Aspects & Impacts Register</strong> - Noting potential environmental impacts of your activities and how they are addressed</li>
                </ul>
                <p>These registers shape your policies and objectives for sustainable practices.</p>''',
                'alignment': 'left',
            }),
            ('contact_form', {
                'heading': 'Get Started with ISO 14001',
                'subheading': 'Request a free consultation to discuss your environmental management needs',
                'background_color': 'light-blue',
            }),
        ]
    )

    # ISO 45001 Page
    iso45001_page = create_flexible_page(
        parent=iso_services_page,
        title="ISO 45001 Health & Safety",
        slug="iso-45001",
        intro="",
        body_content=[
            ('hero', {
                'heading': 'ISO 45001 Health & Safety Management',
                'subheading': '<p>Prove your organisation is monitoring and protecting its workforce with the international health and safety standard.</p>',
                'cta_text': 'Get a Quote',
                'secondary_cta_text': 'Call Us',
                'secondary_cta_link': 'tel:03456006975',
            }),
            ('heading', {
                'text': 'Look After Your People',
                'level': 'h2',
                'alignment': 'left',
            }),
            ('paragraph', {
                'content': '''<p>Risks come in all shapes and sizes for employees. ISO 45001 certification indicates a safety-first approach, often enforced by legislation. The standard enables any organisation to remain compliant with changing health and safety laws while protecting your people.</p>

                <p>ISO 45001 formalises your business's approach to health and safety using thorough documentation, verified by a third party. It is both a legal and moral requirement to protect the people who work for you.</p>''',
                'alignment': 'left',
            }),
            ('heading', {
                'text': 'Requirements',
                'level': 'h2',
                'alignment': 'left',
            }),
            ('paragraph', {
                'content': '''<p>To achieve certification, you need to create registers including:</p>
                <ul>
                    <li>A document outlining current health and safety laws applicable to your operations</li>
                    <li>A ledger detailing risks and hazards for each role and activity</li>
                    <li>Controls and procedures to manage identified risks</li>
                </ul>''',
                'alignment': 'left',
            }),
            ('contact_form', {
                'heading': 'Get Started with ISO 45001',
                'subheading': 'Request a free consultation to discuss your health and safety requirements',
                'background_color': 'light-blue',
            }),
        ]
    )

    # ISO 27001 Page
    iso27001_page = create_flexible_page(
        parent=iso_services_page,
        title="ISO 27001 Information Security",
        slug="iso-27001",
        intro="",
        body_content=[
            ('hero', {
                'heading': 'ISO 27001 Information Security Management',
                'subheading': '<p>Ensure your data is controlled and safe with the leading information security management standard.</p>',
                'cta_text': 'Get a Quote',
                'secondary_cta_text': 'Call Us',
                'secondary_cta_link': 'tel:03456006975',
            }),
            ('heading', {
                'text': 'Ensuring Data is Secure',
                'level': 'h2',
                'alignment': 'left',
            }),
            ('paragraph', {
                'content': '''<p>ISO 27001 is concerned with data security, ensuring data held by companies is controlled and safe. It is in increasing demand as data breaches become more common and regulations more stringent.</p>

                <p>Data is at risk from passwords, breaches, and natural incidents. ISO 27001 helps navigate this complex landscape, resulting in a robust information security management system.</p>''',
                'alignment': 'left',
            }),
            ('heading', {
                'text': 'Scope of the Standard',
                'level': 'h2',
                'alignment': 'left',
            }),
            ('paragraph', {
                'content': '''<p>ISO 27001 covers:</p>
                <ul>
                    <li><strong>Physical damage</strong> - Water, fire, environmental threats</li>
                    <li><strong>Electronic damage</strong> - Hacking, viruses, cyber attacks</li>
                    <li><strong>Inappropriate release</strong> - Data breach prevention and response</li>
                    <li><strong>Straight loss</strong> - Verifying backups, handling theft</li>
                </ul>
                <p>It can extend to assessing the security risk of employees and third parties.</p>''',
                'alignment': 'left',
            }),
            ('paragraph', {
                'content': '''<p><strong>GDPR Compliance:</strong> ISO 27001 is a strong step in dealing with GDPR legislation and demonstrating your commitment to data protection.</p>

                <p><strong>New Product for SMEs:</strong> We offer "The 27k1 ISMS" - a cloud-based programme for SMEs to create and maintain their own ISO 27001 system from just £110/month.</p>''',
                'alignment': 'left',
            }),
            ('contact_form', {
                'heading': 'Get Started with ISO 27001',
                'subheading': 'Request a free consultation to discuss your information security requirements',
                'background_color': 'light-blue',
            }),
        ]
    )

    # Training Courses Page
    training_page = create_flexible_page(
        parent=homepage,
        title="Training Courses",
        slug="training",
        intro="<p>Professional ISO training courses delivered by experienced practitioners.</p>",
        body_content=[
            ('heading', {
                'text': 'ISO Training Courses',
                'level': 'h1',
                'alignment': 'center',
            }),
            ('paragraph', {
                'content': '''<p>Qualitation offers a range of training courses covering business improvement disciplines, provided by specialists. Courses can be held at your organisation, at training locations, or other suitable venues.</p>''',
                'alignment': 'center',
            }),
            ('heading', {
                'text': 'ISO 9001 Quality Management',
                'level': 'h3',
                'alignment': 'left',
            }),
            ('paragraph', {
                'content': '''<ul>
                    <li>1 day Foundation Course</li>
                    <li>2 day Internal Auditor Course</li>
                    <li>5 day IRCA Lead Auditor Course</li>
                </ul>''',
                'alignment': 'left',
            }),
            ('heading', {
                'text': 'ISO 14001 Environment',
                'level': 'h3',
                'alignment': 'left',
            }),
            ('paragraph', {
                'content': '''<ul>
                    <li>1 day Foundation Course</li>
                    <li>2 day Internal Auditor Course</li>
                </ul>''',
                'alignment': 'left',
            }),
            ('heading', {
                'text': 'ISO 45001 Health & Safety',
                'level': 'h3',
                'alignment': 'left',
            }),
            ('paragraph', {
                'content': '''<ul>
                    <li>1 day Foundation Course</li>
                    <li>2 day Internal Auditor Course</li>
                    <li>5 day Lead Auditor Course</li>
                    <li>2 day Auditor Transition Course</li>
                    <li>3 day Auditor Conversion Course</li>
                </ul>''',
                'alignment': 'left',
            }),
            ('heading', {
                'text': 'ISO 27001 Information Security',
                'level': 'h3',
                'alignment': 'left',
            }),
            ('paragraph', {
                'content': '''<ul>
                    <li>Basic Awareness Webinar (FREE)</li>
                    <li>Modular Awareness Programme</li>
                    <li>1 day Foundation Course</li>
                    <li>2 day Internal Auditor Course</li>
                </ul>''',
                'alignment': 'left',
            }),
            ('heading', {
                'text': 'Business Improvement',
                'level': 'h3',
                'alignment': 'left',
            }),
            ('paragraph', {
                'content': '''<ul>
                    <li>APQP - Advanced Product Quality Planning</li>
                    <li>PPAP - Production Part Approval Process</li>
                    <li>8D Problem Solving</li>
                    <li>5S Workplace Organisation</li>
                    <li>Process FMEA</li>
                    <li>MSA - Measurement System Analysis</li>
                    <li>Use of Minitab Software</li>
                </ul>''',
                'alignment': 'left',
            }),
            ('contact_form', {
                'heading': 'Book a Training Course',
                'subheading': 'Contact us to discuss your training requirements',
                'background_color': 'light-blue',
            }),
        ]
    )

    # Quality+ Page
    qualityplus_page = create_flexible_page(
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
            ('heading', {
                'text': 'What is Quality+?',
                'level': 'h2',
                'alignment': 'left',
            }),
            ('paragraph', {
                'content': '''<p>Quality+ is our name for an Integrated Management System (IMS) that combines ISO 9001, ISO 14001 and ISO 45001 into a single, efficient framework.</p>

                <p>Instead of maintaining three separate management systems, Quality+ allows you to manage quality, environment, and health & safety through one unified approach. This reduces duplication, streamlines processes, and makes ongoing maintenance much more efficient.</p>''',
                'alignment': 'left',
            }),
            ('heading', {
                'text': 'Benefits of Quality+',
                'level': 'h2',
                'alignment': 'left',
            }),
            ('columns', {
                'columns': [
                    {'content': '''<h4>Efficiency</h4>
                        <p>Single management system, single set of procedures, single internal audit programme.</p>'''},
                    {'content': '''<h4>Cost Savings</h4>
                        <p>Reduced documentation, fewer audit days, streamlined training requirements.</p>'''},
                    {'content': '''<h4>Simplicity</h4>
                        <p>One management review, one improvement plan, one system to maintain.</p>'''},
                ],
            }),
            ('contact_form', {
                'heading': 'Get Started with Quality+',
                'subheading': 'Discuss how an integrated management system could benefit your organisation',
                'background_color': 'light-blue',
            }),
        ]
    )

    # FAQ Page
    faq_page = create_flexible_page(
        parent=homepage,
        title="Frequently Asked Questions",
        slug="faq",
        intro="<p>Common questions about ISO certification and our consultancy services.</p>",
        body_content=[
            ('heading', {
                'text': 'Frequently Asked Questions',
                'level': 'h1',
                'alignment': 'center',
            }),
            ('heading', {
                'text': 'What is ISO?',
                'level': 'h2',
                'alignment': 'left',
            }),
            ('accordion', {
                'items': [
                    {
                        'title': 'What is ISO?',
                        'content': '<p>ISO stands for the International Organization for Standardization, a global federation promoting international standards. It\'s an independent, non-governmental organisation.</p>',
                    },
                    {
                        'title': 'How did ISO start?',
                        'content': '<p>ISO began after World War II and officially opened in 1947 to facilitate international coordination of industrial standards.</p>',
                    },
                    {
                        'title': 'What is a standard?',
                        'content': '<p>Standards are described as "making things work" - giving best-practice specifications for products, services, and systems. There are over 22,000 ISO standards covering various aspects of business and technology.</p>',
                    },
                    {
                        'title': 'How are standards developed?',
                        'content': '<p>Standards are devised and agreed by experts who need them, through a consensus-based process involving industry specialists from around the world.</p>',
                    },
                    {
                        'title': 'What does certified mean?',
                        'content': '<p>ISO does not perform certification. You need external experts (like Qualitation) to help become certified, and certification is awarded by a separate accredited certification body.</p>',
                    },
                ],
            }),
            ('heading', {
                'text': 'Why Do I Need ISO?',
                'level': 'h2',
                'alignment': 'left',
            }),
            ('accordion', {
                'items': [
                    {
                        'title': 'Why do I need ISO?',
                        'content': '<p>Reasons range from improving efficiency and customer satisfaction to legal requirements in some industries. Many clients require ISO certification from their suppliers.</p>',
                    },
                    {
                        'title': 'What are the benefits?',
                        'content': '<p>Benefits include optimised operations, increased customer retention, enhanced financial returns, expanded customer pool, and improved workforce morale.</p>',
                    },
                    {
                        'title': 'Which ISO do I need?',
                        'content': '<p>This depends on your industry and customer requirements. Some sectors have bespoke standards, while others commonly require ISO 9001, ISO 14001, or ISO 45001.</p>',
                    },
                    {
                        'title': 'Who needs ISO?',
                        'content': '<p>Organisations of all types and sizes benefit from ISO certification. In some sectors, it is legally required. Most organisations rarely reach the top of their industry without it.</p>',
                    },
                    {
                        'title': 'What does the ISO process look like?',
                        'content': '<p>Our experts accompany you through the change, reviewing processes, identifying training needs, implementing audit actions, and building management systems tailored to your organisation.</p>',
                    },
                ],
            }),
        ]
    )

    # Lean Management Page
    lean_page = create_flexible_page(
        parent=homepage,
        title="Lean Management",
        slug="lean-management",
        intro="",
        body_content=[
            ('heading', {
                'text': 'Lean Management',
                'level': 'h1',
                'alignment': 'center',
            }),
            ('paragraph', {
                'content': '''<p>Lean Management is the process of applying continuous improvement through ongoing small changes to develop and improve an organisation's processes. Each aspect is reviewed periodically to determine what can be improved to bring a "better" result - more efficient, more effective, with less resource use.</p>

                <p>Small changes have a ripple effect that compounds over time, leading to significant improvements in efficiency and quality.</p>''',
                'alignment': 'left',
            }),
            ('heading', {
                'text': 'Key Lean Principles',
                'level': 'h2',
                'alignment': 'left',
            }),
            ('columns', {
                'columns': [
                    {'content': '''<h4>Customer Value</h4>
                        <p>Understanding what the customer is looking for to enhance value.</p>'''},
                    {'content': '''<h4>Value Stream</h4>
                        <p>Looking at the product life cycle to understand how value is increased or decreased at each step.</p>'''},
                ],
            }),
            ('columns', {
                'columns': [
                    {'content': '''<h4>Flow</h4>
                        <p>Looking at resources and wastes to minimise waste or convert it to value.</p>'''},
                    {'content': '''<h4>Pull</h4>
                        <p>Ensuring production is made to order, not schedule (Just-In-Time processing), to reduce stockpiles.</p>'''},
                ],
            }),
            ('paragraph', {
                'content': '''<h4>Perfection</h4>
                <p>Ensuring each stage is carried out as perfectly as possible, striving for zero defects (e.g., Six Sigma methodologies).</p>''',
                'alignment': 'left',
            }),
            ('contact_form', {
                'heading': 'Get Started with Lean',
                'subheading': 'Contact us to discuss lean management for your organisation',
                'background_color': 'light-blue',
            }),
        ]
    )

    # AS9100 Aerospace Page
    as9100_page = create_flexible_page(
        parent=iso_services_page,
        title="AS9100 Aerospace Quality",
        slug="as9100",
        intro="",
        body_content=[
            ('hero', {
                'heading': 'AS9100, AS9110 & AS9120 Aerospace Quality',
                'subheading': '<p>Quality management systems for Aviation, Space and Defence industries.</p>',
                'cta_text': 'Get a Quote',
                'secondary_cta_text': 'Call Us',
                'secondary_cta_link': 'tel:03456006975',
            }),
            ('paragraph', {
                'content': '''<p>The AS series are standards specific to the Aviation, Space and Defence industry sectors, which are heavily regulated as lives are at stake. They incorporate ISO 9001 Quality requirements but are adapted for these sectors with additional focus on risk management.</p>''',
                'alignment': 'left',
            }),
            ('heading', {
                'text': 'The AS Standards',
                'level': 'h2',
                'alignment': 'left',
            }),
            ('columns', {
                'columns': [
                    {'content': '''<h4>AS9100 Manufacturing</h4>
                        <p>For Manufacturing in Aviation, Space and Defence. Focuses on meeting customer and industry requirements.</p>'''},
                    {'content': '''<h4>AS9110 Maintenance</h4>
                        <p>For Maintenance operations within the Aerospace industry. Focuses on requirements for maintenance activities.</p>'''},
                    {'content': '''<h4>AS9120 Distribution</h4>
                        <p>For Distributors within the Aviation, Space and Defence sectors. Adapted for the distribution industry.</p>'''},
                ],
            }),
            ('paragraph', {
                'content': '''<p>Many established companies in the aerospace industry demand compliance with the AS9100 series from their suppliers due to the legislative nature of the industry. Qualitation's aerospace consultants are industry experts who understand these demanding requirements.</p>''',
                'alignment': 'left',
            }),
            ('contact_form', {
                'heading': 'Get Started with AS9100',
                'subheading': 'Discuss your aerospace quality requirements with our experts',
                'background_color': 'light-blue',
            }),
        ]
    )

    print("\n  All pages created successfully!")
    return homepage


def setup_header_menu():
    """Create and configure the header menu with Qualitation navigation"""
    print("\n=== Setting Up Header Menu ===")

    # Get or create header menu
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
        header_menu.show_quote_button = True
        header_menu.quote_button_text = "Request a Quote"
        header_menu.quote_button_link = "/contact/"
        header_menu.show_portal_button = True
        header_menu.portal_button_text = "Client Portal"
        header_menu.portal_button_link = "/admin/"
        header_menu.save()

    # Clear existing links
    header_menu.top_links.all().delete()
    header_menu.main_links.all().delete()
    header_menu.iso_standards.all().delete()

    # Top Bar Links
    top_links = [
        ("Why Choose Us", "/about-us/"),
        ("Resources", "/faq/"),
        ("Training", "/training/"),
        ("Contact", "/contact/"),
    ]
    for i, (title, url) in enumerate(top_links):
        HeaderTopLink.objects.create(
            menu=header_menu,
            title=title,
            link_url=url,
            sort_order=i,
        )

    # Main Navigation Links
    main_links = [
        ("ISO Certification", "/iso-standards/"),
        ("Quality+", "/quality-plus/"),
        ("Lean Management", "/lean-management/"),
        ("About Us", "/about-us/"),
    ]
    for i, (title, url) in enumerate(main_links):
        HeaderMainLink.objects.create(
            menu=header_menu,
            title=title,
            link_url=url,
            sort_order=i,
        )

    # ISO Standards Bar
    iso_standards = [
        ("ISO 9001", "/iso-standards/iso-9001/"),
        ("ISO 14001", "/iso-standards/iso-14001/"),
        ("ISO 27001", "/iso-standards/iso-27001/"),
        ("ISO 45001", "/iso-standards/iso-45001/"),
        ("ISO 22301", "/iso-standards/"),
        ("AS9100", "/iso-standards/as9100/"),
    ]
    for i, (title, url) in enumerate(iso_standards):
        HeaderISOStandard.objects.create(
            menu=header_menu,
            title=title,
            link_url=url,
            sort_order=i,
        )

    # Update site menu settings
    from wagtail.models import Site
    site = Site.objects.get(is_default_site=True)
    menu_settings, created = SiteMenuSettings.objects.get_or_create(site=site)
    menu_settings.header_menu = header_menu
    menu_settings.save()

    print("  - Header menu configured with Qualitation navigation")


def setup_footer():
    """Setup footer with Qualitation information"""
    print("\n=== Setting Up Footer ===")

    # Create or update footer menu
    footer_menu = FooterMenu.objects.first()
    if not footer_menu:
        footer_menu = FooterMenu.objects.create(title="Main Footer Menu")

    # Clear existing columns
    footer_menu.footer_columns.all().delete()

    # Create footer columns
    # Column 1: ISO Standards
    col1 = FooterColumn.objects.create(
        footer_menu=footer_menu,
        title="ISO Standards",
        sort_order=0,
    )
    col1_links = [
        ("ISO 9001 Quality", "/iso-standards/iso-9001/"),
        ("ISO 14001 Environment", "/iso-standards/iso-14001/"),
        ("ISO 27001 Security", "/iso-standards/iso-27001/"),
        ("ISO 45001 Health & Safety", "/iso-standards/iso-45001/"),
        ("AS9100 Aerospace", "/iso-standards/as9100/"),
    ]
    for i, (title, url) in enumerate(col1_links):
        FooterLink.objects.create(column=col1, title=title, link_url=url, sort_order=i)

    # Column 2: Services
    col2 = FooterColumn.objects.create(
        footer_menu=footer_menu,
        title="Services",
        sort_order=1,
    )
    col2_links = [
        ("ISO Consultancy", "/iso-standards/"),
        ("Training Courses", "/training/"),
        ("Quality+", "/quality-plus/"),
        ("Lean Management", "/lean-management/"),
    ]
    for i, (title, url) in enumerate(col2_links):
        FooterLink.objects.create(column=col2, title=title, link_url=url, sort_order=i)

    # Column 3: Company
    col3 = FooterColumn.objects.create(
        footer_menu=footer_menu,
        title="Company",
        sort_order=2,
    )
    col3_links = [
        ("About Us", "/about-us/"),
        ("Contact", "/contact/"),
        ("FAQ", "/faq/"),
    ]
    for i, (title, url) in enumerate(col3_links):
        FooterLink.objects.create(column=col3, title=title, link_url=url, sort_order=i)

    # Update footer settings
    from wagtail.models import Site
    site = Site.objects.get(is_default_site=True)
    footer_settings, created = FooterSettings.objects.get_or_create(site=site)
    footer_settings.footer_menu = footer_menu
    footer_settings.phone = "0345 600 6975"
    footer_settings.email = "enquiries@qualitation.co.uk"
    footer_settings.address = "Nationwide coverage across the UK"
    footer_settings.copyright_text = "© 2025 Qualitation. All rights reserved. Company Registration: England & Wales"
    footer_settings.linkedin_url = "https://www.linkedin.com/company/qualitation"
    footer_settings.save()

    # Update site menu settings
    menu_settings, created = SiteMenuSettings.objects.get_or_create(site=site)
    menu_settings.footer_menu = footer_menu
    menu_settings.save()

    print("  - Footer configured with Qualitation information")


def main():
    """Main function to populate all content"""
    print("=" * 60)
    print("  QUALITATION WEBSITE CONTENT POPULATION")
    print("=" * 60)

    # Update homepage
    populate_homepage()

    # Create all pages
    create_pages()

    # Setup navigation
    setup_header_menu()

    # Setup footer
    setup_footer()

    print("\n" + "=" * 60)
    print("  CONTENT POPULATION COMPLETE!")
    print("=" * 60)
    print("\nYou can now visit the website to see the content.")
    print("Admin panel: /admin/")
    print("Homepage: /")


if __name__ == "__main__":
    main()
