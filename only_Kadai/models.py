from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    text = models.TextField("問題文")
    answer = models.CharField("正解", max_length=256)
    genre = models.CharField("ジャンル", max_length=128, blank=True)
    difficulty = models.PositiveSmallIntegerField("難易度", default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text[:20]}…"


class AnswerRecord(models.Model):
    user = models.ForeignKey(User, verbose_name="ユーザー", on_delete=models.CASCADE)
    question = models.ForeignKey(
        Question, verbose_name="問題", on_delete=models.CASCADE
    )
    user_answer = models.CharField("回答", max_length=256)
    is_correct = models.BooleanField("正解か", default=False)
    ai_explanation = models.TextField("Gemini解説", blank=True)
    answered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.question}"
