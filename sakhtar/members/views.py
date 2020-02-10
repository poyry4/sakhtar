from django.shortcuts import render

# Create your views here.
def members_katebi(request):
    #articles = Article.objects.all().order_by('date');
    return render(request, 'members_katebi.htm') #, { 'articles': articles })A

def members_salehi(request):
    #articles = Article.objects.all().order_by('date');
    return render(request, 'members_salehi.htm') #, { 'articles': articles })A
def members_fardi(request):
    #articles = Article.objects.all().order_by('date');
    return render(request, 'members_fardi.htm') #, { 'articles': articles })A