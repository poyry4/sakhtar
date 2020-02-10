from django.urls import path
from . import  views

app_name = 'members'

urlpatterns = [
    path('', views.members_katebi, name="members_katebi"),
    path('', views.members_salehi, name="members_salehi"),
    path('', views.members_fardi, name="members_fardi"),
]