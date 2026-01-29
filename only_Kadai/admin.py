# Register your models here.
from django.contrib import admin
from .models import Question, AnswerRecord


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "answer", "genre", "difficulty", "created_at")
    # 必要に応じてフィルターなど追加


@admin.register(AnswerRecord)
class AnswerRecordAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "question",
        "user_answer",
        "is_correct",
        "answered_at",
    )
