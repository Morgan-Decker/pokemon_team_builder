from django.conf.urls import url
from django.urls import path
from builder import views

app_name = 'builder'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('popular/', views.popular, name='popular'),
    path('recent/', views.recent, name='recent'),
    path('your_teams/', views.Your_Teams, name='your_teams'),
    path('share/<slug:username_private_slug>/', views.share_priv_username, name=''),
    path('share/<slug:username_slug>/', views.share_username, name=''),
    path('friends/', views.friends, name='friends'),
    path('friends/<slug:friendname_slug>/', views.viewfriend, name=''),
    path('builder/', views.builder, name='builder'),
    path('builder/<slug:teamname_slug>/', views.buildteam, name='build_team'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('restricted/', views.restricted, name='restricted'),
    url(r'^teams/(?P<slug>[-\w]+)/$', views.team_view, name='team'),
    path('create_new_team', views.create_new_team, name='create_new_team')
]