from django.conf.urls import url
from django.urls import path
from builder import views

app_name = 'builder'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('popular/', views.popular, name='popular'),
    path('recent/', views.recent, name='recent'),
    path('your_teams/', views.Your_Teams, name='your_teams'),
    path('following/', views.following, name='following'),
    path('builder/', views.builder, name='builder'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('restricted/', views.restricted, name='restricted'),
    url(r'^teams/(?P<slug>[-\w]+)/$', views.team_view, name='team'),
    path('like/<int:pk>', views.LikeView, name='like_team')
]