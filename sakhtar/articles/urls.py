from django.urls import path
from . import  views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name="list"),
    path('maghalat', views.article_maghalat, name="maghalat"),
    path('sakhtar', views.article_sakhtar, name="sakhtar"),
    path('drsalehi', views.article_salehi, name="salehi"),
    path('drfardi', views.article_fardi, name="fardi"),
   # path('(?P<slug>[\w-]+)/$', views.article_detail, name="detail"),
]