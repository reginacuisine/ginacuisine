from django.shortcuts import render, redirect
# 1. AJOUT de 'Utile' ici
from .models import Recette, ContactMessage
from .models import Utile
from datetime import datetime
import locale
from .models import Apropos

def home(request):
    query = request.GET.get('q') # On récupère ce qui est tapé dans le footer
    if query:
        # On cherche dans le titre de la recette (insensible à la casse)
        recettes = Recette.objects.filter(titre__icontains=query)
    else:
        recettes = Recette.objects.all()[:6]
        
    return render(request, 'cuisine/home.html', {'recettes': recettes, 'query': query})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        ContactMessage.objects.create(name=name, email=email, message=message)
        return redirect('contact')
    return render(request, 'cuisine/contact.html')

def liste_par_categorie(request, nom_categorie):
    titre_propre = nom_categorie.replace('_', ' ').capitalize()
    recettes = Recette.objects.filter(categorie=nom_categorie)
    return render(request, 'cuisine/categorie.html', {
        'recettes': recettes,
        'nom_categorie': titre_propre
    })

# VERSION UNIQUE ET CORRIGÉE DU MENU
def menu_semaine(request):
    try:
        locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")
    except:
        locale.setlocale(locale.LC_TIME, "")

    maintenant = datetime.now()
    nom_jour = maintenant.strftime('%A').upper() 
    date_du_jour = maintenant.strftime('%d %B %Y')

    # Filtre les recettes selon le jour réglé dans l'admin
    recettes_du_jour = Recette.objects.filter(jour_menu=nom_jour)

    return render(request, 'cuisine/menu_semaine.html', {
        'recettes': recettes_du_jour,
        'nom_jour': nom_jour,
        'date_du_jour': date_du_jour
    })


def utile_liste(request, slug_utile):
    # On filtre les éléments par la catégorie choisie (ex: 'calendrier')
    elements = Utile.objects.filter(categorie=slug_utile)
    
    # On définit le nom de la page pour le titre h1
    noms = {
        'calendrier': 'Calendrier des fruits & légumes de saison',
        'materiel': 'Mon matériel de cuisine',
        'sante': 'Rééquilibrage alimentaire',
    }
    
    context = {
        'elements': elements,
        'slug': slug_utile,
        'nom_page': noms.get(slug_utile, "Utile") # C'est ici que le titre se joue
    }
    return render(request, 'cuisine/utile_liste.html', context)

def apropos_view(request):
    # On récupère le premier contenu "À propos" enregistré en admin
    contenu = Apropos.objects.first() 
    return render(request, 'cuisine/apropos.html', {'apropos': contenu})
