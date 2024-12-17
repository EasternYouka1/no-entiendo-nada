from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from .models import info_usuario

class PrimerLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            # URLs que deben ser accesibles incluso sin completar la configuración
            exempt_urls = [
                reverse('info_usuarios:primer_setup'),
                reverse('login:logout'),
                '/admin/',
            ]
            
            if request.path_full not in exempt_urls:
                try:
                    user_info = info_usuario.objects.get(user=request.user)
                    if user_info.primer_login:
                        # Si primer_login es True, redirigir al setup
                        messages.info(request, "Por favor complete su información inicial")
                        return redirect('info_usuarios:primer_setup')
                except info_usuario.DoesNotExist:
                    # Si no existe info_usuario, redirigir al setup
                    messages.info(request, "Por favor complete su información inicial")
                    return redirect('info_usuarios:primer_setup')

        response = self.get_response(request)
        return response