from django.db import migrations

def add_predefined_comidas(apps, schema_editor):
    Comida = apps.get_model('dieta', 'Comida')
    predefined_comidas = [
        {'nombre': 'Manzana', 'tipo_comida': 'Fruta', 'calorias': 52, 'carbohidratos': 14, 'proteinas': 0, 'grasas': 0},
        {'nombre': 'Pollo', 'tipo_comida': 'Carne', 'calorias': 239, 'carbohidratos': 0, 'proteinas': 27, 'grasas': 14},
        # Agrega más comidas predefinidas aquí
    ]
    for comida in predefined_comidas:
        Comida.objects.create(**comida)

class Migration(migrations.Migration):

    dependencies = [
        ('dieta', '000X_previous_migration'),
    ]

    operations = [
        migrations.RunPython(add_predefined_comidas),
    ]