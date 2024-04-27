from django.apps import AppConfig


class LoginConfig(AppConfig):
    name = 'login'

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'users'
