import locale
from django.shortcuts import render
from django.http import HttpResponse
from .models import Categoria, Roupa

locale.setlocale(locale.LC_ALL, '')


# Create your views here.
def home(req):
    categorias = Categoria.objects.all()

    return render(
        request=req,
        template_name='site/home.html',
        context={'categorias': categorias}
    )


def produto(req, id):
    roupa = Roupa.objects.get(pk=id)
    roupas_rel = Roupa.objects.select_related().filter(categoria=roupa.categoria)

    return render(
        request=req,
        template_name='site/produto.html',
        context={
            'roupa': roupa,
            'relacionados': roupas_rel,
            'preco': locale.currency(roupa.valor, grouping=True)
        }
    )


def categoria(req, cat):
    categoria = Categoria.objects.get(pk=cat)
    roupas = Roupa.objects.select_related().filter(categoria=cat)

    return render(
        request=req,
        template_name='site/pesquisar_categorias.html',
        context={
            'categoria': categoria,
            'roupas': roupas,
        }
    )


def carrinho(req):
    return render(
        request=req,
        template_name='site/carrinho.html',
        context={'produto': 'Pesro'}
    )


def entrega(req):
    return render(
        request=req,
        template_name='site/entrega.html',
        context={'produto': 'Pesro'}
    )