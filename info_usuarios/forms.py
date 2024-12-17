from django import forms
from .models import info_usuario

genero = (("M", "Hombre"), 
          ("F", "Mujer"))

nivel_actividad = ( 
                (1, "Sedentario"), 
                (2, "Moderado"), 
                (3, "Activo")
                  ) 
                  

preferencias_alimentarias = (("1", "Vegetarianos"), 
                          ("2", "Veganos"), 
                          ("3", "Gluten-free"), 
                          ("4", "Lactosa"),
                          ("5", "Ninguna"))


class primer_setup(forms.Form):
    edad = forms.IntegerField(min_value=0, max_value=120)
    peso = forms.FloatField(min_value=20, max_value=300)
    altura = forms.FloatField(min_value=50, max_value=250)
    litros_dia = forms.IntegerField(min_value=0, max_value=200)
    comidas_dia = forms.IntegerField(min_value=0, max_value=20)
    preferencias_alimentarias = forms.ChoiceField(choices=preferencias_alimentarias)
    nivel_actividad = forms.ChoiceField(choices=nivel_actividad)
    genero = forms.ChoiceField(choices=genero)

    def __init__(self, *args, **kwargs):
        super(primer_setup, self).__init__(*args, **kwargs)
        self.fields['edad'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ingrese su edad'
        })
        self.fields['peso'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ingrese su peso en kg'
        })
        self.fields['altura'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ingrese su altura en cm'
        })
        self.fields['nivel_actividad'].widget.attrs.update({'class': 'form-control'})
        self.fields['genero'].widget.attrs.update({'class': 'form-control'})
        self.fields['litros_dia'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ingrese la cantidad vasos de agua que consume diariamente'
        })
        
        self.fields['comidas_dia'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ingrese la cantidad de comidas que consume diariamente'
        })
        self.fields['preferencias_alimentarias'].widget.attrs.update({'class': 'form-control'})

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = info_usuario
        fields = ['edad', 'peso', 'altura', 'litros_dia', 'comidas_dia', 'preferencias_alimentarias', 'nivel_actividad', 'genero']

    edad = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ingrese su edad'
    }))
    peso = forms.FloatField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ingrese su peso en kg'
    }))
    altura = forms.FloatField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ingrese su altura en cm'
    }))
    litros_dia = forms.FloatField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ingrese la cantidad vasos de agua que consume diariamente'
    }))
    comidas_dia = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ingrese la cantidad de comidas que consume diariamente'
    }))
    preferencias_alimentarias = forms.ChoiceField(choices=[
        ('1', 'Vegetarianos'),
        ('2', 'Vegano'),
        ('3', 'Gluten-free'),
        ('4', 'Lactosa'),
        ('5', 'Ninguna')
    ], widget=forms.Select(attrs={'class': 'form-control'}))
    nivel_actividad = forms.ChoiceField(choices=[
        (1, 'Sedentario'),
        (2, 'Moderado'),
        (3, 'Activo')
    ], widget=forms.Select(attrs={'class': 'form-control'}))
    genero = forms.ChoiceField(choices=[
        ('M', 'Masculino'),
        ('F', 'Femenino')
    ], widget=forms.Select(attrs={'class': 'form-control'}))

         
         
        
       
       
        
