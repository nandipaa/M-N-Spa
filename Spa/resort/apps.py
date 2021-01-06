from django.apps import AppConfig


class ResortConfig(AppConfig):
    name = 'resort'

    def ready(self):
        import resort.signals
