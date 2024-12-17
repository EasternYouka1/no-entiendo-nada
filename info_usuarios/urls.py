from django.urls import path
from .views import primer_login , perfil_usuario

urlpatterns = [
    path('setup/', primer_login, name="primer_setup"),
    path('perfil/', perfil_usuario, name="perfil_usuario"),
]