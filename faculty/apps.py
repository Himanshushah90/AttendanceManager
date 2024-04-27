from django.apps import AppConfig


class FacultyConfig(AppConfig):
    name = 'faculty'

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'users'
