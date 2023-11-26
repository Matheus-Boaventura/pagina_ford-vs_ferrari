from django.urls import path
from .views import home, resumo, onde_encontrar

urlpatterns = [
    path('home/', home, name='home'),
    path('resumo/', resumo, name='resumo'),
    path('onde_encontrar/', onde_encontrar, name='onde_encontrar'),
]