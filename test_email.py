#!/usr/bin/env python
"""
Test script for email functionality
"""
import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_portfolio.settings')
django.setup()

from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

def test_simple_email():
    """Test basic email sending"""
    print("Testing simple email...")
    try:
        send_mail(
            subject='Test Email from Django Portfolio',
            message='This is a test email to verify email functionality is working.',
            from_email=settings.CONTACT_EMAIL,
            recipient_list=[settings.CONTACT_EMAIL],
            fail_silently=False,
        )
        print("✅ Simple email test PASSED")
        return True
    except Exception as e:
        print(f"❌ Simple email test FAILED: {e}")
        return False

def test_html_email():
    """Test HTML email with template"""
    print("\nTesting HTML email with template...")
    try:
        # Test context for email template
        context = {
            'name': 'Test User',
            'email': 'test@example.com',
            'subject': 'Test Subject',
            'message': 'This is a test message to verify HTML email templates are working.',
            'timestamp': '2025-06-26 20:30:00'
        }
        
        # Render HTML template
        html_content = render_to_string('emails/contact_notification.html', context)
        
        # Send HTML email
        email = EmailMessage(
            subject='Test HTML Email from Django Portfolio',
            body=html_content,
            from_email=settings.CONTACT_EMAIL,
            to=[settings.CONTACT_EMAIL]
        )
        email.content_subtype = "html"
        email.send()
        
        print("✅ HTML email test PASSED")
        return True
    except Exception as e:
        print(f"❌ HTML email test FAILED: {e}")
        return False

def test_email_settings():
    """Test email configuration"""
    print("\nChecking email settings...")
    print(f"EMAIL_BACKEND: {settings.EMAIL_BACKEND}")
    print(f"EMAIL_HOST: {settings.EMAIL_HOST}")
    print(f"EMAIL_PORT: {settings.EMAIL_PORT}")
    print(f"EMAIL_USE_TLS: {settings.EMAIL_USE_TLS}")
    print(f"EMAIL_HOST_USER: {settings.EMAIL_HOST_USER}")
    print(f"EMAIL_HOST_PASSWORD: {'*' * len(settings.EMAIL_HOST_PASSWORD) if settings.EMAIL_HOST_PASSWORD else 'Not set'}")
    print(f"CONTACT_EMAIL: {settings.CONTACT_EMAIL}")

def main():
    """Run all email tests"""
    print("🧪 Email Functionality Test")
    print("=" * 50)
    
    # Check settings
    test_email_settings()
    
    # Test simple email
    simple_result = test_simple_email()
    
    # Test HTML email
    html_result = test_html_email()
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 Test Results Summary:")
    print(f"Simple Email: {'✅ PASSED' if simple_result else '❌ FAILED'}")
    print(f"HTML Email: {'✅ PASSED' if html_result else '❌ FAILED'}")
    
    if simple_result and html_result:
        print("\n🎉 All email tests passed! Your email configuration is working.")
    else:
        print("\n⚠️  Some tests failed. Check your email configuration.")
        print("\n💡 Troubleshooting tips:")
        print("1. Make sure you've set the correct EMAIL_HOST_PASSWORD")
        print("2. For Gmail: Enable 'Less secure app access' or use app password")
        print("3. For SendGrid: Make sure your API key is correct")
        print("4. Check your internet connection")

if __name__ == "__main__":
    main() 