from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('kitaplar', views.books, name="books"),
    
    
    path('hakkimda', views.about, name="about"),
    path('iletisim', views.about_form, name="about_form"),
    
    path('podcast', views.podcast, name="podcast"),
    path('podcast/bencesi', views.bencesi, name="bencesi"),
    
    
    path('yazilar', views.articles, name="articles"),
    path('yazilar/<slug:slug>', views.yazilar, name="yazi"),
    path('yazilar/Oduller', views.toyp_odul, name="toyp_odul"),
    
    
    path('kitaplar/secilmishuzursuzluk', views.secilmishuzursuzluk, name="secilmishuzursuzluk"),
    path('kitaplar/varligiminkabuledildigigun', views.varligiminkabuledildigigun, name="varligiminkabuledildigigun"),
    
    path('mentorluk/mentorlukhizmeti', views.mentorluk1, name="mentorluk1"),
    path('mentorluk/mentorluktanım-2', views.mentorluk2, name="mentorluk2"),
    path('mentorluk/gereklikosullar', views.mentorluk3, name="mentorluk3"),
    
    
    
    path('haberler', views.haberler, name="haberler"),
    
    
    path("projeler", views.projeler, name="projeler")
]

