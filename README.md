# django_database_project

Django project with Django REST Framework automatically generated.

## Installation

1. Activate virtual environment:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

2. Install dependencies (if not already installed):
   ```bash
   pip install -r requirements.txt
   ```

## Running

```bash
python manage.py runserver
```

## API Endpoints

- Admin: http://127.0.0.1:8000/admin/
- API Root: http://127.0.0.1:8000/api/
- Hello API: http://127.0.0.1:8000/api/hello/
- Status Check: http://127.0.0.1:8000/api/hello/status/

## Structure

- `django_database_project/` - Main settings
- `api/` - Sample app with API
- `venv/` - Virtual environment
- `manage.py` - Django management script

## Development

To create a superuser:
```bash
python manage.py createsuperuser
```

To create a new app:
```bash
python manage.py startapp app_name
```
