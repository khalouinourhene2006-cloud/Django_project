from django.contrib import admin
from .models import Entreprise, Utilisateur
from django.contrib.auth.admin import UserAdmin
from OffreApp.models import offre
from VehiculesApp.models import vehicules
# Register your models here.

admin.site.site_header='TransConnect-Administration'
admin.site.site_title='Transconnect'
admin.site.index_title='Tableau de bord'

class VehiculeInline(admin.TabularInline): 
    model = vehicules 
    extra = 0 
    fields = ('immatriculation', 'type_vehicule', 'capacite_kg', 'disponible') 
    show_change_link = True

class OffreInline(admin.StackedInline): 
    model = offre 
    extra = 0 
    fk_name = 'expedition' 
    readonly_fields = ('transporteur', 'vehicule', 'prix', 'delai_jours', 'statut') 
    show_change_link = True 
    can_delete = False 

class useradmin (UserAdmin):
    list_display = ('user_id','username', 'email', 'is_active','is_superuser')
    list_editable = ('username','is_active','is_superuser')
    search_fields = ('user_id','username', 'email')
    list_filter = ('is_active','is_superuser','role')
    list_per_page = 1
    fieldsets = (('Identification', {'fields': ('user_id','username', 'email', 'is_active','is_superuser')}),
        ('Permissions', {'fields': ('role','groups','user_permissions')}))
    add_fildsets = ((None, {'classes': ('wide',),"fields":('username','role','password1', 'password2','usable_password','email','telephone')}))


class EntrepriseAdmin(admin.ModelAdmin):
    
    list_display = ('raison_social', 'adresse', 'telephone', 'email', 'created_at', 'updated_at')
    search_fields = ('raison_social', 'adresse', 'telephone', 'email')
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (('Identification', {'fields': ('raison_social', 'adresse', 'telephone', 'email')}),
        ('Horodatage', {'fields': ('created_at', 'updated_at'),'classes': ('collapse',)}))


admin.site.register (Entreprise)
admin.site.register (Utilisateur,useradmin)
# Register your models here.
