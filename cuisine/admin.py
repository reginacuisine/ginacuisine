from django.contrib import admin
from .models import Recette, ContactMessage, Utile, Apropos 

admin.site.register(Recette)
admin.site.register(ContactMessage)
admin.site.register(Apropos)

@admin.register(Utile)
class UtileAdmin(admin.ModelAdmin):
    # On affiche la catégorie pour bien choisir entre Calendrier, Matériel et Santé
    list_display = ('titre', 'categorie')
    list_filter = ('categorie',)