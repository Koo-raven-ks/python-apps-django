# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ReiwaForm
from .forms import BmiForm
from .forms import warikanForm
from .forms import ChokinForm
from .forms import CalculatorForm


def top(request):
    return render(request, "work06/index.html")


def list(request):
    return HttpResponse("Hello, world. You're at the work05 list.")


def index(request):
    return render(request, "work06/index.html")


def reiwa(request):
    result = None
    if request.method == "POST":
        form = ReiwaForm(request.POST)
        if form.is_valid():
            reiwa_year = form.cleaned_data["reiwa_year"]
            result = 2018 + reiwa_year
    else:
        form = ReiwaForm()
    return render(request, "work06/reiwa.html", {"form": form, "result": result})


def bmi(request):
    result = None
    if request.method == "POST":
        form = BmiForm(request.POST)
        if form.is_valid():
            height = form.cleaned_data["height"] / 100  # cm to m
            weight = form.cleaned_data["weight"]
            result = weight / (height * height)
    else:
        form = BmiForm()
    return render(request, "work06/bmi.html", {"form": form, "result": result})


def warikan(request):
    result = None
    if request.method == "POST":
        form = warikanForm(request.POST)
        if form.is_valid():
            total_amount = form.cleaned_data["total_amount"]
            number_of_people = form.cleaned_data["number_of_people"]
            result = total_amount / number_of_people
    else:
        form = warikanForm()
    return render(request, "work06/warikan.html", {"form": form, "result": result})


def chokin(request):
    result = None
    if request.method == "POST":
        form = ChokinForm(request.POST)
        if form.is_valid():
            initial_amount = form.cleaned_data["initial_amount"]
            monthly_deposit = form.cleaned_data["monthly_deposit"]
            annual_interest_rate = form.cleaned_data["annual_interest_rate"] / 100
            years = form.cleaned_data["years"]

            total_months = years * 12
            monthly_interest_rate = annual_interest_rate / 12

            amount = initial_amount
            for month in range(total_months):
                amount += monthly_deposit
                amount += amount * monthly_interest_rate

            result = int(amount)
    else:
        form = ChokinForm()
    return render(request, "work06/chokin.html", {"form": form, "result": result})


def calculator(request):
    result = None
    if request.method == "POST":
        form = CalculatorForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data["num1"]
            num2 = form.cleaned_data["num2"]
            operation = form.cleaned_data["operation"]

            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = "Error: Division by zero"
        else:
            result = "Error: Invalid input"
    else:
        form = CalculatorForm()
    return render(request, "work06/calculator.html", {"form": form, "result": result})
