# Django Portfolio App

A modern, tag-filterable portfolio web application built with Django. Features project showcase, contact form, tag-based filtering, and is ready for deployment on AWS Elastic Beanstalk.

## Features
- Responsive, clean UI with custom CSS
- Project gallery with images and tag filtering (interactive, JavaScript-powered)
- Project detail pages
- Contact form with email notifications
- Admin interface for managing projects, tags, and messages
- Static and media file handling (local and production)
- AWS Elastic Beanstalk deployment ready (with collectstatic automation)

## Local Development

### Prerequisites
- Python 3.8+
- pip
- (Recommended) Virtual environment

### Setup
```bash
# Clone the repository
git clone <your-repo-url>
cd django_portfolio

# Create and activate a virtual environment
python3 -m venv env
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create a superuser (for admin access)
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```

### Static & Media Files
- Static files: `main/static/`, collected to `staticfiles/` on deployment
- Media files (uploads): `media/`

## Deployment: AWS Elastic Beanstalk

### Prerequisites
- AWS CLI & EB CLI installed and configured
- AWS account and Elastic Beanstalk environment

### Steps
1. Set environment variables in Elastic Beanstalk:
   - `DEBUG=False`
   - `SECRET_KEY=<your-secret-key>`
   - `DATABASE_URL=<your-production-db-url>`
2. Ensure `.ebextensions/01_collectstatic.config` exists to automate static file collection.
3. Deploy:
   ```bash
   eb init
   eb deploy
   ```
4. Visit your Elastic Beanstalk environment URL.

## Project Structure
- `main/` – Django app (models, views, templates, static)
- `django_portfolio/` – Project settings and URLs
- `.ebextensions/` – AWS deployment configs
- `staticfiles/` – Collected static files (auto-generated)
- `media/` – Uploaded media files

## Customization
- Add/edit projects and tags via Django admin
- Update styles in `main/static/css/`
- Update JavaScript for filtering in `main/static/js/home.js`

## Troubleshooting
- If static files are missing in production, check AWS logs and ensure `collectstatic` runs (see `.ebextensions/01_collectstatic.config`).
- For database issues, verify `DATABASE_URL` is set correctly in environment variables.

## License
MIT License

---

**Author:** [Your Name]
