# Generated by Django 4.1.6 on 2023-03-27 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sesion', '0006_rename_user_image_user_id_alter_image_tipo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='user_id',
            new_name='user',
        ),
    ]