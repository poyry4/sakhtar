from django.shortcuts import render

# Create your views here.

def database(request):
    #articles = Article.objects.all().order_by('date');
    return render(request, 'database.htm') #, { 'articles': articles })