from django.urls import path
from . import  views

app_name = 'presentations'

urlpatterns = [
    path('', views.presentations, name="presentations"),
]