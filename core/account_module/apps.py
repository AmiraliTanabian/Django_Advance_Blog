from django.apps import AppConfig


class AccountModuleConfig(AppConfig):
    name = 'account_module'

    def ready(self):
        import account_module.signals
        return super().ready()