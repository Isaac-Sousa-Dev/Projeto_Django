# Generated by Django 4.2 on 2023-04-30 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cad_roupas', '0011_rename_categorias_categoria_rename_roupas_roupa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roupa',
            name='categoria',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Roupa',
        ),
    ]
