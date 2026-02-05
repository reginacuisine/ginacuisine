from django.contrib import admin
from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 
# On importe 'apropos_view' au lieu de 'apropros'
from cuisine.views import home, contact, liste_par_categorie, menu_semaine, utile_liste, apropos_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('categorie/<str:nom_categorie>/', liste_par_categorie, name='categorie'),
    path('menu-de-la-semaine/', menu_semaine, name='menu_semaine'),
    
    # Section UTILE (Calendrier, Matériel, Santé)
    path('utile/<str:slug_utile>/', utile_liste, name='utile_cat'),
    
    # Section À PROPOS : on utilise directement la fonction importée
    path('a-propos/', apropos_view, name='apropos'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)