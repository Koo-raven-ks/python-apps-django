from django.http import HttpResponse

from django.shortcuts import render
from openai import OpenAI
import os


def index(request):
    return HttpResponse("Hello, world. You're at the work05 index.")


def top(request):
    return HttpResponse("Hello, world. You're at the work05 index.")


def list(request):
    return HttpResponse("Hello, world. You're at the work05 index.")


def html(request):
    my_name = "白石 光桜"  # ← ここを任意の名前に
    return render(request, "work05/index.html", {"my_name": my_name})


def simple_qa_openai(request):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    # query stringから質問を取得
    question = request.GET.get("question", "おすすめのレシピは？")
    prompt = "質問: {question}\n回答:".format(question=question)

    response = client.chat.completions.create(
        model="gpt-4o-mini",  # または "gpt-4o" など
        messages=[{"role": "user", "content": prompt}],
    )
    return HttpResponse(f"<pre>{response.choices[0].message.content}</pre>")


# ここにアクセス: http://127.0.0.1:8000/work05/simple_qa/?question=%E3%83%86%E3%82%B9%E3%83%88
