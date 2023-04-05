# Generated by Django 4.1.6 on 2023-03-31 13:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Gestion', '0006_alter_ciudad_image_ciudad_alter_ciudad_mes_ciudad'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Viaje',
            fields=[
                ('viaje_id', models.AutoField(primary_key=True, serialize=False)),
                ('presupuesto', models.FloatField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('valoracion', models.FloatField(null=True)),
                ('destino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='Gestion.ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Viajero',
            fields=[
                ('viajero_id', models.AutoField(primary_key=True, serialize=False)),
                ('creador', models.BooleanField()),
                ('administrador', models.BooleanField()),
                ('viaje_aceptado', models.BooleanField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='viajes', to=settings.AUTH_USER_MODEL)),
                ('viaje', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='integrantes', to='Viaje.viaje')),
            ],
        ),
    ]
