from django.core.management.base import BaseCommand
from home.models import FlexiblePage
import uuid


class Command(BaseCommand):
    help = 'Updates AS 9110 page content'

    def handle(self, *args, **options):
        self.stdout.write("=== Updating AS 9110 Page ===\n")

        try:
            page = FlexiblePage.objects.get(slug='as-9110')
            self.stdout.write(f"Found page: {page.title}")
        except FlexiblePage.DoesNotExist:
            self.stdout.write(self.style.ERROR("AS 9110 page not found"))
            return

        content_html = """
        <style>
            main { padding-top: 0 !important; margin-top: 0 !important; }
            .as9110-hero {
                background: linear-gradient(135deg, #ef6c00 0%, #ff9800 100%);
                color: white;
                padding: 80px 20px;
                margin: 0;
                text-align: center;
            }
            .as9110-hero h1 {
                font-size: 3em;
                margin-bottom: 20px;
                font-weight: 700;
            }
            .as9110-icon {
                font-size: 4em;
                margin-bottom: 20px;
            }
            .as9110-subtitle {
                font-size: 1.3em;
                margin-bottom: 30px;
                opacity: 0.95;
                max-width: 800px;
                margin-left: auto;
                margin-right: auto;
                line-height: 1.6;
            }
            .as9110-features {
                display: flex;
                gap: 15px;
                justify-content: center;
                flex-wrap: wrap;
                margin-top: 30px;
            }
            .as9110-feature-badge {
                background: rgba(255,255,255,0.2);
                padding: 10px 20px;
                border-radius: 25px;
                font-weight: 600;
                backdrop-filter: blur(10px);
            }
            .as9110-cta-buttons {
                margin-top: 40px;
                display: flex;
                gap: 20px;
                justify-content: center;
                flex-wrap: wrap;
            }
            .as9110-cta-primary, .as9110-cta-secondary {
                padding: 15px 35px;
                font-size: 1.1em;
                border-radius: 30px;
                text-decoration: none;
                font-weight: 600;
                transition: all 0.3s;
            }
            .as9110-cta-primary {
                background: white;
                color: #ef6c00;
            }
            .as9110-cta-primary:hover {
                transform: translateY(-2px);
                box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            }
            .as9110-cta-secondary {
                background: transparent;
                color: white;
                border: 2px solid white;
            }
            .as9110-cta-secondary:hover {
                background: white;
                color: #ef6c00;
            }
            .as9110-content {
                max-width: 1200px;
                margin: 0 auto;
                padding: 60px 20px;
            }
            .as9110-section {
                margin-bottom: 60px;
            }
            .as9110-section h2 {
                color: #ef6c00;
                font-size: 2.2em;
                margin-bottom: 25px;
                font-weight: 700;
            }
            .as9110-section p {
                font-size: 1.15em;
                line-height: 1.8;
                color: #333;
                margin-bottom: 20px;
            }
            .as9110-cards {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 25px;
                margin-top: 30px;
            }
            .as9110-card {
                background: #f5f5f5;
                padding: 30px;
                border-radius: 15px;
                border-left: 5px solid #ff9800;
            }
            .as9110-card h3 {
                color: #ef6c00;
                font-size: 1.5em;
                margin-bottom: 15px;
                font-weight: 600;
            }
            .as9110-card p, .as9110-card ul {
                font-size: 1.05em;
                line-height: 1.7;
                color: #555;
            }
            .as9110-card ul {
                margin-top: 15px;
                padding-left: 20px;
            }
            .as9110-card li {
                margin-bottom: 10px;
            }
            .as9110-highlight-box {
                background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%);
                padding: 40px;
                border-radius: 15px;
                margin: 40px 0;
                border-left: 6px solid #ef6c00;
            }
            .as9110-highlight-box h3 {
                color: #ef6c00;
                font-size: 1.8em;
                margin-bottom: 20px;
                font-weight: 600;
            }
            .as9110-principles-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
                gap: 20px;
                margin-top: 30px;
            }
            .as9110-principle {
                background: white;
                padding: 25px;
                border-radius: 12px;
                box-shadow: 0 3px 10px rgba(0,0,0,0.1);
            }
            .as9110-principle h4 {
                color: #ef6c00;
                font-size: 1.3em;
                margin-bottom: 12px;
                font-weight: 600;
            }
            .as9110-principle p {
                font-size: 1em;
                color: #666;
                margin: 0;
            }
            .as9110-benefits {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
                gap: 30px;
                margin-top: 30px;
            }
            .as9110-benefit-category {
                background: white;
                padding: 35px;
                border-radius: 15px;
                box-shadow: 0 5px 20px rgba(0,0,0,0.08);
            }
            .as9110-benefit-category h3 {
                color: #ef6c00;
                font-size: 1.6em;
                margin-bottom: 20px;
                font-weight: 600;
            }
            .as9110-benefit-category ul {
                list-style: none;
                padding: 0;
            }
            .as9110-benefit-category li {
                padding: 12px 0;
                border-bottom: 1px solid #eee;
                font-size: 1.05em;
                color: #555;
            }
            .as9110-benefit-category li:before {
                content: "✓ ";
                color: #ff9800;
                font-weight: bold;
                margin-right: 10px;
            }
            .as9110-faq {
                background: #f9f9f9;
                padding: 30px;
                border-radius: 12px;
                margin: 25px 0;
            }
            .as9110-faq h3 {
                color: #ef6c00;
                font-size: 1.4em;
                margin-bottom: 12px;
                font-weight: 600;
            }
            .as9110-faq p {
                font-size: 1.1em;
                color: #666;
                margin: 0;
                line-height: 1.7;
            }
            .as9110-process-steps {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 20px;
                margin-top: 30px;
            }
            .as9110-step {
                background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%);
                padding: 30px;
                border-radius: 12px;
                text-align: center;
            }
            .as9110-step h4 {
                color: #ef6c00;
                font-size: 1.4em;
                margin-bottom: 15px;
                font-weight: 600;
            }
            .as9110-step p {
                font-size: 1.05em;
                color: #555;
                margin: 0;
            }
            .as9110-cta-box {
                background: linear-gradient(135deg, #ef6c00 0%, #ff9800 100%);
                color: white;
                padding: 60px 40px;
                border-radius: 20px;
                text-align: center;
                margin-top: 60px;
            }
            .as9110-cta-box h2 {
                color: white;
                font-size: 2.5em;
                margin-bottom: 20px;
            }
            .as9110-cta-box p {
                font-size: 1.3em;
                margin-bottom: 30px;
                opacity: 0.95;
                color: white;
            }
            @media (max-width: 768px) {
                .as9110-hero h1 { font-size: 2em; }
                .as9110-section h2 { font-size: 1.8em; }
                .as9110-cards, .as9110-benefits { grid-template-columns: 1fr; }
            }
        </style>

        <div class="as9110-hero">
            <div class="as9110-icon">🔧</div>
            <h1>AS 9110 Certification</h1>
            <p class="as9110-subtitle">Aerospace Maintenance, Repair & Overhaul (MRO) Quality Management System</p>
            <div class="as9110-features">
                <span class="as9110-feature-badge">Airworthiness Control</span>
                <span class="as9110-feature-badge">Human Factors</span>
                <span class="as9110-feature-badge">MRO Excellence</span>
            </div>
            <div class="as9110-cta-buttons">
                <a href="/contact/" class="as9110-cta-primary">Get Certified</a>
                <a href="#what-is" class="as9110-cta-secondary">Learn More</a>
            </div>
        </div>

        <div class="as9110-content">
            <div class="as9110-section" id="what-is">
                <h2>Introduction to AS 9110</h2>
                <p>In aerospace, maintenance errors can be just as dangerous as manufacturing defects. For organisations responsible for maintaining, repairing, or overhauling aircraft and components, quality management is inseparable from flight safety and regulatory compliance. AS 9110 provides the internationally recognised framework that ensures MRO organisations operate with the highest levels of control, traceability, and safety assurance.</p>
                <p>AS 9110 is the aerospace quality management standard specifically developed for Maintenance, Repair and Overhaul (MRO) organisations. It builds on ISO 9001 while introducing additional, aviation-critical requirements covering airworthiness, maintenance control, release certification, and human factors.</p>
            </div>

            <div class="as9110-section">
                <h2>What is AS 9110?</h2>
                <p>AS 9110 is a quality management system (QMS) standard designed for organisations that maintain aircraft, engines, components, or parts. Unlike EN/AS 9100 (manufacturing) or AS 9120 (distribution), AS 9110 focuses exclusively on maintenance activities.</p>
                <p>The standard is maintained by the International Aerospace Quality Group (IAQG) and is aligned globally with EN 9110 (Europe) and JISQ 9110 (Asia).</p>

                <div class="as9110-highlight-box">
                    <h3>In practical terms, AS 9110 helps MRO organisations:</h3>
                    <ul>
                        <li>Ensure continued airworthiness of aircraft and components</li>
                        <li>Control maintenance processes and approvals</li>
                        <li>Reduce human-error-related incidents</li>
                        <li>Meet OEM, customer, and regulatory expectations</li>
                    </ul>
                    <p style="margin-top: 20px;"><strong>For many aerospace customers, AS 9110 certification is a prerequisite for approval.</strong></p>
                </div>
            </div>

            <div class="as9110-section">
                <h2>Why AS 9110 was created</h2>
                <p>Historically, maintenance organisations were audited against a mix of aviation regulations and customer-specific quality requirements. This led to inconsistency, duplication, and gaps—particularly around human factors, documentation, and release-to-service controls.</p>

                <div class="as9110-cards">
                    <div class="as9110-card">
                        <h3>Harmonisation</h3>
                        <p>Harmonise quality requirements for aerospace maintenance worldwide</p>
                    </div>
                    <div class="as9110-card">
                        <h3>Process Control</h3>
                        <p>Strengthen maintenance process control and traceability</p>
                    </div>
                    <div class="as9110-card">
                        <h3>Safety Focus</h3>
                        <p>Reduce safety risk caused by maintenance error</p>
                    </div>
                    <div class="as9110-card">
                        <h3>Global Confidence</h3>
                        <p>Provide global confidence in MRO capability</p>
                    </div>
                </div>

                <p style="margin-top: 30px;"><strong>The standard recognises that maintenance is a high-risk, safety-critical activity requiring its own dedicated quality framework.</strong></p>
            </div>

            <div class="as9110-section">
                <h2>Why AS 9110 matters for UK organisations</h2>
                <p>For UK MRO organisations, AS 9110 is often essential to operate within the global aerospace supply chain. It is frequently required by:</p>

                <div class="as9110-cards">
                    <div class="as9110-card">
                        <h3>Aircraft and engine OEMs</h3>
                        <p>Original Equipment Manufacturers require certified MRO partners</p>
                    </div>
                    <div class="as9110-card">
                        <h3>Airlines and leasing companies</h3>
                        <p>Operators demand assured maintenance quality</p>
                    </div>
                    <div class="as9110-card">
                        <h3>Defence primes and MOD suppliers</h3>
                        <p>Military contracts require rigorous MRO standards</p>
                    </div>
                    <div class="as9110-card">
                        <h3>International aviation customers</h3>
                        <p>Global recognition and confidence in UK MRO capability</p>
                    </div>
                </div>

                <p style="margin-top: 30px;">AS 9110 also aligns strongly with regulatory oversight from the Civil Aviation Authority (CAA) and international aviation authorities, reinforcing confidence in maintenance control and airworthiness management.</p>
                <p><strong>Certification demonstrates that your organisation meets international best practice, not just minimum regulatory compliance.</strong></p>
            </div>

            <div class="as9110-section">
                <h2>Who AS 9110 is for</h2>
                <p>AS 9110 applies to organisations involved in:</p>

                <div class="as9110-cards">
                    <div class="as9110-card">
                        <h3>✈️ Aircraft Maintenance Organisations (AMOs)</h3>
                        <p>Organisations approved for aircraft maintenance and repair</p>
                    </div>
                    <div class="as9110-card">
                        <h3>⚙️ Engine & Component Overhaul Facilities</h3>
                        <p>Specialist facilities for engine and component overhaul</p>
                    </div>
                    <div class="as9110-card">
                        <h3>🔧 Line and Base Maintenance Providers</h3>
                        <p>Providers of scheduled and unscheduled maintenance</p>
                    </div>
                    <div class="as9110-card">
                        <h3>🛡️ Defence & Military MRO Providers</h3>
                        <p>Military aviation maintenance and support organisations</p>
                    </div>
                    <div class="as9110-card">
                        <h3>🔬 Specialist Repair Organisations</h3>
                        <p>Specialist repair and testing organisations</p>
                    </div>
                </div>

                <p style="margin-top: 30px;"><strong>It is suitable for civil, defence, and space-related maintenance activities.</strong></p>
            </div>

            <div class="as9110-section">
                <h2>Key principles of AS 9110</h2>
                <p>AS 9110 includes all ISO 9001 requirements plus maintenance-specific aerospace controls, including:</p>

                <div class="as9110-principles-grid">
                    <div class="as9110-principle">
                        <h4>Maintenance Process Control</h4>
                        <p>Clear definition, planning, and execution of maintenance activities.</p>
                    </div>
                    <div class="as9110-principle">
                        <h4>Airworthiness & Release to Service</h4>
                        <p>Robust certification and approval processes for release to service.</p>
                    </div>
                    <div class="as9110-principle">
                        <h4>Human Factors Management</h4>
                        <p>Addressing fatigue, competence, communication, and error prevention.</p>
                    </div>
                    <div class="as9110-principle">
                        <h4>Configuration & Technical Data Control</h4>
                        <p>Ensuring correct manuals, revisions, and instructions are used.</p>
                    </div>
                    <div class="as9110-principle">
                        <h4>Risk Management</h4>
                        <p>Identifying and mitigating maintenance-related risks.</p>
                    </div>
                    <div class="as9110-principle">
                        <h4>Traceability & Records</h4>
                        <p>Full control of maintenance records and history.</p>
                    </div>
                </div>
            </div>

            <div class="as9110-section">
                <h2>Benefits of AS 9110</h2>

                <div class="as9110-benefits">
                    <div class="as9110-benefit-category">
                        <h3>Internal Benefits</h3>
                        <ul>
                            <li>Improved maintenance consistency and control</li>
                            <li>Reduced risk of maintenance error</li>
                            <li>Clear accountability and competence management</li>
                            <li>Stronger safety and reporting culture</li>
                        </ul>
                    </div>

                    <div class="as9110-benefit-category">
                        <h3>Strategic Benefits</h3>
                        <ul>
                            <li>Approved supplier status with OEMs and operators</li>
                            <li>Increased customer and regulator confidence</li>
                            <li>Access to international MRO contracts</li>
                            <li>Enhanced reputation for safety and reliability</li>
                        </ul>
                    </div>

                    <div class="as9110-benefit-category">
                        <h3>Compliance & Risk Benefits</h3>
                        <ul>
                            <li>Strong alignment with aviation regulatory requirements</li>
                            <li>Reduced exposure to safety incidents and liability</li>
                            <li>Robust defence during regulatory or customer audits</li>
                        </ul>
                    </div>
                </div>
            </div>

            <div class="as9110-section">
                <h2>What AS 9110 auditors actually look for</h2>
                <p>AS 9110 audits are rigorous and operationally focused. Auditors typically assess:</p>

                <div class="as9110-cards">
                    <div class="as9110-card">
                        <h3>Maintenance Planning & Control</h3>
                        <p>Evidence of controlled and documented maintenance processes</p>
                    </div>
                    <div class="as9110-card">
                        <h3>Human Factors Awareness</h3>
                        <p>Training, reporting, and mitigation of human error risks</p>
                    </div>
                    <div class="as9110-card">
                        <h3>Technical Data Management</h3>
                        <p>Correct and current documentation, manuals, and procedures</p>
                    </div>
                    <div class="as9110-card">
                        <h3>Release to Service Controls</h3>
                        <p>Certification, authorisation, and airworthiness release processes</p>
                    </div>
                    <div class="as9110-card">
                        <h3>Training & Competence</h3>
                        <p>Engineer qualifications, approvals, and continuing competence</p>
                    </div>
                    <div class="as9110-card">
                        <h3>Evidence of Use</h3>
                        <p>Records showing the system operates effectively day-to-day</p>
                    </div>
                </div>

                <p style="margin-top: 30px;"><strong>Audits go far beyond paperwork and focus heavily on shop-floor and hangar activity.</strong></p>
            </div>

            <div class="as9110-section">
                <h2>AS 9110 in practice (real-world examples)</h2>

                <div class="as9110-cards">
                    <div class="as9110-card">
                        <h3>Aircraft Maintenance Organisation</h3>
                        <p>A UK MRO achieves AS 9110 to support contracts with international airlines. Improved maintenance control and documentation strengthen regulatory confidence and customer trust.</p>
                    </div>
                    <div class="as9110-card">
                        <h3>Component Overhaul Facility</h3>
                        <p>A component repair organisation uses AS 9110 to formalise human factors controls and reduce maintenance-related non-conformities—improving safety and audit outcomes.</p>
                    </div>
                </div>
            </div>

            <div class="as9110-section">
                <h2>Common mistakes when implementing AS 9110</h2>

                <div class="as9110-cards">
                    <div class="as9110-card">
                        <h3>Treating It Like ISO 9001</h3>
                        <p>AS 9110 has far greater operational depth and safety focus than ISO 9001.</p>
                    </div>
                    <div class="as9110-card">
                        <h3>Underestimating Human Factors Requirements</h3>
                        <p>This is a major audit and safety emphasis area.</p>
                    </div>
                    <div class="as9110-card">
                        <h3>Weak Control of Technical Data</h3>
                        <p>Out-of-date manuals and instructions are a common failure point.</p>
                    </div>
                </div>
            </div>

            <div class="as9110-section">
                <h2>AS 9110 certification process</h2>

                <div class="as9110-process-steps">
                    <div class="as9110-step">
                        <h4>Stage 1: Readiness & Documentation Review</h4>
                        <p>The auditor checks that your QMS meets AS 9110 requirements.</p>
                    </div>
                    <div class="as9110-step">
                        <h4>Stage 2: Certification Audit</h4>
                        <p>A detailed on-site audit evaluates implementation and effectiveness.</p>
                    </div>
                    <div class="as9110-step">
                        <h4>Surveillance Audits</h4>
                        <p>Annual audits confirm continued compliance.</p>
                    </div>
                    <div class="as9110-step">
                        <h4>Recertification</h4>
                        <p>A full reassessment every three years renews certification.</p>
                    </div>
                </div>
            </div>

            <div class="as9110-section">
                <h2>How long does AS 9110 certification last?</h2>
                <p>AS 9110 certification is valid for three years, subject to successful annual surveillance audits. Failure to address major non-conformities can lead to suspension or withdrawal, often with immediate commercial impact.</p>
            </div>

            <div class="as9110-section">
                <h2>How much does AS 9110 cost in the UK?</h2>
                <p>Costs depend on:</p>
                <ul>
                    <li>Size and complexity of maintenance activities</li>
                    <li>Number of staff and approvals</li>
                    <li>Number of sites and scope of work</li>
                </ul>

                <div class="as9110-highlight-box">
                    <h3>Typical costs include:</h3>
                    <ul>
                        <li>UKAS-accredited certification audit fees</li>
                        <li>Consultancy and gap analysis (if required)</li>
                        <li>Training and system maintenance costs</li>
                    </ul>
                    <p style="margin-top: 20px;"><strong>Although demanding, AS 9110 delivers strong ROI through market access, safety assurance, and reduced risk.</strong></p>
                </div>
            </div>

            <div class="as9110-section">
                <h2>AS 9110 and integration with other standards</h2>
                <p>AS 9110 follows the Annex SL High-Level Structure, allowing integration with:</p>

                <div class="as9110-cards">
                    <div class="as9110-card">
                        <h3>ISO 9001</h3>
                        <p>Quality Management foundation</p>
                    </div>
                    <div class="as9110-card">
                        <h3>ISO 14001</h3>
                        <p>Environmental Management</p>
                    </div>
                    <div class="as9110-card">
                        <h3>ISO 45001</h3>
                        <p>Health & Safety</p>
                    </div>
                    <div class="as9110-card">
                        <h3>ISO 27001</h3>
                        <p>Information Security</p>
                    </div>
                </div>

                <p style="margin-top: 30px;"><strong>Many MRO organisations operate a fully Integrated Management System (IMS).</strong></p>
            </div>

            <div class="as9110-section">
                <h2>Who should NOT implement AS 9110?</h2>
                <p>If your organisation does not perform aerospace maintenance or overhaul activities and has no customer or regulatory requirement, AS 9110 is unlikely to be appropriate. The standard requires strong operational discipline and continuous oversight.</p>
            </div>

            <div class="as9110-section">
                <h2>Frequently Asked Questions (FAQs)</h2>

                <div class="as9110-faq">
                    <h3>Is AS 9110 mandatory in the UK?</h3>
                    <p>No, but it is often a contractual requirement for MRO approval.</p>
                </div>

                <div class="as9110-faq">
                    <h3>Is AS 9110 the same as EN 9110?</h3>
                    <p>Yes. They are regional versions of the same global standard.</p>
                </div>

                <div class="as9110-faq">
                    <h3>Can SMEs achieve AS 9110?</h3>
                    <p>Yes. Many UK MRO SMEs are successfully certified.</p>
                </div>

                <div class="as9110-faq">
                    <h3>Is AS 9110 harder than ISO 9001?</h3>
                    <p>Yes. It includes significant aviation-specific and safety-critical requirements.</p>
                </div>
            </div>

            <div class="as9110-cta-box">
                <h2>Ready to achieve AS 9110 certification?</h2>
                <p>Get UKAS-accredited AS 9110 certification and demonstrate MRO excellence to global aerospace customers.</p>
                <a href="/contact/" class="as9110-cta-primary">Start Your Certification Journey</a>
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

        self.stdout.write(self.style.SUCCESS(f"✓ Updated AS 9110 page"))
        self.stdout.write(self.style.SUCCESS(f"✓ URL: /{page.slug}/"))
        self.stdout.write(self.style.SUCCESS(f"✓ Published successfully"))
