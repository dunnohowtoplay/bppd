from django.apps import AppConfig


class AppsConfig(AppConfig):
    name = 'apps'
    def ready(self):
        # signals are imported, so that they are defined and can be used
        import apps.signals