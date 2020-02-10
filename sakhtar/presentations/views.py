from django.shortcuts import render

# Create your views here.
def presentations(request):
    #articles = Article.objects.all().order_by('date');
    return render(request, 'presentations.htm') #, { 'articles': articles })