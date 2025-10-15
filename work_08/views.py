from django.shortcuts import render, redirect, get_object_or_404
from .models import Memo
from django.contrib import messages

# Create your views here.


def memo(request):
    memos = Memo.objects.all().order_by("-created_at")
    return render(request, "work_08/memo.html", {"memos": memos})


def crtmemo(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        content = request.POST.get("content", "").strip()

        if not title or not content:
            messages.error(request, "タイトルと内容は空にできません。")
            return render(request, "work_08/crtmemo.html")

        # 🔹 正常時：データベースに保存
        Memo.objects.create(title=title, content=content)
        messages.success(request, "メモを作成しました！")
        return redirect("work_08:memo")

    # GETアクセス時
    return render(request, "work_08/crtmemo.html")


def delete(request, memo_id):
    memo = get_object_or_404(Memo, id=memo_id)

    if request.method == "POST":  # POSTのときだけ削除
        memo.delete()
        messages.success(request, "メモを削除しました。")
        return redirect("work09:todo")
