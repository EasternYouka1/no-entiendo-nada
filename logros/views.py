from django.shortcuts import render
from .models import Logro
from django.db.models import Sum

def logros_view(request):
    logros_obtenidos = Logro.objects.filter(obtenido=True)
    logros_restantes = Logro.objects.filter(obtenido=False)
    puntos_totales = logros_obtenidos.aggregate(Sum('puntos'))['puntos__sum'] or 0

    context = {
        'logros_obtenidos': logros_obtenidos,
        'logros_restantes': logros_restantes,
        'puntos_totales': puntos_totales,
    }
    return render(request, 'modulos/logros.html', context)