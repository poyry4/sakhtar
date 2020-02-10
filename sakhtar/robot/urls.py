from django.urls import path
from . import  views

app_name = 'robot'

urlpatterns = [
    path('', views.robot, name="robot"),
]