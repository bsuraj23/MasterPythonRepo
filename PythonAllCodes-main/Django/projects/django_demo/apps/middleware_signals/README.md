middleware_signals demo

This app demonstrates:

- A simple middleware (`TimingMiddleware`) that measures view execution and adds an `X-View-Duration-ms` header.
- Signal handlers connected to `apps.models_demo.models.BlogPost` for `post_save` and `post_delete` (logging created/updated/deleted events).

How to try:

1. Ensure the demo virtualenv is active and dependencies installed (see project `setup_demo.ps1`).
2. Run migrations: `python manage.py migrate`.
3. Start the server: `python manage.py runserver`.
4. Visit `/middleware_signals/ping/` to create a `Ping` record and see the timing header in the response.

Notes:
- The signals import is triggered by the app's `ready()` method in `apps.py`.
- This is intentionally minimal for teaching; extend with more examples as needed.
