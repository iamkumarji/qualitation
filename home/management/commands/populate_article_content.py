"""
Django management command to populate article content from the original HTML files
"""

from django.core.management.base import BaseCommand
from home.models import ArticlePage


class Command(BaseCommand):
    help = 'Populate article pages with full content'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('\n=== Populating Article Content ===\n'))

        # Article 1: Templates
        templates_content = '''
<p>I was recently contacted out of the blue and asked to help complete some ISO templates that they had attached. I read the attachments they sent and I could see why they were having difficulty working out how to complete the templates.</p>

<p>The templates were not very well structured and were out of date – some were dated over 10 years ago, or they referred to versions of the standard that have been replaced at least once if not twice by now etc.</p>

<p><strong style="color: #f5576c;">I replied expressing the hope they had not paid for them as it was my opinion that they would be spending far more of your time fitting them to their organisation than if they had started from scratch.</strong></p>

<h2 style="color: #1e3a5f; margin-top: 40px; margin-bottom: 20px;">So what are the problems with using a template?</h2>

<p>While a template will allow you to get the standard certified initially, it is useless for several reasons:</p>

<ul style="margin: 20px 0; padding-left: 30px;">
    <li style="margin-bottom: 15px;">It does not relate to your organisation (being generic) so no-one reading it (ie your staff) will understand what it is about – so how can the staff follow it</li>
    <li style="margin-bottom: 15px;">By the time you/someone in your team has adjusted the clauses so that it does relate to your organisation, they might as well have started from scratch.</li>
    <li style="margin-bottom: 15px;">The templates will not detail the way you will actually be working (so you have to run it as an extra task in parallel to your own controls that you already use – ie extra work)</li>
    <li>It will not help you to achieve the goals you are getting the standard for:
        <ul style="margin-top: 10px; padding-left: 30px;">
            <li style="margin-bottom: 10px;">If you want the standard to improve your operations: it won't – as the templates do not relate to your operations without totally rewriting them</li>
            <li style="margin-bottom: 10px;">If you want the standard to meet tender requirements – you might have certification, but so will all others applying and if any of them actually have a proper system supporting it, they will be better than you and you will not get the tender anyway</li>
            <li>If you want the standard to improve your staff capabilities – it won't as they will recognise that you have cut corners plus they will likely be confused by the fact there seem to be 2 parallel systems one of which they don't recognise</li>
        </ul>
    </li>
</ul>

<h2 style="color: #1e3a5f; margin-top: 40px; margin-bottom: 20px;">So what does a good Management System achieve?</h2>

<p><strong>A good control system:</strong></p>

<ul style="margin: 20px 0; padding-left: 30px;">
    <li style="margin-bottom: 10px;">reduces the time you spend on the system,</li>
    <li style="margin-bottom: 10px;">matches what you do already as much as possible,</li>
    <li style="margin-bottom: 10px;">its within your normal procedures so you don't have extra work,</li>
    <li style="margin-bottom: 10px;">is understood and used by everyone in the organisation,</li>
    <li style="margin-bottom: 10px;">the improvements continue to develop year by year for ever,</li>
    <li style="margin-bottom: 10px;">the financial return and profitability improve too.</li>
</ul>

<p style="margin-top: 30px;"><strong style="color: #1e3a5f;">Finally, and often most importantly,</strong> because you have business systems that achieve this, your organisation becomes one that others want to work with – so you will win tenders as well.</p>

<h2 style="color: #1e3a5f; margin-top: 40px; margin-bottom: 20px;">The Bottom Line</h2>

<p style="font-weight: 500; color: #f5576c; font-size: 1.15em;">From a cost efficiency point of view, I would never recommend that anyone use templates.</p>

<p>You can choose whoever you like as a consultant, but even if they are bad, they will be better than using most templates that I have ever seen.</p>

<p><strong>So contact us to have a free, no obligation conversation about how to take things forwards.</strong> It will cost you to get a consultant in. But it will cost you if you use templates as that will be totally wasted money. With any reasonable consultant you will get systems that match what you do in a way that following them is easy.</p>

<p style="margin-top: 30px;">Contact us via our website or call us on <strong>0345 600 6975</strong> or email <a href="mailto:carl.kruger@qualitation.co.uk">carl.kruger@qualitation.co.uk</a></p>
'''

        # Article 2: Automation
        automation_content = '''
<p>We have all seen the headlines telling us that robots are taking over in manufacturing and we have had many versions of the science fiction theory that robots will take over the world – well it is coming closer!</p>

<p><strong style="color: #4facfe;">Rest assured, I am not referring to a military takeover, nor anything detrimental at all actually!</strong></p>

<p>I am referring to the fact that more and more the possibility exists to have programmes take over some of the grunt work behind bureaucracy and tedious repetitive daily grind. Throw in the fact that when it is hooked up correctly, this results in better re ordering of details, trends, nuances and patterns and you can see how these can be better analysed to identify more sensitive indicators to market directions, more precise spotting of quality issues at earlier stages and quicker response times to issues before they turn into problems, than ever before.</p>

<h2 style="color: #1e3a5f; margin-top: 40px; margin-bottom: 20px;">The Impact</h2>

<p>What is happening is an ability to <strong>ascertain the root causes earlier</strong> – leading to prompter action and resulting in:</p>

<ul style="margin: 20px 0; padding-left: 30px;">
    <li style="margin-bottom: 10px;">Less downtime</li>
    <li style="margin-bottom: 10px;">Less financial loss</li>
    <li style="margin-bottom: 10px;">Less customer dissatisfaction</li>
</ul>

<p>Alternatively, it allows us to see where we can improve further than ever before with:</p>

<ul style="margin: 20px 0; padding-left: 30px;">
    <li style="margin-bottom: 10px;">More productivity</li>
    <li style="margin-bottom: 10px;">More profit</li>
    <li style="margin-bottom: 10px;">More customer and staff satisfaction</li>
</ul>

<h2 style="color: #1e3a5f; margin-top: 40px; margin-bottom: 20px;">Where is This Revolution?</h2>

<p>Actually, it is not that new – it has been happening piecemeal in the background for a while, but it is starting to break through to mainstream. It is in the daily control of systems. Documentation, training, auditing and purchasing have experienced this already and now it is moving into development of management systems, installation of controls and cross checking of activities.</p>

<p><strong>Specifically, the ISO Business Management systems are getting automated.</strong> While there is still need for human control of the systems, the installations are becoming sufficiently automated that there will be a time when ISO consultancy will fall away.</p>

<p style="font-style: italic; color: #666; margin: 30px 0;">Remember – this is my field – I run a network of ISO consultants – and I am predicting that our work will decline. I prefer to say it as I see it and note, as I certainly feel, that it is better to go with the flow. This will happen more and more and we should not stand in the way and expect the changes to go away!</p>

<h2 style="color: #1e3a5f; margin-top: 40px; margin-bottom: 20px;">Advantages of Automated ISO Systems</h2>

<p>I know of several automated ISO system programmes now – in 9001, 14001, 45001 and 27001 – with more to come. They offer a number of advantages:</p>

<ul style="margin: 20px 0; padding-left: 30px;">
    <li style="margin-bottom: 15px;">They are as fast or slow to install as the organisation wants them to be</li>
    <li style="margin-bottom: 15px;">They ensure that you have everything you need to gain certification</li>
    <li style="margin-bottom: 15px;">They provide direct links between what you do and the clauses in the Standards</li>
    <li style="margin-bottom: 15px;">The auditing by the certifier is facilitated as everything is in the history logs</li>
    <li style="margin-bottom: 15px;">They can be installed without additional ISO consultants in many cases</li>
    <li style="margin-bottom: 15px;">They can be installed with less ISO consultancy in all cases</li>
    <li style="margin-bottom: 15px;">Over time your organisation will know and understand the systems far deeper</li>
    <li><strong style="color: #66bb6a;">They can be up to 10 times cheaper to install than previously!</strong></li>
</ul>

<h2 style="color: #1e3a5f; margin-top: 40px; margin-bottom: 20px;">Some Considerations</h2>

<p>There are some disadvantages too:</p>

<ul style="margin: 20px 0; padding-left: 30px;">
    <li style="margin-bottom: 15px;">If you don't know anything about ISO standards, this may be quite a learning curve – but that was going to be the case anyway – it is just that you may not have an ISO consultant to hand with the automated systems</li>
    <li style="margin-bottom: 15px;">You may find that you are not sure where to stop – adding controls where they are not needed</li>
    <li>Combining them with existing ISO systems will be more difficult unless the existing systems shift to automated set-ups as well (but that would potentially be cheaper in the long run anyway)</li>
</ul>

<h2 style="color: #1e3a5f; margin-top: 40px; margin-bottom: 20px;">Other Areas of Interest</h2>

<p><strong>Industry-Specific Standards:</strong> Those standards specific to particular industries sectors (aviation, automotive, medical devices, laboratory competence etc) will still require a specialist consultant if the organisation has never used the standard before. They are simply too complex and too uniquely focused to let programmes sort this kind of approach at this time (maybe not for ever, but it will be quite a while).</p>

<p style="margin-top: 30px;"><strong>Revolution in Certification Auditing:</strong> Auditing of automated systems will revolutionise certification – with assessment visits being capable of being carried out from offsite (via cloud) – not every year and not for all aspects of the system, but enough that costs should come down and certifiers become more flexible. This is my opinion, rather than fact, but there seem to me to be enough smaller certifiers that will do this to improve their business reach that others will get left behind if they don't follow suit.</p>

<h2 style="color: #1e3a5f; margin-top: 40px; margin-bottom: 20px;">The Bottom Line</h2>

<p><strong>Automation is here to stay and early movers get a huge advantage over late-comers</strong> – namely that their systems will be less demanding of human time – and consequently should be more productive.</p>

<p>With productivity being the current focus of attention in the UK's economic markets (again), this should sound a very attractive proposition.</p>

<p style="margin-top: 30px;">If you want to find out more, please contact <strong>Carl Kruger on 0345 800 6975</strong></p>
'''

        try:
            # Update Templates article
            templates_article = ArticlePage.objects.get(slug='dont-use-templates-to-achieve-an-iso-standard')
            templates_article.body = templates_content
            templates_article.save_revision().publish()
            self.stdout.write(self.style.SUCCESS('✓ Updated Templates article content'))

            # Update Automation article
            automation_article = ArticlePage.objects.get(slug='automation-is-the-future-for-iso-standards')
            automation_article.body = automation_content
            automation_article.save_revision().publish()
            self.stdout.write(self.style.SUCCESS('✓ Updated Automation article content'))

            self.stdout.write(self.style.SUCCESS('\n✓ All articles populated with full content'))

        except ArticlePage.DoesNotExist as e:
            self.stdout.write(self.style.ERROR(f'✗ Article not found: {e}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ Error: {e}'))
            import traceback
            traceback.print_exc()

        self.stdout.write(self.style.SUCCESS('\n=== Complete ===\n'))
