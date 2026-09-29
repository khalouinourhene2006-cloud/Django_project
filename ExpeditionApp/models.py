from django.db import models

# Create your models here.
class Expedition(models.Model):
    reference=models.CharField(unique=True, max_length=100)
    ville_depart=models.CharField(max_length=60)
    ville_arrive=models.CharField(max_length=60)
    poids_kg=models.DecimalField()
    date_souhaitee=models.DateField()
    description= models.TextField()
    statut=models.CharField(max_length=20, choices=[('p','publiee'),('a','attribuee'),('ec','en_cours'),('l','livree'),('a' ,'annulee')],default='publiee')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    entreprise=models.ForeignKey('EntrepriseApp.entreprise',on_delete=models.CASCADE, related_name='expedition')