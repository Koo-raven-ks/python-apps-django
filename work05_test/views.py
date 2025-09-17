from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the work05_test index.")


def top(request):
    return HttpResponse("Hello, world. You're at the work05_test index.")


def list(request):
    return HttpResponse("Hello, world. You're at the work05_test index.")
# Create your views here.
