from django.contrib import admin
from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 

# Ajoute 'success_view' à la fin de cette liste d'import
from cuisine.views import home, contact, liste_par_categorie, menu_semaine, utile_liste, apropos_view, success_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('categorie/<str:nom_categorie>/', liste_par_categorie, name='categorie'),
    path('menu-de-la-semaine/', menu_semaine, name='menu_semaine'),
    
    # Section UTILE (Calendrier, Matériel, Santé)
    path('utile/<str:slug_utile>/', utile_liste, name='utile_cat'),
    
    # Section À PROPOS
    path('a-propos/', apropos_view, name='apropos'),
    
    # Correction ici : on utilise 'success_view' directement (sans views.)
    path('success/', success_view, name='success'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)