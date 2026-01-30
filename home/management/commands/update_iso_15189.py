from django.core.management.base import BaseCommand
from home.models import FlexiblePage
import uuid


class Command(BaseCommand):
    help = 'Updates ISO 15189 page content'

    def handle(self, *args, **options):
        self.stdout.write("=== Updating ISO 15189 Page ===\n")

        try:
            page = FlexiblePage.objects.get(slug='iso-15189')
            self.stdout.write(f"Found page: {page.title}")
        except FlexiblePage.DoesNotExist:
            self.stdout.write(self.style.ERROR("ISO 15189 page not found"))
            return

        content_html = """
        <style>
            main { padding-top: 0 !important; margin-top: 0 !important; }
            .iso15189-hero {
                background: linear-gradient(135deg, #00695c 0%, #00897b 50%, #26a69a 100%);
                color: white;
                padding: 100px 20px;
                margin: 0;
                text-align: center;
                position: relative;
                overflow: hidden;
            }
            .iso15189-hero::before {
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
            .iso15189-hero-content {
                position: relative;
                z-index: 1;
            }
            .iso15189-hero h1 {
                font-size: 3.5em;
                margin-bottom: 15px;
                font-weight: 800;
                letter-spacing: -1px;
            }
            .iso15189-icon {
                font-size: 5em;
                margin-bottom: 25px;
                display: inline-block;
                animation: float 3s ease-in-out infinite;
            }
            @keyframes float {
                0%, 100% { transform: translateY(0px); }
                50% { transform: translateY(-10px); }
            }
            .iso15189-subtitle {
                font-size: 1.4em;
                margin-bottom: 35px;
                opacity: 0.98;
                max-width: 750px;
                margin-left: auto;
                margin-right: auto;
                line-height: 1.6;
                font-weight: 400;
            }
            .iso15189-features {
                display: flex;
                gap: 15px;
                justify-content: center;
                flex-wrap: wrap;
                margin-top: 30px;
            }
            .iso15189-feature-badge {
                background: rgba(255,255,255,0.2);
                padding: 10px 20px;
                border-radius: 25px;
                font-weight: 600;
                backdrop-filter: blur(10px);
            }
            .iso15189-cta-buttons {
                margin-top: 40px;
                display: flex;
                gap: 20px;
                justify-content: center;
                flex-wrap: wrap;
            }
            .iso15189-cta-primary, .iso15189-cta-secondary {
                padding: 15px 35px;
                font-size: 1.1em;
                border-radius: 30px;
                text-decoration: none;
                font-weight: 600;
                transition: all 0.3s;
            }
            .iso15189-cta-primary {
                background: white;
                color: #00695c;
            }
            .iso15189-cta-primary:hover {
                transform: translateY(-2px);
                box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            }
            .iso15189-cta-secondary {
                background: transparent;
                color: white;
                border: 2px solid white;
            }
            .iso15189-cta-secondary:hover {
                background: white;
                color: #00695c;
            }
            .iso15189-content {
                max-width: 1200px;
                margin: 0 auto;
                padding: 60px 20px;
            }
            .iso15189-section {
                margin-bottom: 60px;
            }
            .iso15189-section h2 {
                color: #00695c;
                font-size: 2.2em;
                margin-bottom: 25px;
                font-weight: 700;
            }
            .iso15189-section p {
                font-size: 1.15em;
                line-height: 1.8;
                color: #333;
                margin-bottom: 20px;
            }
            .iso15189-cards {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 25px;
                margin-top: 30px;
            }
            .iso15189-card {
                background: #f5f5f5;
                padding: 30px;
                border-radius: 15px;
                border-left: 5px solid #26a69a;
            }
            .iso15189-card h3 {
                color: #00695c;
                font-size: 1.5em;
                margin-bottom: 15px;
                font-weight: 600;
            }
            .iso15189-card p, .iso15189-card ul {
                font-size: 1.05em;
                line-height: 1.7;
                color: #555;
            }
            .iso15189-card ul {
                margin-top: 15px;
                padding-left: 20px;
            }
            .iso15189-card li {
                margin-bottom: 10px;
            }
            .iso15189-highlight-box {
                background: linear-gradient(135deg, #e0f2f1 0%, #b2dfdb 100%);
                padding: 40px;
                border-radius: 15px;
                margin: 40px 0;
                border-left: 6px solid #00695c;
            }
            .iso15189-highlight-box h3 {
                color: #00695c;
                font-size: 1.8em;
                margin-bottom: 20px;
                font-weight: 600;
            }
            .iso15189-principles-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
                gap: 20px;
                margin-top: 30px;
            }
            .iso15189-principle {
                background: white;
                padding: 25px;
                border-radius: 12px;
                box-shadow: 0 3px 10px rgba(0,0,0,0.1);
            }
            .iso15189-principle h4 {
                color: #00695c;
                font-size: 1.3em;
                margin-bottom: 12px;
                font-weight: 600;
            }
            .iso15189-principle p {
                font-size: 1em;
                color: #666;
                margin: 0;
            }
            .iso15189-benefits {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
                gap: 30px;
                margin-top: 30px;
            }
            .iso15189-benefit-category {
                background: white;
                padding: 35px;
                border-radius: 15px;
                box-shadow: 0 5px 20px rgba(0,0,0,0.08);
            }
            .iso15189-benefit-category h3 {
                color: #00695c;
                font-size: 1.6em;
                margin-bottom: 20px;
                font-weight: 600;
            }
            .iso15189-benefit-category ul {
                list-style: none;
                padding: 0;
            }
            .iso15189-benefit-category li {
                padding: 12px 0;
                border-bottom: 1px solid #eee;
                font-size: 1.05em;
                color: #555;
            }
            .iso15189-benefit-category li:before {
                content: "✓ ";
                color: #26a69a;
                font-weight: bold;
                margin-right: 10px;
            }
            .iso15189-faq-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));
                gap: 25px;
                margin-top: 30px;
            }
            .iso15189-faq {
                background: white;
                padding: 35px;
                border-radius: 15px;
                border: 2px solid #e0f2f1;
                box-shadow: 0 4px 15px rgba(0, 105, 92, 0.08);
                transition: all 0.3s ease;
            }
            .iso15189-faq:hover {
                border-color: #26a69a;
                box-shadow: 0 6px 20px rgba(0, 105, 92, 0.15);
                transform: translateY(-2px);
            }
            .iso15189-faq h3 {
                color: #00695c;
                font-size: 1.35em;
                margin-bottom: 15px;
                font-weight: 700;
                display: flex;
                align-items: center;
            }
            .iso15189-faq h3:before {
                content: "Q";
                display: inline-flex;
                align-items: center;
                justify-content: center;
                width: 32px;
                height: 32px;
                background: linear-gradient(135deg, #00695c 0%, #26a69a 100%);
                color: white;
                border-radius: 50%;
                font-size: 0.8em;
                font-weight: 700;
                margin-right: 15px;
                flex-shrink: 0;
            }
            .iso15189-faq p {
                font-size: 1.1em;
                color: #555;
                margin: 0;
                line-height: 1.8;
                padding-left: 47px;
            }
            .iso15189-process-steps {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 20px;
                margin-top: 30px;
            }
            .iso15189-step {
                background: linear-gradient(135deg, #e0f2f1 0%, #b2dfdb 100%);
                padding: 30px;
                border-radius: 12px;
                text-align: center;
            }
            .iso15189-step h4 {
                color: #00695c;
                font-size: 1.4em;
                margin-bottom: 15px;
                font-weight: 600;
            }
            .iso15189-step p {
                font-size: 1.05em;
                color: #555;
                margin: 0;
            }
            .iso15189-cta-box {
                background: linear-gradient(135deg, #00695c 0%, #26a69a 100%);
                color: white;
                padding: 60px 40px;
                border-radius: 20px;
                text-align: center;
                margin-top: 60px;
            }
            .iso15189-cta-box h2 {
                color: white;
                font-size: 2.5em;
                margin-bottom: 20px;
            }
            .iso15189-cta-box p {
                font-size: 1.3em;
                margin-bottom: 30px;
                opacity: 0.95;
                color: white;
            }
            @media (max-width: 768px) {
                .iso15189-hero {
                    padding: 60px 20px;
                }
                .iso15189-hero h1 {
                    font-size: 2.2em;
                }
                .iso15189-icon {
                    font-size: 3.5em;
                }
                .iso15189-subtitle {
                    font-size: 1.15em;
                }
                .iso15189-section h2 { font-size: 1.8em; }
                .iso15189-cards, .iso15189-benefits { grid-template-columns: 1fr; }
                .iso15189-faq-grid {
                    grid-template-columns: 1fr;
                }
            }
        </style>

        <div class="iso15189-hero">
            <div class="iso15189-hero-content">
                <div class="iso15189-icon">🔬</div>
                <h1>ISO 15189 Certification</h1>
                <p class="iso15189-subtitle">Medical Laboratories – Quality & Competence</p>
                <div class="iso15189-features">
                    <span class="iso15189-feature-badge">Clinical Accuracy</span>
                    <span class="iso15189-feature-badge">Technical Competence</span>
                    <span class="iso15189-feature-badge">Patient Safety</span>
                </div>
                <div class="iso15189-cta-buttons">
                    <a href="/contact/" class="iso15189-cta-primary">Get Accredited</a>
                    <a href="#what-is" class="iso15189-cta-secondary">Learn More</a>
                </div>
            </div>
        </div>

        <div class="iso15189-content">
            <div class="iso15189-section" id="what-is">
                <h2>Introduction to ISO 15189</h2>
                <p>In healthcare, diagnostic results directly influence clinical decisions, patient outcomes, and safety. For medical laboratories, errors are not just quality issues—they are clinical risks. ISO 15189 provides the internationally recognised framework that ensures medical laboratories operate with proven technical competence, reliability, and quality management.</p>
                <p>ISO 15189 is the global standard specifically developed for medical laboratories. It combines quality management principles with detailed technical requirements, ensuring laboratory results are accurate, consistent, and clinically valid.</p>
            </div>

            <div class="iso15189-section">
                <h2>What is ISO 15189?</h2>
                <p>ISO 15189 is an international standard published by the International Organization for Standardization. It specifies requirements for quality and competence in medical laboratories, covering both management systems and technical operations.</p>

                <div class="iso15189-highlight-box">
                    <h3>In practical terms, ISO 15189 helps laboratories:</h3>
                    <ul>
                        <li>Produce accurate, reliable, and timely test results</li>
                        <li>Demonstrate technical competence of staff and methods</li>
                        <li>Control pre-examination, examination, and post-examination processes</li>
                        <li>Build confidence with clinicians, patients, and regulators</li>
                    </ul>
                    <p style="margin-top: 20px;"><strong>Unlike generic quality standards, ISO 15189 is written by and for medical laboratories, reflecting real clinical and diagnostic practice.</strong></p>
                </div>
            </div>

            <div class="iso15189-section">
                <h2>Why ISO 15189 was created</h2>
                <p>Historically, laboratories were assessed either on quality systems alone or purely technical capability—rarely both together. This led to gaps where procedures existed, but competence was unproven, or skilled staff worked without consistent quality controls.</p>
                <p><strong>ISO 15189 was created to integrate quality management with clinical competence, ensuring laboratories are not only well organised, but also technically capable of delivering trustworthy diagnostic results.</strong></p>
            </div>

            <div class="iso15189-section">
                <h2>Why ISO 15189 matters for UK organisations</h2>
                <p>In the UK, ISO 15189 is the recognised benchmark for medical laboratory competence and underpins accreditation by UKAS.</p>
                <p>ISO 15189 accreditation is essential for laboratories supporting:</p>

                <div class="iso15189-cards">
                    <div class="iso15189-card">
                        <h3>NHS diagnostic services</h3>
                        <p>Supporting patient diagnosis and treatment decisions</p>
                    </div>
                    <div class="iso15189-card">
                        <h3>Private healthcare providers</h3>
                        <p>Delivering reliable diagnostic services to private patients</p>
                    </div>
                    <div class="iso15189-card">
                        <h3>Clinical trials and research</h3>
                        <p>Providing quality-assured laboratory support for research</p>
                    </div>
                    <div class="iso15189-card">
                        <h3>Public health and screening programmes</h3>
                        <p>Supporting population health initiatives and screening</p>
                    </div>
                </div>

                <p style="margin-top: 30px;">It demonstrates compliance with regulatory expectations from bodies such as the Care Quality Commission (CQC) and provides assurance that patient results can be trusted.</p>
            </div>

            <div class="iso15189-section">
                <h2>Who ISO 15189 is for</h2>
                <p>ISO 15189 applies to all types of medical laboratories, including:</p>

                <div class="iso15189-cards">
                    <div class="iso15189-card">
                        <h3>🏥 NHS Pathology Laboratories</h3>
                        <p>Hospital and community pathology services</p>
                    </div>
                    <div class="iso15189-card">
                        <h3>🔬 Private Diagnostic Laboratories</h3>
                        <p>Independent and commercial diagnostic providers</p>
                    </div>
                    <div class="iso15189-card">
                        <h3>🧪 Specialist Clinical Testing Facilities</h3>
                        <p>Specialist reference and testing laboratories</p>
                    </div>
                    <div class="iso15189-card">
                        <h3>📊 Point-of-Care Testing (POCT) Services</h3>
                        <p>Near-patient and decentralised testing services</p>
                    </div>
                    <div class="iso15189-card">
                        <h3>🔍 Research and Clinical Trial Laboratories</h3>
                        <p>Laboratories supporting clinical research and trials</p>
                    </div>
                </div>

                <p style="margin-top: 30px;"><strong>It is applicable regardless of size, provided the laboratory performs medical testing on human samples.</strong></p>
            </div>

            <div class="iso15189-section">
                <h2>Key principles of ISO 15189</h2>
                <p>ISO 15189 is built around core clinical and quality principles:</p>

                <div class="iso15189-principles-grid">
                    <div class="iso15189-principle">
                        <h4>Patient Focus</h4>
                        <p>Ensuring results support safe and effective patient care.</p>
                    </div>
                    <div class="iso15189-principle">
                        <h4>Technical Competence</h4>
                        <p>Validated methods, calibrated equipment, and skilled personnel.</p>
                    </div>
                    <div class="iso15189-principle">
                        <h4>Quality Management</h4>
                        <p>Documented, controlled, and continually improved processes.</p>
                    </div>
                    <div class="iso15189-principle">
                        <h4>Risk Management</h4>
                        <p>Identifying and mitigating risks across the testing pathway.</p>
                    </div>
                    <div class="iso15189-principle">
                        <h4>Impartiality & Ethics</h4>
                        <p>Maintaining confidentiality and professional integrity.</p>
                    </div>
                    <div class="iso15189-principle">
                        <h4>Continual Improvement</h4>
                        <p>Learning from errors, audits, and performance data.</p>
                    </div>
                </div>
            </div>

            <div class="iso15189-section">
                <h2>Benefits of ISO 15189</h2>

                <div class="iso15189-benefits">
                    <div class="iso15189-benefit-category">
                        <h3>Internal Benefits</h3>
                        <ul>
                            <li>Improved accuracy and consistency of test results</li>
                            <li>Clear definition of roles, responsibilities, and competence</li>
                            <li>Reduced errors and repeat testing</li>
                            <li>Stronger staff confidence and professionalism</li>
                        </ul>
                    </div>

                    <div class="iso15189-benefit-category">
                        <h3>Clinical & Strategic Benefits</h3>
                        <ul>
                            <li>Increased trust from clinicians and patients</li>
                            <li>Recognition as a competent and reliable laboratory</li>
                            <li>Eligibility to support NHS and regulated diagnostic services</li>
                            <li>Improved reputation and credibility</li>
                        </ul>
                    </div>

                    <div class="iso15189-benefit-category">
                        <h3>Compliance & Risk Benefits</h3>
                        <ul>
                            <li>Alignment with UK regulatory and accreditation expectations</li>
                            <li>Reduced risk of clinical error and liability</li>
                            <li>Robust evidence during inspections and assessments</li>
                        </ul>
                    </div>
                </div>
            </div>

            <div class="iso15189-section">
                <h2>What ISO 15189 assessors look for</h2>
                <p>UKAS assessors evaluate both management systems and technical practice. Typical focus areas include:</p>

                <div class="iso15189-cards">
                    <div class="iso15189-card">
                        <h3>Staff Competence</h3>
                        <p>Qualifications, training, and ongoing assessment of personnel</p>
                    </div>
                    <div class="iso15189-card">
                        <h3>Method Validation & Verification</h3>
                        <p>Proving tests are fit for purpose and clinically appropriate</p>
                    </div>
                    <div class="iso15189-card">
                        <h3>Equipment Control</h3>
                        <p>Calibration, maintenance, and performance checks</p>
                    </div>
                    <div class="iso15189-card">
                        <h3>Sample Handling</h3>
                        <p>Traceability from receipt to disposal of samples</p>
                    </div>
                    <div class="iso15189-card">
                        <h3>Quality Control & Assurance</h3>
                        <p>Internal QC and external quality assessment (EQA) participation</p>
                    </div>
                    <div class="iso15189-card">
                        <h3>Audit & Management Review</h3>
                        <p>Evidence of monitoring, review, and improvement activities</p>
                    </div>
                </div>

                <p style="margin-top: 30px;"><strong>Assessments are detailed and evidence-based, often involving observation of live testing.</strong></p>
            </div>

            <div class="iso15189-section">
                <h2>ISO 15189 in practice (real-world examples)</h2>

                <div class="iso15189-cards">
                    <div class="iso15189-card">
                        <h3>NHS Pathology Laboratory</h3>
                        <p>An NHS laboratory maintains ISO 15189 accreditation to demonstrate competence across haematology, biochemistry, and microbiology—supporting patient diagnosis and treatment decisions.</p>
                    </div>
                    <div class="iso15189-card">
                        <h3>Private Diagnostic Provider</h3>
                        <p>A private laboratory uses ISO 15189 to expand services to regulated healthcare contracts, proving technical reliability and governance maturity.</p>
                    </div>
                </div>
            </div>

            <div class="iso15189-section">
                <h2>Common mistakes when implementing ISO 15189</h2>

                <div class="iso15189-cards">
                    <div class="iso15189-card">
                        <h3>Treating It Like ISO 9001</h3>
                        <p>ISO 15189 has extensive technical and clinical requirements beyond generic quality management.</p>
                    </div>
                    <div class="iso15189-card">
                        <h3>Weak Competence Records</h3>
                        <p>Staff competence must be demonstrable and current with documented evidence.</p>
                    </div>
                    <div class="iso15189-card">
                        <h3>Poor Method Validation</h3>
                        <p>Assumptions without evidence are a common finding during assessments.</p>
                    </div>
                </div>
            </div>

            <div class="iso15189-section">
                <h2>ISO 15189 accreditation process in the UK</h2>

                <div class="iso15189-process-steps">
                    <div class="iso15189-step">
                        <h4>Application & Preparation</h4>
                        <p>Gap analysis, documentation, and method validation.</p>
                    </div>
                    <div class="iso15189-step">
                        <h4>UKAS Assessment</h4>
                        <p>On-site assessment of management systems and technical competence.</p>
                    </div>
                    <div class="iso15189-step">
                        <h4>Corrective Actions</h4>
                        <p>Addressing any non-conformities identified during assessment.</p>
                    </div>
                    <div class="iso15189-step">
                        <h4>Accreditation Decision</h4>
                        <p>Successful laboratories are granted ISO 15189 accreditation.</p>
                    </div>
                    <div class="iso15189-step">
                        <h4>Surveillance & Reassessment</h4>
                        <p>Ongoing assessments ensure continued competence.</p>
                    </div>
                </div>
            </div>

            <div class="iso15189-section">
                <h2>How long does ISO 15189 accreditation last?</h2>
                <p>ISO 15189 accreditation is maintained through regular surveillance and reassessment cycles set by UKAS. Accreditation can be suspended or withdrawn if serious non-conformities are not addressed.</p>
            </div>

            <div class="iso15189-section">
                <h2>How much does ISO 15189 cost in the UK?</h2>
                <p>Costs depend on:</p>
                <ul>
                    <li>Scope of testing and disciplines covered</li>
                    <li>Number of staff and sites</li>
                    <li>Complexity of methods and equipment</li>
                </ul>

                <div class="iso15189-highlight-box">
                    <h3>Typical costs include:</h3>
                    <ul>
                        <li>UKAS assessment fees</li>
                        <li>Consultancy and gap analysis (if used)</li>
                        <li>Staff training and validation activities</li>
                    </ul>
                    <p style="margin-top: 20px;"><strong>While demanding, ISO 15189 accreditation is essential for laboratories delivering regulated medical diagnostics.</strong></p>
                </div>
            </div>

            <div class="iso15189-section">
                <h2>ISO 15189 and integration with other standards</h2>
                <p>ISO 15189 aligns well with:</p>

                <div class="iso15189-cards">
                    <div class="iso15189-card">
                        <h3>ISO 9001</h3>
                        <p>Quality Management foundation</p>
                    </div>
                    <div class="iso15189-card">
                        <h3>ISO 17025</h3>
                        <p>Testing & Calibration (non-clinical)</p>
                    </div>
                    <div class="iso15189-card">
                        <h3>ISO 22301</h3>
                        <p>Business Continuity</p>
                    </div>
                    <div class="iso15189-card">
                        <h3>ISO 27001</h3>
                        <p>Information Security (LIMS and patient data)</p>
                    </div>
                </div>

                <p style="margin-top: 30px;"><strong>Many laboratories operate integrated governance systems across quality, information security, and resilience.</strong></p>
            </div>

            <div class="iso15189-section">
                <h2>Who should NOT use ISO 15189?</h2>
                <p>ISO 15189 is not suitable for non-medical testing laboratories. Organisations performing industrial, environmental, or product testing should consider ISO 17025 instead.</p>
            </div>

            <div class="iso15189-section">
                <h2>Frequently Asked Questions (FAQs)</h2>

                <div class="iso15189-faq-grid">
                    <div class="iso15189-faq">
                        <h3>Is ISO 15189 mandatory in the UK?</h3>
                        <p>It is not law, but it is required for UKAS-accredited medical laboratories.</p>
                    </div>

                    <div class="iso15189-faq">
                        <h3>Is ISO 15189 the same as ISO 17025?</h3>
                        <p>No. ISO 15189 is specific to medical laboratories and patient testing.</p>
                    </div>

                    <div class="iso15189-faq">
                        <h3>Can small laboratories achieve ISO 15189?</h3>
                        <p>Yes. The standard is scalable, but technical competence must always be demonstrated.</p>
                    </div>

                    <div class="iso15189-faq">
                        <h3>Does ISO 15189 cover POCT?</h3>
                        <p>Yes. Point-of-care testing falls within scope when managed by a laboratory service.</p>
                    </div>
                </div>
            </div>

            <div class="iso15189-cta-box">
                <h2>Ready to achieve ISO 15189 accreditation?</h2>
                <p>Get UKAS-accredited ISO 15189 certification and demonstrate medical laboratory competence.</p>
                <a href="/contact/" class="iso15189-cta-primary">Start Your Accreditation Journey</a>
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

        self.stdout.write(self.style.SUCCESS(f"✓ Updated ISO 15189 page"))
        self.stdout.write(self.style.SUCCESS(f"✓ URL: /{page.slug}/"))
        self.stdout.write(self.style.SUCCESS(f"✓ Published successfully"))
