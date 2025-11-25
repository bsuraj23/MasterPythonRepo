# models_demo

This app demonstrates Django models, migrations, admin and basic ORM usage.

How to use (PowerShell):

1. From `projects/django_demo` create venv and install requirements (if not already done):

```powershell
.\setup_demo.ps1
```

2. Make and apply migrations:

```powershell
python manage.py makemigrations models_demo
python manage.py migrate
```

3. Create a superuser to access admin:

```powershell
python manage.py createsuperuser
```

4. Start the dev server and open:

- Admin: http://127.0.0.1:8000/admin/ (create BlogPost entries)
- Posts list: http://127.0.0.1:8000/models/

5. To load the included sample posts fixture (so the list shows content immediately):

```powershell
python manage.py loaddata fixtures/sample_posts.json
```

6. Run tests (optional):

```powershell
python manage.py test apps.models_demo
```
