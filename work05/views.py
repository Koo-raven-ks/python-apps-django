from django.http import HttpResponse

from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the work05 index.")


def top(request):
    return HttpResponse("Hello, world. You're at the work05 index.")


def list(request):
    return HttpResponse("Hello, world. You're at the work05 index.")


def html(request):
    my_name = "白石 光桜"  # ← ここを任意の名前に
    return render(request, "work05/index.html", {"my_name": my_name})
