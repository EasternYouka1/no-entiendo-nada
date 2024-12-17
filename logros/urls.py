from django.urls import path
from .views import logros_view

urlpatterns = [
    path('', logros_view, name='lista_logros'),
]