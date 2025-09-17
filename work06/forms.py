from django import forms


class ReiwaForm(forms.Form):
    reiwa_year = forms.IntegerField(label="令和何年？")


class BmiForm(forms.Form):
    height = forms.FloatField(label="身長（cm）")
    weight = forms.FloatField(label="体重（kg）")


class warikanForm(forms.Form):
    total_amount = forms.IntegerField(label="合計金額")
    number_of_people = forms.IntegerField(label="人数")


class ChokinForm(forms.Form):
    initial_amount = forms.IntegerField(label="初期金額")
    monthly_deposit = forms.IntegerField(label="毎月の預金額")
    annual_interest_rate = forms.FloatField(label="年利（％）")
    years = forms.IntegerField(label="預ける年数")


class CalculatorForm(forms.Form):
    num1 = forms.FloatField(label="数値1")
    num2 = forms.FloatField(label="数値2")
    operation = forms.ChoiceField(
        label="演算子",
        choices=[
            ("add", "加算"),
            ("subtract", "減算"),
            ("multiply", "乗算"),
            ("divide", "除算"),
        ],
    )
