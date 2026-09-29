from django.db import models

# Create your models here.
class VehiculeApp(models.Model):
    immatriculation=models.CharField(max_length=20, unique=True)
    capacite_kg=models.PositiveIntegerField()
    entreprise=models.ForeignKey('EntrepriseApp.entreprise',on_delete=models.CASCADE, related_name='expedition')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)