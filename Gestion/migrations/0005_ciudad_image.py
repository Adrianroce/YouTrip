# Generated by Django 4.1.6 on 2023-03-29 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion', '0004_rename_ciudad_id_ciudad_mes_ciudad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad_Image',
            fields=[
                ('imagen_id', models.AutoField(primary_key=True, serialize=False)),
                ('img', models.ImageField(default=None, upload_to='Image')),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion.ciudad')),
            ],
        ),
    ]
