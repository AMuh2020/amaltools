from django.urls import path

from . import views

urlpatterns = [
    path("bintodec/", views.binToDec, name="binToDec"),
    path("dectobin/", views.decToBin, name="decToBin"),
    path("bintohex/", views.binToHex, name="binToHex"),
    path("zeckendorf/",views.numberToZeckendorf_representation, name="zeckendorf notation"),
    path("bintotext/",views.binaryToText,name="binaryToText"),
    path("texttobin/",views.textToBinary,name="textToBinary"),
    path("integertotext/",views.numberToText,name="numberToText")

]

# list of urls for the converters app
# https://amaltools.com/tools/bintodec/
# https://amaltools.com/tools/dectobin/
# https://amaltools.com/tools/bintohex/
# https://amaltools.com/tools/zeckendorf/
# https://amaltools.com/tools/bintotext/
# https://amaltools.com/tools/texttobin/
# https://amaltools.com/tools/integertotext/
