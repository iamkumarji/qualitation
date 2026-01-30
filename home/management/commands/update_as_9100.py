from django.core.management.base import BaseCommand
from home.models import FlexiblePage
import uuid


class Command(BaseCommand):
    help = 'Updates AS 9100 page content'

    def handle(self, *args, **options):
        self.stdout.write("=== Updating AS 9100 Page ===\n")

        try:
            page = FlexiblePage.objects.get(slug='as-9100')
            self.stdout.write(f"Found page: {page.title}")
        except FlexiblePage.DoesNotExist:
            self.stdout.write(self.style.ERROR("AS 9100 page not found"))
            return

        content_html = """
        <style>
            main { padding-top: 0 !important; margin-top: 0 !important; }
            .as9100-hero {
                background: linear-gradient(135deg, #0d47a1 0%, #1565c0 50%, #1976d2 100%);
                color: white;
                padding: 100px 20px;
                margin: 0;
                text-align: center;
                position: relative;
                overflow: hidden;
            }
            .as9100-hero::before {
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
            .as9100-hero-content {
                position: relative;
                z-index: 1;
            }
            .as9100-hero h1 {
                font-size: 3.5em;
                margin-bottom: 15px;
                font-weight: 800;
                letter-spacing: -1px;
            }
            .as9100-icon {
                font-size: 5em;
                margin-bottom: 25px;
                display: inline-block;
                animation: float 3s ease-in-out infinite;
            }
            @keyframes float {
                0%, 100% { transform: translateY(0px); }
                50% { transform: translateY(-10px); }
            }
            .as9100-subtitle {
                font-size: 1.4em;
                margin-bottom: 35px;
                opacity: 0.98;
                max-width: 750px;
                margin-left: auto;
                margin-right: auto;
                line-height: 1.6;
                font-weight: 400;
            }
            .as9100-features {
                display: flex;
                gap: 15px;
                justify-content: center;
                flex-wrap: wrap;
                margin-top: 30px;
            }
            .as9100-feature-badge {
                background: rgba(255,255,255,0.2);
                padding: 10px 20px;
                border-radius: 25px;
                font-weight: 600;
                backdrop-filter: blur(10px);
            }
            .as9100-cta-buttons {
                margin-top: 40px;
                display: flex;
                gap: 20px;
                justify-content: center;
                flex-wrap: wrap;
            }
            .as9100-cta-primary, .as9100-cta-secondary {
                padding: 15px 35px;
                font-size: 1.1em;
                border-radius: 30px;
                text-decoration: none;
                font-weight: 600;
                transition: all 0.3s;
            }
            .as9100-cta-primary {
                background: white;
                color: #0d47a1;
            }
            .as9100-cta-primary:hover {
                transform: translateY(-2px);
                box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            }
            .as9100-cta-secondary {
                background: transparent;
                color: white;
                border: 2px solid white;
            }
            .as9100-cta-secondary:hover {
                background: white;
                color: #0d47a1;
            }
            .as9100-content {
                max-width: 1200px;
                margin: 0 auto;
                padding: 60px 20px;
            }
            .as9100-section {
                margin-bottom: 60px;
            }
            .as9100-section h2 {
                color: #0d47a1;
                font-size: 2.2em;
                margin-bottom: 25px;
                font-weight: 700;
            }
            .as9100-section p {
                font-size: 1.15em;
                line-height: 1.8;
                color: #333;
                margin-bottom: 20px;
            }
            .as9100-cards {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 25px;
                margin-top: 30px;
            }
            .as9100-card {
                background: #f5f5f5;
                padding: 30px;
                border-radius: 15px;
                border-left: 5px solid #1976d2;
            }
            .as9100-card h3 {
                color: #0d47a1;
                font-size: 1.5em;
                margin-bottom: 15px;
                font-weight: 600;
            }
            .as9100-card p, .as9100-card ul {
                font-size: 1.05em;
                line-height: 1.7;
                color: #555;
            }
            .as9100-card ul {
                margin-top: 15px;
                padding-left: 20px;
            }
            .as9100-card li {
                margin-bottom: 10px;
            }
            .as9100-highlight-box {
                background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
                padding: 40px;
                border-radius: 15px;
                margin: 40px 0;
                border-left: 6px solid #0d47a1;
            }
            .as9100-highlight-box h3 {
                color: #0d47a1;
                font-size: 1.8em;
                margin-bottom: 20px;
                font-weight: 600;
            }
            .as9100-principles-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
                gap: 20px;
                margin-top: 30px;
            }
            .as9100-principle {
                background: white;
                padding: 25px;
                border-radius: 12px;
                box-shadow: 0 3px 10px rgba(0,0,0,0.1);
            }
            .as9100-principle h4 {
                color: #0d47a1;
                font-size: 1.3em;
                margin-bottom: 12px;
                font-weight: 600;
            }
            .as9100-principle p {
                font-size: 1em;
                color: #666;
                margin: 0;
            }
            .as9100-benefits {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
                gap: 30px;
                margin-top: 30px;
            }
            .as9100-benefit-category {
                background: white;
                padding: 35px;
                border-radius: 15px;
                box-shadow: 0 5px 20px rgba(0,0,0,0.08);
            }
            .as9100-benefit-category h3 {
                color: #0d47a1;
                font-size: 1.6em;
                margin-bottom: 20px;
                font-weight: 600;
            }
            .as9100-benefit-category ul {
                list-style: none;
                padding: 0;
            }
            .as9100-benefit-category li {
                padding: 12px 0;
                border-bottom: 1px solid #eee;
                font-size: 1.05em;
                color: #555;
            }
            .as9100-benefit-category li:before {
                content: "✓ ";
                color: #1976d2;
                font-weight: bold;
                margin-right: 10px;
            }
            .as9100-faq-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));
                gap: 25px;
                margin-top: 30px;
            }
            .as9100-faq {
                background: white;
                padding: 35px;
                border-radius: 15px;
                border: 2px solid #e3f2fd;
                box-shadow: 0 4px 15px rgba(13, 71, 161, 0.08);
                transition: all 0.3s ease;
            }
            .as9100-faq:hover {
                border-color: #1976d2;
                box-shadow: 0 6px 20px rgba(13, 71, 161, 0.15);
                transform: translateY(-2px);
            }
            .as9100-faq h3 {
                color: #0d47a1;
                font-size: 1.35em;
                margin-bottom: 15px;
                font-weight: 700;
                display: flex;
                align-items: center;
            }
            .as9100-faq h3:before {
                content: "Q";
                display: inline-flex;
                align-items: center;
                justify-content: center;
                width: 32px;
                height: 32px;
                background: linear-gradient(135deg, #0d47a1 0%, #1976d2 100%);
                color: white;
                border-radius: 50%;
                font-size: 0.8em;
                font-weight: 700;
                margin-right: 15px;
                flex-shrink: 0;
            }
            .as9100-faq p {
                font-size: 1.1em;
                color: #555;
                margin: 0;
                line-height: 1.8;
                padding-left: 47px;
            }
            @media (max-width: 768px) {
                .as9100-faq-grid {
                    grid-template-columns: 1fr;
                }
            }
            .as9100-process-steps {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 20px;
                margin-top: 30px;
            }
            .as9100-step {
                background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
                padding: 30px;
                border-radius: 12px;
                text-align: center;
            }
            .as9100-step h4 {
                color: #0d47a1;
                font-size: 1.4em;
                margin-bottom: 15px;
                font-weight: 600;
            }
            .as9100-step p {
                font-size: 1.05em;
                color: #555;
                margin: 0;
            }
            .as9100-cta-box {
                background: linear-gradient(135deg, #0d47a1 0%, #1976d2 100%);
                color: white;
                padding: 60px 40px;
                border-radius: 20px;
                text-align: center;
                margin-top: 60px;
            }
            .as9100-cta-box h2 {
                color: white;
                font-size: 2.5em;
                margin-bottom: 20px;
            }
            .as9100-cta-box p {
                font-size: 1.3em;
                margin-bottom: 30px;
                opacity: 0.95;
                color: white;
            }
            @media (max-width: 768px) {
                .as9100-hero {
                    padding: 60px 20px;
                }
                .as9100-hero h1 {
                    font-size: 2.2em;
                }
                .as9100-icon {
                    font-size: 3.5em;
                }
                .as9100-subtitle {
                    font-size: 1.15em;
                }
                .as9100-section h2 { font-size: 1.8em; }
                .as9100-cards, .as9100-benefits { grid-template-columns: 1fr; }
            }
        </style>

        <div class="as9100-hero">
            <div class="as9100-hero-content">
                <div class="as9100-icon">🚀</div>
                <h1>AS 9100 Certification</h1>
                <p class="as9100-subtitle">Aerospace Quality Management System</p>
                <div class="as9100-features">
                    <span class="as9100-feature-badge">Product Safety</span>
                    <span class="as9100-feature-badge">Global Recognition</span>
                    <span class="as9100-feature-badge">Supply Chain Excellence</span>
                </div>
                <div class="as9100-cta-buttons">
                    <a href="/contact/" class="as9100-cta-primary">Get Certified</a>
                    <a href="#what-is" class="as9100-cta-secondary">Learn More</a>
                </div>
            </div>
        </div>

        <div class="as9100-content">
            <div class="as9100-section" id="what-is">
                <h2>Introduction to AS 9100</h2>
                <p>In aerospace and defence, quality failures are not an inconvenience—they are a safety, regulatory, and commercial risk. Organisations operating anywhere in the aerospace supply chain are expected to meet exacting global standards for control, traceability, and risk management. AS 9100 is the internationally recognised benchmark that demonstrates your organisation can be trusted to deliver safe, conforming aerospace products and services.</p>
                <p>AS 9100 is the aerospace quality management system (QMS) standard used primarily in North America, and is fully equivalent to EN 9100 (Europe) and JISQ 9100 (Asia). Together, these form a single global aerospace standard recognised by OEMs, Tier 1 suppliers, and regulators worldwide.</p>
            </div>

            <div class="as9100-section">
                <h2>What is AS 9100?</h2>
                <p>AS 9100 is a sector-specific quality management standard developed for the aerospace, aviation, and defence (AAD) industry. It is based on ISO 9001 but includes extensive additional requirements to address aerospace risks such as product safety, counterfeit parts, configuration control, and complex supply chains.</p>
                <p>The standard is maintained by the International Aerospace Quality Group (IAQG) to ensure global consistency and acceptance.</p>

                <div class="as9100-highlight-box">
                    <h3>In practical terms, AS 9100 helps organisations:</h3>
                    <ul>
                        <li>Deliver safe and reliable aerospace products</li>
                        <li>Control complex and safety-critical processes</li>
                        <li>Meet OEM, regulatory, and contractual requirements</li>
                        <li>Gain and retain access to the global aerospace supply chain</li>
                    </ul>
                    <p style="margin-top: 20px;"><strong>For many customers, AS 9100 certification is mandatory.</strong></p>
                </div>
            </div>

            <div class="as9100-section">
                <h2>Why AS 9100 was created</h2>
                <p>Before AS 9100, aerospace suppliers were subject to numerous customer-specific quality requirements. This resulted in duplicated audits, inconsistent expectations, and increased risk across the supply chain.</p>

                <div class="as9100-cards">
                    <div class="as9100-card">
                        <h3>Harmonisation</h3>
                        <p>Harmonise aerospace quality requirements globally across all major markets</p>
                    </div>
                    <div class="as9100-card">
                        <h3>Product Safety</h3>
                        <p>Strengthen product safety and airworthiness controls throughout the supply chain</p>
                    </div>
                    <div class="as9100-card">
                        <h3>Supplier Performance</h3>
                        <p>Improve supplier consistency and performance across the aerospace industry</p>
                    </div>
                    <div class="as9100-card">
                        <h3>Risk Reduction</h3>
                        <p>Reduce supply-chain risk and audit burden for OEMs and suppliers</p>
                    </div>
                </div>

                <p style="margin-top: 30px;"><strong>It provides a single, trusted quality framework recognised throughout the aerospace industry.</strong></p>
            </div>

            <div class="as9100-section">
                <h2>Why AS 9100 matters for UK organisations</h2>
                <p>Although AS 9100 is the American designation, it is fully equivalent to EN 9100, which is widely used in the UK and Europe. Many UK organisations supplying North American OEMs or defence contractors will see AS 9100 referenced contractually.</p>
                <p>Certification demonstrates that your organisation meets the highest international aerospace quality expectations, supporting approval by major customers and alignment with regulatory oversight such as the Civil Aviation Authority (CAA).</p>
                <p><strong>Without AS/EN 9100, many UK aerospace businesses are excluded from tendering or supplier approval lists.</strong></p>
            </div>

            <div class="as9100-section">
                <h2>Who AS 9100 is for</h2>
                <p>AS 9100 applies to organisations involved in:</p>

                <div class="as9100-cards">
                    <div class="as9100-card">
                        <h3>🏭 Aerospace Manufacturing & Assembly</h3>
                        <p>Manufacturers of aircraft, engines, and aerospace systems</p>
                    </div>
                    <div class="as9100-card">
                        <h3>⚙️ Precision Engineering & Machining</h3>
                        <p>Precision component manufacturers and machine shops</p>
                    </div>
                    <div class="as9100-card">
                        <h3>📐 Design & Engineering Services</h3>
                        <p>Design bureaus and engineering service providers</p>
                    </div>
                    <div class="as9100-card">
                        <h3>🔬 Special Process Providers</h3>
                        <p>Heat treatment, surface finishing, and NDT providers</p>
                    </div>
                    <div class="as9100-card">
                        <h3>🛡️ Defence & Space Sector Suppliers</h3>
                        <p>Suppliers to defence and space programmes</p>
                    </div>
                </div>

                <p style="margin-top: 30px;"><strong>It is relevant to OEMs, Tier 1, Tier 2, and Tier 3 suppliers across civil, defence, and space programmes.</strong></p>
            </div>

            <div class="as9100-section">
                <h2>Key principles of AS 9100</h2>
                <p>AS 9100 incorporates all ISO 9001 requirements plus critical aerospace-specific controls, including:</p>

                <div class="as9100-principles-grid">
                    <div class="as9100-principle">
                        <h4>Product Safety</h4>
                        <p>Identification and management of safety-critical risks throughout the product lifecycle.</p>
                    </div>
                    <div class="as9100-principle">
                        <h4>Risk-Based Thinking</h4>
                        <p>Proactive control of operational and supply-chain risks.</p>
                    </div>
                    <div class="as9100-principle">
                        <h4>Configuration Management</h4>
                        <p>Strict control of designs, changes, and revisions.</p>
                    </div>
                    <div class="as9100-principle">
                        <h4>Counterfeit Part Prevention</h4>
                        <p>Preventing counterfeit or suspect parts entering the supply chain.</p>
                    </div>
                    <div class="as9100-principle">
                        <h4>Traceability</h4>
                        <p>Full traceability of materials, processes, and approvals.</p>
                    </div>
                    <div class="as9100-principle">
                        <h4>Human Factors Awareness</h4>
                        <p>Managing fatigue, competence, and error prevention.</p>
                    </div>
                    <div class="as9100-principle">
                        <h4>Supplier Management</h4>
                        <p>Robust approval, monitoring, and performance evaluation.</p>
                    </div>
                </div>
            </div>

            <div class="as9100-section">
                <h2>Benefits of AS 9100</h2>

                <div class="as9100-benefits">
                    <div class="as9100-benefit-category">
                        <h3>Internal Benefits</h3>
                        <ul>
                            <li>Improved process consistency and control</li>
                            <li>Reduced rework, scrap, and non-conformities</li>
                            <li>Clear accountability and defined responsibilities</li>
                            <li>Stronger quality and safety culture</li>
                        </ul>
                    </div>

                    <div class="as9100-benefit-category">
                        <h3>Strategic Benefits</h3>
                        <ul>
                            <li>Access to global aerospace and defence markets</li>
                            <li>Approved supplier status with OEMs and primes</li>
                            <li>Increased customer confidence and trust</li>
                            <li>Long-term, high-value contract opportunities</li>
                        </ul>
                    </div>

                    <div class="as9100-benefit-category">
                        <h3>Compliance & Risk Benefits</h3>
                        <ul>
                            <li>Alignment with aviation regulatory expectations</li>
                            <li>Reduced operational, safety, and reputational risk</li>
                            <li>Strong defence against product liability claims</li>
                        </ul>
                    </div>
                </div>
            </div>

            <div class="as9100-section">
                <h2>What AS 9100 auditors actually look for</h2>
                <p>AS 9100 audits are significantly more rigorous than ISO 9001 audits. Auditors will assess:</p>

                <div class="as9100-cards">
                    <div class="as9100-card">
                        <h3>Risk & Opportunity Management</h3>
                        <p>Evidence of proactive risk control and opportunity identification</p>
                    </div>
                    <div class="as9100-card">
                        <h3>Product Safety Controls</h3>
                        <p>Identification, escalation, and mitigation of safety risks</p>
                    </div>
                    <div class="as9100-card">
                        <h3>Configuration & Change Management</h3>
                        <p>Traceable and approved changes to designs and processes</p>
                    </div>
                    <div class="as9100-card">
                        <h3>Supplier Oversight</h3>
                        <p>Approval, monitoring, and performance data for suppliers</p>
                    </div>
                    <div class="as9100-card">
                        <h3>Operational Discipline</h3>
                        <p>Adherence to procedures and controls on the shop floor</p>
                    </div>
                    <div class="as9100-card">
                        <h3>Evidence of Effectiveness</h3>
                        <p>Records proving the system works in practice</p>
                    </div>
                </div>

                <p style="margin-top: 30px;"><strong>Audits focus heavily on real-world implementation, not just documentation.</strong></p>
            </div>

            <div class="as9100-section">
                <h2>AS 9100 in practice (real-world examples)</h2>

                <div class="as9100-cards">
                    <div class="as9100-card">
                        <h3>Precision Engineering Supplier</h3>
                        <p>A UK machining company achieves AS/EN 9100 to supply components to a US aerospace OEM. Enhanced traceability, inspection control, and risk management unlock long-term contracts.</p>
                    </div>
                    <div class="as9100-card">
                        <h3>Aerospace Design Organisation</h3>
                        <p>An engineering services firm uses AS 9100 to formalise design control, configuration management, and change approval—meeting strict customer and regulatory expectations.</p>
                    </div>
                </div>
            </div>

            <div class="as9100-section">
                <h2>Common mistakes when implementing AS 9100</h2>

                <div class="as9100-cards">
                    <div class="as9100-card">
                        <h3>Treating It Like ISO 9001</h3>
                        <p>AS 9100 has far greater depth and aerospace-specific rigour than ISO 9001.</p>
                    </div>
                    <div class="as9100-card">
                        <h3>Weak Supplier Control</h3>
                        <p>Supply-chain failures are a major audit focus and risk area.</p>
                    </div>
                    <div class="as9100-card">
                        <h3>Underestimating Cultural Change</h3>
                        <p>Aerospace quality requires discipline at every level of the organisation.</p>
                    </div>
                </div>
            </div>

            <div class="as9100-section">
                <h2>AS 9100 certification process</h2>

                <div class="as9100-process-steps">
                    <div class="as9100-step">
                        <h4>Stage 1: Readiness & Documentation Review</h4>
                        <p>The auditor checks that your QMS meets AS 9100 requirements.</p>
                    </div>
                    <div class="as9100-step">
                        <h4>Stage 2: Certification Audit</h4>
                        <p>A detailed on-site audit evaluates implementation and effectiveness.</p>
                    </div>
                    <div class="as9100-step">
                        <h4>Surveillance Audits</h4>
                        <p>Annual audits confirm continued compliance.</p>
                    </div>
                    <div class="as9100-step">
                        <h4>Recertification</h4>
                        <p>A full reassessment every three years renews certification.</p>
                    </div>
                </div>
            </div>

            <div class="as9100-section">
                <h2>How long does AS 9100 certification last?</h2>
                <p>AS 9100 certification is valid for three years, subject to successful annual surveillance audits. Failure to address major non-conformities can result in suspension or withdrawal—often with immediate contractual consequences.</p>
            </div>

            <div class="as9100-section">
                <h2>How much does AS 9100 cost in the UK?</h2>
                <p>Costs depend on:</p>
                <ul>
                    <li>Organisation size and complexity</li>
                    <li>Scope (design, manufacture, or both)</li>
                    <li>Number of sites and employees</li>
                </ul>

                <div class="as9100-highlight-box">
                    <h3>Typical costs include:</h3>
                    <ul>
                        <li>UKAS-accredited certification audit fees</li>
                        <li>Consultancy and gap analysis (if required)</li>
                        <li>Training and internal resource time</li>
                    </ul>
                    <p style="margin-top: 20px;"><strong>While more demanding than ISO 9001, AS 9100 offers exceptional return on investment through market access and reduced risk.</strong></p>
                </div>
            </div>

            <div class="as9100-section">
                <h2>AS 9100 and integration with other standards</h2>
                <p>AS 9100 follows the Annex SL High-Level Structure, allowing integration with:</p>

                <div class="as9100-cards">
                    <div class="as9100-card">
                        <h3>ISO 9001</h3>
                        <p>Quality Management foundation</p>
                    </div>
                    <div class="as9100-card">
                        <h3>ISO 14001</h3>
                        <p>Environmental Management</p>
                    </div>
                    <div class="as9100-card">
                        <h3>ISO 45001</h3>
                        <p>Health & Safety</p>
                    </div>
                    <div class="as9100-card">
                        <h3>ISO 27001</h3>
                        <p>Information Security</p>
                    </div>
                </div>

                <p style="margin-top: 30px;"><strong>Many aerospace organisations operate a fully Integrated Management System (IMS).</strong></p>
            </div>

            <div class="as9100-section">
                <h2>Who should NOT implement AS 9100?</h2>
                <p>If your organisation has no involvement in the aerospace or defence supply chain and no customer requirement, AS 9100 is unlikely to be appropriate. The standard demands sustained leadership commitment and operational discipline.</p>
            </div>

            <div class="as9100-section">
                <h2>Frequently Asked Questions (FAQs)</h2>

                <div class="as9100-faq-grid">
                    <div class="as9100-faq">
                        <h3>Is AS 9100 mandatory in the UK?</h3>
                        <p>No, but it is frequently a contractual requirement for aerospace suppliers.</p>
                    </div>

                    <div class="as9100-faq">
                        <h3>Is AS 9100 the same as EN 9100?</h3>
                        <p>Yes. They are equivalent regional versions of the same global standard.</p>
                    </div>

                    <div class="as9100-faq">
                        <h3>Can SMEs achieve AS 9100?</h3>
                        <p>Yes. Many UK aerospace SMEs are successfully certified to AS 9100.</p>
                    </div>

                    <div class="as9100-faq">
                        <h3>Is AS 9100 harder than ISO 9001?</h3>
                        <p>Yes. It includes extensive aerospace-specific and safety-critical requirements.</p>
                    </div>
                </div>
            </div>

            <div class="as9100-cta-box">
                <h2>Ready to achieve AS 9100 certification?</h2>
                <p>Get UKAS-accredited AS 9100 certification and unlock access to global aerospace and defence supply chains.</p>
                <a href="/contact/" class="as9100-cta-primary">Start Your Certification Journey</a>
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

        self.stdout.write(self.style.SUCCESS(f"✓ Updated AS 9100 page"))
        self.stdout.write(self.style.SUCCESS(f"✓ URL: /{page.slug}/"))
        self.stdout.write(self.style.SUCCESS(f"✓ Published successfully"))
