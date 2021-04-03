from django.urls import path
from builder import views

app_name = 'builder'

urlpatterns = [
    path('home/', views.home , name='home'),
    path('home/popular/', views.popular , name='popular'),
    path('home/recent/', views.recent , name='recent'),
    path('share/', views.share , name='share'),
    path('share/<slug:username_private_slug>/', views.share_priv_username , name=''),
    path('share/<slug:username_slug>/', views.share_username , name=''),
    path('friends/', views.friends , name='friends'),
    path('friends/<slug:friendname_slug>/', views.viewfriend , name=''),
    path('builder/', views.builder , name='builder'),
    path('builder/<slug:teamname_slug>/', views.buildteam , name='build_team'),
    path('login/', views.user_login , name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.signup , name='signup'),
    path('request/<slug:username_slug>/', views.request_friend, name='request_friend')
    path('accept/<slug:username_slug>/' views.accept_friend, name='accept_friend')
    ]
