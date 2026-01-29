# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # ユーザー作成
            login(request, user)
            return redirect("top")  # ホームページなどにリダイレクト
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", {"form": form})
