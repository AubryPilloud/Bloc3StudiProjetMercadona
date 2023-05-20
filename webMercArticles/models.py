from django.db import models
from django.utils import timezone
from datetime import date

# Create your models here.

class Article(models.Model):
    nom = models.CharField(max_length=64)
    description = models.TextField()
    prix = models.FloatField(default=10)
    photoArticle = models.ImageField(upload_to='photoArticle', default=None)
    categorie = models.ForeignKey("Categorie", on_delete=models.CASCADE, default=1)
    promo = models.BooleanField(default=False)
    promoPourcent = models.IntegerField("En Pourcent", default=0)
    promoDebut = models.DateField("Date de Début", default=timezone.now)
    promoFin = models.DateField("Date de Fin", default=timezone.now)
    dateCreation = models.DateField(editable=False, default=timezone.now)

    class Meta:
        ordering  = ["-dateCreation"]

    def articleEnPromo(self):
        if self.promo:
            prixPromo = self.prix - (self.prix * (self.promoPourcent / 100))
            return round(prixPromo, 2)
        else:
            return round(self.prix, 2)
        
    def DatesPromo(self):
        if self.promo == True and self.promoDebut <= date.today() and self.promoFin >= date.today():
            return True
        else:
            return False

    def __str__(self):
        return f'{self.nom}'

class Categorie(models.Model):
    nomCateg = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nomCateg}'