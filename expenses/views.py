from django.shortcuts import render
from .forms import ExpensesForm
# Create your views here.

def index(request):
    context = {
        'form':ExpensesForm()
    }
    return render(request,'expenses/expenses.html',context)