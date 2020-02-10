from django.shortcuts import render

# Create your views here.
def schedule(request):
    #articles = Article.objects.all().order_by('date');
    return render(request, 'schedule.htm') #, { 'articles': articles })