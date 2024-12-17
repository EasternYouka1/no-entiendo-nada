from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import LoginForm
from django.contrib import messages
from .forms import RegisterForm
from info_usuarios.models import info_usuario
from django.contrib.auth import logout

def landing(request):
    return render(request, "landing/index.html")

@login_required
def home(request):
    return render(request, "dashboard/dashboard.html", {})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                try:
                    user_info = info_usuario.objects.get(user=user)
                    if user_info.primer_login:
                        return redirect('info_usuarios:primer_setup')  
                    else:
                        return redirect('dieta:dashboard') 
                except info_usuario.DoesNotExist:
                    return redirect('info_usuarios:primer_setup')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos')
    else:
        form = LoginForm()
    
    return render(request, 'registration/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '¡Registro exitoso!')
            return redirect('login:login')
    else:
        form = RegisterForm()
    
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def logout_view(request):
    
    return render(request, 'landing/index.html')