# Generated by Django 4.1.6 on 2023-03-25 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('ciudad_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('codigo', models.CharField(max_length=255, unique=True)),
                ('familia', models.IntegerField()),
                ('gastronomia', models.IntegerField()),
                ('cultura', models.IntegerField()),
                ('transporte', models.IntegerField()),
                ('pareja', models.IntegerField()),
                ('alojamiento', models.IntegerField()),
                ('ocio', models.IntegerField()),
                ('fiesta', models.IntegerField()),
                ('mejor_epoca', models.CharField(max_length=255)),
            ],
        ),
    ]
