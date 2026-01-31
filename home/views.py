from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from django.contrib import messages
from django.conf import settings
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods
from wagtail.models import Site
from home.models import EmailSettings
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


@csrf_protect
@require_http_methods(["POST"])
def contact_form_submission(request):
    """Handle contact form submissions and send email notifications"""

    # Get email settings from admin panel
    site = Site.find_for_request(request)
    email_settings = EmailSettings.for_site(site)

    # Check if email is configured
    if not email_settings.is_configured:
        messages.error(request, 'Email is not configured. Please contact the administrator.')
        logger.error('Contact form submission attempted but email is not configured')
        return redirect(request.META.get('HTTP_REFERER', '/'))

    # Get form data
    name = request.POST.get('name', '').strip()
    email = request.POST.get('email', '').strip()
    phone = request.POST.get('phone', '').strip()
    company = request.POST.get('company', '').strip()
    message = request.POST.get('message', '').strip()

    # Validate required fields
    if not name or not email:
        messages.error(request, 'Name and email are required.')
        return redirect(request.META.get('HTTP_REFERER', '/'))

    # Prepare email content
    subject = f'🔔 New Contact Form Submission from {name}'

    # Get current timestamp
    timestamp = datetime.now().strftime('%B %d, %Y at %I:%M %p')

    # HTML Email body for admin
    html_body = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body style="margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; background-color: #f5f5f5;">
        <table width="100%" cellpadding="0" cellspacing="0" style="background-color: #f5f5f5; padding: 40px 20px;">
            <tr>
                <td align="center">
                    <table width="600" cellpadding="0" cellspacing="0" style="background-color: #ffffff; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.1);">
                        <!-- Header -->
                        <tr>
                            <td style="background: linear-gradient(135deg, #2563eb 0%, #7c3aed 100%); padding: 40px 30px; text-align: center;">
                                <h1 style="margin: 0; color: #ffffff; font-size: 28px; font-weight: 700;">📬 New Contact Form Submission</h1>
                                <p style="margin: 10px 0 0; color: rgba(255,255,255,0.9); font-size: 14px;">{timestamp}</p>
                            </td>
                        </tr>

                        <!-- Content -->
                        <tr>
                            <td style="padding: 40px 30px;">
                                <!-- Contact Information -->
                                <div style="background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%); border-left: 4px solid #2563eb; border-radius: 8px; padding: 25px; margin-bottom: 25px;">
                                    <h2 style="margin: 0 0 20px; color: #1e40af; font-size: 20px; font-weight: 600;">👤 Contact Information</h2>

                                    <table width="100%" cellpadding="8" cellspacing="0">
                                        <tr>
                                            <td style="width: 120px; color: #64748b; font-weight: 600; font-size: 14px; padding: 8px 0;">Name:</td>
                                            <td style="color: #1e293b; font-size: 15px; font-weight: 500; padding: 8px 0;">{name}</td>
                                        </tr>
                                        <tr>
                                            <td style="width: 120px; color: #64748b; font-weight: 600; font-size: 14px; padding: 8px 0;">Email:</td>
                                            <td style="padding: 8px 0;">
                                                <a href="mailto:{email}" style="color: #2563eb; text-decoration: none; font-size: 15px; font-weight: 500;">{email}</a>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td style="width: 120px; color: #64748b; font-weight: 600; font-size: 14px; padding: 8px 0;">Phone:</td>
                                            <td style="color: #1e293b; font-size: 15px; font-weight: 500; padding: 8px 0;">{phone if phone else '<span style="color: #94a3b8;">Not provided</span>'}</td>
                                        </tr>
                                        <tr>
                                            <td style="width: 120px; color: #64748b; font-weight: 600; font-size: 14px; padding: 8px 0;">Company:</td>
                                            <td style="color: #1e293b; font-size: 15px; font-weight: 500; padding: 8px 0;">{company if company else '<span style="color: #94a3b8;">Not provided</span>'}</td>
                                        </tr>
                                    </table>
                                </div>

                                <!-- Message -->
                                <div style="background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%); border-left: 4px solid #f59e0b; border-radius: 8px; padding: 25px; margin-bottom: 25px;">
                                    <h2 style="margin: 0 0 15px; color: #92400e; font-size: 20px; font-weight: 600;">💬 Message</h2>
                                    <div style="color: #451a03; font-size: 15px; line-height: 1.7; white-space: pre-wrap;">{message if message else '<span style="color: #a16207;">No message provided</span>'}</div>
                                </div>

                                <!-- Action Button -->
                                <div style="text-align: center; margin-top: 30px;">
                                    <a href="mailto:{email}?subject=Re: Contact Form Inquiry" style="display: inline-block; background: linear-gradient(135deg, #2563eb, #7c3aed); color: #ffffff; text-decoration: none; padding: 15px 35px; border-radius: 8px; font-weight: 600; font-size: 16px; box-shadow: 0 4px 15px rgba(37, 99, 235, 0.3);">
                                        📧 Reply to {name.split()[0]}
                                    </a>
                                </div>
                            </td>
                        </tr>

                        <!-- Footer -->
                        <tr>
                            <td style="background-color: #f8fafc; padding: 25px 30px; border-top: 1px solid #e2e8f0; text-align: center;">
                                <p style="margin: 0; color: #64748b; font-size: 13px; line-height: 1.6;">
                                    This email was automatically sent from your website's contact form.<br>
                                    <strong style="color: #475569;">Qualitation</strong> - Quality Management Solutions
                                </p>
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
        </table>
    </body>
    </html>
    """

    # Plain text fallback
    text_body = f"""
New Contact Form Submission - {timestamp}

CONTACT INFORMATION:
Name: {name}
Email: {email}
Phone: {phone if phone else 'Not provided'}
Company: {company if company else 'Not provided'}

MESSAGE:
{message if message else 'No message provided'}

---
Reply to: {email}
This email was sent from your website's contact form.
    """

    try:
        # Temporarily apply email settings from admin panel
        old_backend = getattr(settings, 'EMAIL_BACKEND', None)
        old_host = getattr(settings, 'EMAIL_HOST', None)
        old_port = getattr(settings, 'EMAIL_PORT', None)
        old_use_tls = getattr(settings, 'EMAIL_USE_TLS', None)
        old_use_ssl = getattr(settings, 'EMAIL_USE_SSL', None)
        old_user = getattr(settings, 'EMAIL_HOST_USER', None)
        old_password = getattr(settings, 'EMAIL_HOST_PASSWORD', None)
        old_from = getattr(settings, 'DEFAULT_FROM_EMAIL', None)

        # Apply settings from admin panel
        settings.EMAIL_BACKEND = email_settings.email_backend
        settings.EMAIL_HOST = email_settings.smtp_host
        settings.EMAIL_PORT = email_settings.smtp_port
        settings.EMAIL_USE_TLS = email_settings.use_tls
        settings.EMAIL_USE_SSL = email_settings.use_ssl
        settings.EMAIL_HOST_USER = email_settings.smtp_username
        settings.EMAIL_HOST_PASSWORD = email_settings.smtp_password
        settings.DEFAULT_FROM_EMAIL = email_settings.from_email

        # Send HTML email to site administrator
        admin_email = EmailMultiAlternatives(
            subject=subject,
            body=text_body,
            from_email=email_settings.from_email,
            to=[email_settings.contact_form_recipient],
        )
        admin_email.attach_alternative(html_body, "text/html")
        admin_email.send(fail_silently=False)

        # Send confirmation email to the user if enabled
        if email_settings.send_confirmation_email:
            confirmation_subject = '✅ Thank you for contacting Qualitation'

            # HTML confirmation email
            confirmation_html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
            </head>
            <body style="margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; background-color: #f5f5f5;">
                <table width="100%" cellpadding="0" cellspacing="0" style="background-color: #f5f5f5; padding: 40px 20px;">
                    <tr>
                        <td align="center">
                            <table width="600" cellpadding="0" cellspacing="0" style="background-color: #ffffff; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.1);">
                                <!-- Header -->
                                <tr>
                                    <td style="background: linear-gradient(135deg, #10b981 0%, #059669 100%); padding: 40px 30px; text-align: center;">
                                        <div style="font-size: 48px; margin-bottom: 10px;">✅</div>
                                        <h1 style="margin: 0; color: #ffffff; font-size: 28px; font-weight: 700;">Message Received!</h1>
                                        <p style="margin: 10px 0 0; color: rgba(255,255,255,0.95); font-size: 16px;">We'll be in touch soon</p>
                                    </td>
                                </tr>

                                <!-- Content -->
                                <tr>
                                    <td style="padding: 40px 30px;">
                                        <p style="margin: 0 0 20px; color: #1e293b; font-size: 16px; line-height: 1.7;">
                                            Dear <strong>{name}</strong>,
                                        </p>

                                        <p style="margin: 0 0 20px; color: #475569; font-size: 15px; line-height: 1.7;">
                                            Thank you for reaching out to <strong style="color: #2563eb;">Qualitation</strong>! We've received your message and one of our team members will get back to you as soon as possible, typically within 24 hours.
                                        </p>

                                        <!-- Message Copy -->
                                        <div style="background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%); border-left: 4px solid #2563eb; border-radius: 8px; padding: 20px; margin: 25px 0;">
                                            <h3 style="margin: 0 0 12px; color: #1e40af; font-size: 16px; font-weight: 600;">📝 Your Message:</h3>
                                            <p style="margin: 0; color: #334155; font-size: 14px; line-height: 1.6; white-space: pre-wrap;">{message if message else 'No message provided'}</p>
                                        </div>

                                        <p style="margin: 25px 0 0; color: #475569; font-size: 15px; line-height: 1.7;">
                                            In the meantime, feel free to explore our <a href="https://yourwebsite.com" style="color: #2563eb; text-decoration: none; font-weight: 600;">ISO certification services</a> or check out our <a href="https://yourwebsite.com/resources" style="color: #2563eb; text-decoration: none; font-weight: 600;">resources</a>.
                                        </p>

                                        <!-- Contact Info -->
                                        <div style="background-color: #f8fafc; border-radius: 8px; padding: 20px; margin-top: 30px; text-align: center;">
                                            <p style="margin: 0 0 8px; color: #64748b; font-size: 13px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px;">Need immediate assistance?</p>
                                            <p style="margin: 0; color: #1e293b; font-size: 15px;">
                                                📞 <strong>03456006975</strong><br>
                                                📧 <a href="mailto:{email_settings.from_email}" style="color: #2563eb; text-decoration: none; font-weight: 600;">{email_settings.from_email}</a>
                                            </p>
                                        </div>
                                    </td>
                                </tr>

                                <!-- Footer -->
                                <tr>
                                    <td style="background-color: #1e293b; padding: 30px; text-align: center;">
                                        <p style="margin: 0 0 15px; color: #ffffff; font-size: 18px; font-weight: 600;">
                                            Qualitation
                                        </p>
                                        <p style="margin: 0; color: #94a3b8; font-size: 13px; line-height: 1.6;">
                                            Your trusted partner in ISO certification and quality management<br>
                                            <span style="color: #64748b;">© 2026 Qualitation. All rights reserved.</span>
                                        </p>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                </table>
            </body>
            </html>
            """

            # Plain text fallback for confirmation
            confirmation_text = f"""
Dear {name},

Thank you for reaching out to Qualitation!

We've received your message and one of our team members will get back to you as soon as possible, typically within 24 hours.

YOUR MESSAGE:
{message if message else 'No message provided'}

Need immediate assistance?
Phone: 03456006975
Email: {email_settings.from_email}

Best regards,
The Qualitation Team

---
Qualitation - Your trusted partner in ISO certification
            """

            # Send HTML confirmation email
            user_email = EmailMultiAlternatives(
                subject=confirmation_subject,
                body=confirmation_text,
                from_email=email_settings.from_email,
                to=[email],
            )
            user_email.attach_alternative(confirmation_html, "text/html")
            user_email.send(fail_silently=True)  # Don't fail if confirmation email fails

        # Restore old settings
        if old_backend: settings.EMAIL_BACKEND = old_backend
        if old_host: settings.EMAIL_HOST = old_host
        if old_port: settings.EMAIL_PORT = old_port
        if old_use_tls is not None: settings.EMAIL_USE_TLS = old_use_tls
        if old_use_ssl is not None: settings.EMAIL_USE_SSL = old_use_ssl
        if old_user: settings.EMAIL_HOST_USER = old_user
        if old_password: settings.EMAIL_HOST_PASSWORD = old_password
        if old_from: settings.DEFAULT_FROM_EMAIL = old_from

        messages.success(request, 'Thank you! Your message has been sent successfully.')
        logger.info(f'Contact form submitted by {name} ({email})')

    except Exception as e:
        logger.error(f'Error sending contact form email: {str(e)}')
        messages.error(request, 'Sorry, there was an error sending your message. Please try again later.')

    # Redirect back to the referring page
    return redirect(request.META.get('HTTP_REFERER', '/'))
