from django.db import models

class Recette(models.Model):
    CATEGORIES = [
        ('salade', 'Salade'),
        ('plat_burkinabe', 'Plat burkinabé'),
        ('plat_international', 'Plat international'),
        ('dessert', 'Dessert'),
        ('boisson', 'Boisson | Cocktail'),
        ('petit_dejeuner', 'Petit-déjeuner'),
    ]

    CHOIX_JOURS = [
        ('LUNDI', 'Lundi'), ('MARDI', 'Mardi'), ('MERCREDI', 'Mercredi'),
        ('JEUDI', 'Jeudi'), ('VENDREDI', 'Vendredi'), ('SAMEDI', 'Samedi'),
        ('DIMANCHE', 'Dimanche'), ('AUCUN', 'Pas au menu'),
    ]

    titre = models.CharField(max_length=200)
    categorie = models.CharField(max_length=50, choices=CATEGORIES)
    image = models.ImageField(upload_to='recettes/', null=True, blank=True)
    ingredients = models.TextField(blank=True)
    instructions = models.TextField(blank=True)
    jour_menu = models.CharField(max_length=20, choices=CHOIX_JOURS, default='AUCUN', verbose_name="Jour de vente")
    date_creation = models.DateTimeField(auto_now_add=True)
    prix = models.DecimalField(max_digits=10, decimal_places=0, default=0, verbose_name="Prix (FCFA)")
    temps_cuisson = models.IntegerField(default=0, verbose_name="Temps de cuisson (minutes)")

    def __str__(self):
        return self.titre

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message de {self.name}"
    

class Utile(models.Model):
    CATEGORIES_UTILES = [
        ('calendrier', 'Calendrier des fruits & légumes de saison'),
        ('materiel', 'Mon matériel de cuisine'),
        ('sante', 'Rééquilibrage alimentaire'),
    ]
    
    # Pour le calendrier, le titre sera la saison (ex: Hiver)
    titre = models.CharField(max_length=200, verbose_name="Titre ou Saison")
    categorie = models.CharField(max_length=50, choices=CATEGORIES_UTILES)
    
    # Contenu flexible pour tes listes ou descriptions
    liste_fruits = models.TextField(blank=True, help_text="Uniquement pour le calendrier")
    liste_legumes = models.TextField(blank=True, help_text="Uniquement pour le calendrier")
    description_generale = models.TextField(blank=True, help_text="Pour le matériel ou la santé")
    
    image = models.ImageField(upload_to='utiles/', null=True, blank=True)

    def __str__(self):
        return f"{self.get_categorie_display()} - {self.titre}"
    

# --- Aligne cette ligne tout à gauche (colonne 0) ---
class Apropos(models.Model):
    titre = models.CharField(max_length=200, default="À propos de moi")
    image = models.ImageField(upload_to='apropos/', null=True, blank=True)
    description = models.TextField(help_text="Racontez votre parcours culinaire ici")
    citation = models.CharField(max_length=255, blank=True, help_text="Une petite phrase qui vous inspire")

    class Meta:
        verbose_name = "À Propos"
        verbose_name_plural = "À Propos"

    def __str__(self):
        return self.titre