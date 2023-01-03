from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-=sq=t=$(e!n6c9@+rzjrk0vw97z6gbr)f$&5k$#+&64$qe2&3_"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.168.43.77', 'localhost', '127.0.0.1']

CORS_ALLOWED_ORIGINS = ['http://localhost:3000', 'http://127.0.0.1:3000', 'http://*']

CORS_ALLOW_ALL_ORIGINS = True

#CORS_ALLOWED_ORIGINS_REGEXES = ['http://*']

# = True
# Application definition

INSTALLED_APPS = [
    
    #  OG APPS
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    #  MY APPS
    "warehouse.apps.WarehouseConfig",
    "orders.apps.OrdersConfig",
    "HR",
    "authentication",
    "delivery",
    "stores.apps.StoresConfig",
    "userapp.apps.UserappConfig",
    
    #  THIRD PARTY APPS
    'rest_framework',
    'address',
    'djoser',
    'corsheaders',

]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",

    "corsheaders.middleware.CorsMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "lemall.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'build')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "lemall.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis:127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]



# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# STATIC FILES

STATIC_URL = "static/"

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# AUTHENTICATION

AUTH_USER_MODEL = 'authentication.UserAccount'


DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': 'username/reset/confirm/{uid}/{token}',
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
    'USERNAME_CHANGED_EMAIL_CONFIRMATION': True,

    'ACTIVATION_URL': 'activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'SEND_CONFIRMATION_EMAIL': True,

    'SERIALIZERS': {
        'user_create': 'authentication.serializers.UserCreateSerializer',
        'user_delete': 'djoser.serializers.UserDeleteSerializer',
        'user': 'djoser.serializers.UserSerializer'
    },
    'LOGIN_FIELD': 'email',

    'USER_CREATE_PASSWORD_RETYPE': True,
    'SET_PASSWORD_RETYPE': True,
    'LOGOUT_ON_PASSWORD_CHANGE': True,
    'PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND': True,


}

SIMPLE_JWT = {
   'AUTH_HEADER_TYPES': ('JWT',),
}
# REST FRAMEWORK


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.AllowAny'),

    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination'
}


# EMAIL BACKEND

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'yusufteppei11@gmail.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True


# LINODE STORAGE SETTINGS
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

LINODE_BUCKET=os.environ.get('LINODE_BUCKET', 'lemall-images')
LINODE_BUCKET_REGION=os.environ.get('LINODE_BUCKET_REGION',  'us-east-1')
LINODE_BUCKET_ACCESS_KEY=os.environ.get('LINODE_BUCKET_ACCESS_KEY', 'Y55VPZU8WCERT7CC1DDR') 
LINODE_BUCKET_SECRET_KEY=os.environ.get('LINODE_BUCKET_SECRET_KEY', 'yTsXilLB1oEMtoX1c5ETDoapwGR3CRXDGoZrTam1') 


AWS_S3_ENDPOINT_URL=f'https://{LINODE_BUCKET_REGION}.linodeobjects.com'
AWS_ACCESS_KEY_ID=LINODE_BUCKET_ACCESS_KEY
AWS_SECRET_ACCESS_KEY=LINODE_BUCKET_SECRET_KEY
AWS_S3_REGION_NAME=LINODE_BUCKET_REGION
AWS_S3_USE_SSL=True
AWS_STORAGE_BUCKET_NAME=LINODE_BUCKET