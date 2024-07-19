from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    # path("load_temp/", views.temp, name="temp"),
    path("logout/", views.logout_view, name="logout"),
]