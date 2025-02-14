import os
import environ
from pathlib import Path


env = environ.Env()
BASE_DIR = Path(__file__).resolve().parent.parent.parent
environ.Env.read_env(BASE_DIR / ".env")

ENV_MODE = env.str('ENV_MODE', default='development')

if ENV_MODE == 'development':
    from course_enrollment.settings.development import *
elif ENV_MODE == 'testing':
    from course_enrollment.settings.testing import *
elif ENV_MODE == 'production':
    from course_enrollment.settings.production import *
else:
    raise ValueError("Invalid ENV_MODE environment variable")
