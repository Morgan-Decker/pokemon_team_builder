from django.urls import path
from builder import views

app_name='pokemon_team_builder'

urlpatterns=[
    path('', views.index, name='index'),
]