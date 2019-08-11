from django.shortcuts import render,redirect
from .forms import IncomeForm
from .models import Income
from django.contrib.auth.decorators import login_required
# Create your views here.
def income(request):
    data = {
        'income':Income.objects.all(),
    }
    return render(request,'income/index.html',data)
def delete_income(request,id):
    i = Income.objects.get(pk=id)
    i.delete()
    return redirect('income_home')

def income_edit(request,id):
        income = Income.objects.get(pk=id)
        form = IncomeForm(request.POST or None,instance=income)
        if form.is_valid():
            form.save()
            return redirect('income_home')
        return render(request,'income/edit.html',{'form':form})



@login_required(login_url='dashboard/login/')
def create(request):
    print("funciton called")
    if request.method=='GET':
        form = IncomeForm()
        return render(request,'income/create.html',{'form':form})
    else:
        print("User id is "+str(request.user.id))
        form = IncomeForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user_id = request.user.id
            data.save()
            return redirect('income_home')
        else:
            print("form invalid")
            return render(request, 'income/create.html', {'form': form, 'error': 'error occured'})

