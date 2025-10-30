from django.urls import path
from . import views

app_name = "work09"

urlpatterns = [
    path("", views.todo, name="todo"),
    path("edit/<int:todo_id>/", views.edit, name="edit"),
    path("delete/<int:todo_id>/", views.delete, name="delete"),
    path("fin/<int:todo_id>/", views.fin, name="fin")
]
