from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def signup(request):
    if request.method=='GET':
        context = {
            'form':UserCreationForm()
        }
        return render(request,'signup.html',context)
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
             form.save()
             return redirect('login')
        return render(request,'signup.html',{'form':form})

def _login(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        u = request.POST.get('username')
        print(u)
        p = request.POST.get('password')
        print(p)
        user = authenticate(username=u,password=p)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        return render(request,'login.html',{'err':'sorry some error occured'})

@login_required(login_url='/login')
def dashboard(request):
    return render(request,'dashboard.html')

def _logout(request):
    logout(request)
    return redirect('login')