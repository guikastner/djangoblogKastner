from pathlib import Path
import os


# Base directories
BASE_DIR = Path(__file__).resolve().parent.parent


# Security
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "insecure-dev-key-change-me")
DEBUG = os.getenv("DJANGO_DEBUG", "True").lower() in {"1", "true", "yes", "on"}
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "").split(",") if os.getenv("DJANGO_ALLOWED_HOSTS") else []


# Applications
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third-party
    "django_ckeditor_5",

    # Local apps
    "apps.blog",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "project.wsgi.application"
ASGI_APPLICATION = "project.asgi.application"


# Database (SQLite by default)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
LANGUAGE_CODE = os.getenv("LANGUAGE_CODE", "pt-br")
TIME_ZONE = os.getenv("TIME_ZONE", "America/Sao_Paulo")
USE_I18N = True
USE_TZ = True


# Static and media
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"] if (BASE_DIR / "static").exists() else []

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# CKEditor 5 configuration (advanced editing with image upload)
CKEDITOR_5_CONFIGS = {
    "default": {
        "toolbar": [
            "heading", "|",
            "bold", "italic", "underline", "strikethrough", "subscript", "superscript", "removeFormat", "|",
            "fontFamily", "fontSize", "fontColor", "fontBackgroundColor", "highlight", "|",
            "alignment", "outdent", "indent", "|",
            "bulletedList", "numberedList", "todoList", "|",
            "blockQuote", "code", "codeBlock", "horizontalLine", "|",
            "link", "mediaEmbed", "insertTable", "imageUpload", "|",
            "findAndReplace", "specialCharacters", "undo", "redo",
        ],
        "image": {
            "toolbar": [
                "toggleImageCaption", "imageTextAlternative", "|",
                "imageStyle:inline", "imageStyle:block", "imageStyle:side", "|",
                "imageStyle:alignLeft", "imageStyle:alignCenter", "imageStyle:alignRight", "|",
                "resizeImage",
            ],
            "styles": ["inline", "block", "side", "alignLeft", "alignCenter", "alignRight"],
        },
        "table": {
            "contentToolbar": [
                "tableColumn", "tableRow", "mergeTableCells", "tableProperties", "tableCellProperties",
            ]
        },
        "link": {
            "decorators": {
                "addTargetToExternalLinks": True,
                "defaultProtocol": "https://",
            }
        },
        "language": "en",
        "height": 600,
    }
}

# Allow document types and restrict image types for CKEditor 5 uploads
# Accept documents and also the allowed image extensions to cover drag/drop or generic upload flows
CKEDITOR_5_UPLOAD_FILE_TYPES = [
    ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".csv", ".md",
    ".png", ".jpg", ".jpeg", ".jpe", ".gif",
    "png", "jpg", "jpeg", "jpe", "gif",
    ".PNG", ".JPG", ".JPEG", ".JPE", ".GIF",
    "PNG", "JPG", "JPEG", "JPE", "GIF",
]
# Only PNG, JPG (and variants), and GIF (and variants)
CKEDITOR_5_UPLOAD_IMAGE_TYPES = [
    ".png", ".jpg", ".jpeg", ".jpe", ".gif",
    "png", "jpg", "jpeg", "jpe", "gif",
    ".PNG", ".JPG", ".JPEG", ".JPE", ".GIF",
    "PNG", "JPG", "JPEG", "JPE", "GIF",
]

# Optional: base upload path under MEDIA_ROOT
CKEDITOR_5_UPLOAD_PATH = "uploads/"

# Auth redirects
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

# Use WhiteNoise for efficient static file serving in containers/prod
STORAGES = {
    "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
    "staticfiles": {"BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage"},
}
