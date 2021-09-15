"""tweets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from core.views import splash, login, signup, logout, home
from core.views import my_profile, del_post, user_profs, hashtag, like_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', splash, name='splash'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout, name='logout'),
    path('home/', home, name='home'),
    path('profile/', my_profile, name='my_profile'),
    path('del_post/', del_post, name='del_post'),
    path('user_profs/', user_profs, name='user_profs'),
    path('hashtag/<str:hashtag>/', hashtag, name = 'hashtag'),
    path('like_post/', like_post, name = 'like_post'),
]
