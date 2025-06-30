# Email Setup Guide for Contact Form

## Overview
Your Django portfolio now sends email notifications when someone submits the contact form. Currently configured for development (console output), but can be easily set up for production.

## Current Setup (Development)

### What's Working Now
- ✅ Contact form saves messages to database
- ✅ Email notifications are sent (printed to console)
- ✅ Confirmation emails sent to form submitters
- ✅ HTML email templates with professional formatting
- ✅ Error handling (form still works if email fails)

### Testing Email in Development
1. Run the server: `python manage.py runserver`
2. Submit a contact form at `http://127.0.0.1:8000/contact/`
3. Check your terminal/console for email output

## Production Email Setup

### Option 1: Gmail SMTP (Recommended for beginners)

1. **Enable 2-Factor Authentication** on your Gmail account
2. **Generate an App Password:**
   - Go to Google Account settings
   - Security → 2-Step Verification → App passwords
   - Generate a password for "Mail"
3. **Update settings.py:**

```python
# Email Configuration for Production
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-16-character-app-password'

# Contact form email settings
CONTACT_EMAIL = 'xia.summer.huang@gmail.com'
```

### Option 2: SendGrid (Recommended for production)

1. **Sign up for SendGrid** (free tier: 100 emails/day)
2. **Create an API key** in SendGrid dashboard
3. **Install SendGrid:** `pip install sendgrid`
4. **Update settings.py:**

```python
# Email Configuration for Production
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'apikey'  # Always 'apikey' for SendGrid
EMAIL_HOST_PASSWORD = 'your-sendgrid-api-key'

# Contact form email settings
CONTACT_EMAIL = 'xia.summer.huang@gmail.com'
```

### Option 3: Mailgun (Alternative)

1. **Sign up for Mailgun** (free tier: 5,000 emails/month)
2. **Get your SMTP credentials** from Mailgun dashboard
3. **Update settings.py:**

```python
# Email Configuration for Production
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-mailgun-username'
EMAIL_HOST_PASSWORD = 'your-mailgun-password'

# Contact form email settings
CONTACT_EMAIL = 'xia.summer.huang@gmail.com'
```

## Environment Variables (Recommended)

For security, use environment variables instead of hardcoding credentials:

1. **Install python-decouple:** `pip install python-decouple`
2. **Create .env file** in your project root:

```env
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
CONTACT_EMAIL=xia.summer.huang@gmail.com
```

3. **Update settings.py:**

```python
from decouple import config

# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # or your provider's SMTP
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

# Contact form email settings
CONTACT_EMAIL = config('CONTACT_EMAIL')
```

## Email Features

### What Gets Sent
1. **Admin Notification Email** (to you):
   - Sender's name, email, subject, and message
   - Timestamp of submission
   - Professional HTML formatting
   - Reply-to set to sender's email

2. **Confirmation Email** (to sender):
   - Thank you message
   - Copy of their original message
   - Professional HTML formatting

### Email Templates
- **Location:** `main/templates/emails/`
- **Files:**
  - `contact_notification.html` - Admin notification
  - `contact_confirmation.html` - Sender confirmation
- **Styling:** Matches your portfolio theme (orange/black)

## Troubleshooting

### Common Issues

1. **"Authentication failed"**
   - Check your email/password
   - For Gmail: Use app password, not regular password
   - Enable "Less secure app access" (not recommended)

2. **"Connection refused"**
   - Check EMAIL_HOST and EMAIL_PORT
   - Verify firewall settings
   - Try different port (465 for SSL, 587 for TLS)

3. **"Email not received"**
   - Check spam folder
   - Verify CONTACT_EMAIL setting
   - Test with a different email address

### Testing Email Setup

1. **Test in Django shell:**
```bash
python manage.py shell
```

```python
from django.core.mail import send_mail
send_mail(
    'Test Email',
    'This is a test email from your Django app.',
    'your-email@gmail.com',
    ['your-email@gmail.com'],
    fail_silently=False,
)
```

2. **Check email logs** in your email provider's dashboard

## Security Best Practices

1. **Never commit credentials** to version control
2. **Use environment variables** for sensitive data
3. **Use app passwords** instead of regular passwords
4. **Enable 2FA** on your email account
5. **Regularly rotate** API keys and passwords

## Deployment Considerations

### For AWS Elastic Beanstalk
- Set environment variables in EB console
- Use IAM roles for email permissions
- Consider using AWS SES for email

### For Heroku
- Use Heroku config vars for environment variables
- Consider using SendGrid add-on

### For VPS/Dedicated Server
- Configure local mail server (Postfix)
- Or use external SMTP service
- Set up proper DNS records (SPF, DKIM)

## Next Steps

1. **Choose an email provider** (Gmail recommended for testing)
2. **Update settings.py** with your credentials
3. **Test the contact form** with real email sending
4. **Monitor email delivery** and adjust as needed
5. **Consider adding email analytics** for better insights 