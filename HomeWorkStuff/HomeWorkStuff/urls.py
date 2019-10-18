"""HomeWorkStuff URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.contrib.auth import views as auth_views
from main_site.views import register, main, Login, \
    Logout, \
    ChangePassword, \
    UserProfile, \
    PostArticleCreate, \
    UserViewSet, \
    userProfileViewSet, \
    userArticleViewSet, \
    GroupViewSet




router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'userProfiles', userProfileViewSet)
router.register(r'userArticle', userArticleViewSet)
router.register(r'groups', GroupViewSet)
app_name = "main"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name="index"),
    path('register/', register, name="register"),
    path('logout/', Logout, name="Logout"),
    path('login/', Login, name="Login"),
    path('changepassword/', ChangePassword, name="ChangePassword"),
    path('userprofile/', UserProfile, name="UserProfile"),
    path('postarticlecreate/', PostArticleCreate, name="PostArticleCreate"),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('accounts/', include('django.contrib.auth.urls')),

]
