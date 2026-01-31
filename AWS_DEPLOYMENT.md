# AWS Deployment Guide - Fix CSRF Error

## Quick Fix for CSRF Error

The CSRF error is happening because your production settings need to know your AWS domain. Follow these steps:

### Step 1: Set Environment Variables on AWS

You need to set these environment variables on your AWS server:

```bash
# Replace with your actual domain
export CSRF_TRUSTED_ORIGINS="https://yourdomain.com,http://yourdomain.com"
export ALLOWED_HOSTS="yourdomain.com,www.yourdomain.com"
export WAGTAILADMIN_BASE_URL="https://yourdomain.com"
```

**For AWS Elastic Beanstalk:**
1. Go to AWS Console → Elastic Beanstalk → Your environment
2. Click "Configuration" → "Software" → "Edit"
3. Under "Environment properties", add:
   - `CSRF_TRUSTED_ORIGINS` = `https://yourdomain.com,http://yourdomain.com`
   - `ALLOWED_HOSTS` = `yourdomain.com,*.elasticbeanstalk.com`
   - `WAGTAILADMIN_BASE_URL` = `https://yourdomain.com`

**For AWS EC2 (manual setup):**
1. SSH into your server
2. Edit your environment file (usually `/etc/environment` or in your virtualenv)
3. Add the exports shown above
4. Restart your web server

### Step 2: Pull Latest Code on AWS Server

SSH into your AWS server and run:

```bash
cd /path/to/qualitation
git pull origin main
```

### Step 3: Collect Static Files

```bash
python3 manage.py collectstatic --noinput
```

### Step 4: Run Migrations (if needed)

```bash
python3 manage.py migrate
```

### Step 5: Restart Your Web Server

**If using Gunicorn:**
```bash
sudo systemctl restart gunicorn
```

**If using Gunicorn with Nginx:**
```bash
sudo systemctl restart gunicorn
sudo systemctl restart nginx
```

**If using Elastic Beanstalk:**
- The environment will restart automatically after updating configuration

### Step 6: Test the Contact Form

1. Visit your website: `https://yourdomain.com/contact`
2. Fill out the contact form
3. Submit - the CSRF error should be gone!

---

## Alternative: Temporary Fix (If You Don't Know Your Domain)

If you're still setting up and don't have a domain yet, you can temporarily use your AWS public IP or Elastic Beanstalk URL:

1. Find your AWS public URL (e.g., `http://ec2-xx-xx-xx-xx.compute-1.amazonaws.com` or `http://yourapp.elasticbeanstalk.com`)

2. SSH into server and set:
```bash
export CSRF_TRUSTED_ORIGINS="http://ec2-xx-xx-xx-xx.compute-1.amazonaws.com"
export ALLOWED_HOSTS="*"
```

3. Restart web server

---

## Common Issues

### Issue: "ALLOWED_HOSTS" error
**Solution:** Make sure ALLOWED_HOSTS environment variable includes your domain

### Issue: Still getting CSRF error
**Solution:**
1. Check that environment variables are actually set: `echo $CSRF_TRUSTED_ORIGINS`
2. Make sure you restarted the web server after setting them
3. Clear browser cookies and try again

### Issue: 403 Forbidden on admin
**Solution:** Add your domain to both ALLOWED_HOSTS and CSRF_TRUSTED_ORIGINS

---

## Settings File Priority

Django loads settings in this order:
1. `base.py` (base settings)
2. `production.py` (production overrides)
3. `local.py` (optional local overrides - not on server)

Make sure you're using the production settings on AWS:
```bash
export DJANGO_SETTINGS_MODULE=mysite.settings.production
```

---

## Need Help?

If you're still getting CSRF errors, provide:
1. Your AWS domain/URL
2. Output of: `echo $CSRF_TRUSTED_ORIGINS`
3. The exact error message from browser
