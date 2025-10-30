from django.shortcuts import render, redirect, get_object_or_404
from .models import toDo
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

# Create your views here.


def todo(request):
    todos = toDo.objects.all().order_by("-created_at")
    if request.method == "POST":
        taskName = request.POST.get("taskName", "").strip()
        timeLimit = request.POST.get("timeLimit", "").strip()

        if not taskName or not timeLimit:
            messages.error(request, "タイトルと内容は空にできません。")
            return render(request, "work09/top.html")

        # 🔹 正常時：データベースに保存
        toDo.objects.create(title=taskName, timeLimit=timeLimit)
        messages.success(request, "メモを作成しました！")
        return redirect("work09:todo")
    return render(request, "work09/top.html", {"todos": todos})


def todohs(request):
    return render(request, "work09/todohs.html")


def delete(request, todo_id):
    todo = get_object_or_404(toDo, id=todo_id)

    if request.method == "POST":  # POSTのときだけ削除
        todo.delete()
        messages.success(request, "メモを削除しました。")
        return redirect("work09:todo")


def edit(request, todo_id):
    todo = get_object_or_404(toDo, id=todo_id)
    if request.method == "POST":
        # フォームからデータ取得
        taskMei = request.POST.get("taskMei", "").strip()
        timeKigen = request.POST.get("timeKigen", "").strip()
        if not taskMei or not timeKigen:
            messages.error(request, "タイトルと期限日は空にできません。")
            return render(request, "work09/todohs.html", {"todo": todo})
        # 更新
        todo.title = taskMei
        todo.timeLimit = timeKigen
        todo.save()
        messages.success(request, "タスクを更新しました！")
        return redirect("work09:todo")
    # GETの場合は編集フォームを表示
    return render(request, "work09/todohs.html", {"todo": todo})


def fin(request, todo_id):
    todo = get_object_or_404(toDo, id=todo_id)
    if request.method == "POST":
        todo.is_completed = not todo.is_completed  # True/Falseを切り替え
        todo.save()
        if todo.is_completed:
            messages.success(request, "タスクを完了しました。")
        else:
            messages.success(request, "タスクを未完了にしました。")
        return redirect("work09:todo")


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"
