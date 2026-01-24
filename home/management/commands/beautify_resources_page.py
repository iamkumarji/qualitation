"""
Django management command to beautify the Resources page with modern design
"""

from django.core.management.base import BaseCommand
from django.db import connection
import json
import uuid


class Command(BaseCommand):
    help = 'Redesign Resources page with beautiful modern layout'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('\n=== Beautifying Resources Page ===\n'))

        # Create beautiful new design
        new_body = []

        # Hero Section - Beautiful gradient hero
        hero_html = '''
<style>
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes float {
    0%, 100% {
        transform: translateY(0px);
    }
    50% {
        transform: translateY(-20px);
    }
}

.resource-hero {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
    padding: 120px 20px 100px;
    position: relative;
    overflow: hidden;
}

.resource-hero::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: url('data:image/svg+xml,<svg width="100" height="100" xmlns="http://www.w3.org/2000/svg"><defs><pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><circle cx="20" cy="20" r="1.5" fill="rgba(255,255,255,0.1)"/></pattern></defs><rect width="100" height="100" fill="url(%23grid)"/></svg>');
    opacity: 0.4;
}

.floating-shape {
    position: absolute;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.1);
    animation: float 6s ease-in-out infinite;
}

.shape-1 { width: 100px; height: 100px; top: 10%; left: 10%; animation-delay: 0s; }
.shape-2 { width: 150px; height: 150px; top: 60%; left: 80%; animation-delay: 2s; }
.shape-3 { width: 80px; height: 80px; top: 30%; left: 85%; animation-delay: 4s; }

.hero-content {
    position: relative;
    z-index: 1;
    max-width: 900px;
    margin: 0 auto;
    text-align: center;
    animation: fadeInUp 0.8s ease-out;
}

.article-card {
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    height: 100%;
}

.article-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 20px 40px rgba(102, 126, 234, 0.25) !important;
}

.article-card:hover .article-icon {
    transform: scale(1.1) rotate(5deg);
}

.article-icon {
    transition: transform 0.3s ease;
}

.cta-gradient {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    position: relative;
    overflow: hidden;
}

.cta-gradient::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
    animation: float 8s ease-in-out infinite;
}

.cta-button {
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.cta-button::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 0;
    height: 0;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.2);
    transform: translate(-50%, -50%);
    transition: width 0.6s, height 0.6s;
}

.cta-button:hover::before {
    width: 300px;
    height: 300px;
}

.cta-button:hover {
    transform: scale(1.05);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
}
</style>

<section class="resource-hero">
    <div class="floating-shape shape-1"></div>
    <div class="floating-shape shape-2"></div>
    <div class="floating-shape shape-3"></div>

    <div class="hero-content">
        <div style="display: inline-block; background: rgba(255,255,255,0.2); padding: 8px 20px; border-radius: 30px; margin-bottom: 20px; backdrop-filter: blur(10px);">
            <span style="color: white; font-size: 0.9em; font-weight: 600; letter-spacing: 1px;">KNOWLEDGE HUB</span>
        </div>
        <h1 style="color: white; font-size: 3.5em; font-weight: 800; margin-bottom: 25px; line-height: 1.2; text-shadow: 0 4px 20px rgba(0,0,0,0.2);">
            ISO Resources & Insights
        </h1>
        <p style="color: rgba(255,255,255,0.95); font-size: 1.4em; line-height: 1.7; max-width: 700px; margin: 0 auto 35px; text-shadow: 0 2px 10px rgba(0,0,0,0.1);">
            Stay informed with expert insights, industry news, and practical guidance on ISO standards and quality management
        </p>
        <div style="display: flex; gap: 15px; justify-content: center; align-items: center; flex-wrap: wrap;">
            <div style="display: flex; align-items: center; gap: 8px; background: rgba(255,255,255,0.15); padding: 12px 24px; border-radius: 30px; backdrop-filter: blur(10px);">
                <svg width="20" height="20" fill="white" viewBox="0 0 20 20"><path d="M9 2a1 1 0 000 2h2a1 1 0 100-2H9z"/><path fill-rule="evenodd" d="M4 5a2 2 0 012-2 3 3 0 003 3h2a3 3 0 003-3 2 2 0 012 2v11a2 2 0 01-2 2H6a2 2 0 01-2-2V5zm3 4a1 1 0 000 2h.01a1 1 0 100-2H7zm3 0a1 1 0 000 2h3a1 1 0 100-2h-3zm-3 4a1 1 0 100 2h.01a1 1 0 100-2H7zm3 0a1 1 0 100 2h3a1 1 0 100-2h-3z" clip-rule="evenodd"/></svg>
                <span style="color: white; font-weight: 600; font-size: 0.95em;">12 Articles</span>
            </div>
            <div style="display: flex; align-items: center; gap: 8px; background: rgba(255,255,255,0.15); padding: 12px 24px; border-radius: 30px; backdrop-filter: blur(10px);">
                <svg width="20" height="20" fill="white" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z" clip-rule="evenodd"/></svg>
                <span style="color: white; font-weight: 600; font-size: 0.95em;">Regularly Updated</span>
            </div>
        </div>
    </div>
</section>
'''
        new_body.append({
            'type': 'html',
            'value': {'html': hero_html},
            'id': str(uuid.uuid4())
        })

        # News & Articles Section - Enhanced design
        articles_html = '''
<section style="background: linear-gradient(to bottom, #f8f9ff 0%, #ffffff 100%); padding: 90px 20px;">
    <div style="max-width: 1200px; margin: 0 auto;">
        <div style="text-align: center; margin-bottom: 60px;">
            <div style="display: inline-block; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 8px 24px; border-radius: 30px; margin-bottom: 20px;">
                <span style="color: white; font-size: 0.85em; font-weight: 700; letter-spacing: 1.5px;">LATEST INSIGHTS</span>
            </div>
            <h2 style="color: #1a202c; font-size: 3em; font-weight: 800; margin-bottom: 15px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">
                News & Articles
            </h2>
            <p style="color: #4a5568; font-size: 1.2em; max-width: 600px; margin: 0 auto; line-height: 1.6;">
                Expert perspectives on ISO standards, quality management, and industry best practices
            </p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(380px, 1fr)); gap: 35px;">

            <!-- Article 1 -->
            <article class="article-card" style="background: white; border-radius: 20px; overflow: hidden; box-shadow: 0 10px 30px rgba(102, 126, 234, 0.1); border: 1px solid rgba(102, 126, 234, 0.1);">
                <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 35px 35px 25px; position: relative;">
                    <div class="article-icon" style="width: 60px; height: 60px; background: rgba(255,255,255,0.2); border-radius: 15px; display: flex; align-items: center; justify-content: center; margin-bottom: 15px; backdrop-filter: blur(10px);">
                        <svg width="30" height="30" fill="white" viewBox="0 0 20 20"><path d="M9 2a1 1 0 000 2h2a1 1 0 100-2H9z"/><path fill-rule="evenodd" d="M4 5a2 2 0 012-2 3 3 0 003 3h2a3 3 0 003-3 2 2 0 012 2v11a2 2 0 01-2 2H6a2 2 0 01-2-2V5zm9.707 5.707a1 1 0 00-1.414-1.414L9 12.586l-1.293-1.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
                    </div>
                    <div style="color: rgba(255,255,255,0.9); font-size: 0.9em; font-weight: 600; margin-bottom: 8px; letter-spacing: 0.5px;">27 October 2020</div>
                    <h3 style="color: white; font-size: 1.5em; font-weight: 700; line-height: 1.3; margin: 0;">Don't use templates to achieve an ISO Standard</h3>
                </div>
                <div style="padding: 30px;">
                    <p style="color: #4a5568; line-height: 1.7; margin-bottom: 25px; font-size: 0.98em;">Why you should not use someone else's templates to 'help' you attain an ISO Certification</p>
                    <a href="https://qualitation.co.uk/dont-use-templates-to-achieve-an-iso-standard" target="_blank" rel="noopener noreferrer" style="color: #667eea; text-decoration: none; font-weight: 700; display: inline-flex; align-items: center; gap: 8px; font-size: 0.95em;">
                        Read Full Article
                        <svg width="16" height="16" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd"/></svg>
                    </a>
                </div>
            </article>

            <!-- Article 2 -->
            <article class="article-card" style="background: white; border-radius: 20px; overflow: hidden; box-shadow: 0 10px 30px rgba(102, 126, 234, 0.1); border: 1px solid rgba(102, 126, 234, 0.1);">
                <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); padding: 35px 35px 25px; position: relative;">
                    <div class="article-icon" style="width: 60px; height: 60px; background: rgba(255,255,255,0.2); border-radius: 15px; display: flex; align-items: center; justify-content: center; margin-bottom: 15px; backdrop-filter: blur(10px);">
                        <svg width="30" height="30" fill="white" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M11.3 1.046A1 1 0 0112 2v5h4a1 1 0 01.82 1.573l-7 10A1 1 0 018 18v-5H4a1 1 0 01-.82-1.573l7-10a1 1 0 011.12-.38z" clip-rule="evenodd"/></svg>
                    </div>
                    <div style="color: rgba(255,255,255,0.9); font-size: 0.9em; font-weight: 600; margin-bottom: 8px; letter-spacing: 0.5px;">24 October 2019</div>
                    <h3 style="color: white; font-size: 1.5em; font-weight: 700; line-height: 1.3; margin: 0;">Automation is the future for ISO Standards!</h3>
                </div>
                <div style="padding: 30px;">
                    <p style="color: #4a5568; line-height: 1.7; margin-bottom: 25px; font-size: 0.98em;">How robots and automation are increasingly prevalent in manufacturing and ISO Standards implementation</p>
                    <a href="https://qualitation.co.uk/automation-is-the-future-for-iso-standards" target="_blank" rel="noopener noreferrer" style="color: #f5576c; text-decoration: none; font-weight: 700; display: inline-flex; align-items: center; gap: 8px; font-size: 0.95em;">
                        Read Full Article
                        <svg width="16" height="16" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd"/></svg>
                    </a>
                </div>
            </article>

            <!-- Article 3 -->
            <article class="article-card" style="background: white; border-radius: 20px; overflow: hidden; box-shadow: 0 10px 30px rgba(102, 126, 234, 0.1); border: 1px solid rgba(102, 126, 234, 0.1);">
                <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); padding: 35px 35px 25px; position: relative;">
                    <div class="article-icon" style="width: 60px; height: 60px; background: rgba(255,255,255,0.2); border-radius: 15px; display: flex; align-items: center; justify-content: center; margin-bottom: 15px; backdrop-filter: blur(10px);">
                        <svg width="30" height="30" fill="white" viewBox="0 0 20 20"><path d="M2 11a1 1 0 011-1h2a1 1 0 011 1v5a1 1 0 01-1 1H3a1 1 0 01-1-1v-5zM8 7a1 1 0 011-1h2a1 1 0 011 1v9a1 1 0 01-1 1H9a1 1 0 01-1-1V7zM14 4a1 1 0 011-1h2a1 1 0 011 1v12a1 1 0 01-1 1h-2a1 1 0 01-1-1V4z"/></svg>
                    </div>
                    <div style="color: rgba(255,255,255,0.9); font-size: 0.9em; font-weight: 600; margin-bottom: 8px; letter-spacing: 0.5px;">8 October 2019</div>
                    <h3 style="color: white; font-size: 1.5em; font-weight: 700; line-height: 1.3; margin: 0;">What is an ISO Standard for?</h3>
                </div>
                <div style="padding: 30px;">
                    <p style="color: #4a5568; line-height: 1.7; margin-bottom: 25px; font-size: 0.98em;">Everyone wants to buy good quality goods and services for a realistic value. Explores how ISO Standards help organizations optimize quality</p>
                    <a href="https://qualitation.co.uk/what-is-an-iso-standard-for" target="_blank" rel="noopener noreferrer" style="color: #00f2fe; text-decoration: none; font-weight: 700; display: inline-flex; align-items: center; gap: 8px; font-size: 0.95em;">
                        Read Full Article
                        <svg width="16" height="16" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd"/></svg>
                    </a>
                </div>
            </article>

            <!-- Article 4 -->
            <article class="article-card" style="background: white; border-radius: 20px; overflow: hidden; box-shadow: 0 10px 30px rgba(102, 126, 234, 0.1); border: 1px solid rgba(102, 126, 234, 0.1);">
                <div style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); padding: 35px 35px 25px; position: relative;">
                    <div class="article-icon" style="width: 60px; height: 60px; background: rgba(255,255,255,0.2); border-radius: 15px; display: flex; align-items: center; justify-content: center; margin-bottom: 15px; backdrop-filter: blur(10px);">
                        <svg width="30" height="30" fill="white" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M6.267 3.455a3.066 3.066 0 001.745-.723 3.066 3.066 0 013.976 0 3.066 3.066 0 001.745.723 3.066 3.066 0 012.812 2.812c.051.643.304 1.254.723 1.745a3.066 3.066 0 010 3.976 3.066 3.066 0 00-.723 1.745 3.066 3.066 0 01-2.812 2.812 3.066 3.066 0 00-1.745.723 3.066 3.066 0 01-3.976 0 3.066 3.066 0 00-1.745-.723 3.066 3.066 0 01-2.812-2.812 3.066 3.066 0 00-.723-1.745 3.066 3.066 0 010-3.976 3.066 3.066 0 00.723-1.745 3.066 3.066 0 012.812-2.812zm7.44 5.252a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
                    </div>
                    <div style="color: rgba(255,255,255,0.9); font-size: 0.9em; font-weight: 600; margin-bottom: 8px; letter-spacing: 0.5px;">30 September 2019</div>
                    <h3 style="color: white; font-size: 1.5em; font-weight: 700; line-height: 1.3; margin: 0;">Trust but Verify</h3>
                </div>
                <div style="padding: 30px;">
                    <p style="color: #4a5568; line-height: 1.7; margin-bottom: 25px; font-size: 0.98em;">Addresses verification across complex supply chains where products become components in larger offerings</p>
                    <a href="https://qualitation.co.uk/trust-but-verify" target="_blank" rel="noopener noreferrer" style="color: #fa709a; text-decoration: none; font-weight: 700; display: inline-flex; align-items: center; gap: 8px; font-size: 0.95em;">
                        Read Full Article
                        <svg width="16" height="16" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd"/></svg>
                    </a>
                </div>
            </article>

            <!-- Article 5 -->
            <article class="article-card" style="background: white; border-radius: 20px; overflow: hidden; box-shadow: 0 10px 30px rgba(102, 126, 234, 0.1); border: 1px solid rgba(102, 126, 234, 0.1);">
                <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 35px 35px 25px; position: relative;">
                    <div class="article-icon" style="width: 60px; height: 60px; background: rgba(255,255,255,0.2); border-radius: 15px; display: flex; align-items: center; justify-content: center; margin-bottom: 15px; backdrop-filter: blur(10px);">
                        <svg width="30" height="30" fill="white" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd"/></svg>
                    </div>
                    <div style="color: rgba(255,255,255,0.9); font-size: 0.9em; font-weight: 600; margin-bottom: 8px; letter-spacing: 0.5px;">26 September 2019</div>
                    <h3 style="color: white; font-size: 1.5em; font-weight: 700; line-height: 1.3; margin: 0;">Rewarding Failure – should we?</h3>
                </div>
                <div style="padding: 30px;">
                    <p style="color: #4a5568; line-height: 1.7; margin-bottom: 25px; font-size: 0.98em;">Examines uncertainty and disruption caused by failure in various contexts and organizational settings</p>
                    <a href="https://qualitation.co.uk/rewarding-failure-should-we" target="_blank" rel="noopener noreferrer" style="color: #667eea; text-decoration: none; font-weight: 700; display: inline-flex; align-items: center; gap: 8px; font-size: 0.95em;">
                        Read Full Article
                        <svg width="16" height="16" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd"/></svg>
                    </a>
                </div>
            </article>

            <!-- Article 6 -->
            <article class="article-card" style="background: white; border-radius: 20px; overflow: hidden; box-shadow: 0 10px 30px rgba(102, 126, 234, 0.1); border: 1px solid rgba(102, 126, 234, 0.1);">
                <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); padding: 35px 35px 25px; position: relative;">
                    <div class="article-icon" style="width: 60px; height: 60px; background: rgba(255,255,255,0.2); border-radius: 15px; display: flex; align-items: center; justify-content: center; margin-bottom: 15px; backdrop-filter: blur(10px);">
                        <svg width="30" height="30" fill="white" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M3 3a1 1 0 000 2v8a2 2 0 002 2h2.586l-1.293 1.293a1 1 0 101.414 1.414L10 15.414l2.293 2.293a1 1 0 001.414-1.414L12.414 15H15a2 2 0 002-2V5a1 1 0 100-2H3zm11 4a1 1 0 10-2 0v4a1 1 0 102 0V7zm-3 1a1 1 0 10-2 0v3a1 1 0 102 0V8zM8 9a1 1 0 00-2 0v2a1 1 0 102 0V9z" clip-rule="evenodd"/></svg>
                    </div>
                    <div style="color: rgba(255,255,255,0.9); font-size: 0.9em; font-weight: 600; margin-bottom: 8px; letter-spacing: 0.5px;">23 September 2019</div>
                    <h3 style="color: white; font-size: 1.5em; font-weight: 700; line-height: 1.3; margin: 0;">Why choose to automate quality first NOT volume?</h3>
                </div>
                <div style="padding: 30px;">
                    <p style="color: #4a5568; line-height: 1.7; margin-bottom: 25px; font-size: 0.98em;">Explores automated systems in manufacturing, emphasizing quality prioritization over volume</p>
                    <a href="https://qualitation.co.uk/why-choose-to-automate-quality-first-not-volume" target="_blank" rel="noopener noreferrer" style="color: #f5576c; text-decoration: none; font-weight: 700; display: inline-flex; align-items: center; gap: 8px; font-size: 0.95em;">
                        Read Full Article
                        <svg width="16" height="16" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd"/></svg>
                    </a>
                </div>
            </article>

            <!-- Article 7 -->
            <article class="article-card" style="background: white; border-radius: 20px; overflow: hidden; box-shadow: 0 10px 30px rgba(102, 126, 234, 0.1); border: 1px solid rgba(102, 126, 234, 0.1);">
                <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); padding: 35px 35px 25px; position: relative;">
                    <div class="article-icon" style="width: 60px; height: 60px; background: rgba(255,255,255,0.2); border-radius: 15px; display: flex; align-items: center; justify-content: center; margin-bottom: 15px; backdrop-filter: blur(10px);">
                        <svg width="30" height="30" fill="white" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M2 5a2 2 0 012-2h12a2 2 0 012 2v2a2 2 0 01-2 2H4a2 2 0 01-2-2V5zm14 1a1 1 0 11-2 0 1 1 0 012 0zM2 13a2 2 0 012-2h12a2 2 0 012 2v2a2 2 0 01-2 2H4a2 2 0 01-2-2v-2zm14 1a1 1 0 11-2 0 1 1 0 012 0z" clip-rule="evenodd"/></svg>
                    </div>
                    <div style="color: rgba(255,255,255,0.9); font-size: 0.9em; font-weight: 600; margin-bottom: 8px; letter-spacing: 0.5px;">13 June 2019</div>
                    <h3 style="color: white; font-size: 1.5em; font-weight: 700; line-height: 1.3; margin: 0;">Why IT is the Key to More Efficient ISO Administration</h3>
                </div>
                <div style="padding: 30px;">
                    <p style="color: #4a5568; line-height: 1.7; margin-bottom: 25px; font-size: 0.98em;">Explains how automated systems reduce tedious ISO administrator workload while maintaining standards compliance</p>
                    <a href="https://qualitation.co.uk/why-it-is-the-key-to-more-efficient-iso-administration" target="_blank" rel="noopener noreferrer" style="color: #00f2fe; text-decoration: none; font-weight: 700; display: inline-flex; align-items: center; gap: 8px; font-size: 0.95em;">
                        Read Full Article
                        <svg width="16" height="16" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd"/></svg>
                    </a>
                </div>
            </article>

            <!-- Article 8 -->
            <article class="article-card" style="background: white; border-radius: 20px; overflow: hidden; box-shadow: 0 10px 30px rgba(102, 126, 234, 0.1); border: 1px solid rgba(102, 126, 234, 0.1);">
                <div style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); padding: 35px 35px 25px; position: relative;">
                    <div class="article-icon" style="width: 60px; height: 60px; background: rgba(255,255,255,0.2); border-radius: 15px; display: flex; align-items: center; justify-content: center; margin-bottom: 15px; backdrop-filter: blur(10px);">
                        <svg width="30" height="30" fill="white" viewBox="0 0 20 20"><path d="M13 7H7v6h6V7z"/><path fill-rule="evenodd" d="M7 2a1 1 0 012 0v1h2V2a1 1 0 112 0v1h2a2 2 0 012 2v2h1a1 1 0 110 2h-1v2h1a1 1 0 110 2h-1v2a2 2 0 01-2 2h-2v1a1 1 0 11-2 0v-1H9v1a1 1 0 11-2 0v-1H5a2 2 0 01-2-2v-2H2a1 1 0 110-2h1V9H2a1 1 0 010-2h1V5a2 2 0 012-2h2V2zM5 5h10v10H5V5z" clip-rule="evenodd"/></svg>
                    </div>
                    <div style="color: rgba(255,255,255,0.9); font-size: 0.9em; font-weight: 600; margin-bottom: 8px; letter-spacing: 0.5px;">3 June 2019</div>
                    <h3 style="color: white; font-size: 1.5em; font-weight: 700; line-height: 1.3; margin: 0;">The wide-ranging benefits of ISO IT software</h3>
                </div>
                <div style="padding: 30px;">
                    <p style="color: #4a5568; line-height: 1.7; margin-bottom: 25px; font-size: 0.98em;">Describes how ISO software reduces administrative burden and improves organizational processes and staff motivation</p>
                    <a href="https://qualitation.co.uk/the-wide-ranging-benefits-of-iso-it-software" target="_blank" rel="noopener noreferrer" style="color: #fa709a; text-decoration: none; font-weight: 700; display: inline-flex; align-items: center; gap: 8px; font-size: 0.95em;">
                        Read Full Article
                        <svg width="16" height="16" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd"/></svg>
                    </a>
                </div>
            </article>

            <!-- Article 9 -->
            <article class="article-card" style="background: white; border-radius: 20px; overflow: hidden; box-shadow: 0 10px 30px rgba(102, 126, 234, 0.1); border: 1px solid rgba(102, 126, 234, 0.1);">
                <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 35px 35px 25px; position: relative;">
                    <div class="article-icon" style="width: 60px; height: 60px; background: rgba(255,255,255,0.2); border-radius: 15px; display: flex; align-items: center; justify-content: center; margin-bottom: 15px; backdrop-filter: blur(10px);">
                        <svg width="30" height="30" fill="white" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
                    </div>
                    <div style="color: rgba(255,255,255,0.9); font-size: 0.9em; font-weight: 600; margin-bottom: 8px; letter-spacing: 0.5px;">29 May 2019</div>
                    <h3 style="color: white; font-size: 1.5em; font-weight: 700; line-height: 1.3; margin: 0;">Why Put Quality First?</h3>
                </div>
                <div style="padding: 30px;">
                    <p style="color: #4a5568; line-height: 1.7; margin-bottom: 25px; font-size: 0.98em;">Putting quality management at the forefront of your operations by investing in internationally recognised ISO standards is vital</p>
                    <a href="https://qualitation.co.uk/why-put-quality-first" target="_blank" rel="noopener noreferrer" style="color: #667eea; text-decoration: none; font-weight: 700; display: inline-flex; align-items: center; gap: 8px; font-size: 0.95em;">
                        Read Full Article
                        <svg width="16" height="16" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd"/></svg>
                    </a>
                </div>
            </article>

            <!-- Article 10 -->
            <article class="article-card" style="background: white; border-radius: 20px; overflow: hidden; box-shadow: 0 10px 30px rgba(102, 126, 234, 0.1); border: 1px solid rgba(102, 126, 234, 0.1);">
                <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); padding: 35px 35px 25px; position: relative;">
                    <div class="article-icon" style="width: 60px; height: 60px; background: rgba(255,255,255,0.2); border-radius: 15px; display: flex; align-items: center; justify-content: center; margin-bottom: 15px; backdrop-filter: blur(10px);">
                        <svg width="30" height="30" fill="white" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M3.172 5.172a4 4 0 015.656 0L10 6.343l1.172-1.171a4 4 0 115.656 5.656L10 17.657l-6.828-6.829a4 4 0 010-5.656z" clip-rule="evenodd"/></svg>
                    </div>
                    <div style="color: rgba(255,255,255,0.9); font-size: 0.9em; font-weight: 600; margin-bottom: 8px; letter-spacing: 0.5px;">21 May 2019</div>
                    <h3 style="color: white; font-size: 1.5em; font-weight: 700; line-height: 1.3; margin: 0;">Why Should Quality Matter More To Your Business?</h3>
                </div>
                <div style="padding: 30px;">
                    <p style="color: #4a5568; line-height: 1.7; margin-bottom: 25px; font-size: 0.98em;">Emphasizes quality as essential for customer loyalty and profit growth, advocating for ISO 9001 certification</p>
                    <a href="https://qualitation.co.uk/why-should-quality-matter-more-to-your-business" target="_blank" rel="noopener noreferrer" style="color: #f5576c; text-decoration: none; font-weight: 700; display: inline-flex; align-items: center; gap: 8px; font-size: 0.95em;">
                        Read Full Article
                        <svg width="16" height="16" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd"/></svg>
                    </a>
                </div>
            </article>

            <!-- Article 11 -->
            <article class="article-card" style="background: white; border-radius: 20px; overflow: hidden; box-shadow: 0 10px 30px rgba(102, 126, 234, 0.1); border: 1px solid rgba(102, 126, 234, 0.1);">
                <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); padding: 35px 35px 25px; position: relative;">
                    <div class="article-icon" style="width: 60px; height: 60px; background: rgba(255,255,255,0.2); border-radius: 15px; display: flex; align-items: center; justify-content: center; margin-bottom: 15px; backdrop-filter: blur(10px);">
                        <svg width="30" height="30" fill="white" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M12 1.586l-4 4v12.828l4-4V1.586zM3.707 3.293A1 1 0 002 4v10a1 1 0 00.293.707L6 18.414V5.586L3.707 3.293zM17.707 5.293L14 1.586v12.828l2.293 2.293A1 1 0 0018 16V6a1 1 0 00-.293-.707z" clip-rule="evenodd"/></svg>
                    </div>
                    <div style="color: rgba(255,255,255,0.9); font-size: 0.9em; font-weight: 600; margin-bottom: 8px; letter-spacing: 0.5px;">11 March 2019</div>
                    <h3 style="color: white; font-size: 1.5em; font-weight: 700; line-height: 1.3; margin: 0;">Brexit – how are ISO standards affected?</h3>
                </div>
                <div style="padding: 30px;">
                    <p style="color: #4a5568; line-height: 1.7; margin-bottom: 25px; font-size: 0.98em;">Explains that ISO infrastructure remains unchanged despite Brexit, as ISO operates independently from the UK</p>
                    <a href="https://qualitation.co.uk/brexit-how-are-iso-standards-affected" target="_blank" rel="noopener noreferrer" style="color: #00f2fe; text-decoration: none; font-weight: 700; display: inline-flex; align-items: center; gap: 8px; font-size: 0.95em;">
                        Read Full Article
                        <svg width="16" height="16" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd"/></svg>
                    </a>
                </div>
            </article>

            <!-- Article 12 -->
            <article class="article-card" style="background: white; border-radius: 20px; overflow: hidden; box-shadow: 0 10px 30px rgba(102, 126, 234, 0.1); border: 1px solid rgba(102, 126, 234, 0.1);">
                <div style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); padding: 35px 35px 25px; position: relative;">
                    <div class="article-icon" style="width: 60px; height: 60px; background: rgba(255,255,255,0.2); border-radius: 15px; display: flex; align-items: center; justify-content: center; margin-bottom: 15px; backdrop-filter: blur(10px);">
                        <svg width="30" height="30" fill="white" viewBox="0 0 20 20"><path d="M3 12v3c0 1.657 3.134 3 7 3s7-1.343 7-3v-3c0 1.657-3.134 3-7 3s-7-1.343-7-3z"/><path d="M3 7v3c0 1.657 3.134 3 7 3s7-1.343 7-3V7c0 1.657-3.134 3-7 3S3 8.657 3 7z"/><path d="M17 5c0 1.657-3.134 3-7 3S3 6.657 3 5s3.134-3 7-3 7 1.343 7 3z"/></svg>
                    </div>
                    <div style="color: rgba(255,255,255,0.9); font-size: 0.9em; font-weight: 600; margin-bottom: 8px; letter-spacing: 0.5px;">22 June 2018</div>
                    <h3 style="color: white; font-size: 1.5em; font-weight: 700; line-height: 1.3; margin: 0;">Sustainable Business Practices with ISO 14001</h3>
                </div>
                <div style="padding: 30px;">
                    <p style="color: #4a5568; line-height: 1.7; margin-bottom: 25px; font-size: 0.98em;">Focuses on consumer demand for ethical purchasing and manufacturer sustainability commitments through ISO 14001</p>
                    <a href="https://qualitation.co.uk/sustainable-business-practices-with-iso-14001" target="_blank" rel="noopener noreferrer" style="color: #fa709a; text-decoration: none; font-weight: 700; display: inline-flex; align-items: center; gap: 8px; font-size: 0.95em;">
                        Read Full Article
                        <svg width="16" height="16" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd"/></svg>
                    </a>
                </div>
            </article>

        </div>
    </div>
</section>
'''
        new_body.append({
            'type': 'html',
            'value': {'html': articles_html},
            'id': str(uuid.uuid4())
        })

        # CTA Section - Beautiful call to action
        cta_html = '''
<section style="background: linear-gradient(to bottom, #ffffff 0%, #f8f9ff 100%); padding: 90px 20px;">
    <div style="max-width: 900px; margin: 0 auto;">
        <div class="cta-gradient" style="padding: 70px 50px; border-radius: 30px; text-align: center; color: white; box-shadow: 0 25px 50px rgba(102, 126, 234, 0.3);">
            <div style="width: 80px; height: 80px; background: rgba(255,255,255,0.2); border-radius: 20px; display: flex; align-items: center; justify-content: center; margin: 0 auto 25px; backdrop-filter: blur(10px);">
                <svg width="40" height="40" fill="white" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M18 10c0 3.866-3.582 7-8 7a8.841 8.841 0 01-4.083-.98L2 17l1.338-3.123C2.493 12.767 2 11.434 2 10c0-3.866 3.582-7 8-7s8 3.134 8 7zM7 9H5v2h2V9zm8 0h-2v2h2V9zM9 9h2v2H9V9z" clip-rule="evenodd"/></svg>
            </div>
            <h2 style="font-size: 2.8em; font-weight: 800; margin-bottom: 20px; line-height: 1.2;">Need Personalized Guidance?</h2>
            <p style="font-size: 1.3em; margin-bottom: 40px; opacity: 0.95; line-height: 1.6; max-width: 600px; margin-left: auto; margin-right: auto;">
                Our expert team is here to help. Get in touch for a free consultation and discover how we can support your ISO certification journey.
            </p>
            <a href="/contact/" class="cta-button" style="background: white; color: #667eea; padding: 18px 50px; border-radius: 50px; text-decoration: none; font-size: 1.2em; display: inline-block; font-weight: 700; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);">
                Contact Us Today
            </a>
        </div>
    </div>
</section>
'''
        new_body.append({
            'type': 'html',
            'value': {'html': cta_html},
            'id': str(uuid.uuid4())
        })

        # Update the database
        new_body_json = json.dumps(new_body)

        with connection.cursor() as cursor:
            cursor.execute('''
                SELECT p.id
                FROM home_flexiblepage fp
                JOIN wagtailcore_page p ON fp.page_ptr_id = p.id
                WHERE p.slug = 'resources'
            ''')
            page_id = cursor.fetchone()[0]

            cursor.execute('''
                UPDATE home_flexiblepage
                SET body = %s
                WHERE page_ptr_id = %s
            ''', [new_body_json, page_id])

        # Publish the page
        from home.models import FlexiblePage
        page = FlexiblePage.objects.get(id=page_id)
        page.save_revision().publish()

        self.stdout.write(self.style.SUCCESS('✓ Resources page beautifully redesigned!'))
        self.stdout.write(self.style.SUCCESS('  - Modern gradient hero section'))
        self.stdout.write(self.style.SUCCESS('  - 12 colorful article cards with hover effects'))
        self.stdout.write(self.style.SUCCESS('  - Beautiful CTA section with animations'))
        self.stdout.write(self.style.SUCCESS('  - Enhanced typography and spacing'))
        self.stdout.write(self.style.SUCCESS('✓ Page published successfully'))

        self.stdout.write(self.style.SUCCESS('\n=== Complete ===\n'))
