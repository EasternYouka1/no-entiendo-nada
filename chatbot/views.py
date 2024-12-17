from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import google.generativeai as ga
from concurrent.futures import ThreadPoolExecutor
from info_usuarios.models import info_usuario

api_key = 

ga.configure(api_key=api_key)
model = ga.GenerativeModel('gemini-1.5-flash')

executor = ThreadPoolExecutor(max_workers=3)

def chat_home(request):
    return render(request, 'chat/chat.html')

def generate_response(message):
    response = model.generate_content(message)
    return response.text

@csrf_exempt
def chat_message(request):
    if request.method == 'POST':
        try:
            user_info = info_usuario.objects.get(user=request.user)
            datos = json.loads(request.body)
            mensaje_usuario = datos.get('message', '')
            


            
            if user_info.preferencias_alimentarias == "1":
                result = "Soy Vegetariano"
            elif user_info.preferencias_alimentarias == "2":
                result = "Soy Vegano"
            elif user_info.preferencias_alimentarias == "3":
                result = "no como alimentos con gluten"
            elif user_info.preferencias_alimentarias == "4":
                result = "Soy Intolerante a la Lactosa"
            elif user_info.preferencias_alimentarias == "5":
                result = ""

            # Concatenar la información de las preferencias alimentarias con el mensaje del usuario
            mensaje_usuario = f" {result}. {mensaje_usuario}"
            print(f"Mensaje del usuario: {mensaje_usuario}")

            # Generar la respuesta con la información adicional
            respuesta = executor.submit(generate_response, mensaje_usuario).result()

            return JsonResponse({
                'response': respuesta
            })
        except Exception as e:
            print(f"Error: {str(e)}")
            return JsonResponse({
                'error': 'error encontrado intentelo mas tarde',
                'details': str(e)
            }, status=500)
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)