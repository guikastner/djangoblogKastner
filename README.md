# Django Blog Kastner

Simple, extensible blog built with Django. It includes a modern rich-text editor (CKEditor 5) with image and document uploads, categories, and user comments with authentication.

This guide covers local setup, features, environment variables, Docker Compose deployment, and useful commands.

## Features

- Posts with draft/published status and unique slugs
- CKEditor 5 rich editor with embedded images and document uploads
- Categories with per-category listing pages and counts
- Comments per post (login required), basic flash messages
- Public “New Post” page for staff users (`/post/new/`)
- Django Admin for full content management
- Static files with WhiteNoise
- i18n defaults for pt-BR and timezone configurable

## Tech Stack

- Python 3.14 and Django 5.x
- DB: SQLite (dev/prototype) — can switch to PostgreSQL later
- Editor: `django-ckeditor-5` (CKEditor 5)
- Web server: Gunicorn (in Docker), static via WhiteNoise
- Dockerfile and `docker-compose.yml` for containerized deploy

## Prerequisites

- Python 3.14 and `pip`
- Virtualenv (`python -m venv`) recommended
- Docker (optional, for containerized run)

## Local Development

Windows (PowerShell):

```powershell
.venv\Scripts\Deactivate 2>$null; $null = Remove-Item -Recurse -Force .venv 2>$null
py -3.14 -m venv .venv
.venv\Scripts\Activate
pip install -U pip
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

macOS/Linux:

```bash
python3.14 -m venv .venv  # or: python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Access:
- App: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## Authentication and Content

- Login: `/accounts/login/`
- Sign up: `/accounts/signup/`
- New post (staff only): `/post/new/`
- Home with categories panel: `/`
- All categories: `/categories/`
- Category detail: `/category/<slug>/`
- Post detail + comments: `/post/<slug>/`

## Rich Editor (CKEditor 5)

- Full toolbar: headings, bold/italic/underline/strikethrough, sub/superscript, fonts, colors, alignment, lists (including todo), blockquote, code, code block, tables, media embed, find/replace, special characters, undo/redo.
- Images: upload, captions, alt text, alignment, styles (inline/block/side), resize.
- Documents: common file types allowed (PDF, DOCX, XLSX, PPTX, TXT, CSV, etc.).
- Configuration lives in `project/settings.py` under `CKEDITOR_5_CONFIGS` and `CKEDITOR_5_UPLOAD_*`.

## Environment Variables

Use a `.env` file (example provided in `.env.example`) or set system env vars. Minimum suggested keys:

```
DJANGO_SECRET_KEY=replace-with-a-secure-key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
TIME_ZONE=America/Sao_Paulo
LANGUAGE_CODE=pt-br
```

Note: The project reads from OS environment; Docker Compose uses `env_file: .env` automatically. If you want automatic `.env` loading for local runs, we can add `django-environ`.

## Docker Compose

Build and run (SQLite persisted to host, media persisted):

```bash
docker compose up --build -d
docker compose logs -f
```

Default ports and volumes:
- Web: `http://127.0.0.1:8000/`
- Volumes: `./db.sqlite3:/app/db.sqlite3`, `./media:/app/media`

Note: The Docker image uses `python:3.14-slim` as base.

First-time setup inside the container:

```bash
docker compose exec web python manage.py createsuperuser
```

The entrypoint runs `migrate` and `collectstatic` automatically on startup.

## Useful Commands

- Make migrations: `python manage.py makemigrations`
- Apply migrations: `python manage.py migrate`
- Collect static: `python manage.py collectstatic`
- Django shell: `python manage.py shell`

## Production Notes

- Set `DJANGO_DEBUG=False`, a strong `DJANGO_SECRET_KEY`, and proper `DJANGO_ALLOWED_HOSTS`.
- Static files are served with WhiteNoise (no Nginx required, though a reverse proxy is recommended).
- SQLite is fine for small deployments; consider PostgreSQL for production (update settings/`DATABASE_URL` and Compose).
- Media files are served by Django in this setup; consider cloud storage (S3/GCS) for scale.

## Troubleshooting

- Missing editor toolbar on `/post/new/`: ensure `{{ form.media }}` is present (it is) and hard-refresh the page; check browser console for static errors.
- “no such table”: run `makemigrations` then `migrate` (or restart Compose to let entrypoint run migrations).
- 404 on `/post/new/`: URL order matters; specific route is already placed before the slug route.
- Static files in Docker: `collectstatic` runs on startup; verify `staticfiles/` is created and WhiteNoise is enabled.

## Python 3.14 Notes

- Ensure Python 3.14 is installed on your machine.
- On Windows, prefer `py -3.14 -m venv .venv` to create the environment.
- If your IDE still points to an older interpreter, select `.venv\Scripts\python.exe` as the interpreter.

## Contributing

Issues and PRs are welcome. Please include a clear description and steps to reproduce when reporting bugs.

## License

Choose and add a license (e.g., MIT). If desired, add a `LICENSE` file and update this section.

## Author

Adjust to list project authors and contact details.
