from django.test import TestCase

# Create your tests here.

from webMercArticles.models import *
import datetime


class testModel(TestCase):

    @classmethod
    def setUpTestData(cls):
        Article.objects.create(nom='ArticleTest1')
        Categorie.objects.create(nomCateg='CategoTest') #Nécessaire Pour le ForeignKey des Articles
        Article.objects.create(nom='ArticleTest2',
                               promo = True,
                               promoDebut= datetime.date.today() - datetime.timedelta(weeks=1), 
                               promoFin= datetime.date.today() + datetime.timedelta(weeks=1))
        Article.objects.create(nom='ArticleTest3',
                               promo = True,
                               promoDebut= datetime.date.today() - datetime.timedelta(weeks=1), 
                               promoFin= datetime.date.today() - datetime.timedelta(days=1))
        Article.objects.create(nom='ArticleTest4',
                               prix = 60,
                               promo = True,
                               promoPourcent = 24)


    def test_nom_label(self):
        article = Article.objects.get(id=1)
        champLabel = article._meta.get_field('nom').verbose_name
        self.assertEqual(champLabel, 'nom')

    def test_prix_label(self):
        article = Article.objects.get(id=1)
        champLabel = article._meta.get_field('prix').verbose_name
        self.assertEqual(champLabel, 'prix')

    def test_prix_defaut(self):
        article = Article.objects.get(id=1)
        prixDefaut = article._meta.get_field('prix').default
        self.assertEqual(prixDefaut, 10)

    def test_dateLimite_true(self):
        article = Article.objects.get(id=2) 
        self.assertEqual(article.DatesPromo(), True)

    def test_dateLimite_false(self):
        article = Article.objects.get(id=3)
        self.assertEqual(article.DatesPromo(), False)

    def test_prix_promo(self):
        article = Article.objects.get(id=4)
        self.assertEqual(article.articleEnPromo(), 45.6)