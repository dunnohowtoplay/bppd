from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = 'api'
    def ready(self):
        # signals are imported, so that they are defined and can be used
        import apps.signals
