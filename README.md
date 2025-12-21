# Qualitation - ISO Certification Consultants

A modern, professional website for Qualitation (The British Quality Centre) built with Django and Wagtail CMS.

## Features

- **Wagtail CMS** - Full content management system with admin panel
- **Flexible Page Builder** - Drag-and-drop blocks for creating pages
- **Carousel/Slider** - Image and video slides with customizable transitions
- **Responsive Design** - Mobile-first, works on all devices
- **Custom Navigation** - Multi-level header and footer menus
- **Color Theme Settings** - Customize colors from admin panel
- **Docker Ready** - Production-ready containerization
- **Azure Compatible** - Ready for Azure Web App deployment

## Content Blocks

| Block | Description |
|-------|-------------|
| Carousel | Image/video slider with autoplay |
| Hero | Full-width hero section with CTA |
| Service Cards | Grid of service offerings |
| Testimonials | Client testimonial slider |
| Accordion/FAQ | Collapsible content sections |
| Image & Text | Side-by-side image and content |
| Contact Form | Contact form with styling options |
| Sitemap | Multi-column sitemap section |
| HTML/CSS/JS | Custom code blocks |

## Tech Stack

- Python 3.12
- Django 5.2
- Wagtail 7.1
- SQLite (development) / PostgreSQL (production)
- Gunicorn
- WhiteNoise (static files)
- Docker

## Quick Start

### Local Development

```bash
# Clone the repository
git clone https://github.com/iamkumarji/qualitation.git
cd qualitation

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

Visit:
- Website: http://localhost:8000
- Admin: http://localhost:8000/admin

### Docker

```bash
# Build image
docker build -t qualitation .

# Run container
docker run -p 8000:8000 qualitation
```

## Production Deployment

### Environment Variables

Set these in your production environment:

| Variable | Description | Example |
|----------|-------------|---------|
| `DJANGO_SECRET_KEY` | Secret key for Django | (random string) |
| `DJANGO_SETTINGS_MODULE` | Settings module | `mysite.settings.production` |
| `ALLOWED_HOSTS` | Comma-separated hosts | `qualitation.azurewebsites.net` |
| `CSRF_TRUSTED_ORIGINS` | Trusted origins for CSRF | `https://qualitation.azurewebsites.net` |

### Azure Web App

1. Create a Web App in Azure Portal
2. Set environment variables in Configuration
3. Deploy using one of:
   - GitHub Actions (connect repo in Deployment Center)
   - Docker container
   - Git push deployment

```bash
# Using Azure CLI
az webapp up --name your-app-name --resource-group your-rg --runtime "PYTHON:3.12"
```

## Project Structure

```
qualitation/
├── home/                   # Main app with page models
│   ├── models.py          # Page and block definitions
│   ├── templates/         # Page templates
│   └── management/        # Management commands
├── mysite/                 # Project configuration
│   ├── settings/          # Settings (base, dev, production)
│   ├── templates/         # Base templates and blocks
│   └── static/            # CSS, JS, images
├── media/                  # User uploads
├── static/                 # Collected static files
├── Dockerfile             # Docker configuration
├── requirements.txt       # Python dependencies
└── manage.py              # Django management script
```

## Admin Guide

### Accessing Admin
1. Go to `/admin`
2. Login with superuser credentials

### Managing Content
- **Pages**: Pages → Home → Edit to modify content
- **Menus**: Snippets → Header Menu / Footer Menu
- **Settings**: Settings → Color Theme / Navigation / Footer

### Adding New Pages
1. Pages → Add child page under Home
2. Choose "Flexible Page"
3. Add content blocks as needed
4. Publish

## Default Credentials

After running `populate_content` command:
- Username: `admin`
- Password: `admin123`

**Change these in production!**

## License

Proprietary - Qualitation Ltd.

## Support

For support, contact: info@qualitation.co.uk
