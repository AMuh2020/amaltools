from django.urls import path

from . import views

urlpatterns = [
    path("2point/", views.straight_line, name="2point"),
    path("herons_formula/", views.herons_formula_view, name="herons_formula"),
    path("midpoint/", views.mid_point_view, name="midpoint"),
    path("fibonacci/",views.fibonacci_sequence, name="fibonacci"),
    path("suvat/",views.suvat, name="suvat"),
    path("quadratic_formula/",views.quadratic, name="quadratic"),
    path("simultaneous/",views.simultaneous, name="simultaneous"),
    path("calculator/",views.calculator, name="calculator"),
    path("integral/",views.integralCalculator, name="integral"),
    path("derivative/",views.derivativeCalculator, name="derivative"),
]
# list of urls for the maths app
# https://amaltools.com/tools/2point/
# https://amaltools.com/tools/herons_formula/
# https://amaltools.com/tools/midpoint/
# https://amaltools.com/tools/fibonacci/
# https://amaltools.com/tools/suvat/
# https://amaltools.com/tools/quadratic_formula/
# https://amaltools.com/tools/simultaneous/
# https://amaltools.com/tools/calculator/
# https://amaltools.com/tools/integral/