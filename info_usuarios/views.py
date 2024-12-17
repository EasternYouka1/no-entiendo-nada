from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import primer_setup 
import logging
from .models import info_usuario
from metas.models import MetaNutricional
from logros.models import Logro
import numpy as np
import tensorflow as tf
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from .models import info_usuario

logger = logging.getLogger(__name__)

@login_required
def primer_login(request):
    try:
        user_info = info_usuario.objects.get(user=request.user)
        if not user_info.primer_login:

            return redirect('dieta:dashboard')
    except info_usuario.DoesNotExist:
        user_info = None

    if request.method == "POST":
        form = primer_setup(request.POST)
        if form.is_valid():
            try:
                # Guardar la información del usuario
                user_info, created = info_usuario.objects.update_or_create(
                    user=request.user,
                    defaults={
                        'edad': form.cleaned_data['edad'],
                        'peso': form.cleaned_data['peso'],
                        'altura': form.cleaned_data['altura'],
                        'nivel_actividad': form.cleaned_data['nivel_actividad'],
                        'genero': form.cleaned_data['genero'],
                        'litros_dia': form.cleaned_data['litros_dia'],
                        'comidas_dia': form.cleaned_data['comidas_dia'],
                        'preferencias_alimentarias': form.cleaned_data['preferencias_alimentarias'],
                        'primer_login': False
                    }
                )

                # Cargar el modelo
                modelo = tf.keras.models.load_model('info_usuarios/modelo_calorias.h5')

                # Preparar los datos para la predicción
                datos_usuario = np.array([[user_info.edad, user_info.peso, user_info.nivel_actividad]], dtype=np.float32)

                # Realizar la predicción
                calorias_recomendadas = float(modelo.predict(datos_usuario)[0][0])
                logro_primer_setup = Logro.objects.get(nombre='Primer Login')
                logro_primer_setup.obtenido = True
                logro_primer_setup.save()

                # Imprimir las calorías recomendadas
                print(f"Calorías diarias recomendadas: {calorias_recomendadas:.2f} kcal")

                # Nos aseguramos que las caloris sean un valor con sentido

                vasos_agua = user_info.litros_dia

         

                # Guardar las calorías diarias recomendadas en MetaNutricional
                MetaNutricional.objects.update_or_create(
                    usuario=request.user,
                    defaults={
                        'calorias_diarias': calorias_recomendadas,
                        'vasos_agua': vasos_agua
                        
                    }
                )



                
                return redirect('dieta:dashboard')
            except Exception as e:
                logger.error(f"Error al guardar la configuración inicial: {str(e)}")

    else:
        form = primer_setup()

    return render(request, 'primer_login/setup.html', {'form': form})




@login_required
def perfil_usuario(request):
    user_info = info_usuario.objects.get(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_info)
        if form.is_valid():
            form.save()
            return redirect('info_usuarios:perfil_usuario')
    else:
        form = UserProfileForm(instance=user_info)
    
    imc = user_info.peso / ((user_info.altura / 100) ** 2)
    
    return render(request, 'modulos/perfil_usuario.html', {
        'form': form,
        'user_info': user_info,
        'imc': imc,
    })