from django.urls import path

from . import views

urlpatterns = [
    path("html_viewer/",views.html_viewer,name="html_viewer"),
    path("css_to_inline/", views.css_to_inline_view, name="css_to_inline"),
    path("image_b64/", views.image_b64, name="image_b64"),

]
# list of urls for the othertools app
# https://amaltools.com/tools/html_viewer/
# https://amaltools.com/tools/css_to_inline/
# https://amaltools.com/tools/image_b64/