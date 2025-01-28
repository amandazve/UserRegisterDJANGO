
from app_cadastro_usuarios import views
from django.urls import path

urlpatterns = [
    #rota, view responsável e nome de referência
    #usuarios.com
    path('', views.home, name='home'),
    #usuarios.com/usuarios
    path('usuarios/', views.usuarios, name='listagem_usuarios')
]
