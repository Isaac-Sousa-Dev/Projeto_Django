# Generated by Django 4.2 on 2023-04-30 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cad_roupas', '0013_categoria_roupa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roupa',
            name='descricao',
            field=models.TextField(max_length=150),
        ),
    ]