from django.forms import ModelForm
from .models import Income,Expense

class addIncomeForm(ModelForm):
    class Meta:
        model = Income
        fields = ['amount', 'category','date', 'note']
class addExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = ['amount', 'category','date', 'note']