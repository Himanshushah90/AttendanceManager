from django.apps import AppConfig


class StudentConfig(AppConfig):
    name = 'student'

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'users'