from .base import *

DEBUG=True
STATIC_URL='/static/'
ALLOWED_HOSTS=env.list('ALLOWED_HOSTS', default=['localhost', '127.0.0.1'])

CORS_ALLOWED_ORIGINS = env.list('CORS_ALLOWED_ORIGINS', default=[
    "http://localhost:8000",
])
CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS', default=[
    "http://localhost:8000",
])