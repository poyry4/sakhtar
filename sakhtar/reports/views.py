from django.shortcuts import render

# Create your views here.
def reports(request):
    #articles = Article.objects.all().order_by('date');
    return render(request, 'reports.htm') #, { 'articles': articles })
