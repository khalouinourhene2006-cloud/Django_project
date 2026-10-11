from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.utils import timezone

def validate_email(value):
    if not value:
        raise ValidationError ("l'adresse emailest obligatoire")
    if not value.endswith("@gmail.com"):
        raise VAlidationError("l'adresse email doit se terminer par @gmail.com")

matricule_fiscale_validator=RegexValidator(regex=r'^\d{7}[/ -]?[A-Za-z][/ -]?[ABDNPEabdnpe][/ -]?[MPCNEmpcne][/ -]?\d{3}$', message="format erroné")
# Create your models here.
class Utilisateur(AbstractUser):
    user_id= models.CharField(primary_key=True, max_length=8)
    email=models.EmailField(unique=True, validators=[validate_email])
    telephone= models.CharField(max_length=15, blank=True ,null=True)
    role=models.CharField(max_length=20, choices=[('admin','Admin'),('c','Chargeur'),('t', 'Transporteur')], default='c')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

 def _generate_user_id(cls):
        annee = timezone.now().strftime('%y')
        prefixe = f"{annee}user"
        dernier = (cls.objects.filter(user_id__startswith=prefixe).order_by('-user_id').first())
        compteur = int(dernier.user_id[-2:]) + 1 if dernier else 0
        if compteur > 99:
            raise ValidationError("pas plus de 99")
        return f"{prefixe}{compteur:02d}"

 def save(self, *args, **kwargs):
        if not self.user_id:
            self.user_id = self._generate_user_id()

        self.full_clean()
        super().save(*args, **kwargs)



class Entreprise(models.Model):
    raison_social= models.CharField(max_length=200, blank=False ,null=False)
    matricule_fiscale = models.CharField(max_length=17 ,unique=True, validators=[matricule_fiscale_validator])
    adresse = models.TextField(validators=[MinLengthValidator(20, "l'adresse ne peut pas avoir moins de 20 char"),MinLengthValidator(400, "l'adressene peut pas passer les 400 char")])
    type_entreprise= models.CharField(max_length=100, choices=[('c','Chargeur') ,('t','Transporteur')], default='c')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    gerant=models.OneToOneField(Utilisateur, on_delete=models.CASCADE, related_name='Entreprise')
    
