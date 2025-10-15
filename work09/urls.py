from django.urls import path
from . import views

app_name = "work09"

urlpatterns = [
    path("", views.todo, name="todo"),
    path("todohs/", views.todohs, name="todohs"),
    path("delete/<int:todo_id>/", views.delete, name="delete"),
]
