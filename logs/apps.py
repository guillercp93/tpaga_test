from django.apps import AppConfig


class LogsConfig(AppConfig):
    name = 'logs'

    def ready(self):
        import logs.signals
