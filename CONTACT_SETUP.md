# Contact Page Setup Guide

## Overview
Your Django portfolio now has a comprehensive contact page with:
- Contact information display
- Contact form with validation
- Database storage for messages
- Admin interface for managing messages

## Customizing Contact Information

### 1. Update Contact Details
Edit the contact information in `main/templates/contact.html`:

```html
<!-- Replace these placeholder values with your actual information -->
<p><a href="mailto:your.email@example.com">your.email@example.com</a></p>
<p><a href="tel:+1234567890">+1 (234) 567-890</a></p>
<p>San Francisco, CA</p>
<p><a href="https://linkedin.com/in/yourprofile" target="_blank">linkedin.com/in/yourprofile</a></p>
<p><a href="https://github.com/yourusername" target="_blank">github.com/yourusername</a></p>
```

### 2. Update Availability Message
Modify the availability section in `main/templates/contact.html`:

```html
<div class="availability-section">
    <h3>Availability</h3>
    <p>I'm currently available for freelance opportunities and full-time positions. I typically respond to messages within 24 hours.</p>
</div>
```

### 3. Customize Form Fields
You can add or remove form fields by editing the form section in `main/templates/contact.html` and updating the corresponding view logic in `main/views.py`.

## Features

### Contact Form
- **Name** (required)
- **Email** (required)
- **Subject** (optional)
- **Message** (required)
- Form validation with error messages
- Success confirmation messages

### Database Storage
- All contact messages are stored in the database
- Access messages through Django admin at `/admin/`
- Mark messages as read/unread
- Search and filter messages

### Admin Interface
- View all contact messages
- Mark messages as read/unread
- Search by name, email, subject, or message content
- Filter by read status and date
- Bulk actions for managing multiple messages

## Running the Application

1. **Activate virtual environment:**
   ```bash
   source env/bin/activate
   ```

2. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

3. **Access the contact page:**
   - Visit `http://127.0.0.1:8000/contact/`
   - Or click the "Contact" link in the navigation

4. **Access admin interface:**
   - Visit `http://127.0.0.1:8000/admin/`
   - Create a superuser if you haven't already: `python manage.py createsuperuser`

## Styling Customization

The contact page uses `main/static/css/contact.css` for styling. You can customize:
- Colors and themes
- Layout and spacing
- Responsive design
- Animations and hover effects

## Future Enhancements

Consider adding these features:
- Email notifications when new messages are received
- CAPTCHA protection for spam prevention
- File upload capabilities
- Contact form analytics
- Integration with email services (SendGrid, Mailgun, etc.) 