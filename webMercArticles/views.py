from django.shortcuts import render

# Create your views here.

from .models import Article, Categorie
from django.conf import settings

def accueil_view(request):
    return render(request, "pages/accueil.html")

def catalogue(request):

    if request.GET.get('choixCateg') and request.GET.get('choixCateg') != "":
        featured_filter = request.GET.get('choixCateg')
        listings = Article.objects.filter(categorie=featured_filter)
    else:
        listings = Article.objects.all()

    c = {'articles': listings, 
         'categories': Categorie.objects.all(),}

    return render(request, 'pages/catalogue.html', context=c)