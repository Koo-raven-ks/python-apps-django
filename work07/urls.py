from django.urls import path
from . import views

urlpatterns = [
    path("", views.top, name="top"),
    path("omi/", views.omi, name="omi"),
    path("janken/", views.janken, name="janken"),
]
