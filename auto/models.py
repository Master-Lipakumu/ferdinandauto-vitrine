from django.db import models

# Create your models here.
from django.contrib.auth.models import User



class Article(models.Model):

    image = models.ImageField(upload_to='articles_images/')

    nom = models.CharField(max_length=100)

    details = models.TextField()

    prix = models.DecimalField(max_digits=10, decimal_places=2)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom
    


class ContactForm(models.Model):

    nom_complet = models.CharField(max_length=100)

    objet = models.CharField(max_length=200)

    email = models.EmailField()

    contenu_message = models.TextField()

    def __str__(self):
        return self.objet
