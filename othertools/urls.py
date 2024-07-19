from django.urls import path

from . import views

urlpatterns = [
    path("yt_converter/",views.yt_to_x_view, name="yt_x"),
    path("word_counter/",views.word_count,name="word_counter"),
    path("qr_code/", views.qr_code, name="qr_code"),
    path("ocr/", views.ocr_view, name="ocr"),
    path("plot/", views.plot_view, name="plot"),
    path("paste/", views.paste_image, name="paste"),
    path("pdf_merger/", views.pdf_merger_view, name="pdf_merger"),
    # path("time_tools/", views.time_tools, name="time_tools"),
    # path("teleprompter/", views.teleprompter, name="teleprompter"),
    # path("teleprompter_scroller/", views.teleprompter_scroller, name="teleprompter_scroller"),
    path("pdf_rotate/", views.pdf_rotate_veiw, name="pdf_rotate"),
]
# list of urls for the othertools app
# https://amaltools.com/tools/yt_converter/
# https://amaltools.com/tools/word_counter/
# https://amaltools.com/tools/qr_code/
# https://amaltools.com/tools/ocr/
# https://amaltools.com/tools/plot/
# https://amaltools.com/tools/paste/