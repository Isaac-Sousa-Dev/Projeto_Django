# Generated by Django 4.2 on 2023-04-30 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cad_roupas', '0010_categorias_roupas'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categorias',
            new_name='Categoria',
        ),
        migrations.RenameModel(
            old_name='Roupas',
            new_name='Roupa',
        ),
    ]