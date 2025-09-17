from django.urls import path

from . import views

urlpatterns = [
    path("", views.top, name="top"),
    path("index/", views.index, name="index"),
    path("list/", views.list, name="list"),
    path("reiwa/", views.reiwa, name="reiwa"),
    path("bmi/", views.bmi, name="bmi"),
    path("warikan/", views.warikan, name="warikan"),
    path("chokin/", views.chokin, name="chokin"),
    path("calculator/", views.calculator, name="calculator"),
]
