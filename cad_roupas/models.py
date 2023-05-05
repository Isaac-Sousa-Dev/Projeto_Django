from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.db import models


def utc_ten_days_future():
    return datetime.utcnow() + timedelta(days=10)


class Cliente(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Cliente", null=True)
    imagem = models.ImageField(upload_to="clientes", default="cat-img.png")
    nome = models.CharField(max_length=250, default="Genérica")

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=1000)
    imagem = models.ImageField(upload_to="categoria")

    def __str__(self):
        return self.nome


class Roupa(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.FloatField(default=0)
    descricao = models.TextField(max_length=150)
    precoLavagem = models.FloatField(default=30)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, related_name="categoria"
    )
    imagem = models.ImageField(upload_to="images")

    def __str__(self):
        return self.nome


class Carrinho(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="carrinho")
    pago = models.BooleanField(default=False)


class CarrinhoItem(models.Model):
    carrinho = models.ForeignKey(
        Carrinho, on_delete=models.CASCADE, related_name="carrinho_item"
    )
    roupa = models.ForeignKey(
        Roupa, on_delete=models.CASCADE, related_name="carrinho_item"
    )
    tamanho = models.CharField(max_length=1)
    quantidade = models.IntegerField()
    data_compra = models.CharField(max_length=12, default='00000')

    def get_product_price(self):
        price = [self.roupa.valor]
        return sum(price)


class Pedido(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE, related_name="Pedido")
    preco_total = models.FloatField(default=0)
    numero_cliente = models.CharField(max_length=20)
    data_pedido = models.DateTimeField(default=datetime.utcnow)
    data_devolucao = models.DateTimeField(default=utc_ten_days_future())
