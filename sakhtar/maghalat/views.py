from django.shortcuts import render

# Create your views here.
def maghalat(request):
    #articles = Article.objects.all().order_by('date');
    return render(request, 'maghalat.htm') #, { 'articles': articles })