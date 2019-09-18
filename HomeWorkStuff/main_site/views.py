from django.shortcuts import render,redirect
from django.http import HttpRequest
# Create your views here.
from django.contrib import messages 
from django .contrib .auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

def Login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, data= request.POST)
        if form.is_valid():
            name = form.cleaned_data.get ('username')
            password = form.cleaned_data.get ('password')
            user = authenticate(username=name,password=password)
            if user != None:
                login(request ,user)
                messages.info(request, f"成功登入")
                return redirect ('/')
            else:
                messages.error(request, f"帳號或密碼錯誤")
        else:
            messages.error(request, f"帳號或密碼錯誤")
    return render(request,'Login.html',context={"form":form})

def main(request):
    return render(request,'main_site.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form .save()
            login(request,user)
            return redirect ('/')
            
    form = UserCreationForm()
    return render(request,'register.html',context={"form":form})

def Logout(request):
    logout(request)
    messages.info(request, f"登出成功")
    return redirect('/')
    
    