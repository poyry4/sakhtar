from django.urls import path
from . import  views

app_name = 'maghalat'

urlpatterns = [
    path('', views.maghalat, name="maghalat"),
]