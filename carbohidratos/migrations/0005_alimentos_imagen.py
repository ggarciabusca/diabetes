# Generated by Django 4.1.2 on 2022-12-01 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carbohidratos', '0004_alter_medicion_dni'),
    ]

    operations = [
        migrations.AddField(
            model_name='alimentos',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes'),
        ),
    ]
