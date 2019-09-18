from django.shortcuts import render,redirect
from django.http import HttpRequest
# Create your views here.
from django .contrib .auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm

def Login(request):
    return render(request,'Login.html')

def main(request):
    return render(request,'main_site.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form .save()
            login(request,user)
            redirect('http://127.0.0.1:8000/')
            


    form = UserCreationForm
    return render(request,'register.html',context={"form":form})