from django.core.management.base import BaseCommand
from home.models import FlexiblePage
import uuid


class Command(BaseCommand):
    help = 'Updates ISO 9001 page content'

    def handle(self, *args, **options):
        self.stdout.write("=== Updating ISO 9001 Page ===\n")

        try:
            page = FlexiblePage.objects.get(slug='iso-9001')
            self.stdout.write(f"Found page: {page.title}")
        except FlexiblePage.DoesNotExist:
            self.stdout.write(self.style.ERROR("ISO 9001 page not found"))
            return

        content_html = """
        <style>
            main { padding-top: 0 !important; margin-top: 0 !important; }
            .iso9001-hero {
                background: linear-gradient(135deg, #283593 0%, #3949ab 50%, #5c6bc0 100%);
                color: white;
                padding: 80px 20px;
                margin: 0;
                position: relative;
                overflow: hidden;
            }
            .iso9001-hero::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: radial-gradient(circle at 20% 50%, rgba(255,255,255,0.1) 0%, transparent 50%),
                            radial-gradient(circle at 80% 80%, rgba(255,255,255,0.1) 0%, transparent 50%);
                pointer-events: none;
            }
            .iso9001-hero-content {
                position: relative;
                z-index: 1;
                max-width: 1200px;
                margin: 0 auto;
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 60px;
                align-items: center;
            }
            .iso9001-hero-text {
                text-align: left;
            }
            .iso9001-hero h1 {
                font-size: 3.5em;
                margin-bottom: 20px;
                font-weight: 800;
                letter-spacing: -1px;
                line-height: 1.1;
            }
            .iso9001-hero-illustration {
                display: flex;
                align-items: center;
                justify-content: center;
                position: relative;
            }
            .iso9001-icon {
                font-size: 15em;
                opacity: 0.9;
                filter: drop-shadow(0 10px 30px rgba(0,0,0,0.3));
                animation: float 3s ease-in-out infinite;
            }
            @keyframes float {
                0%, 100% { transform: translateY(0px); }
                50% { transform: translateY(-20px); }
            }
            .iso9001-subtitle {
                font-size: 1.3em;
                margin-bottom: 30px;
                opacity: 0.95;
                line-height: 1.6;
                font-weight: 400;
            }
            .iso9001-features {
                display: flex;
                gap: 12px;
                flex-wrap: wrap;
                margin-top: 30px;
                margin-bottom: 35px;
            }
            .iso9001-feature-badge {
                background: rgba(255,255,255,0.2);
                padding: 10px 20px;
                border-radius: 25px;
                font-weight: 600;
                backdrop-filter: blur(10px);
                font-size: 0.95em;
            }
            .iso9001-cta-buttons {
                display: flex;
                gap: 15px;
                flex-wrap: wrap;
            }
            .iso9001-cta-primary, .iso9001-cta-secondary {
                padding: 15px 35px;
                font-size: 1.1em;
                border-radius: 30px;
                text-decoration: none;
                font-weight: 600;
                transition: all 0.3s;
            }
            .iso9001-cta-primary {
                background: white;
                color: #283593;
            }
            .iso9001-cta-primary:hover {
                transform: translateY(-2px);
                box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            }
            .iso9001-cta-secondary {
                background: transparent;
                color: white;
                border: 2px solid white;
            }
            .iso9001-cta-secondary:hover {
                background: white;
                color: #283593;
            }
            .iso9001-content {
                max-width: 1200px;
                margin: 0 auto;
                padding: 60px 20px;
            }
            .iso9001-section {
                margin-bottom: 60px;
            }
            .iso9001-section h2 {
                color: #283593;
                font-size: 2.2em;
                margin-bottom: 25px;
                font-weight: 700;
            }
            .iso9001-section p {
                font-size: 1.15em;
                line-height: 1.8;
                color: #333;
                margin-bottom: 20px;
            }
            .iso9001-cards {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 25px;
                margin-top: 30px;
            }
            .iso9001-card {
                background: #f5f5f5;
                padding: 30px;
                border-radius: 15px;
                border-left: 5px solid #5c6bc0;
            }
            .iso9001-card h3 {
                color: #283593;
                font-size: 1.5em;
                margin-bottom: 15px;
                font-weight: 600;
            }
            .iso9001-card p, .iso9001-card ul {
                font-size: 1.05em;
                line-height: 1.7;
                color: #555;
            }
            .iso9001-card ul {
                margin-top: 15px;
                padding-left: 20px;
            }
            .iso9001-card li {
                margin-bottom: 10px;
            }
            .iso9001-highlight-box {
                background: linear-gradient(135deg, #e8eaf6 0%, #c5cae9 100%);
                padding: 40px;
                border-radius: 15px;
                margin: 40px 0;
                border-left: 6px solid #283593;
            }
            .iso9001-highlight-box h3 {
                color: #283593;
                font-size: 1.8em;
                margin-bottom: 20px;
                font-weight: 600;
            }
            .iso9001-principles-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
                gap: 20px;
                margin-top: 30px;
            }
            .iso9001-principle {
                background: white;
                padding: 25px;
                border-radius: 12px;
                box-shadow: 0 3px 10px rgba(0,0,0,0.1);
            }
            .iso9001-principle h4 {
                color: #283593;
                font-size: 1.3em;
                margin-bottom: 12px;
                font-weight: 600;
            }
            .iso9001-principle p {
                font-size: 1em;
                color: #666;
                margin: 0;
            }
            .iso9001-benefits {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
                gap: 30px;
                margin-top: 30px;
            }
            .iso9001-benefit-category {
                background: white;
                padding: 35px;
                border-radius: 15px;
                box-shadow: 0 5px 20px rgba(0,0,0,0.08);
            }
            .iso9001-benefit-category h3 {
                color: #283593;
                font-size: 1.6em;
                margin-bottom: 20px;
                font-weight: 600;
            }
            .iso9001-benefit-category ul {
                list-style: none;
                padding: 0;
            }
            .iso9001-benefit-category li {
                padding: 12px 0;
                border-bottom: 1px solid #eee;
                font-size: 1.05em;
                color: #555;
            }
            .iso9001-benefit-category li:before {
                content: "✓ ";
                color: #5c6bc0;
                font-weight: bold;
                margin-right: 10px;
            }
            .iso9001-faq-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));
                gap: 25px;
                margin-top: 30px;
            }
            .iso9001-faq {
                background: white;
                padding: 35px;
                border-radius: 15px;
                border: 2px solid #e8eaf6;
                box-shadow: 0 4px 15px rgba(40, 53, 147, 0.08);
                transition: all 0.3s ease;
            }
            .iso9001-faq:hover {
                border-color: #5c6bc0;
                box-shadow: 0 6px 20px rgba(40, 53, 147, 0.15);
                transform: translateY(-2px);
            }
            .iso9001-faq h3 {
                color: #283593;
                font-size: 1.35em;
                margin-bottom: 15px;
                font-weight: 700;
                display: flex;
                align-items: center;
            }
            .iso9001-faq h3:before {
                content: "Q";
                display: inline-flex;
                align-items: center;
                justify-content: center;
                width: 32px;
                height: 32px;
                background: linear-gradient(135deg, #283593 0%, #5c6bc0 100%);
                color: white;
                border-radius: 50%;
                font-size: 0.8em;
                font-weight: 700;
                margin-right: 15px;
                flex-shrink: 0;
            }
            .iso9001-faq p {
                font-size: 1.1em;
                color: #555;
                margin: 0;
                line-height: 1.8;
                padding-left: 47px;
            }
            .iso9001-process-steps {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 20px;
                margin-top: 30px;
            }
            .iso9001-step {
                background: linear-gradient(135deg, #e8eaf6 0%, #c5cae9 100%);
                padding: 30px;
                border-radius: 12px;
                text-align: center;
            }
            .iso9001-step h4 {
                color: #283593;
                font-size: 1.4em;
                margin-bottom: 15px;
                font-weight: 600;
            }
            .iso9001-step p {
                font-size: 1.05em;
                color: #555;
                margin: 0;
            }
            .iso9001-cta-box {
                background: linear-gradient(135deg, #283593 0%, #5c6bc0 100%);
                color: white;
                padding: 60px 40px;
                border-radius: 20px;
                text-align: center;
                margin-top: 60px;
            }
            .iso9001-cta-box h2 {
                color: white;
                font-size: 2.5em;
                margin-bottom: 20px;
            }
            .iso9001-cta-box p {
                font-size: 1.3em;
                margin-bottom: 30px;
                opacity: 0.95;
                color: white;
            }
            @media (max-width: 968px) {
                .iso9001-hero-content {
                    grid-template-columns: 1fr;
                    gap: 40px;
                }
                .iso9001-hero-text {
                    text-align: center;
                }
                .iso9001-hero-illustration {
                    order: -1;
                }
                .iso9001-icon {
                    font-size: 8em;
                }
                .iso9001-features {
                    justify-content: center;
                }
                .iso9001-cta-buttons {
                    justify-content: center;
                }
            }
            @media (max-width: 768px) {
                .iso9001-hero {
                    padding: 60px 20px;
                }
                .iso9001-hero h1 {
                    font-size: 2.2em;
                }
                .iso9001-icon {
                    font-size: 6em;
                }
                .iso9001-subtitle {
                    font-size: 1.15em;
                }
                .iso9001-section h2 { font-size: 1.8em; }
                .iso9001-cards, .iso9001-benefits { grid-template-columns: 1fr; }
                .iso9001-faq-grid {
                    grid-template-columns: 1fr;
                }
            }
        </style>

        <div class="iso9001-hero">
            <div class="iso9001-hero-content">
                <div class="iso9001-hero-text">
                    <h1>ISO 9001 Certification UK</h1>
                    <p class="iso9001-subtitle">Quality Management System. Ensure consistent quality, customer satisfaction, and operational excellence across your organisation.</p>
                    <div class="iso9001-features">
                        <span class="iso9001-feature-badge">Customer Focus</span>
                        <span class="iso9001-feature-badge">Process Excellence</span>
                        <span class="iso9001-feature-badge">Continual Improvement</span>
                    </div>
                    <div class="iso9001-cta-buttons">
                        <a href="/contact/" class="iso9001-cta-primary">Get Certified</a>
                        <a href="#what-is" class="iso9001-cta-secondary">Learn More</a>
                    </div>
                </div>
                <div class="iso9001-hero-illustration">
                    <div class="iso9001-icon">✓</div>
                </div>
            </div>
        </div>

        <div class="iso9001-content">
            <div class="iso9001-section" id="what-is">
                <h2>Introduction to ISO 9001</h2>
                <p>In competitive and highly regulated markets, organisations must consistently deliver products and services that meet customer expectations—every time. Poor quality leads to complaints, rework, lost contracts, and reputational damage. ISO 9001 provides the internationally recognised framework to control, improve, and professionalise how your organisation operates.</p>
                <p>ISO 9001 is the world's most widely adopted Quality Management System (QMS) standard. It helps organisations of all sizes demonstrate that they can consistently provide products and services that meet customer, statutory, and regulatory requirements—while driving continual improvement across the business.</p>
            </div>

            <div class="iso9001-section">
                <h2>What is ISO 9001?</h2>
                <p>ISO 9001 is a voluntary international standard published by the International Organization for Standardization. It sets out the requirements for establishing, implementing, maintaining, and continually improving a Quality Management System.</p>

                <div class="iso9001-highlight-box">
                    <h3>In plain English, ISO 9001 helps organisations:</h3>
                    <ul>
                        <li>Deliver consistent products and services</li>
                        <li>Reduce errors, rework, and inefficiencies</li>
                        <li>Improve customer satisfaction</li>
                        <li>Control processes rather than rely on individuals</li>
                    </ul>
                    <p style="margin-top: 20px;"><strong>The standard is based on risk-based thinking, ensuring that effort is focused where failure would have the greatest impact on customers and the business.</strong></p>
                </div>
            </div>

            <div class="iso9001-section">
                <h2>Why ISO 9001 was created</h2>
                <p>Before ISO 9001, quality was often inspected after problems occurred. Organisations relied on final checks rather than controlling how work was done in the first place—leading to waste, inconsistency, and customer dissatisfaction.</p>
                <p><strong>ISO 9001 was created to shift quality from inspection to prevention.</strong> It embeds quality into everyday operations through defined processes, leadership accountability, and continual improvement. Today, it is used across every sector—from manufacturing and construction to healthcare, professional services, and IT.</p>
            </div>

            <div class="iso9001-section">
                <h2>Why ISO 9001 matters for UK organisations</h2>
                <p>For UK organisations, ISO 9001 is often the entry requirement for doing business. It is frequently expected or required in:</p>

                <div class="iso9001-cards">
                    <div class="iso9001-card">
                        <h3>Public sector and local authority contracts</h3>
                        <p>Required for government and public procurement opportunities</p>
                    </div>
                    <div class="iso9001-card">
                        <h3>Construction and infrastructure frameworks</h3>
                        <p>Essential for construction tenders and framework agreements</p>
                    </div>
                    <div class="iso9001-card">
                        <h3>Manufacturing and engineering supply chains</h3>
                        <p>Mandatory for many manufacturing and engineering suppliers</p>
                    </div>
                    <div class="iso9001-card">
                        <h3>Professional and outsourced services</h3>
                        <p>Demonstrates credibility in service delivery</p>
                    </div>
                </div>

                <p style="margin-top: 30px;"><strong>ISO 9001 demonstrates that your organisation is controlled, credible, and customer-focused. It reassures clients and procurement teams that quality is managed systematically—not left to chance.</strong></p>
            </div>

            <div class="iso9001-section">
                <h2>Who ISO 9001 is for</h2>
                <p>ISO 9001 is suitable for organisations of any size and sector, including:</p>

                <div class="iso9001-cards">
                    <div class="iso9001-card">
                        <h3>🚀 Small Businesses & Startups</h3>
                        <p>Building credibility and structure early in your growth journey</p>
                    </div>
                    <div class="iso9001-card">
                        <h3>📈 Growing SMEs</h3>
                        <p>Professionalising operations and reducing business risk</p>
                    </div>
                    <div class="iso9001-card">
                        <h3>🏭 Manufacturing & Engineering Firms</h3>
                        <p>Controlling production processes and supply chains</p>
                    </div>
                    <div class="iso9001-card">
                        <h3>🏗️ Construction & Trades</h3>
                        <p>Improving consistency and tender success rates</p>
                    </div>
                    <div class="iso9001-card">
                        <h3>💼 Professional & Service Organisations</h3>
                        <p>Delivering reliable and consistent client outcomes</p>
                    </div>
                    <div class="iso9001-card">
                        <h3>🏛️ Public & Third-Sector Bodies</h3>
                        <p>Demonstrating accountability and governance standards</p>
                    </div>
                </div>

                <p style="margin-top: 30px;"><strong>The standard is fully scalable and proportionate to organisational size and complexity.</strong></p>
            </div>

            <div class="iso9001-section">
                <h2>Key principles of ISO 9001</h2>
                <p>ISO 9001 is built on seven quality management principles:</p>

                <div class="iso9001-principles-grid">
                    <div class="iso9001-principle">
                        <h4>Customer Focus</h4>
                        <p>Understanding and meeting customer needs consistently.</p>
                    </div>
                    <div class="iso9001-principle">
                        <h4>Leadership</h4>
                        <p>Clear direction, accountability, and engagement from top management.</p>
                    </div>
                    <div class="iso9001-principle">
                        <h4>Engagement of People</h4>
                        <p>Defined roles, competence, and responsibility at all levels.</p>
                    </div>
                    <div class="iso9001-principle">
                        <h4>Process Approach</h4>
                        <p>Managing activities as controlled, interrelated processes.</p>
                    </div>
                    <div class="iso9001-principle">
                        <h4>Improvement</h4>
                        <p>Continual improvement embedded into daily operations.</p>
                    </div>
                    <div class="iso9001-principle">
                        <h4>Evidence-Based Decision Making</h4>
                        <p>Using data, metrics, and performance information.</p>
                    </div>
                    <div class="iso9001-principle">
                        <h4>Relationship Management</h4>
                        <p>Managing suppliers and partners effectively.</p>
                    </div>
                </div>
            </div>

            <div class="iso9001-section">
                <h2>Benefits of ISO 9001</h2>

                <div class="iso9001-benefits">
                    <div class="iso9001-benefit-category">
                        <h3>Internal Benefits</h3>
                        <ul>
                            <li>Reduced errors, rework, and waste</li>
                            <li>Clearer roles, responsibilities, and processes</li>
                            <li>Improved efficiency and consistency</li>
                            <li>Better staff understanding and engagement</li>
                        </ul>
                    </div>

                    <div class="iso9001-benefit-category">
                        <h3>Strategic Benefits</h3>
                        <ul>
                            <li>Increased customer confidence and retention</li>
                            <li>Improved success in tenders and procurement</li>
                            <li>Stronger reputation and market credibility</li>
                            <li>Better management control and decision-making</li>
                        </ul>
                    </div>

                    <div class="iso9001-benefit-category">
                        <h3>Compliance & Risk Benefits</h3>
                        <ul>
                            <li>Improved control of legal and contractual requirements</li>
                            <li>Reduced operational and reputational risk</li>
                            <li>Strong foundation for other ISO standards</li>
                        </ul>
                    </div>
                </div>
            </div>

            <div class="iso9001-section">
                <h2>What ISO 9001 auditors actually look for</h2>
                <p>ISO 9001 auditors are not just checking documents—they are checking how your business really works.</p>
                <p><strong>They typically look for:</strong></p>

                <div class="iso9001-cards">
                    <div class="iso9001-card">
                        <h3>Process Control</h3>
                        <p>Are processes defined, followed, and monitored effectively?</p>
                    </div>
                    <div class="iso9001-card">
                        <h3>Risk & Opportunity Management</h3>
                        <p>Have risks been identified and addressed appropriately?</p>
                    </div>
                    <div class="iso9001-card">
                        <h3>Customer Focus</h3>
                        <p>Feedback mechanisms, complaints handling, and satisfaction monitoring</p>
                    </div>
                    <div class="iso9001-card">
                        <h3>Competence & Training</h3>
                        <p>Staff know what they are doing and why it matters</p>
                    </div>
                    <div class="iso9001-card">
                        <h3>Internal Audits & Management Review</h3>
                        <p>Evidence of oversight, monitoring, and improvement</p>
                    </div>
                </div>

                <p style="margin-top: 30px;"><strong>Auditors want to see a living system, not a folder on a shelf.</strong></p>
            </div>

            <div class="iso9001-section">
                <h2>ISO 9001 in practice (real-world examples)</h2>

                <div class="iso9001-cards">
                    <div class="iso9001-card">
                        <h3>Construction Company</h3>
                        <p>A UK contractor uses ISO 9001 to standardise site processes, reduce defects, and improve performance on public sector frameworks.</p>
                    </div>
                    <div class="iso9001-card">
                        <h3>Professional Services Firm</h3>
                        <p>A consultancy applies ISO 9001 to improve consistency in client delivery, manage risks, and build trust with corporate clients.</p>
                    </div>
                </div>
            </div>

            <div class="iso9001-section">
                <h2>Common mistakes when implementing ISO 9001</h2>

                <div class="iso9001-cards">
                    <div class="iso9001-card">
                        <h3>Treating It as a Paper Exercise</h3>
                        <p>ISO 9001 must reflect how the business actually operates, not just documentation.</p>
                    </div>
                    <div class="iso9001-card">
                        <h3>Over-Documenting</h3>
                        <p>The standard requires control, not excessive paperwork or bureaucracy.</p>
                    </div>
                    <div class="iso9001-card">
                        <h3>Lack of Leadership Involvement</h3>
                        <p>Without senior buy-in and engagement, the system quickly fails.</p>
                    </div>
                </div>
            </div>

            <div class="iso9001-section">
                <h2>ISO 9001 certification process</h2>

                <div class="iso9001-process-steps">
                    <div class="iso9001-step">
                        <h4>Stage 1: Documentation Review</h4>
                        <p>The auditor checks that your QMS meets ISO 9001 requirements.</p>
                    </div>
                    <div class="iso9001-step">
                        <h4>Stage 2: Certification Audit</h4>
                        <p>A practical audit verifies implementation and effectiveness.</p>
                    </div>
                    <div class="iso9001-step">
                        <h4>Surveillance Audits</h4>
                        <p>Annual audits confirm ongoing compliance and improvement.</p>
                    </div>
                    <div class="iso9001-step">
                        <h4>Recertification</h4>
                        <p>A full reassessment every three years renews certification.</p>
                    </div>
                </div>
            </div>

            <div class="iso9001-section">
                <h2>How long does ISO 9001 certification last?</h2>
                <p>ISO 9001 certification is valid for three years, subject to successful annual surveillance audits. Serious or unresolved non-conformities can lead to suspension or withdrawal.</p>
            </div>

            <div class="iso9001-section">
                <h2>How much does ISO 9001 cost in the UK?</h2>
                <p>Costs vary depending on:</p>
                <ul>
                    <li>Organisation size and complexity</li>
                    <li>Number of sites and employees</li>
                    <li>Level of existing systems</li>
                </ul>

                <div class="iso9001-highlight-box">
                    <h3>Typical costs include:</h3>
                    <ul>
                        <li>UKAS-accredited certification audit fees</li>
                        <li>Consultancy and gap analysis (if used)</li>
                        <li>Internal staff time and training</li>
                    </ul>
                    <p style="margin-top: 20px;"><strong>ISO 9001 should be viewed as an investment in efficiency, credibility, and growth, not just a compliance cost.</strong></p>
                </div>
            </div>

            <div class="iso9001-section">
                <h2>ISO 9001 and integration with other standards</h2>
                <p>ISO 9001 follows the Annex SL High-Level Structure, making it ideal for integration with:</p>

                <div class="iso9001-cards">
                    <div class="iso9001-card">
                        <h3>ISO 14001</h3>
                        <p>Environmental Management</p>
                    </div>
                    <div class="iso9001-card">
                        <h3>ISO 45001</h3>
                        <p>Health & Safety</p>
                    </div>
                    <div class="iso9001-card">
                        <h3>ISO 27001</h3>
                        <p>Information Security</p>
                    </div>
                    <div class="iso9001-card">
                        <h3>ISO 22301</h3>
                        <p>Business Continuity</p>
                    </div>
                </div>

                <p style="margin-top: 30px;"><strong>Many UK organisations operate a single Integrated Management System (IMS) to reduce duplication and cost.</strong></p>
            </div>

            <div class="iso9001-section">
                <h2>Who should NOT implement ISO 9001?</h2>
                <p>If an organisation has no customers, no repeat processes, and no desire to improve consistency or credibility, ISO 9001 may offer limited value. For most organisations, however, it forms the foundation of effective management.</p>
            </div>

            <div class="iso9001-section">
                <h2>Frequently Asked Questions (FAQs)</h2>

                <div class="iso9001-faq-grid">
                    <div class="iso9001-faq">
                        <h3>Is ISO 9001 a legal requirement in the UK?</h3>
                        <p>No, but it is often contractually required for public and private sector work.</p>
                    </div>

                    <div class="iso9001-faq">
                        <h3>Can small businesses get ISO 9001?</h3>
                        <p>Yes. The standard is fully scalable and widely used by SMEs across all sectors.</p>
                    </div>

                    <div class="iso9001-faq">
                        <h3>Does ISO 9001 guarantee quality?</h3>
                        <p>It guarantees a controlled system—not perfection—but it significantly reduces risk and improves consistency.</p>
                    </div>

                    <div class="iso9001-faq">
                        <h3>Is ISO 9001 worth it?</h3>
                        <p>For most organisations, yes. It improves efficiency, credibility, and customer trust.</p>
                    </div>
                </div>
            </div>

            <div class="iso9001-cta-box">
                <h2>Ready to achieve ISO 9001 certification?</h2>
                <p>Get UKAS-accredited ISO 9001 certification and demonstrate your commitment to quality management excellence.</p>
                <a href="/contact/" class="iso9001-cta-primary">Start Your Certification Journey</a>
            </div>
        </div>
        """

        # Update the page
        new_body = [
            {
                'type': 'html',
                'value': {
                    'html': content_html
                },
                'id': str(uuid.uuid4())
            }
        ]

        page.body = new_body
        page.intro = ''

        revision = page.save_revision()
        revision.publish()

        self.stdout.write(self.style.SUCCESS(f"✓ Updated ISO 9001 page"))
        self.stdout.write(self.style.SUCCESS(f"✓ URL: /{page.slug}/"))
        self.stdout.write(self.style.SUCCESS(f"✓ Published successfully"))
