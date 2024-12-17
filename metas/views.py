from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from datetime import date
from .models import MetaNutricional
from logros.models import Logro
from dieta.models import Comida
from .forms import MetaNutricionalForm
from info_usuarios.models import info_usuario

@login_required
def metas_view(request):
    # Obtener o crear metas del usuario
    metas, creado = MetaNutricional.objects.get_or_create(usuario=request.user)
    
    if request.method == 'POST':
        form = MetaNutricionalForm(request.POST, instance=metas)
        if form.is_valid():
            meta = form.save(commit=False)
            meta.usuario = request.user
            meta.save()
            return redirect('metas:metas')
    else:
        form = MetaNutricionalForm(instance=metas)
    
    context = {
        'form': form,
        'metas': metas
    }
    return render(request, 'modulos/metas.html', context)

@login_required
def dashboard_view(request):
    metas = MetaNutricional.objects.get(usuario=request.user)
    user_info = info_usuario.objects.get(user=request.user)
    comidas_diarias = Comida.objects.filter(usuario=request.user, fecha=date.today())
    totales = comidas_diarias.aggregate(
        calorias=Sum('calorias'),
        carbohidratos=Sum('carbohidratos'),
        proteinas=Sum('proteinas'),
        grasas=Sum('grasas')
    )
    # Asegurarse de que los valores no sean None
    calorias_totales = totales.get('calorias', 0) or 0
    carbohidratos_totales = totales.get('carbohidratos', 0) or 0
    proteinas_totales = totales.get('proteinas', 0) or 0
    grasas_totales = totales.get('grasas', 0) or 0

    porcentaje_calorias = min((calorias_totales / metas.calorias_diarias) * 100, 100) if metas.calorias_diarias else 0
    porcentaje_carbohidratos = min((carbohidratos_totales / metas.carbohidratos_diarios) * 100, 100) if metas.carbohidratos_diarios else 0
    porcentaje_proteinas = min((proteinas_totales / metas.proteinas_diarias) * 100, 100) if metas.proteinas_diarias else 0
    porcentaje_grasas = min((grasas_totales / metas.grasas_diarias) * 100, 100) if metas.grasas_diarias else 0

    # Verificar si se ha completado la meta diaria de calorias
    if calorias_totales >= metas.calorias_diarias:
        metas.veces_completadas += 1
        metas.save()
        messages.success(request, '¡Objetivo diario de calorías completado!')

        # Eliminar los alimentos del día para reiniciar el conteo
        comidas_diarias.delete()

        # Verificar si se han completado 3 veces y si el primer login ha sido completado
        if metas.veces_completadas % 3 == 0 and not user_info.primer_login:
            messages.success(request, '¡Has alcanzado un logro por completar tu objetivo diario 3 veces!')
            logro_tres_veces, _ = Logro.objects.get_or_create(nombre='Third Strike')
            if not logro_tres_veces.obtenido:
                logro_tres_veces.obtenido = True
                logro_tres_veces.save()

    # Verificar si se ha completado la meta diaria de carbohidratos
    if carbohidratos_totales >= metas.carbohidratos_diarios:
        messages.success(request, '¡Objetivo diario de carbohidratos completado!')

    # Verificar si se ha completado la meta diaria de proteínas
    if proteinas_totales >= metas.proteinas_diarias:
        messages.success(request, '¡Objetivo diario de proteínas completado!')

    # Verificar si se ha completado la meta diaria de grasas
    if grasas_totales >= metas.grasas_diarias:
        messages.success(request, '¡Objetivo diario de grasas completado!')

    context = {
        'totales': totales,
        'porcentaje_calorias': porcentaje_calorias,
        'porcentaje_carbohidratos': porcentaje_carbohidratos,
        'porcentaje_proteinas': porcentaje_proteinas,
        'porcentaje_grasas': porcentaje_grasas,
        'metas': metas,
        'comidas_diarias': comidas_diarias,
    }
    return render(request, 'dashboard/dashboard.html', context)