from django.db import models

class Cliente(models.Model):
    nomeDoCliente = models.CharField(max_length=200)
    senhaDoCliente = models.CharField(max_length=200)

    def __str__(self):
        return self.nomeDoCliente


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=1000)
    imagem = models.ImageField(upload_to='categoria')

    def __str__(self):
        return self.nome


class Roupa(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.FloatField(default=0)
    descricao = models.TextField(max_length=150)
    precoLavagem = models.FloatField(default=30)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="categoria")
    imagem = models.ImageField(upload_to='images')

    def __str__(self):
        return self.nome