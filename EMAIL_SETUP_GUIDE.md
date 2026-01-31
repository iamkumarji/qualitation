# Email Setup Guide - Yahoo Business SMTP

This guide will help you configure the contact form to send emails using Yahoo Business SMTP.

## Prerequisites

- Yahoo Business email account
- Access to Yahoo account security settings

## Step 1: Generate Yahoo App-Specific Password

Yahoo requires app-specific passwords for third-party applications. Follow these steps:

1. **Log in to your Yahoo Account**: Go to https://login.yahoo.com
2. **Go to Account Security**: Navigate to Account Info → Security
3. **Generate App Password**:
   - Click on "Generate app password" or "Manage app passwords"
   - Select "Other App" from the dropdown
   - Enter a name like "Django Contact Form"
   - Click "Generate"
   - **IMPORTANT**: Copy the generated password immediately (you won't be able to see it again)

## Step 2: Configure Email Settings

1. **Open the local settings file**:
   ```
   mysite/settings/local.py
   ```

2. **Update the following settings with your Yahoo Business credentials**:

   ```python
   # Replace with your actual Yahoo Business email
   EMAIL_HOST_USER = 'yourname@yourdomain.com'

   # Replace with the app-specific password you generated
   EMAIL_HOST_PASSWORD = 'abcd efgh ijkl mnop'  # 16-character app password

   # This is the "From" address in emails
   DEFAULT_FROM_EMAIL = 'yourname@yourdomain.com'

   # Where contact form submissions will be sent
   CONTACT_FORM_EMAIL = 'yourname@yourdomain.com'
   ```

## Step 3: Yahoo Business SMTP Settings (Already Configured)

The following settings are already configured in `local.py`:

- **SMTP Server**: smtp.mail.yahoo.com
- **Port**: 587
- **Encryption**: TLS
- **Authentication**: Required

## Step 4: Test the Configuration

### Method 1: Test via Django Shell

```bash
python3 manage.py shell
```

Then run:

```python
from django.core.mail import send_mail

send_mail(
    'Test Email',
    'This is a test email from Django.',
    'yourname@yourdomain.com',  # From email
    ['recipient@example.com'],   # To email
    fail_silently=False,
)
```

### Method 2: Test via Contact Form

1. Start the development server:
   ```bash
   python3 manage.py runserver
   ```

2. Navigate to any page with a contact form (e.g., http://localhost:8000/contact/)

3. Fill out and submit the form

4. Check your email inbox for:
   - Admin notification email (sent to CONTACT_FORM_EMAIL)
   - User confirmation email (sent to the email they provided)

## Step 5: Security Best Practices

1. **Never commit `local.py` to version control**
   - It's already in `.gitignore` by default
   - Contains sensitive credentials

2. **Use environment variables for production**:
   ```python
   import os
   EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
   EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
   ```

3. **Enable logging** to monitor email sending:
   ```python
   LOGGING = {
       'version': 1,
       'handlers': {
           'file': {
               'level': 'INFO',
               'class': 'logging.FileHandler',
               'filename': 'email.log',
           },
       },
       'loggers': {
           'django.core.mail': {
               'handlers': ['file'],
               'level': 'INFO',
           },
       },
   }
   ```

## Troubleshooting

### Error: "SMTPAuthenticationError"
- **Solution**: Make sure you're using an app-specific password, not your regular Yahoo password
- Verify the email address and password are correct
- Check if Yahoo has blocked the login attempt (check your email for security alerts)

### Error: "SMTPServerDisconnected"
- **Solution**: Verify the SMTP settings (host, port, TLS)
- Try using port 465 with SSL instead:
  ```python
  EMAIL_PORT = 465
  EMAIL_USE_TLS = False
  EMAIL_USE_SSL = True
  ```

### Error: "Connection refused"
- **Solution**: Check your firewall settings
- Ensure your network allows outbound connections on port 587

### Emails not arriving
- Check spam/junk folder
- Verify CONTACT_FORM_EMAIL is correct
- Check server logs for errors:
  ```bash
  tail -f email.log
  ```

### For Development Testing
If you want to test without sending real emails, use the console backend in `local.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

This will print emails to the console instead of sending them.

## Alternative SMTP Providers

If Yahoo doesn't work, you can also use:

### Gmail
```python
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
```

### SendGrid
```python
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = 'your-sendgrid-api-key'
```

### Mailgun
```python
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
```

## Contact Form Features

The current implementation includes:

1. **Admin notification**: You receive an email with all form details
2. **User confirmation**: Submitter receives a thank you email
3. **Form validation**: Name and email are required
4. **Success/Error messages**: User sees feedback after submission
5. **CSRF protection**: Form is protected against cross-site attacks

## Need Help?

If you encounter issues, check:
1. Django logs in the console
2. Yahoo security settings
3. Network/firewall settings
4. Email delivery logs

For production deployment, consider using a transactional email service like SendGrid, Mailgun, or Amazon SES for better deliverability.
