from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.utils import timezone
from .models import Project, Tag, ProjectImage, ContactMessage
# Create your views here.
def home(request):
    projects = Project.objects.all()
    tags = Tag.objects.all()
    image = ProjectImage.objects.all()
    context = {
        'projects': projects,
        'tags': tags,
        'image': image,
    }
    
    return render(request, 'home.html', context)

def contact(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()
        
        # Basic validation
        if not name or not email or not message:
            messages.error(request, 'Please fill in all required fields.')
            return render(request, 'contact.html', {
                'form_data': {
                    'name': name,
                    'email': email,
                    'subject': subject,
                    'message': message
                }
            })
        
        # Save the contact message to database
        try:
            contact_message = ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            
            # Send email notification
            try:
                # Prepare email content for admin notification
                email_subject = f"New Contact Form Message: {subject}" if subject else "New Contact Form Message"
                
                # Render HTML email template for admin notification
                admin_email_context = {
                    'name': name,
                    'email': email,
                    'subject': subject,
                    'message': message,
                    'timestamp': timezone.now().strftime('%Y-%m-%d %H:%M:%S')
                }
                
                admin_email_html = render_to_string('emails/contact_notification.html', admin_email_context)
                admin_email_text = f"""
New contact form submission received:

Name: {name}
Email: {email}
Subject: {subject if subject else 'No subject provided'}
Message:
{message}

Time: {admin_email_context['timestamp']}
---
This message was sent from your portfolio contact form.
                """.strip()
                
                # Send HTML email to admin
                admin_email = EmailMessage(
                    subject=email_subject,
                    body=admin_email_html,
                    from_email=settings.CONTACT_EMAIL,
                    to=[settings.CONTACT_EMAIL],
                    reply_to=[email]
                )
                admin_email.content_subtype = "html"
                admin_email.send()
                
                # Send confirmation email to the person who submitted the form
                confirmation_subject = "Thank you for your message"
                
                # Render HTML email template for confirmation
                confirmation_context = {
                    'name': name,
                    'message': message
                }
                
                confirmation_email_html = render_to_string('emails/contact_confirmation.html', confirmation_context)
                confirmation_email_text = f"""
Dear {name},

Thank you for reaching out! I've received your message and will get back to you as soon as possible.

Your message:
{message}

Best regards,
Your Portfolio
                """.strip()
                
                confirmation_email = EmailMessage(
                    subject=confirmation_subject,
                    body=confirmation_email_html,
                    from_email=settings.CONTACT_EMAIL,
                    to=[email]
                )
                confirmation_email.content_subtype = "html"
                confirmation_email.send(fail_silently=True)  # Don't fail if confirmation email fails
                
            except Exception as email_error:
                # Log email error but don't fail the form submission
                print(f"Email sending failed: {email_error}")
            
            messages.success(request, f'Thank you for your message, {name}! I\'ll get back to you soon.')
            
        except Exception as e:
            messages.error(request, 'Sorry, there was an error sending your message. Please try again.')
            return render(request, 'contact.html', {
                'form_data': {
                    'name': name,
                    'email': email,
                    'subject': subject,
                    'message': message
                }
            })
        
        # Redirect to prevent form resubmission
        return HttpResponseRedirect(reverse('contact'))
    
    return render(request, 'contact.html')

