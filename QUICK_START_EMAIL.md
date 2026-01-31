# Quick Start: Email Setup in 3 Minutes ⚡

## Step 1: Get Yahoo App Password (2 min)

1. Go to https://login.yahoo.com
2. Account Info → Security → Generate app password
3. Name it "Django Website"
4. Copy the password: `xxxx xxxx xxxx xxxx`

## Step 2: Configure in Admin Panel (1 min)

1. Go to http://localhost:8000/admin/
2. Click **Settings** → **Email Settings**
3. Fill in:

```
SMTP Host: smtp.mail.yahoo.com
SMTP Port: 587
Use TLS: ✅
SMTP Username: your-email@yourdomain.com
SMTP Password: xxxx xxxx xxxx xxxx (paste app password)
From Email: your-email@yourdomain.com
Contact Form Recipient: your-email@yourdomain.com
Send Confirmation: ✅
Test Email: your-email@example.com
```

4. Click **Save**

## Step 3: Done! ✅

- Check your email for test message
- Contact form now works automatically
- Change settings anytime via admin panel

---

## Other Providers Quick Config

### Gmail
```
Host: smtp.gmail.com
Port: 587
TLS: ✅
Get app password: https://myaccount.google.com/apppasswords
```

### SendGrid
```
Host: smtp.sendgrid.net
Port: 587
TLS: ✅
Username: apikey
Password: [Your API Key]
```

### Office 365
```
Host: smtp.office365.com
Port: 587
TLS: ✅
```

---

That's it! No config files, no code changes needed. 🎉
