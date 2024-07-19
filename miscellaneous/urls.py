from django.urls import path

from . import views

urlpatterns = [
    # path("suggestion/", views.suggestion_page, name="suggestion_page"),
    path("", views.home_page, name="home"),
    # path("suggestion_overview/",views.suggestions_overview, name="suggestions_overview"),
    path("sitemap.txt",views.sitemap_txt, name="sitemap"),
    path("robots.txt",views.robots_txt, name="robots"),
    path("tags/<str:tags>", views.tags, name="tag_page"),
    # path("maintenance/", views.maintenance, name="maintenance"),
    path("about/", views.about, name="about"),
    path("comment_section/", views.comment_section, name="comment_section"),
    path("comment/", views.comment, name="comment"),
    path("search/", views.search, name="search"),
    path("tester/", views.secret_tester, name="tester"),
    path("acknowledgement/", views.acknowledgement, name="acknowledgement"),
    path("math_tools/", views.maths_tools_page, name="math_tools"),
    path("programming_tools/", views.programming_tools_page, name="programming_tools"),
    path("other_tools/", views.others_tools_page, name="other_tools"),
    path("fileconverter_tools/", views.fileconverters_tools_page, name="fileconverter_tools"),
    path("converter_tools/", views.converters_tools_page, name="converter_tools"),
    
    # path("theme/", views.theme, name="theme"),
]