from django.urls import path

from . import views

app_name = "work_08"

urlpatterns = [
    path("", views.memo, name="memo"),
    path("crtmemo/", views.crtmemo, name="crtmemo"),
    path("delete/<int:memo_id>/", views.delete, name="delete"),
]
