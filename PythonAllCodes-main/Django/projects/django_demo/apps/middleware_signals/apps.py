from django.apps import AppConfig


class MiddlewareSignalsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.middleware_signals'

    def ready(self):
        # import signal handlers
        from . import signals  # noqa: F401
