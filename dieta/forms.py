from django import forms
from .models import Comida

class ComidaForm(forms.ModelForm):
    nombre = forms.CharField(required=False, label='Comida predefinida o personalizada', widget=forms.TextInput(attrs={'class': 'w-full p-2 border rounded-lg'}))
    custom_comida = forms.CharField(required=False, label='Comida personalizada', widget=forms.TextInput(attrs={'class': 'w-full p-2 border rounded-lg', 'style': 'display:none;'}))

    class Meta:
        model = Comida
        fields = ['nombre', 'custom_comida', 'tipo_comida', 'calorias', 'carbohidratos', 'proteinas', 'grasas']
        widgets = {
            'tipo_comida': forms.Select(attrs={'class': 'w-full p-2 border rounded-lg'}),
            'calorias': forms.NumberInput(attrs={'class': 'w-full p-2 border rounded-lg'}),
            'carbohidratos': forms.NumberInput(attrs={'class': 'w-full p-2 border rounded-lg'}),
            'proteinas': forms.NumberInput(attrs={'class': 'w-full p-2 border rounded-lg'}),
            'grasas': forms.NumberInput(attrs={'class': 'w-full p-2 border rounded-lg'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get('nombre')
        custom_comida = cleaned_data.get('custom_comida')

        predefined_data = {
            'Manzana': {'tipo_comida': 'desayuno', 'calorias': 52, 'carbohidratos': 14, 'proteinas': 0.3, 'grasas': 0.2},
            'Pollo': {'tipo_comida': 'almuerzo', 'calorias': 239, 'carbohidratos': 0, 'proteinas': 27, 'grasas': 14},
    
        }

        if nombre and nombre in predefined_data:
            for field, value in predefined_data[nombre].items():
                cleaned_data[field] = value
        elif nombre == 'Personalizado' and custom_comida:
            cleaned_data['nombre'] = custom_comida
        elif not nombre:
            raise forms.ValidationError('Debe seleccionar una comida predefinida o ingresar una comida personalizada.')

        return cleaned_data