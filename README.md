# Django Blog Kastner

Simple and extensible blog built with Django, focused on clean structure, good defaults, and easy customization.

This README covers local setup, useful commands, environment variables, and a deployment overview.

## Features

- Posts CRUD with draft/published status and slugs
- Categories and/or tags
- Comments with optional moderation
- Django Admin for content management
- Pagination and basic search
- Extensible templates (Bootstrap/Tailwind optional)
- i18n for pt-BR and configurable timezone

## Tech Stack

- Python 3.10+ and Django 4.x/5.x
- Database: `sqlite3` (dev) or PostgreSQL (prod)
- Optional: `django-environ`, `gunicorn/uvicorn`, `whitenoise`, Docker

## Prerequisites

- Python 3.10+ and `pip`
- Virtualenv (`python -m venv`)
- Git (optional, if cloning)

## Quick Start

Create and activate a virtual environment, then install dependencies.

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate
pip install -U pip
pip install -r requirements.txt
```

macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt
```

If the project uses Poetry:

```bash
poetry install
poetry shell
```

## Environment Variables

Create a `.env` at the project root (or configure variables by your preferred method). Minimum suggested keys:

```
DJANGO_SECRET_KEY=replace-with-a-secure-key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=sqlite:///db.sqlite3
TIME_ZONE=America/Sao_Paulo
LANGUAGE_CODE=pt-br
```

Without `django-environ`, set these directly in `settings.py`.

## Database and Migrations

```bash
python manage.py migrate
python manage.py createsuperuser
```

## Run the Development Server

```bash
python manage.py runserver
```

Access:

- App: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## Tests

- Django test runner:

  ```bash
  python manage.py test
  ```

- Pytest (if configured):

  ```bash
  pytest -q
  ```

- Coverage (if available):

  ```bash
  coverage run -m pytest && coverage html
  ```

## Suggested Project Structure

```
manage.py
project/               # Django project dir (rename accordingly)
  settings.py
  urls.py
  wsgi.py
  asgi.py
apps/blog/
  models.py
  views.py
  urls.py
  forms.py
  templates/
  static/
requirements.txt or pyproject.toml
.env
.gitignore
README.md
```

## Useful Commands

- Make migrations: `python manage.py makemigrations`
- Apply migrations: `python manage.py migrate`
- Create app: `python manage.py startapp your_app_name`
- Django shell: `python manage.py shell`
- Collect static (prod): `python manage.py collectstatic`

## Code Quality (optional)

- Format: `black .`
- Imports: `isort .`
- Lint: `flake8` or `ruff .`

## Deployment (Summary)

- Set `DJANGO_DEBUG=False`
- Configure `DJANGO_SECRET_KEY` and `DJANGO_ALLOWED_HOSTS`
- Configure database (e.g., PostgreSQL) via `DATABASE_URL`
- Run `python manage.py collectstatic`
- Serve with `gunicorn`/`uvicorn` behind Nginx/Caddy
- Static/Media: `whitenoise` (static) or S3/GCS for media
- Configure HTTPS (Let's Encrypt) and logging

## Troubleshooting

- "Command not found": confirm your virtualenv is activated
- Migration errors: run `makemigrations` then `migrate`
- Static files not loading in prod: run `collectstatic` and verify middleware/headers
- `psycopg` issues: ensure build tools and libpq are installed (or use `psycopg-binary` cautiously)

## Contributing

Contributions are welcome! Please open an issue or pull request with a clear description and steps to reproduce (if applicable).

## License

Choose and add a license (e.g., MIT). If you want, we can add a `LICENSE` file and update this section.

## Author

Adjust to list project authors and contact details.

