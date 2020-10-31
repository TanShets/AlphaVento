from django.apps import AppConfig


class BetaargentiConfig(AppConfig):
    name = 'BetaArgenti'
    
    def ready(self):
        import BetaArgenti.signals