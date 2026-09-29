from django.db import models

# Create your models here.
class OffreApp(models.Model):
    prix=models.DecimalField()
    delai_jours=models.PositiveIntegerField()
    statut=models.CharField(max_length=20, choices=[('p','proposee'),('a','acceptee'),('r','refusee'),('re','retiree')],default='proposee')
    date_proposition=models.DateField(auto_now_add=True)
    expedition=models.ForeignKey('ExpeditionApp.expedition', on_delete=models.CASCADE ,related_name='offre')
    transporteur=models.ForeignKey('VehiculeApp.vehicule', on_delete=models.CASCADE ,related_name='vehicule')
    vehicule=models.ForeignKey('VehiculeApp.vehicule', on_delete=models.CASCADE ,related_name='vehicule')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)