from django.urls import path
from .views import listar_produtos

urlpatterns = [
    path('listar_produtos', listar_produtos),
]
