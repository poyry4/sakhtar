from django.shortcuts import render

# Create your views here.
def tutorial(request):
    #articles = Article.objects.all().order_by('date');
    return render(request, 'tutorial.htm') #, { 'articles': articles })