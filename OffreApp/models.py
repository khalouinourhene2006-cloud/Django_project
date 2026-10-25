from django.db import models
from EntrepriseApp.models import Entreprise
from VehiculeApp.models import Vehicule
from ExpeditionApp.models import Expedition
from decimal import Decimal
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
# Create your models here.
class OffreApp(models.Model):
    prix=models.DecimalField(max_digits=10,decimal_places=3)
    delai_jours=models.PositiveIntegerField()
    statut=models.CharField(max_length=20, choices=[('p','proposee'),('a','acceptee'),('r','refusee'),('re','retiree')],default='p')
    date_proposition=models.DateField(auto_now_add=True)
    entreprise =models.ForeignKey(Entreprise, on_delete=models.CASCADE,related_name='offres')
    expedition =models.ForeignKey(Expedition, on_delete=models.CASCADE,related_name='offres')
    vehicule=models.ForeignKey(Vehicule, on_delete=models.CASCADE,related_name='offres')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    def clean(self):
        super().clean()
        if self.entreprise_id and self.entreprise.type_entreprise != 't':
            raise ValidationError("une offre ne peut pas etre faite par un transporteur.")
        if self.vehicule_id and self.vehicule.entreprise_id != self.entreprise_id:
            raise ValidationError("Le véhicule associé à l'offre doit appartenir à la même entreprise que l'offre.")
        if self.expedition_id and self.expedition.statut != 'publiee':
            raise ValidationError("L'expédition associée à l'offre doit être publiée pour pouvoir recevoir des offres.")
        if offre.objects.filter(entreprise_id=self.entreprise_id, expedition_id=self.expedition_id, statut='proposee').exclude(pk=self.pk).exists():
            raise ValidationError("Cette entreprise a déjà une offre proposée pour cette expédition.")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.statut == 'a' and self.expedition_id:
            self.expedition.statut = 'attribuee'
            self.expedition.save()
        offre.objects.filter(expedition_id=self.expedition_id, statut='proposee').update(statut='r')