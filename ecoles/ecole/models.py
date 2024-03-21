from django.db import models

# Create your models here.
from django.db import models


class Etudiants(models.Model):
    prenom = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    pays = models.CharField(max_length=50, blank=True, null=True)
    adresse = models.CharField(max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'etudiants'
