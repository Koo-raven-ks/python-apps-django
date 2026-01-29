import os
import requests
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Question, AnswerRecord
from openai import OpenAI
import spacy

nlp = spacy.load("ja_ginza")


def is_similar_question(new_q, existing_questions, threshold=0.9):
    doc1 = nlp(new_q)
    print(f"existing_questions: {existing_questions}")
    for q in existing_questions:
        doc2 = nlp(q)
        print(f"doc1: {doc1} doc2:{doc2}")
        print(f"doc1.similarity(doc2) {doc1.similarity(doc2)}")
        if doc1.similarity(doc2) > threshold:
            return True  # 類似あり
    return False


# def get_ai_explanation(question_text, user_answer):
#     API_KEY = os.environ.get("GEMINI_API_KEY")
#     url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
#     headers = {"Content-Type": "application/json"}
#     data = {
#         "contents": [
#             {
#                 "parts": [
#                     {
#                         "text": (
#                             f"問題: {question_text}\n"
#                             f"回答: {user_answer}\n"
#                             "この誤答の理由やヒントを日本語で簡単に解説してください。"
#                         )
#                     }
#                 ]
#             }
#         ]
#     }
#     params = {"key": API_KEY}
#     try:
#         response = requests.post(
#             url, headers=headers, params=params, json=data, timeout=8
#         )
#         result = response.json()
#         explanation = result["candidates"][0]["content"]["parts"][0]["text"]
#         return explanation
#     except Exception as e:
#         return f"AI解説取得に失敗しました: {e}"


# --- 追加・修正ここまで ---#


# duplicate quiz view removed — keep the first @login_required def quiz defined above
@login_required
def quiz(request):
    if request.method == "POST":
        qid = int(request.POST.get("question_id"))
        question = Question.objects.get(id=qid)
        user_answer = request.POST.get("user_answer", "").strip()

        # ===== 複数正解対応 =====
        correct_answers = [ans.strip() for ans in question.answer.split(",")]
        is_correct = user_answer in correct_answers
        # =========================

        print(
            {
                "user_answer": user_answer,
                "correct_answers": correct_answers,  # 配列で表示
                "is_correct": is_correct,
                "qid": qid,
            }
        )

        ai_explanation = ""
        if not is_correct:
            ai_explanation = get_openai_explanation(question.text, user_answer)

        AnswerRecord.objects.create(
            user=request.user,
            question=question,
            user_answer=user_answer,
            is_correct=is_correct,
            ai_explanation=ai_explanation,
        )
        context = {
            "question": question,
            "user_answer": user_answer,
            "is_correct": is_correct,
            "ai_explanation": ai_explanation,
        }
        return render(request, "only_Kadai/result.html", context)
    else:
        question = Question.objects.order_by("?").first()
        return render(request, "only_Kadai/quiz.html", {"question": question})


# --- 追加・修正ここから ---#


def generate_ai_question(genre="一般", difficulty=1):
    api_key = os.environ.get("OPENAI_API_KEY")
    client = OpenAI(api_key=api_key)
    prompt = f"{genre}ジャンルで難易度{difficulty}レベルの日本語クイズ問題（一問一答）とその正解を「問題文: ～\\n正解候補:正解1,正解2, ～」の形でください。"
    try:
        completion = client.chat.completions.create(
            model="gpt-4o",  # または "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "あなたは日本語のクイズ作成AIです。"},
                {"role": "user", "content": prompt},
            ],
            max_tokens=256,
            temperature=0.7,
        )
        text = completion.choices[0].message.content
        import re

        m = re.search(r"問題文[:：](.*)\n正解候補[:：](.*)", text)
        if m:
            q_text, answer = m.group(1).strip(), m.group(2).strip()
        else:
            q_text, answer = text, ""
    except Exception as e:
        q_text, answer = f"OpenAIエラー: {str(e)}", ""
    return q_text, answer


@login_required
def ai_create_question(request):
    if request.method == "POST":
        genre = request.POST.get("genre", "一般")
        difficulty = int(request.POST.get("difficulty", "1"))

        # 1. 問題生成
        q_text, answer = generate_ai_question(genre, difficulty)

        # 2. 類似判定！！（ここを追加）
        from .models import Question

        existing_questions = Question.objects.values_list("text", flat=True)
        if is_similar_question(q_text, existing_questions):
            msg = "似た問題が既に存在します。"
            return render(
                request,
                "only_Kadai/ai_create_result.html",
                {"msg": msg, "q_text": q_text, "answer": answer},
            )

        # 3. 保存
        Question.objects.create(
            text=q_text, answer=answer, genre=genre, difficulty=difficulty
        )
        msg = "AI問題生成＆保存完了"
        return render(
            request,
            "only_Kadai/ai_create_result.html",
            {"msg": msg, "q_text": q_text, "answer": answer},
        )
    return render(request, "only_Kadai/ai_create_form.html")


# is_similar_questionは別途定義（前の回答例などを参考）


def get_openai_explanation(question_text, user_answer):
    api_key = os.environ.get("OPENAI_API_KEY")
    client = OpenAI(api_key=api_key)
    prompt = f"問題: {question_text}\n誤答: {user_answer}\nどこが間違いか、理由やヒントを日本語で生徒向けに分かりやすく短く解説してください。"
    try:
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "あなたは日本語の教育用AI解説者です。"},
                {"role": "user", "content": prompt},
            ],
            max_tokens=150,
            temperature=0.3,
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"AI解説失敗: {str(e)}"
