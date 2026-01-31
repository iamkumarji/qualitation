# Admin Panel Email Setup Guide

Now you can configure email settings directly from the Wagtail admin panel - no need to edit config files!

## Quick Start

### 1. Access Email Settings

1. **Start your server** (if not already running):
   ```bash
   python3 manage.py runserver
   ```

2. **Log into Wagtail Admin**:
   - Go to: http://localhost:8000/admin/
   - Login with your admin credentials

3. **Navigate to Email Settings**:
   - In the left sidebar, click **Settings**
   - Click on **Email Settings**

### 2. Configure SMTP Settings

#### For Yahoo Business:

Fill in these fields:

**📧 SMTP Server Settings:**
- **SMTP Host**: `smtp.mail.yahoo.com`
- **SMTP Port**: `587`
- **Use TLS**: ✅ Checked
- **Use SSL**: ☐ Unchecked

**🔐 Authentication:**
- **SMTP Username / Email**: `yourname@yourdomain.com`
- **SMTP Password / App Password**: `xxxx xxxx xxxx xxxx` (16-character app password)

**✉️ Email Addresses:**
- **From Email**: `yourname@yourdomain.com`
- **Contact Form Recipient**: `yourname@yourdomain.com` (where you'll receive submissions)

**⚙️ Options:**
- **Send Confirmation to User**: ✅ Checked (sends thank you email to form submitters)

### 3. Get Yahoo App Password

If you don't have an app password yet:

1. Go to https://login.yahoo.com
2. Click your profile → Account Info → Security
3. Click "Generate app password"
4. Select "Other App" and name it "Django Website"
5. Copy the 16-character password (format: `xxxx xxxx xxxx xxxx`)
6. Paste it in the **SMTP Password** field

### 4. Test Your Configuration

**🧪 Test Configuration Section:**
- Enter your email in **Test Email Address**: `youremail@example.com`
- Click **Save**
- Check your inbox for a test email

If successful, you'll receive:
```
✅ Email Configuration Test - Success!

Your email settings are configured correctly!
```

### 5. Verify Contact Form

1. Go to any page with a contact form (e.g., http://localhost:8000/contact/)
2. Fill out the form
3. Submit it
4. You should receive:
   - Admin notification at your **Contact Form Recipient** email
   - User confirmation email (if enabled)

## Alternative Email Providers

### Gmail

**SMTP Settings:**
- **Host**: `smtp.gmail.com`
- **Port**: `587`
- **TLS**: ✅ Enabled
- **SSL**: ☐ Disabled

**App Password:**
1. Go to https://myaccount.google.com/security
2. Enable 2-Step Verification
3. Go to "App passwords"
4. Generate password for "Mail"
5. Use the 16-character password

### SendGrid

**SMTP Settings:**
- **Host**: `smtp.sendgrid.net`
- **Port**: `587`
- **TLS**: ✅ Enabled
- **Username**: `apikey` (literally the word "apikey")
- **Password**: Your SendGrid API key

### Office 365 / Outlook

**SMTP Settings:**
- **Host**: `smtp.office365.com`
- **Port**: `587`
- **TLS**: ✅ Enabled

### Mailgun

**SMTP Settings:**
- **Host**: `smtp.mailgun.org`
- **Port**: `587`
- **TLS**: ✅ Enabled
- **Username**: Your Mailgun SMTP username
- **Password**: Your Mailgun SMTP password

## Features

### What the Admin Panel Does

✅ **Easy Configuration**: No code editing required
✅ **Built-in Test**: Test emails before going live
✅ **Secure Storage**: Credentials stored in database
✅ **Visual Status**: Shows if email is configured correctly
✅ **Last Test Date**: Track when you last tested
✅ **Confirmation Emails**: Toggle user confirmations on/off

### Field Descriptions

| Field | Purpose | Example |
|-------|---------|---------|
| **SMTP Host** | Your email provider's server | `smtp.mail.yahoo.com` |
| **SMTP Port** | Connection port | `587` (TLS) or `465` (SSL) |
| **Use TLS** | Encryption for port 587 | ✅ Recommended |
| **Use SSL** | Encryption for port 465 | ☐ Usually unchecked |
| **SMTP Username** | Your email login | `you@yourdomain.com` |
| **SMTP Password** | App-specific password | `xxxx xxxx xxxx xxxx` |
| **From Email** | Sender address on emails | `noreply@yourdomain.com` |
| **Contact Form Recipient** | Where submissions go | `info@yourdomain.com` |
| **Send Confirmation** | Thank user after submission | ✅ Recommended |
| **Test Email** | Test configuration | `test@example.com` |

## Troubleshooting

### ⚠️ "Email is not configured" error

**Problem**: Required fields are missing

**Solution**:
1. Go to Settings → Email Settings
2. Fill in ALL required fields:
   - SMTP Host
   - SMTP Username
   - SMTP Password
   - From Email
   - Contact Form Recipient
3. Click Save

### ❌ Test email fails

**Check these:**
- ✅ App password (not regular password) for Yahoo/Gmail
- ✅ Port number matches encryption (587=TLS, 465=SSL)
- ✅ Username is your full email address
- ✅ No typos in email addresses
- ✅ Firewall allows outbound SMTP connections

### 🔍 Check if configured correctly

In the Email Settings page, look for:
- Status: **✅ Configured** (top of page)
- **Last Tested** date should be recent

### 📧 Test emails arrive but contact form doesn't work

1. Check server logs for errors
2. Verify **Contact Form Recipient** is correct
3. Check spam/junk folder
4. Test with a different email address

## Security Notes

### ✅ Best Practices

1. **Use App Passwords**: Never use your main account password
2. **Separate Accounts**: Use a dedicated email for sending (e.g., `noreply@`)
3. **Monitor**: Regularly check the recipient inbox
4. **Backups**: Keep SMTP credentials in a secure password manager

### 🔒 What's Stored

Email settings are stored in your database:
- Credentials are in plain text in DB (consider encryption for production)
- Only admins can access via Wagtail admin panel
- Not exposed to front-end users

### 🚀 Production Recommendations

For production sites, consider:
1. **Environment Variables**: Store credentials outside database
2. **Transactional Email Services**: SendGrid, Mailgun, AWS SES
3. **Rate Limiting**: Prevent spam abuse
4. **Email Validation**: Verify email addresses
5. **Queue System**: Use Celery for async email sending

## Advantages Over Config Files

| Feature | Config Files | Admin Panel |
|---------|-------------|-------------|
| Edit Settings | ❌ Need file access | ✅ Via web UI |
| Test Email | ❌ Manual testing | ✅ Built-in tester |
| Non-technical | ❌ Requires dev | ✅ Anyone can do |
| Visual Status | ❌ No feedback | ✅ Shows status |
| Quick Changes | ❌ Edit + restart | ✅ Save & done |
| Multiple Sites | ❌ One config | ✅ Per-site settings |

## Support

If you need help:
1. Check the **Last Tested** date - if recent, settings are correct
2. Send a test email - if it arrives, everything works
3. Check Django/Wagtail logs for detailed errors
4. Review your email provider's SMTP documentation

## Next Steps

Once configured:
- ✅ All contact form submissions will email you automatically
- ✅ Users receive confirmation emails
- ✅ No more config file editing needed
- ✅ Change settings anytime via admin panel

Happy emailing! 📧
