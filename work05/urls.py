from django.urls import path

from . import views

urlpatterns = [
    path("", views.top, name="top"),
    path("index/", views.index, name="index"),
    path("list/", views.list, name="list"),
    path("html/", views.html, name="html"),
    path("html/", views.html, name="html"),
    path("simple_qa/", views.simple_qa_openai, name="simple_qa"),
]
