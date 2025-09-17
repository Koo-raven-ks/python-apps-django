from django.shortcuts import render

# Create your views here.


def omi(repuest):
    import random

    result = None
    if repuest.method == "POST":
        fortunes = [
            "大吉",
            "中吉",
            "小吉",
            "吉",
            "末吉",
            "凶",
        ]
        result = random.choice(fortunes)
    return render(repuest, "work07/omikuji.html", {"result": result})


def top(request):
    return render(request, "work07/top.html")


def janken(reqest):
    result = None
    import random

    if reqest.method == "POST":
        ai_hands = ["gu-", "tyoki", "pa-"]
        user_hands = reqest.POST.get("te")
        ko_hands = random.choice(ai_hands)
        if user_hands == ko_hands:
            result = "あいこ"
        elif (
            (user_hands == "gu-" and ko_hands == "tyoki")
            or (user_hands == "tyoki" and ko_hands == "pa-")
            or (user_hands == "pa-" and ko_hands == "gu-")
        ):
            result = "あなたの勝ち"
        else:
            result = "負け"

    return render(reqest, "work07/janken.html", {"result": result})
