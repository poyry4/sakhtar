from django.shortcuts import render

# Create your views here.
def leaflets(request):
    #articles = Article.objects.all().order_by('date');
    return render(request, 'leaflets.htm') #, { 'articles': articles })