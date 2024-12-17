from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from datetime import date
from metas.models import MetaNutricional, ConsumoAgua
from .forms import ComidaForm
from dieta.models import Comida

@login_required
def dashboard(request):
    metas = MetaNutricional.objects.get_or_create(usuario=request.user)[0]
    
    # Obtener comidas del día
    hoy = date.today()
    comidas_diarias = Comida.objects.filter(usuario=request.user, fecha=hoy)
    
    # Calcular totales del día
    totales = comidas_diarias.aggregate(
        calorias=Sum('calorias'),
        carbohidratos=Sum('carbohidratos'),
        proteinas=Sum('proteinas'),
        grasas=Sum('grasas')
    )
    
    # Obtener ingesta de agua
    consumo_agua = ConsumoAgua.objects.get_or_create(usuario=request.user, fecha=hoy)[0]
    #  Instancia de calorias_diarias
    calorias_diarias = metas.calorias_diarias
    # Calcular porcentajes
    porcentaje_calorias = (totales['calorias'] or 0) / metas.calorias_diarias * 100 if metas.calorias_diarias else 0
    porcentaje_agua = (consumo_agua.vasos / metas.vasos_agua * 100) if metas.vasos_agua else 0
    if porcentaje_calorias > 100:
        porcentaje_calorias = 100
    
    else:
        porcentaje_calorias     
        
    context = {
        'metas': metas,
        'totales': totales,
        "calorias_diarias": calorias_diarias,
        'consumo_agua': consumo_agua,
        'porcentaje_calorias': porcentaje_calorias,
        'porcentaje_agua': porcentaje_agua,
        'comidas_diarias': comidas_diarias,
    }
    
    return render(request, 'dashboard/dashboard.html', context)

@login_required
def dieta(request):
    hoy = date.today()
    comidas = Comida.objects.filter(usuario=request.user, fecha=hoy)
    
    if request.method == 'POST':
        form = ComidaForm(request.POST)
        if form.is_valid():
            comida = form.save(commit=False)
            comida.usuario = request.user
            comida.fecha = hoy
            comida.save()
            print("Comida guardada:", comida)  # Mensaje de depuración
            return redirect('dieta:dieta')
        else:
            print("Formulario no válido:", form.errors)  # Mensaje de depuración
    else:
        form = ComidaForm()
    
    # Calcular totales del día
    totales = comidas.aggregate(
        calorias=Sum('calorias'),
        carbohidratos=Sum('carbohidratos'),
        proteinas=Sum('proteinas'),
        grasas=Sum('grasas')
    )
    
    context = {
        'form': form,
        'comidas': comidas,
        'totales': totales,
    }
    return render(request, 'modulos/dieta.html', context)
@login_required
def eliminar_comida(request, comida_id):
    comida = get_object_or_404(Comida, id=comida_id, usuario=request.user)
    comida.delete()
   
    return redirect('dieta:dieta')

@login_required
def editar_comida(request, comida_id):
    comida = get_object_or_404(Comida, id=comida_id, usuario=request.user)
    
    if request.method == 'POST':
        form = ComidaForm(request.POST, instance=comida)
        if form.is_valid():
            form.save()
           
            return redirect('dieta:dieta')
    else:
        form = ComidaForm(instance=comida)
    
    context = {
        'form': form,
        'comida': comida
    }
    return render(request, 'modulos/editar_comida.html', context)

@login_required
def registrar_agua(request):

    consumo_agua = MetaNutricional.objects.get_or_create(usuario=request.user)[0]
    
    if request.method == 'POST':
        if 'sumar' in request.POST:
            consumo_agua.vasos_agua += 1
        elif 'restar' in request.POST and consumo_agua.vasos_agua > 0:
            consumo_agua.vasos_agua -= 1
        consumo_agua.save()
       
        return redirect('dieta:dashboard')
    
    return redirect('dieta:dashboard')