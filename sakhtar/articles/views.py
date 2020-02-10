from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms
 
def article_list(request):
    #articles = Article.objects.all().order_by('date');
    return render(request, 'articles/articles.htm') #, { 'articles': articles })


def article_maghalat(request):
    #articles = Article.objects.all().order_by('date');
    return render(request, 'articles/maghalat.htm') #, { 'articles': articles })

def article_sakhtar(request):
    #articles = Article.objects.all().order_by('date');
    return render(request, 'articles/sakhtar.htm') #, { 'articles': articles })

def article_salehi(request):
    #articles = Article.objects.all().order_by('date');
    return render(request, 'articles/salehi.htm') #, { 'articles': articles })

def article_fardi(request):
    #articles = Article.objects.all().order_by('date');
    return render(request, 'articles/fardi.htm') #, { 'articles': articles })



#@login_required(login_url="/accounts/login/")
#def article_create(request):
#    if request.method == 'POST':
#        form = forms.CreateArticle(request.POST, request.FILES)
#        if form.is_valid():
#            # save article to db
#            instance = form.save(commit=False)
#            instance.author = request.user
#            instance.save()
#            return redirect('articles:list')
#    else:
#        form = forms.CreateArticle()
#    return render(request, 'articles/create.htm', { 'form': form })
