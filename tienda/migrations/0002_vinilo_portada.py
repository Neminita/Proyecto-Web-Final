# Generated by Django 5.0.6 on 2024-07-01 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vinilo',
            name='portada',
            field=models.ImageField(null=True, upload_to='vinilos'),
        ),
    ]
