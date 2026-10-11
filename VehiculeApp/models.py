from django.db import models
from EntrepriseApp.models import Entreprise
from django.core.validators import MaxLengthValidator, MinLengthValidator, MinValueValidator
# Create your models here.
class VehiculeApp(models.Model):
    immatriculation=models.CharField(max_length=20, unique=True)
    type_vehicule=models.CharField(max_length=100,choices=[('c','camionnette'),('f','fourgon'),('sr','semi-remorque'),('cp','camion porteur')])
    capacite_kg=models.PositiveIntegerField(validators=[MinLengthValidator(1, "capacite_kg doit etre sup a 0") ])
    entreprise=models.ForeignKey(Entreprise,on_delete=models.CASCADE, related_name='vehicules')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)