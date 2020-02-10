from django.shortcuts import render

# Create your views here.
def meeting(request):
    #articles = Article.objects.all().order_by('date');
    return render(request, 'meeting.htm') #, { 'articles': articles })