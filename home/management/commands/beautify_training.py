"""
Django management command to beautify the Training page
Transforms the plain list-based design into an attractive modern layout
"""

from django.core.management.base import BaseCommand
from home.models import FlexiblePage


class Command(BaseCommand):
    help = 'Beautify the Training page with modern design'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('\n=== Beautifying Training Page ===\n'))

        try:
            # Get the Training page
            training_page = FlexiblePage.objects.get(slug='training')

            # Create beautiful new content structure
            new_body = []

            # 1. Hero Section with Gradient
            new_body.append({
                'type': 'html',
                'value': {
                    'html': '''
<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%); padding: 80px 20px; text-align: center; color: white; position: relative; overflow: hidden; margin: 0 -20px 60px -20px; border-radius: 0 0 30px 30px; box-shadow: 0 10px 40px rgba(0,0,0,0.15);">
    <div style="position: absolute; top: 10%; left: 5%; width: 100px; height: 100px; background: rgba(255,255,255,0.1); border-radius: 50%; animation: float 6s ease-in-out infinite;"></div>
    <div style="position: absolute; bottom: 15%; right: 8%; width: 80px; height: 80px; background: rgba(255,255,255,0.1); border-radius: 50%; animation: float 5s ease-in-out infinite 1s;"></div>

    <div style="max-width: 900px; margin: 0 auto; position: relative; z-index: 1;">
        <div style="display: inline-block; background: rgba(255,255,255,0.2); padding: 10px 20px; border-radius: 50px; font-size: 0.9em; margin-bottom: 20px; backdrop-filter: blur(10px);">
            <i class="fas fa-graduation-cap" style="margin-right: 8px;"></i> Professional ISO Training
        </div>

        <h1 style="font-size: 3em; margin: 20px 0; font-weight: 800; line-height: 1.2; text-shadow: 0 2px 20px rgba(0,0,0,0.2);">
            ISO Training Courses
        </h1>

        <p style="font-size: 1.3em; margin: 25px 0 35px; opacity: 0.95; max-width: 700px; margin-left: auto; margin-right: auto; line-height: 1.6;">
            Expert-led training courses delivered by specialists in each field. Available at your organisation, training locations, or suitable venues nationwide.
        </p>

        <div style="display: flex; gap: 15px; justify-content: center; flex-wrap: wrap; margin-top: 30px;">
            <a href="#courses" style="background: white; color: #667eea; padding: 15px 35px; border-radius: 50px; text-decoration: none; font-weight: 700; box-shadow: 0 8px 25px rgba(0,0,0,0.2); transition: transform 0.3s; display: inline-flex; align-items: center; gap: 10px;">
                <i class="fas fa-book-open"></i> View Courses
            </a>
            <a href="#contact" style="background: rgba(255,255,255,0.2); color: white; padding: 15px 35px; border-radius: 50px; text-decoration: none; font-weight: 700; backdrop-filter: blur(10px); border: 2px solid white; transition: all 0.3s; display: inline-flex; align-items: center; gap: 10px;">
                <i class="fas fa-phone"></i> Contact Us
            </a>
        </div>
    </div>
</div>

<style>
@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-20px); }
}
</style>
'''
                }

            })

            # 2. Training Features Section
            new_body.append({
                'type': 'html',
                'value': {'html': '''
<div style="max-width: 1200px; margin: 60px auto; padding: 0 20px;">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 30px; margin-bottom: 80px;">
        <div style="text-align: center; padding: 40px 30px; background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); border-radius: 20px; color: white; box-shadow: 0 10px 30px rgba(240,147,251,0.3); transition: transform 0.3s;" onmouseover="this.style.transform='translateY(-10px)'" onmouseout="this.style.transform='translateY(0)'">
            <div style="font-size: 3em; margin-bottom: 15px;">
                <i class="fas fa-user-graduate"></i>
            </div>
            <h3 style="margin: 0 0 10px 0; font-size: 1.3em;">Expert Instructors</h3>
            <p style="margin: 0; opacity: 0.95; font-size: 0.95em;">Taught by industry specialists with real-world experience</p>
        </div>

        <div style="text-align: center; padding: 40px 30px; background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); border-radius: 20px; color: white; box-shadow: 0 10px 30px rgba(79,172,254,0.3); transition: transform 0.3s;" onmouseover="this.style.transform='translateY(-10px)'" onmouseout="this.style.transform='translateY(0)'">
            <div style="font-size: 3em; margin-bottom: 15px;">
                <i class="fas fa-map-marker-alt"></i>
            </div>
            <h3 style="margin: 0 0 10px 0; font-size: 1.3em;">Flexible Locations</h3>
            <p style="margin: 0; opacity: 0.95; font-size: 0.95em;">On-site, training centers, or venues across the UK</p>
        </div>

        <div style="text-align: center; padding: 40px 30px; background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%); border-radius: 20px; color: white; box-shadow: 0 10px 30px rgba(67,233,123,0.3); transition: transform 0.3s;" onmouseover="this.style.transform='translateY(-10px)'" onmouseout="this.style.transform='translateY(0)'">
            <div style="font-size: 3em; margin-bottom: 15px;">
                <i class="fas fa-certificate"></i>
            </div>
            <h3 style="margin: 0 0 10px 0; font-size: 1.3em;">Certified Courses</h3>
            <p style="margin: 0; opacity: 0.95; font-size: 0.95em;">IRCA approved and industry recognized qualifications</p>
        </div>

        <div style="text-align: center; padding: 40px 30px; background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); border-radius: 20px; color: white; box-shadow: 0 10px 30px rgba(250,112,154,0.3); transition: transform 0.3s;" onmouseover="this.style.transform='translateY(-10px)'" onmouseout="this.style.transform='translateY(0)'">
            <div style="font-size: 3em; margin-bottom: 15px;">
                <i class="fas fa-users"></i>
            </div>
            <h3 style="margin: 0 0 10px 0; font-size: 1.3em;">Group Training</h3>
            <p style="margin: 0; opacity: 0.95; font-size: 0.95em;">Customized training for teams of any size</p>
        </div>
    </div>
</div>
'''
                }

            })

            # 3. Courses Section Header
            new_body.append({
                'type': 'html',
                'value': {'html': '''
<div id="courses" style="max-width: 1200px; margin: 80px auto 60px; padding: 0 20px; text-align: center;">
    <h2 style="font-size: 2.5em; color: #1e3a5f; margin-bottom: 15px; font-weight: 800;">
        Available Training Courses
    </h2>
    <p style="font-size: 1.2em; color: #666; max-width: 700px; margin: 0 auto 50px; line-height: 1.6;">
        Choose from our comprehensive range of ISO training courses, designed to meet your organization's needs
    </p>
</div>
'''
                }

            })

            # 4. ISO 9001 Quality Management
            new_body.append({
                'type': 'html',
                'value': {'html': '''
<div style="max-width: 1200px; margin: 0 auto 50px; padding: 0 20px;">
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 40px; border-radius: 25px; color: white; box-shadow: 0 15px 50px rgba(102,126,234,0.3); margin-bottom: 30px;">
        <div style="display: flex; align-items: center; gap: 20px; margin-bottom: 25px;">
            <div style="background: rgba(255,255,255,0.2); padding: 20px; border-radius: 15px; backdrop-filter: blur(10px);">
                <i class="fas fa-award" style="font-size: 2.5em;"></i>
            </div>
            <div>
                <h3 style="font-size: 2em; margin: 0; font-weight: 700;">ISO 9001 Quality Management</h3>
                <p style="margin: 5px 0 0; opacity: 0.9; font-size: 1.1em;">Quality Management System Training</p>
            </div>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px;">
            <div style="background: rgba(255,255,255,0.15); padding: 25px; border-radius: 15px; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2); transition: all 0.3s;" onmouseover="this.style.background='rgba(255,255,255,0.25)'" onmouseout="this.style.background='rgba(255,255,255,0.15)'">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 15px;">
                    <div style="background: rgba(255,255,255,0.3); width: 50px; height: 50px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 1.2em;">
                        1
                    </div>
                    <div>
                        <div style="font-weight: 700; font-size: 1.1em;">Foundation Course</div>
                        <div style="opacity: 0.9; font-size: 0.9em;">ISO 9001:2015</div>
                    </div>
                </div>
                <div style="display: flex; align-items: center; gap: 8px; opacity: 0.95;">
                    <i class="fas fa-clock"></i>
                    <span>1 Day Duration</span>
                </div>
            </div>

            <div style="background: rgba(255,255,255,0.15); padding: 25px; border-radius: 15px; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2); transition: all 0.3s;" onmouseover="this.style.background='rgba(255,255,255,0.25)'" onmouseout="this.style.background='rgba(255,255,255,0.15)'">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 15px;">
                    <div style="background: rgba(255,255,255,0.3); width: 50px; height: 50px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 1.2em;">
                        2
                    </div>
                    <div>
                        <div style="font-weight: 700; font-size: 1.1em;">Internal Auditing</div>
                        <div style="opacity: 0.9; font-size: 0.9em;">ISO 9001:2015</div>
                    </div>
                </div>
                <div style="display: flex; align-items: center; gap: 8px; opacity: 0.95;">
                    <i class="fas fa-clock"></i>
                    <span>2 Day Duration</span>
                </div>
            </div>

            <div style="background: rgba(255,255,255,0.15); padding: 25px; border-radius: 15px; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2); transition: all 0.3s;" onmouseover="this.style.background='rgba(255,255,255,0.25)'" onmouseout="this.style.background='rgba(255,255,255,0.15)'">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 15px;">
                    <div style="background: rgba(255,255,255,0.3); width: 50px; height: 50px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 1.2em;">
                        5
                    </div>
                    <div>
                        <div style="font-weight: 700; font-size: 1.1em;">IRCA Lead Auditor</div>
                        <div style="opacity: 0.9; font-size: 0.9em;">ISO 9001:2015</div>
                    </div>
                </div>
                <div style="display: flex; align-items: center; gap: 8px; opacity: 0.95;">
                    <i class="fas fa-clock"></i>
                    <span>5 Day Duration</span>
                </div>
            </div>
        </div>
    </div>
</div>
'''
                }

            })

            # 5. ISO 14001 Environment
            new_body.append({
                'type': 'html',
                'value': {'html': '''
<div style="max-width: 1200px; margin: 0 auto 50px; padding: 0 20px;">
    <div style="background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); padding: 40px; border-radius: 25px; color: white; box-shadow: 0 15px 50px rgba(17,153,142,0.3); margin-bottom: 30px;">
        <div style="display: flex; align-items: center; gap: 20px; margin-bottom: 25px;">
            <div style="background: rgba(255,255,255,0.2); padding: 20px; border-radius: 15px; backdrop-filter: blur(10px);">
                <i class="fas fa-leaf" style="font-size: 2.5em;"></i>
            </div>
            <div>
                <h3 style="font-size: 2em; margin: 0; font-weight: 700;">ISO 14001 Environment</h3>
                <p style="margin: 5px 0 0; opacity: 0.9; font-size: 1.1em;">Environmental Management System Training</p>
            </div>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px;">
            <div style="background: rgba(255,255,255,0.15); padding: 25px; border-radius: 15px; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2); transition: all 0.3s;" onmouseover="this.style.background='rgba(255,255,255,0.25)'" onmouseout="this.style.background='rgba(255,255,255,0.15)'">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 15px;">
                    <div style="background: rgba(255,255,255,0.3); width: 50px; height: 50px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 1.2em;">
                        1
                    </div>
                    <div>
                        <div style="font-weight: 700; font-size: 1.1em;">Foundation Course</div>
                        <div style="opacity: 0.9; font-size: 0.9em;">ISO 14001:2015</div>
                    </div>
                </div>
                <div style="display: flex; align-items: center; gap: 8px; opacity: 0.95;">
                    <i class="fas fa-clock"></i>
                    <span>1 Day Duration</span>
                </div>
            </div>

            <div style="background: rgba(255,255,255,0.15); padding: 25px; border-radius: 15px; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2); transition: all 0.3s;" onmouseover="this.style.background='rgba(255,255,255,0.25)'" onmouseout="this.style.background='rgba(255,255,255,0.15)'">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 15px;">
                    <div style="background: rgba(255,255,255,0.3); width: 50px; height: 50px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 1.2em;">
                        2
                    </div>
                    <div>
                        <div style="font-weight: 700; font-size: 1.1em;">Internal Auditing</div>
                        <div style="opacity: 0.9; font-size: 0.9em;">ISO 14001:2015</div>
                    </div>
                </div>
                <div style="display: flex; align-items: center; gap: 8px; opacity: 0.95;">
                    <i class="fas fa-clock"></i>
                    <span>2 Day Duration</span>
                </div>
            </div>
        </div>
    </div>
</div>
'''
                }

            })

            # 6. ISO 45001 Health & Safety
            new_body.append({
                'type': 'html',
                'value': {'html': '''
<div style="max-width: 1200px; margin: 0 auto 50px; padding: 0 20px;">
    <div style="background: linear-gradient(135deg, #ee0979 0%, #ff6a00 100%); padding: 40px; border-radius: 25px; color: white; box-shadow: 0 15px 50px rgba(238,9,121,0.3); margin-bottom: 30px;">
        <div style="display: flex; align-items: center; gap: 20px; margin-bottom: 25px;">
            <div style="background: rgba(255,255,255,0.2); padding: 20px; border-radius: 15px; backdrop-filter: blur(10px);">
                <i class="fas fa-shield-alt" style="font-size: 2.5em;"></i>
            </div>
            <div>
                <h3 style="font-size: 2em; margin: 0; font-weight: 700;">ISO 45001 Health & Safety</h3>
                <p style="margin: 5px 0 0; opacity: 0.9; font-size: 1.1em;">Occupational Health & Safety Management Training</p>
            </div>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px;">
            <div style="background: rgba(255,255,255,0.15); padding: 25px; border-radius: 15px; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2); transition: all 0.3s;" onmouseover="this.style.background='rgba(255,255,255,0.25)'" onmouseout="this.style.background='rgba(255,255,255,0.15)'">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 15px;">
                    <div style="background: rgba(255,255,255,0.3); width: 50px; height: 50px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 1.2em;">
                        1
                    </div>
                    <div>
                        <div style="font-weight: 700; font-size: 1.1em;">Foundation Course</div>
                        <div style="opacity: 0.9; font-size: 0.9em;">ISO 45001</div>
                    </div>
                </div>
                <div style="display: flex; align-items: center; gap: 8px; opacity: 0.95;">
                    <i class="fas fa-clock"></i>
                    <span>1 Day Duration</span>
                </div>
            </div>

            <div style="background: rgba(255,255,255,0.15); padding: 25px; border-radius: 15px; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2); transition: all 0.3s;" onmouseover="this.style.background='rgba(255,255,255,0.25)'" onmouseout="this.style.background='rgba(255,255,255,0.15)'">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 15px;">
                    <div style="background: rgba(255,255,255,0.3); width: 50px; height: 50px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 1.2em;">
                        2
                    </div>
                    <div>
                        <div style="font-weight: 700; font-size: 1.1em;">Internal Auditor</div>
                        <div style="opacity: 0.9; font-size: 0.9em;">ISO 45001</div>
                    </div>
                </div>
                <div style="display: flex; align-items: center; gap: 8px; opacity: 0.95;">
                    <i class="fas fa-clock"></i>
                    <span>2 Day Duration</span>
                </div>
            </div>

            <div style="background: rgba(255,255,255,0.15); padding: 25px; border-radius: 15px; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2); transition: all 0.3s;" onmouseover="this.style.background='rgba(255,255,255,0.25)'" onmouseout="this.style.background='rgba(255,255,255,0.15)'">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 15px;">
                    <div style="background: rgba(255,255,255,0.3); width: 50px; height: 50px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 1.2em;">
                        2
                    </div>
                    <div>
                        <div style="font-weight: 700; font-size: 1.1em;">Auditor Transition</div>
                        <div style="opacity: 0.9; font-size: 0.9em;">ISO 45001</div>
                    </div>
                </div>
                <div style="display: flex; align-items: center; gap: 8px; opacity: 0.95;">
                    <i class="fas fa-clock"></i>
                    <span>2 Day Duration</span>
                </div>
            </div>

            <div style="background: rgba(255,255,255,0.15); padding: 25px; border-radius: 15px; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2); transition: all 0.3s;" onmouseover="this.style.background='rgba(255,255,255,0.25)'" onmouseout="this.style.background='rgba(255,255,255,0.15)'">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 15px;">
                    <div style="background: rgba(255,255,255,0.3); width: 50px; height: 50px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 1.2em;">
                        3
                    </div>
                    <div>
                        <div style="font-weight: 700; font-size: 1.1em;">Auditor Conversion</div>
                        <div style="opacity: 0.9; font-size: 0.9em;">ISO 45001</div>
                    </div>
                </div>
                <div style="display: flex; align-items: center; gap: 8px; opacity: 0.95;">
                    <i class="fas fa-clock"></i>
                    <span>3 Day Duration</span>
                </div>
            </div>

            <div style="background: rgba(255,255,255,0.15); padding: 25px; border-radius: 15px; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2); transition: all 0.3s;" onmouseover="this.style.background='rgba(255,255,255,0.25)'" onmouseout="this.style.background='rgba(255,255,255,0.15)'">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 15px;">
                    <div style="background: rgba(255,255,255,0.3); width: 50px; height: 50px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 1.2em;">
                        5
                    </div>
                    <div>
                        <div style="font-weight: 700; font-size: 1.1em;">Lead Auditor</div>
                        <div style="opacity: 0.9; font-size: 0.9em;">ISO 45001</div>
                    </div>
                </div>
                <div style="display: flex; align-items: center; gap: 8px; opacity: 0.95;">
                    <i class="fas fa-clock"></i>
                    <span>5 Day Duration</span>
                </div>
            </div>
        </div>
    </div>
</div>
'''
                }

            })

            # 7. ISO 27001 Information Security
            new_body.append({
                'type': 'html',
                'value': {'html': '''
<div style="max-width: 1200px; margin: 0 auto 50px; padding: 0 20px;">
    <div style="background: linear-gradient(135deg, #3a1c71 0%, #d76d77 50%, #ffaf7b 100%); padding: 40px; border-radius: 25px; color: white; box-shadow: 0 15px 50px rgba(58,28,113,0.3); margin-bottom: 30px;">
        <div style="display: flex; align-items: center; gap: 20px; margin-bottom: 25px;">
            <div style="background: rgba(255,255,255,0.2); padding: 20px; border-radius: 15px; backdrop-filter: blur(10px);">
                <i class="fas fa-lock" style="font-size: 2.5em;"></i>
            </div>
            <div>
                <h3 style="font-size: 2em; margin: 0; font-weight: 700;">ISO 27001 Information Security</h3>
                <p style="margin: 5px 0 0; opacity: 0.9; font-size: 1.1em;">Information Security Management System Training</p>
            </div>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px;">
            <div style="background: rgba(255,255,255,0.15); padding: 25px; border-radius: 15px; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2); transition: all 0.3s;" onmouseover="this.style.background='rgba(255,255,255,0.25)'" onmouseout="this.style.background='rgba(255,255,255,0.15)'">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 15px;">
                    <div style="background: rgba(255,255,255,0.3); width: 50px; height: 50px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 1.2em;">
                        1
                    </div>
                    <div>
                        <div style="font-weight: 700; font-size: 1.1em;">Foundation Course</div>
                        <div style="opacity: 0.9; font-size: 0.9em;">ISO 27001:2013</div>
                    </div>
                </div>
                <div style="display: flex; align-items: center; gap: 8px; opacity: 0.95;">
                    <i class="fas fa-clock"></i>
                    <span>1 Day Duration</span>
                </div>
            </div>

            <div style="background: rgba(255,255,255,0.15); padding: 25px; border-radius: 15px; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2); transition: all 0.3s;" onmouseover="this.style.background='rgba(255,255,255,0.25)'" onmouseout="this.style.background='rgba(255,255,255,0.15)'">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 15px;">
                    <div style="background: rgba(255,255,255,0.3); width: 50px; height: 50px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 1.2em;">
                        2
                    </div>
                    <div>
                        <div style="font-weight: 700; font-size: 1.1em;">Internal Auditing</div>
                        <div style="opacity: 0.9; font-size: 0.9em;">ISO 27001:2013</div>
                    </div>
                </div>
                <div style="display: flex; align-items: center; gap: 8px; opacity: 0.95;">
                    <i class="fas fa-clock"></i>
                    <span>2 Day Duration</span>
                </div>
            </div>
        </div>
    </div>
</div>
'''
                }

            })

            # Add remaining ISO standards with compact view
            new_body.append({
                'type': 'html',
                'value': {'html': '''
<div style="max-width: 1200px; margin: 60px auto; padding: 0 20px;">
    <h2 style="font-size: 2.2em; color: #1e3a5f; margin-bottom: 30px; text-align: center; font-weight: 800;">
        Additional ISO Training Courses
    </h2>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 30px;">

        <!-- ISO 13485 -->
        <div style="background: white; padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.08); border-left: 5px solid #e74c3c; transition: transform 0.3s, box-shadow 0.3s;" onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 15px 40px rgba(0,0,0,0.12)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 10px 30px rgba(0,0,0,0.08)'">
            <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                <div style="background: linear-gradient(135deg, #e74c3c, #c0392b); width: 60px; height: 60px; border-radius: 15px; display: flex; align-items: center; justify-content: center; color: white; font-size: 1.8em;">
                    <i class="fas fa-heartbeat"></i>
                </div>
                <div>
                    <h3 style="margin: 0; font-size: 1.4em; color: #1e3a5f;">ISO 13485</h3>
                    <p style="margin: 5px 0 0; color: #666; font-size: 0.95em;">Medical Devices</p>
                </div>
            </div>
            <ul style="margin: 0; padding-left: 20px; color: #555; line-height: 2;">
                <li>1 day ISO 13485:2016 Foundation Course</li>
                <li>2 day ISO 13485:2016 Internal Auditing Course</li>
            </ul>
        </div>

        <!-- ISO 22000 -->
        <div style="background: white; padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.08); border-left: 5px solid #16a085; transition: transform 0.3s, box-shadow 0.3s;" onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 15px 40px rgba(0,0,0,0.12)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 10px 30px rgba(0,0,0,0.08)'">
            <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                <div style="background: linear-gradient(135deg, #16a085, #1abc9c); width: 60px; height: 60px; border-radius: 15px; display: flex; align-items: center; justify-content: center; color: white; font-size: 1.8em;">
                    <i class="fas fa-utensils"></i>
                </div>
                <div>
                    <h3 style="margin: 0; font-size: 1.4em; color: #1e3a5f;">ISO 22000</h3>
                    <p style="margin: 5px 0 0; color: #666; font-size: 0.95em;">Food Safety</p>
                </div>
            </div>
            <ul style="margin: 0; padding-left: 20px; color: #555; line-height: 2;">
                <li>1 day ISO 22000:2018 Foundation Course</li>
                <li>2 day ISO 22000:2018 Internal Auditing Course</li>
            </ul>
        </div>

        <!-- IATF 16949 -->
        <div style="background: white; padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.08); border-left: 5px solid #2980b9; transition: transform 0.3s, box-shadow 0.3s;" onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 15px 40px rgba(0,0,0,0.12)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 10px 30px rgba(0,0,0,0.08)'">
            <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                <div style="background: linear-gradient(135deg, #2980b9, #3498db); width: 60px; height: 60px; border-radius: 15px; display: flex; align-items: center; justify-content: center; color: white; font-size: 1.8em;">
                    <i class="fas fa-car"></i>
                </div>
                <div>
                    <h3 style="margin: 0; font-size: 1.4em; color: #1e3a5f;">IATF 16949</h3>
                    <p style="margin: 5px 0 0; color: #666; font-size: 0.95em;">Automotive Quality</p>
                </div>
            </div>
            <ul style="margin: 0; padding-left: 20px; color: #555; line-height: 2;">
                <li>1 day IATF 16949:2016 Foundation Course</li>
                <li>2 day IATF 16949:2016 Internal Auditing Course</li>
            </ul>
        </div>

        <!-- ISO 50001 -->
        <div style="background: white; padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.08); border-left: 5px solid #f39c12; transition: transform 0.3s, box-shadow 0.3s;" onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 15px 40px rgba(0,0,0,0.12)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 10px 30px rgba(0,0,0,0.08)'">
            <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                <div style="background: linear-gradient(135deg, #f39c12, #f1c40f); width: 60px; height: 60px; border-radius: 15px; display: flex; align-items: center; justify-content: center; color: white; font-size: 1.8em;">
                    <i class="fas fa-bolt"></i>
                </div>
                <div>
                    <h3 style="margin: 0; font-size: 1.4em; color: #1e3a5f;">ISO 50001</h3>
                    <p style="margin: 5px 0 0; color: #666; font-size: 0.95em;">Energy Management</p>
                </div>
            </div>
            <ul style="margin: 0; padding-left: 20px; color: #555; line-height: 2;">
                <li>1 day ISO 50001:2018 Foundation Course</li>
                <li>2 day ISO 50001:2018 Internal Auditing Course</li>
            </ul>
        </div>

        <!-- ISO 22301 -->
        <div style="background: white; padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.08); border-left: 5px solid #8e44ad; transition: transform 0.3s, box-shadow 0.3s;" onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 15px 40px rgba(0,0,0,0.12)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 10px 30px rgba(0,0,0,0.08)'">
            <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                <div style="background: linear-gradient(135deg, #8e44ad, #9b59b6); width: 60px; height: 60px; border-radius: 15px; display: flex; align-items: center; justify-content: center; color: white; font-size: 1.8em;">
                    <i class="fas fa-briefcase"></i>
                </div>
                <div>
                    <h3 style="margin: 0; font-size: 1.4em; color: #1e3a5f;">ISO 22301</h3>
                    <p style="margin: 5px 0 0; color: #666; font-size: 0.95em;">Business Continuity</p>
                </div>
            </div>
            <ul style="margin: 0; padding-left: 20px; color: #555; line-height: 2;">
                <li>1 day ISO 22301:2019 Foundation Course</li>
                <li>2 day ISO 22301:2019 Internal Auditing Course</li>
            </ul>
        </div>

        <!-- ISO 20000 -->
        <div style="background: white; padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.08); border-left: 5px solid #34495e; transition: transform 0.3s, box-shadow 0.3s;" onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 15px 40px rgba(0,0,0,0.12)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 10px 30px rgba(0,0,0,0.08)'">
            <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                <div style="background: linear-gradient(135deg, #34495e, #2c3e50); width: 60px; height: 60px; border-radius: 15px; display: flex; align-items: center; justify-content: center; color: white; font-size: 1.8em;">
                    <i class="fas fa-server"></i>
                </div>
                <div>
                    <h3 style="margin: 0; font-size: 1.4em; color: #1e3a5f;">ISO 20000</h3>
                    <p style="margin: 5px 0 0; color: #666; font-size: 0.95em;">IT Service Management</p>
                </div>
            </div>
            <ul style="margin: 0; padding-left: 20px; color: #555; line-height: 2;">
                <li>1 day ISO 20000-1:2018 Foundation Course</li>
                <li>2 day ISO 20000-1:2018 Internal Auditing Course</li>
            </ul>
        </div>
    </div>
</div>
'''
                }

            })

            # CTA Section
            new_body.append({
                'type': 'html',
                'value': {'html': '''
<div id="contact" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 80px 20px; margin: 80px -20px -40px -20px; border-radius: 30px 30px 0 0; color: white; text-align: center; position: relative; overflow: hidden;">
    <div style="position: absolute; top: -50px; right: -50px; width: 200px; height: 200px; background: rgba(255,255,255,0.1); border-radius: 50%; animation: float 8s ease-in-out infinite;"></div>
    <div style="position: absolute; bottom: -30px; left: -30px; width: 150px; height: 150px; background: rgba(255,255,255,0.1); border-radius: 50%; animation: float 6s ease-in-out infinite 2s;"></div>

    <div style="max-width: 800px; margin: 0 auto; position: relative; z-index: 1;">
        <h2 style="font-size: 2.8em; margin: 0 0 20px; font-weight: 800;">
            Ready to Book Your Training?
        </h2>
        <p style="font-size: 1.3em; margin: 0 0 35px; opacity: 0.95; line-height: 1.6;">
            Contact our team to discuss your training requirements and get a customized quote
        </p>

        <div style="display: flex; gap: 20px; justify-content: center; flex-wrap: wrap; margin-bottom: 40px;">
            <a href="/contact/" style="background: white; color: #667eea; padding: 18px 40px; border-radius: 50px; text-decoration: none; font-weight: 700; font-size: 1.1em; box-shadow: 0 8px 25px rgba(0,0,0,0.2); transition: all 0.3s; display: inline-flex; align-items: center; gap: 10px;">
                <i class="fas fa-envelope"></i> Get in Touch
            </a>
            <a href="tel:03456006975" style="background: rgba(255,255,255,0.2); color: white; padding: 18px 40px; border-radius: 50px; text-decoration: none; font-weight: 700; font-size: 1.1em; backdrop-filter: blur(10px); border: 2px solid white; transition: all 0.3s; display: inline-flex; align-items: center; gap: 10px;">
                <i class="fas fa-phone"></i> 0345 600 6975
            </a>
        </div>

        <div style="background: rgba(255,255,255,0.15); padding: 30px; border-radius: 20px; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2);">
            <h3 style="margin: 0 0 15px; font-size: 1.5em;">Why Choose Qualitation Training?</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin-top: 20px; text-align: left;">
                <div>
                    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
                        <i class="fas fa-check-circle" style="color: #43e97b; font-size: 1.3em;"></i>
                        <strong>Expert Trainers</strong>
                    </div>
                    <p style="margin: 0; opacity: 0.9; font-size: 0.95em; padding-left: 32px;">Industry specialists with real-world experience</p>
                </div>
                <div>
                    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
                        <i class="fas fa-check-circle" style="color: #43e97b; font-size: 1.3em;"></i>
                        <strong>IRCA Approved</strong>
                    </div>
                    <p style="margin: 0; opacity: 0.9; font-size: 0.95em; padding-left: 32px;">Internationally recognized qualifications</p>
                </div>
                <div>
                    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
                        <i class="fas fa-check-circle" style="color: #43e97b; font-size: 1.3em;"></i>
                        <strong>Flexible Delivery</strong>
                    </div>
                    <p style="margin: 0; opacity: 0.9; font-size: 0.95em; padding-left: 32px;">On-site, training centers, or virtual options</p>
                </div>
            </div>
        </div>
    </div>
</div>
'''
                }

            })

            # Save the new content
            # StreamField should be set directly with the list, not JSON stringified
            training_page.body = new_body
            training_page.save_revision().publish()

            self.stdout.write(self.style.SUCCESS('✓ Training page beautified successfully!'))
            self.stdout.write(self.style.SUCCESS(f'✓ Created {len(new_body)} content blocks'))
            self.stdout.write(self.style.SUCCESS('✓ Added modern hero section'))
            self.stdout.write(self.style.SUCCESS('✓ Created course cards with gradients'))
            self.stdout.write(self.style.SUCCESS('✓ Added CTA section'))
            self.stdout.write(self.style.SUCCESS('\nView at: http://localhost:8000/training/'))

        except FlexiblePage.DoesNotExist:
            self.stdout.write(self.style.ERROR('✗ Training page not found'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ Error: {e}'))
            import traceback
            traceback.print_exc()

        self.stdout.write(self.style.SUCCESS('\n=== Complete ===\n'))
