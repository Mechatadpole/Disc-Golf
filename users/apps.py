from django.apps import AppConfig

# Helping patty
class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals
