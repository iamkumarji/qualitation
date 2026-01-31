import os
from .base import *

DEBUG = False

# Security settings
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'change-me-in-production')

# Allowed hosts - add your Azure domain
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')

# CSRF trusted origins - configure via environment variable
# For AWS: Set CSRF_TRUSTED_ORIGINS to your domain(s), e.g., 'https://yourdomain.com,https://*.amazonaws.com'
# For HTTP (development): 'http://yourdomain.com'
CSRF_TRUSTED_ORIGINS = []
if os.environ.get('CSRF_TRUSTED_ORIGINS'):
    CSRF_TRUSTED_ORIGINS = [origin.strip() for origin in os.environ.get('CSRF_TRUSTED_ORIGINS').split(',')]
else:
    # Fallback for common AWS patterns (add your specific domain)
    CSRF_TRUSTED_ORIGINS = [
        'https://*.amazonaws.com',
        'https://*.elasticbeanstalk.com',
        'http://*.amazonaws.com',  # If not using HTTPS yet
        'http://*.elasticbeanstalk.com',
    ]

# WhiteNoise for static files
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

# ManifestStaticFilesStorage is recommended in production
STORAGES["staticfiles"]["BACKEND"] = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Security headers
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True

# If using HTTPS (recommended for production)
if os.environ.get('SECURE_SSL_REDIRECT', 'False').lower() == 'true':
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Wagtail base URL - set to your actual domain
WAGTAILADMIN_BASE_URL = os.environ.get('WAGTAILADMIN_BASE_URL', 'https://yourdomain.com')

try:
    from .local import *
except ImportError:
    pass
