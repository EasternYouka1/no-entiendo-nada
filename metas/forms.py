from django import forms
from .models import MetaNutricional

class MetaNutricionalForm(forms.ModelForm):
    class Meta:
        model = MetaNutricional
        fields = ['calorias_diarias', 'carbohidratos_diarios', 'proteinas_diarias', 'grasas_diarias', 'vasos_agua']
        widgets = {
            'calorias_diarias': forms.NumberInput(attrs={'class': 'w-full p-2 border rounded-lg'}),
            'carbohidratos_diarios': forms.NumberInput(attrs={'class': 'w-full p-2 border rounded-lg'}),
            'proteinas_diarias': forms.NumberInput(attrs={'class': 'w-full p-2 border rounded-lg'}),
            'grasas_diarias': forms.NumberInput(attrs={'class': 'w-full p-2 border rounded-lg'}),
            'vasos_agua': forms.NumberInput(attrs={'class': 'w-full p-2 border rounded-lg'}),
        }