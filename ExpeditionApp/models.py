from django.db import models
from django.core.validators import MinLengthValidator ,MaxLengthValidator, RegexValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.
class Expedition(models.Model):
    reference=models.CharField(unique=True, max_length=100, editable=False)
    ville_depart=models.CharField(max_length=60)
    ville_arrive=models.CharField(max_length=60)
    poids_kg=models.DecimalField( max_digits=10,decimal_places=3,validators=[MinValueValidator(0.001, "Le poids doit être supérieur à 0 kg.") ])
    date_souhaitee=models.DateField()
    description= models.TextField(blank=True,null=True)
    statut=models.CharField(max_length=20, choices=[('p','publiee'),('a','attribuee'),('ec','en_cours'),('l','livree'),('a' ,'annulee')],default='p')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    entreprise=models.ForeignKey(Entreprise,on_delete=models.CASCADE, related_name='expeditions')

 def clean(self):
        super().clean()
        if self.entreprise_id and self.entreprise.type_entreprise != 'c':
            raise ValidationError("une expedition ne peut être créée que par un chargeur")

def _generate_reference(cls):
        annee = timezone.now().strftime('%Y')
        prefixe = annee
        dernier=(cls.objects.filter(reference__startswith=prefixe).order_by('reference').last()) 
        compteur = (int(dernier.reference[-5]) + 1 
        if dernier else 1)
        if compteur > 99999:
            raise ValidationError("Limit exceeded .")
        return f"{prefixe}{compteur:05d}"
    
 def save(self, *args, **kwargs):
        if not self.reference:
            self.reference = self._generate_reference()
        #fct appellé pour appliquer les validateurs
        self.full_clean()
        super().save(*args, **kwargs)