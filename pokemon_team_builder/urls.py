"""pokemon_team_builder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from builder import views

urlpatterns = [
    path('', views.home, name='home'),
    path('your_teams/', views.Your_Teams, name='your_teams'),
    path('following/', views.following, name='following'),
    path('builder/', views.builder, name='builder'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('popular/', views.popular, name='popular'),
    path('recent/', views.recent, name='recent'),
    path('restricted/', views.restricted, name='restricted'),
    path('builder/', include('builder.urls')),
    path('admin/', admin.site.urls),
    url(r'^teams/(?P<slug>[-\w]+)/$', views.team_view, name='team'),
    path('like/<int:pk>', views.LikeView, name='like_team')
]
