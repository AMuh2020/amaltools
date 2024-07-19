from django.apps import AppConfig

# from django.core.signals import request_finished
# from .views import yt_to_x_view

class MiscellaneousConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'miscellaneous'

    # def ready(self):
    #     request_finished.connect(yt_to_x_view)
