from django.contrib import admin

# Register your models here.

from .models import Article, Categorie

class ArticleAdmin(admin.ModelAdmin):
    list_display  = ('nom', 'categorie', 'dateCreation')

class CategorieAdmin(admin.ModelAdmin):
    display = ('nomCateg')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Categorie, CategorieAdmin)