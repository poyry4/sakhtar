from django.urls import path
from . import  views

app_name = 'signup'

urlpatterns = [
    path('',  views.signup_view, name="signup"),
    path('ajax/validate_username/', views.validate_username, name='validate_username')
]