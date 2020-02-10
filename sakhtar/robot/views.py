from django.shortcuts import render

# Create your views here.
def robot(request):
    #articles = Article.objects.all().order_by('date');
    return render(request, 'robot.htm') #, { 'articles': articles })