from django.core.management.base import BaseCommand
from home.models import FlexiblePage
import uuid


class Command(BaseCommand):
    help = 'Updates AS 9120 page content'

    def handle(self, *args, **options):
        self.stdout.write("=== Updating AS 9120 Page ===\n")

        try:
            page = FlexiblePage.objects.get(slug='as-9120')
            self.stdout.write(f"Found page: {page.title}")
        except FlexiblePage.DoesNotExist:
            self.stdout.write(self.style.ERROR("AS 9120 page not found"))
            return

        content_html = """
        <style>
            main { padding-top: 0 !important; margin-top: 0 !important; }
            .as9120-hero {
                background: linear-gradient(135deg, #455a64 0%, #607d8b 100%);
                color: white;
                padding: 80px 20px;
                margin: 0;
                text-align: center;
            }
            .as9120-hero h1 {
                font-size: 3em;
                margin-bottom: 20px;
                font-weight: 700;
            }
            .as9120-icon {
                font-size: 4em;
                margin-bottom: 20px;
            }
            .as9120-subtitle {
                font-size: 1.3em;
                margin-bottom: 30px;
                opacity: 0.95;
                max-width: 800px;
                margin-left: auto;
                margin-right: auto;
                line-height: 1.6;
            }
            .as9120-features {
                display: flex;
                gap: 15px;
                justify-content: center;
                flex-wrap: wrap;
                margin-top: 30px;
            }
            .as9120-feature-badge {
                background: rgba(255,255,255,0.2);
                padding: 10px 20px;
                border-radius: 25px;
                font-weight: 600;
                backdrop-filter: blur(10px);
            }
            .as9120-cta-buttons {
                margin-top: 40px;
                display: flex;
                gap: 20px;
                justify-content: center;
                flex-wrap: wrap;
            }
            .as9120-cta-primary, .as9120-cta-secondary {
                padding: 15px 35px;
                font-size: 1.1em;
                border-radius: 30px;
                text-decoration: none;
                font-weight: 600;
                transition: all 0.3s;
            }
            .as9120-cta-primary {
                background: white;
                color: #455a64;
            }
            .as9120-cta-primary:hover {
                transform: translateY(-2px);
                box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            }
            .as9120-cta-secondary {
                background: transparent;
                color: white;
                border: 2px solid white;
            }
            .as9120-cta-secondary:hover {
                background: white;
                color: #455a64;
            }
            .as9120-content {
                max-width: 1200px;
                margin: 0 auto;
                padding: 60px 20px;
            }
            .as9120-section {
                margin-bottom: 60px;
            }
            .as9120-section h2 {
                color: #455a64;
                font-size: 2.2em;
                margin-bottom: 25px;
                font-weight: 700;
            }
            .as9120-section p {
                font-size: 1.15em;
                line-height: 1.8;
                color: #333;
                margin-bottom: 20px;
            }
            .as9120-cards {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 25px;
                margin-top: 30px;
            }
            .as9120-card {
                background: #f5f5f5;
                padding: 30px;
                border-radius: 15px;
                border-left: 5px solid #607d8b;
            }
            .as9120-card h3 {
                color: #455a64;
                font-size: 1.5em;
                margin-bottom: 15px;
                font-weight: 600;
            }
            .as9120-card p, .as9120-card ul {
                font-size: 1.05em;
                line-height: 1.7;
                color: #555;
            }
            .as9120-card ul {
                margin-top: 15px;
                padding-left: 20px;
            }
            .as9120-card li {
                margin-bottom: 10px;
            }
            .as9120-highlight-box {
                background: linear-gradient(135deg, #eceff1 0%, #cfd8dc 100%);
                padding: 40px;
                border-radius: 15px;
                margin: 40px 0;
                border-left: 6px solid #455a64;
            }
            .as9120-highlight-box h3 {
                color: #455a64;
                font-size: 1.8em;
                margin-bottom: 20px;
                font-weight: 600;
            }
            .as9120-principles-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
                gap: 20px;
                margin-top: 30px;
            }
            .as9120-principle {
                background: white;
                padding: 25px;
                border-radius: 12px;
                box-shadow: 0 3px 10px rgba(0,0,0,0.1);
            }
            .as9120-principle h4 {
                color: #455a64;
                font-size: 1.3em;
                margin-bottom: 12px;
                font-weight: 600;
            }
            .as9120-principle p {
                font-size: 1em;
                color: #666;
                margin: 0;
            }
            .as9120-benefits {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
                gap: 30px;
                margin-top: 30px;
            }
            .as9120-benefit-category {
                background: white;
                padding: 35px;
                border-radius: 15px;
                box-shadow: 0 5px 20px rgba(0,0,0,0.08);
            }
            .as9120-benefit-category h3 {
                color: #455a64;
                font-size: 1.6em;
                margin-bottom: 20px;
                font-weight: 600;
            }
            .as9120-benefit-category ul {
                list-style: none;
                padding: 0;
            }
            .as9120-benefit-category li {
                padding: 12px 0;
                border-bottom: 1px solid #eee;
                font-size: 1.05em;
                color: #555;
            }
            .as9120-benefit-category li:before {
                content: "✓ ";
                color: #607d8b;
                font-weight: bold;
                margin-right: 10px;
            }
            .as9120-faq {
                background: #f9f9f9;
                padding: 30px;
                border-radius: 12px;
                margin: 25px 0;
            }
            .as9120-faq h3 {
                color: #455a64;
                font-size: 1.4em;
                margin-bottom: 12px;
                font-weight: 600;
            }
            .as9120-faq p {
                font-size: 1.1em;
                color: #666;
                margin: 0;
                line-height: 1.7;
            }
            .as9120-process-steps {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 20px;
                margin-top: 30px;
            }
            .as9120-step {
                background: linear-gradient(135deg, #eceff1 0%, #cfd8dc 100%);
                padding: 30px;
                border-radius: 12px;
                text-align: center;
            }
            .as9120-step h4 {
                color: #455a64;
                font-size: 1.4em;
                margin-bottom: 15px;
                font-weight: 600;
            }
            .as9120-step p {
                font-size: 1.05em;
                color: #555;
                margin: 0;
            }
            .as9120-cta-box {
                background: linear-gradient(135deg, #455a64 0%, #607d8b 100%);
                color: white;
                padding: 60px 40px;
                border-radius: 20px;
                text-align: center;
                margin-top: 60px;
            }
            .as9120-cta-box h2 {
                color: white;
                font-size: 2.5em;
                margin-bottom: 20px;
            }
            .as9120-cta-box p {
                font-size: 1.3em;
                margin-bottom: 30px;
                opacity: 0.95;
                color: white;
            }
            @media (max-width: 768px) {
                .as9120-hero h1 { font-size: 2em; }
                .as9120-section h2 { font-size: 1.8em; }
                .as9120-cards, .as9120-benefits { grid-template-columns: 1fr; }
            }
        </style>

        <div class="as9120-hero">
            <div class="as9120-icon">📦</div>
            <h1>AS 9120 Certification</h1>
            <p class="as9120-subtitle">Aerospace Stockist & Distributor Quality Management System</p>
            <div class="as9120-features">
                <span class="as9120-feature-badge">Supply Chain Integrity</span>
                <span class="as9120-feature-badge">Counterfeit Prevention</span>
                <span class="as9120-feature-badge">Traceability Control</span>
            </div>
            <div class="as9120-cta-buttons">
                <a href="/contact/" class="as9120-cta-primary">Get Certified</a>
                <a href="#what-is" class="as9120-cta-secondary">Learn More</a>
            </div>
        </div>

        <div class="as9120-content">
            <div class="as9120-section" id="what-is">
                <h2>Introduction to AS 9120</h2>
                <p>In the aerospace and defence supply chain, traceability, authenticity, and product integrity are just as critical as manufacturing quality. For stockists and distributors, the risk is not how parts are made—but how they are sourced, stored, handled, and supplied. AS 9120 provides the internationally recognised framework that ensures aerospace distributors meet the highest expectations for safety, compliance, and trust.</p>
                <p>AS 9120 is the aerospace quality management standard specifically designed for stockists, distributors, and suppliers of aerospace parts. It builds on ISO 9001 while adding stringent aerospace controls for counterfeit prevention, traceability, documentation, and supplier assurance.</p>
            </div>

            <div class="as9120-section">
                <h2>What is AS 9120?</h2>
                <p>AS 9120 is a quality management system (QMS) standard developed for organisations that procure, store, and distribute aerospace parts, without performing manufacturing or design activities.</p>
                <p>It is maintained by the International Aerospace Quality Group (IAQG) and is aligned globally with EN 9120 (Europe) and JISQ 9120 (Asia).</p>

                <div class="as9120-highlight-box">
                    <h3>In practical terms, AS 9120 helps organisations:</h3>
                    <ul>
                        <li>Ensure parts are authentic, conforming, and traceable</li>
                        <li>Prevent counterfeit or suspect parts entering the supply chain</li>
                        <li>Maintain strict control of storage, handling, and documentation</li>
                        <li>Meet OEM, Tier 1, and regulatory requirements</li>
                    </ul>
                    <p style="margin-top: 20px;"><strong>For many aerospace customers, AS 9120 certification is mandatory for approval as a supplier.</strong></p>
                </div>
            </div>

            <div class="as9120-section">
                <h2>Why AS 9120 was created</h2>
                <p>Historically, aerospace distributors were audited to a mix of customer-specific requirements, leading to inconsistency and gaps—particularly around counterfeit parts, documentation control, and traceability.</p>

                <div class="as9120-cards">
                    <div class="as9120-card">
                        <h3>Standardisation</h3>
                        <p>Standardise quality requirements for aerospace distributors across the global supply chain</p>
                    </div>
                    <div class="as9120-card">
                        <h3>Integrity</h3>
                        <p>Strengthen supply-chain integrity and airworthiness assurance</p>
                    </div>
                    <div class="as9120-card">
                        <h3>Risk Reduction</h3>
                        <p>Reduce risk associated with falsified or non-conforming parts</p>
                    </div>
                    <div class="as9120-card">
                        <h3>Global Confidence</h3>
                        <p>Provide global confidence in distributor competence</p>
                    </div>
                </div>

                <p style="margin-top: 30px;"><strong>The standard recognises that distributors play a critical safety role, even though they do not manufacture parts.</strong></p>
            </div>

            <div class="as9120-section">
                <h2>Why AS 9120 matters for UK organisations</h2>
                <p>For UK-based aerospace stockists and distributors, AS 9120 is often the gateway to doing business with:</p>

                <div class="as9120-cards">
                    <div class="as9120-card">
                        <h3>Aircraft and engine OEMs</h3>
                        <p>Original Equipment Manufacturers require certified suppliers</p>
                    </div>
                    <div class="as9120-card">
                        <h3>Defence primes</h3>
                        <p>Ministry of Defence and defence contractors mandate compliance</p>
                    </div>
                    <div class="as9120-card">
                        <h3>MRO organisations</h3>
                        <p>Maintenance, Repair, and Overhaul facilities need assured supply chains</p>
                    </div>
                    <div class="as9120-card">
                        <h3>Tier 1 and Tier 2 suppliers</h3>
                        <p>Major aerospace manufacturers require certified distributors</p>
                    </div>
                </div>

                <p style="margin-top: 30px;">Without AS 9120 certification, many organisations are excluded from approved supplier lists. Certification demonstrates compliance with international aerospace expectations and supports regulatory oversight from bodies such as the Civil Aviation Authority (CAA).</p>
                <p><strong>It also provides strong protection against reputational damage arising from counterfeit or undocumented parts.</strong></p>
            </div>

            <div class="as9120-section">
                <h2>Who AS 9120 is for</h2>
                <p>AS 9120 applies to organisations involved in:</p>

                <div class="as9120-cards">
                    <div class="as9120-card">
                        <h3>📦 Aerospace Parts Stockists & Distributors</h3>
                        <p>Companies that stock and distribute aerospace components</p>
                    </div>
                    <div class="as9120-card">
                        <h3>🔧 Hardware & Component Suppliers</h3>
                        <p>Suppliers of fasteners, fittings, and hardware</p>
                    </div>
                    <div class="as9120-card">
                        <h3>🧪 Material & Consumables Distributors</h3>
                        <p>Distributors of raw materials and consumables</p>
                    </div>
                    <div class="as9120-card">
                        <h3>⚙️ Spare Parts & Rotables Suppliers</h3>
                        <p>Suppliers of spare parts and repairable components</p>
                    </div>
                    <div class="as9120-card">
                        <h3>🔄 Aftermarket Aerospace Supply Chains</h3>
                        <p>Aftermarket suppliers and support organisations</p>
                    </div>
                </div>

                <p style="margin-top: 30px;"><strong>It is suitable for organisations supplying civil aviation, defence, and space sectors.</strong></p>
            </div>

            <div class="as9120-section">
                <h2>Key principles of AS 9120</h2>
                <p>AS 9120 includes all ISO 9001 requirements plus aerospace-specific controls, including:</p>

                <div class="as9120-principles-grid">
                    <div class="as9120-principle">
                        <h4>Traceability</h4>
                        <p>Full traceability of parts, documentation, and approvals throughout the supply chain.</p>
                    </div>
                    <div class="as9120-principle">
                        <h4>Counterfeit Part Prevention</h4>
                        <p>Robust controls to prevent counterfeit or suspect parts from entering the supply chain.</p>
                    </div>
                    <div class="as9120-principle">
                        <h4>Supplier Approval & Monitoring</h4>
                        <p>Ensuring parts are sourced only from approved and verified suppliers.</p>
                    </div>
                    <div class="as9120-principle">
                        <h4>Storage & Handling Controls</h4>
                        <p>Protecting product integrity during storage, handling, and transport operations.</p>
                    </div>
                    <div class="as9120-principle">
                        <h4>Documentation & Record Control</h4>
                        <p>Managing certificates of conformity, airworthiness data, and traceability records.</p>
                    </div>
                    <div class="as9120-principle">
                        <h4>Risk Management</h4>
                        <p>Identifying and mitigating supply-chain risks and quality threats.</p>
                    </div>
                </div>
            </div>

            <div class="as9120-section">
                <h2>Benefits of AS 9120</h2>

                <div class="as9120-benefits">
                    <div class="as9120-benefit-category">
                        <h3>Internal Benefits</h3>
                        <ul>
                            <li>Improved control of inventory and documentation</li>
                            <li>Reduced risk of non-conforming or suspect parts</li>
                            <li>Clear responsibilities and accountability</li>
                            <li>Stronger operational discipline</li>
                        </ul>
                    </div>

                    <div class="as9120-benefit-category">
                        <h3>Strategic Benefits</h3>
                        <ul>
                            <li>Access to global aerospace supply chains</li>
                            <li>Approved supplier status with OEMs and MROs</li>
                            <li>Increased customer confidence and trust</li>
                            <li>Long-term contract opportunities</li>
                        </ul>
                    </div>

                    <div class="as9120-benefit-category">
                        <h3>Compliance & Risk Benefits</h3>
                        <ul>
                            <li>Reduced exposure to counterfeit-related incidents</li>
                            <li>Strong defence against regulatory or contractual challenges</li>
                            <li>Alignment with aviation safety expectations</li>
                        </ul>
                    </div>
                </div>
            </div>

            <div class="as9120-section">
                <h2>What AS 9120 auditors actually look for</h2>
                <p>AS 9120 audits are detailed and evidence-driven. Auditors typically assess:</p>

                <div class="as9120-cards">
                    <div class="as9120-card">
                        <h3>Supplier Approval Processes</h3>
                        <p>Verification of authorised sources and approved supplier lists</p>
                    </div>
                    <div class="as9120-card">
                        <h3>Traceability Records</h3>
                        <p>Batch, serial, and documentation control throughout the supply chain</p>
                    </div>
                    <div class="as9120-card">
                        <h3>Counterfeit Prevention Measures</h3>
                        <p>Risk assessment and controls to prevent suspect parts</p>
                    </div>
                    <div class="as9120-card">
                        <h3>Storage & Handling Conditions</h3>
                        <p>Preservation of product integrity in storage and distribution</p>
                    </div>
                    <div class="as9120-card">
                        <h3>Training & Competence</h3>
                        <p>Staff awareness of aerospace risks and quality requirements</p>
                    </div>
                    <div class="as9120-card">
                        <h3>Evidence of Use</h3>
                        <p>Proof the system operates effectively day-to-day</p>
                    </div>
                </div>

                <p style="margin-top: 30px;"><strong>Audits are typically more demanding than ISO 9001 audits due to the safety-critical nature of aerospace supply chains.</strong></p>
            </div>

            <div class="as9120-section">
                <h2>AS 9120 in practice (real-world examples)</h2>

                <div class="as9120-cards">
                    <div class="as9120-card">
                        <h3>Aerospace Stockist</h3>
                        <p>A UK aerospace distributor achieves AS 9120 to supply certified components to MROs and defence customers. Improved traceability and supplier controls unlock new approved supplier listings.</p>
                    </div>
                    <div class="as9120-card">
                        <h3>Aftermarket Parts Supplier</h3>
                        <p>An aftermarket supplier uses AS 9120 to strengthen counterfeit prevention and documentation management—reducing risk and increasing customer trust.</p>
                    </div>
                </div>
            </div>

            <div class="as9120-section">
                <h2>Common mistakes when implementing AS 9120</h2>

                <div class="as9120-cards">
                    <div class="as9120-card">
                        <h3>Assuming ISO 9001 Is Sufficient</h3>
                        <p>AS 9120 introduces significant aerospace-specific requirements beyond ISO 9001.</p>
                    </div>
                    <div class="as9120-card">
                        <h3>Weak Counterfeit Controls</h3>
                        <p>This is a major audit focus and common non-conformity area.</p>
                    </div>
                    <div class="as9120-card">
                        <h3>Poor Documentation Management</h3>
                        <p>Missing or incorrect paperwork can result in serious audit findings.</p>
                    </div>
                </div>
            </div>

            <div class="as9120-section">
                <h2>AS 9120 certification process</h2>

                <div class="as9120-process-steps">
                    <div class="as9120-step">
                        <h4>Stage 1: Documentation & Readiness Review</h4>
                        <p>The auditor confirms your QMS meets AS 9120 requirements.</p>
                    </div>
                    <div class="as9120-step">
                        <h4>Stage 2: Certification Audit</h4>
                        <p>A detailed audit verifies implementation and effectiveness.</p>
                    </div>
                    <div class="as9120-step">
                        <h4>Surveillance Audits</h4>
                        <p>Annual audits ensure ongoing compliance and improvement.</p>
                    </div>
                    <div class="as9120-step">
                        <h4>Recertification</h4>
                        <p>A full reassessment every three years renews certification.</p>
                    </div>
                </div>
            </div>

            <div class="as9120-section">
                <h2>How long does AS 9120 certification last?</h2>
                <p>AS 9120 certification is valid for three years, subject to successful annual surveillance audits. Failure to address major non-conformities can lead to suspension or withdrawal—often with immediate contractual consequences.</p>
            </div>

            <div class="as9120-section">
                <h2>How much does AS 9120 cost in the UK?</h2>
                <p>Costs vary depending on:</p>
                <ul>
                    <li>Organisation size and number of employees</li>
                    <li>Scope of distribution activities</li>
                    <li>Number of sites and suppliers</li>
                </ul>

                <div class="as9120-highlight-box">
                    <h3>Typical costs include:</h3>
                    <ul>
                        <li>UKAS-accredited certification audit fees</li>
                        <li>Consultancy and gap analysis (if required)</li>
                        <li>Internal training and system maintenance</li>
                    </ul>
                    <p style="margin-top: 20px;"><strong>While demanding, AS 9120 delivers strong ROI through market access and risk reduction.</strong></p>
                </div>
            </div>

            <div class="as9120-section">
                <h2>AS 9120 and integration with other standards</h2>
                <p>AS 9120 follows the Annex SL High-Level Structure, allowing integration with:</p>

                <div class="as9120-cards">
                    <div class="as9120-card">
                        <h3>ISO 9001</h3>
                        <p>Quality Management foundation</p>
                    </div>
                    <div class="as9120-card">
                        <h3>ISO 14001</h3>
                        <p>Environmental Management</p>
                    </div>
                    <div class="as9120-card">
                        <h3>ISO 45001</h3>
                        <p>Health & Safety</p>
                    </div>
                    <div class="as9120-card">
                        <h3>ISO 27001</h3>
                        <p>Information Security</p>
                    </div>
                </div>

                <p style="margin-top: 30px;"><strong>Many aerospace distributors operate a fully Integrated Management System (IMS).</strong></p>
            </div>

            <div class="as9120-section">
                <h2>Who should NOT implement AS 9120?</h2>
                <p>If your organisation does not distribute aerospace parts or supply the aerospace/defence sector, AS 9120 is unlikely to be appropriate. The standard requires strong discipline, documentation control, and ongoing oversight.</p>
            </div>

            <div class="as9120-section">
                <h2>Frequently Asked Questions (FAQs)</h2>

                <div class="as9120-faq">
                    <h3>Is AS 9120 mandatory in the UK?</h3>
                    <p>No, but it is frequently a contractual requirement for approved supplier status.</p>
                </div>

                <div class="as9120-faq">
                    <h3>Is AS 9120 the same as EN 9120?</h3>
                    <p>Yes. They are regional versions of the same global standard maintained by IAQG.</p>
                </div>

                <div class="as9120-faq">
                    <h3>Can SMEs achieve AS 9120?</h3>
                    <p>Yes. Many UK aerospace SMEs are successfully certified to AS 9120.</p>
                </div>

                <div class="as9120-faq">
                    <h3>Is AS 9120 harder than ISO 9001?</h3>
                    <p>Yes. It includes additional aerospace-specific and safety-focused requirements.</p>
                </div>
            </div>

            <div class="as9120-cta-box">
                <h2>Ready to achieve AS 9120 certification?</h2>
                <p>Get UKAS-accredited AS 9120 certification and unlock access to global aerospace supply chains.</p>
                <a href="/contact/" class="as9120-cta-primary">Start Your Certification Journey</a>
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

        self.stdout.write(self.style.SUCCESS(f"✓ Updated AS 9120 page"))
        self.stdout.write(self.style.SUCCESS(f"✓ URL: /{page.slug}/"))
        self.stdout.write(self.style.SUCCESS(f"✓ Published successfully"))
