# Generated by Django 5.1.3 on 2024-12-17 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metas', '0002_consumoagua_metanutricional_remove_waterintake_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='metanutricional',
            name='veces_completadas',
            field=models.IntegerField(default=0),
        ),
    ]