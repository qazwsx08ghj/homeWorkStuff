from django.shortcuts import render,redirect
from django.http import HttpRequest
# Create your views here.
from django.contrib import messages 
from django .contrib .auth import login,logout,authenticate ,update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm

def main(request):
    return render(request,'main_site.html')

def register(request):
    if request.method == "POST":
        registerform = UserCreationForm(request.POST)
        if registerform.is_valid():
            user = registerform .save()       
            login(request,user)
            messages.success(request, f"成功註冊")
            return redirect ('/')
    form = UserCreationForm()
    return render(request,'register.html',context={})            

def Login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        Loginform = AuthenticationForm(request, data= request.POST)
        if Loginform.is_valid():
            name = Loginform.cleaned_data.get ('username')
            password = Loginform.cleaned_data.get ('password')
            user = authenticate(username=name,password=password)
            if user != None:
                login(request ,user)
                messages.success(request, f"成功登入")
                return redirect ('/')
            else:
                messages.error(request, f"帳號或密碼錯誤")
        else:
            messages.error(request, f"帳號或密碼錯誤")
    return render(request,'Login.html',context={})




def Logout(request):
    logout(request)
    messages.info(request, f"登出成功")
    return redirect('/')

def ChangePassword(request):
    
    if request .method == "POST":
        CPform = PasswordChangeForm(user=request.user,data = request.POST)
        if CPform .is_valid():
            messages.info(request, f"密碼更換成功")
            CPform.save()
            update_session_auth_hash(request,CPform .user)
        return redirect('/')
    return render(request ,'ChangePassword.html')