from django.urls import path
from . import views

urlpatterns = [
    path("quiz/", views.quiz, name="quiz"),
    path("ai_create/", views.ai_create_question, name="ai_create_question"),
]
