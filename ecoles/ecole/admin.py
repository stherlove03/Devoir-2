from django.contrib import admin
from .models import Etudiants

# Register your models here.
class affichagetable(admin.ModelAdmin):
    list_display = ['id','prenom','nom','pays','adresse','telephone']
    
admin.site.register(Etudiants, affichagetable)
