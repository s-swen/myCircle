from django.apps import AppConfig


class CircleConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "circle"
    def ready(self):
        import circle.signals  # Register the signals