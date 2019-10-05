from django.shortcuts import render, redirect
from django.http import HttpRequest
# Create your views here.
from django.contrib import messages

from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UserChangeForm
from main_site.models import userProfile, userArticle
from django.forms.models import model_to_dict


def main(request):
    user_Article_data = userArticle.objects.all()

    if 'search' in request.GET:
        search = request.GET['search']
        user_Article_data = userArticle.objects.filter(Article_writer=search)
    return render(request, 'main_site.html', {'user_Article_data': user_Article_data})


def register(request):
    if request.method == "POST":
        registerform = UserCreationForm(request.POST)
        if registerform.is_valid():
            user = registerform.save()
            login(request, user)
            messages.success(request, f"成功註冊")
            return redirect('/')
        else:
            messages.success(request, f"註冊失敗")
            return redirect('/')

    form = UserCreationForm()
    return render(request, 'register.html')


def Login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        Loginform = AuthenticationForm(request, data=request.POST)
        if Loginform.is_valid():
            name = Loginform.cleaned_data.get('username')
            password = Loginform.cleaned_data.get('password')
            user = authenticate(username=name, password=password)
            if user != None:
                login(request, user)
                messages.success(request, f"成功登入")
                return redirect('/')
            else:
                messages.error(request, f"帳號或密碼錯誤")
        else:
            messages.error(request, f"帳號或密碼錯誤")
    return render(request, 'Login.html')


def Logout(request):
    logout(request)
    messages.info(request, f"登出成功")
    return redirect('/')


@login_required
def ChangePassword(request):
    if request.method == "POST":
        CPform = PasswordChangeForm(user=request.user, data=request.POST)
        if CPform.is_valid():
            messages.info(request, f"密碼更換成功")
            CPform.save()
            update_session_auth_hash(request, CPform.user)

            user = User.objects.get(username=request.user.username)
            logout(request)
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, f"密碼更換失敗")
    return render(request, 'ChangePassword.html')


@login_required
def UserProfile(request):
    if request.method == "POST":
        openUser = User()

        request.user.email = request.POST.get("email")
        request.user.first_name = request.POST.get("first_name")
        request.user.last_name = request.POST.get("last_name")
        request.user.save()

        # models
        # OpenUserProfile = userProfile()
        # OpenUserProfile.USER = User.objects.get(username=request.user.username)
        # OpenUserProfile.hobbies = request.POST.get("hobbies")
        # OpenUserProfile.selfIntroduction = request.POST.get("introduction")
        # OpenUserProfile.save()
        userProfile.objects.update_or_create(
            USER=User.objects.get(username=request.user.username),
            defaults={
                'hobbies': request.POST.get("hobbies"),
                'selfIntroduction': request.POST.get("introduction"),
            }
        )
        # OpenUserProfile.objects.update_or_create(
        #     USER = User.objects.get(username=request.user.username),
        #     hobbies = request.POST.get("hobbies"),
        #     selfIntroduction =request.POST.get("introduction"),
        #     defaults= {
        #         'USER' : User.objects.get(username=request.user.username)
        #     }
        #
        # )
        messages.info(request, f"使用者資料更換成功")
        return redirect('/')
    return render(request, 'UserProfile.html')


def PostArticleCreate(request):
    if request.method == "POST":
        OpenUserArticle = userArticle()
        OpenUserArticle.USER = request.user
        OpenUserArticle.Article_writer = request.POST.get("writer")
        OpenUserArticle.Article_title = request.POST.get("Article_title")
        OpenUserArticle.Article = request.POST.get("Article")
        OpenUserArticle.save()
        return redirect('/')
    return render(request, 'PostArticlePage.html')
