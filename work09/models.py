from django.db import models


# models.py
class toDo(models.Model):
    title = models.CharField(max_length=100)
    timeLimit = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)  # 追加

    def __str__(self):
        return self.title
