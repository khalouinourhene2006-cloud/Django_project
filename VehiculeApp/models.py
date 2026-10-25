from django.db import models
from EntrepriseApp.models import Entreprise
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
# Create your models here.
CAPACITES_VEHICULE = {'camionnette': (1, 1500),'fourgon': (1, 3500),'camion_porteur': (3500, 19000),'semi_remorque': (19000, 26000)}
class VehiculeApp(models.Model):
    immatriculation=models.CharField(max_length=20, unique=True)
    type_vehicule=models.CharField(max_length=100,choices=[('c','camionnette'),('f','fourgon'),('sr','semi-remorque'),('cp','camion porteur')])
    capacite_kg=models.PositiveIntegerField(validators=[MinLengthValidator(1, "capacite_kg doit etre sup a 0") ])
    entreprise=models.ForeignKey(Entreprise,on_delete=models.CASCADE, related_name='vehicules')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    def clean(self):
        super().clean()
        if self.type_vehicule in CAPACITES_VEHICULE and self.capacite_kg is not None:
            minimum, maximum = CAPACITES_VEHICULE[self.type_vehicule]
            if not minimum <= self.capacite_kg <= maximum:
                raise ValidationError({'capacite_kg': f"La capacite doit etre entre {minimum} et {maximum} kg pour ce type de vehicule."})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    def __str__(self):
        return self.immatriculation