from django.shortcuts import render, redirect, get_object_or_404
from .models import toDo
from django.contrib import messages


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
        
