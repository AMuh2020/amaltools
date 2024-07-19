from django.urls import path

from . import views

urlpatterns = [
    path("mp4_mp3/", views.mp4_mp3, name="mp3"),
    path("video_extract/", views.vid_extractor, name="video_extract"),
    path("csv_tsv/", views.csv_tsv_view, name="csv_tsv"),
    path("pdf_image/", views.pdf_image_view, name="pdf_image"),
    # path("test/",views.test,name="testi")
]
# list of urls for the fileconverters app
# https://amaltools.com/tools/mp4_mp3/
# https://amaltools.com/tools/video_extract/
# https://amaltools.com/tools/csv_tsv/