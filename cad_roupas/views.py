import locale

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseServerError
from .models import Categoria, Roupa, Carrinho, CarrinhoItem, Pedido
from django.contrib.auth.mixins import LoginRequiredMixin

locale.setlocale(locale.LC_ALL, "")


# Create your views here.
def home(req):
    categorias = Categoria.objects.all()

    return render(
        request=req, template_name="site/home.html", context={"categorias": categorias}
    )


def produto(req, id_roupa):
    roupa = Roupa.objects.get(pk=id_roupa)
    roupas_rel = Roupa.objects.select_related().filter(categoria=roupa.categoria)

    return render(
        request=req,
        template_name="site/produto.html",
        context={
            "roupa": roupa,
            "relacionados": roupas_rel,
            "preco": locale.currency(roupa.valor, grouping=True),
        },
    )


def categoria(req, cat):
    categoria_instance = Categoria.objects.get(pk=cat)
    roupas = Roupa.objects.select_related().filter(categoria=cat)

    return render(
        request=req,
        template_name="site/pesquisar_categorias.html",
        context={
            "categoria": categoria_instance,
            "roupas": roupas,
        },
    )


@login_required(login_url="/accounts/login/")
def carrinho(req):
    carrinho_instance, _ = Carrinho.objects.get_or_create(pago=False, usuario=req.user)
    carrinho_itens = CarrinhoItem.objects.filter(carrinho=carrinho_instance)

    carrinho_valor = sum([i.roupa.valor for i in carrinho_itens])
    lavagem_preco = sum([i.roupa.precoLavagem for i in carrinho_itens])

    return render(
        request=req,
        template_name="site/carrinho.html",
        context={
            "carrinho": carrinho_instance,
            "carrinho_items": carrinho_itens,
            "carrinho_preco": carrinho_valor,
            "carrinho_lavagem": lavagem_preco,
        },
    )


@login_required(login_url="/accounts/login/")
def carrinho_add(req, id_roupa):
    roupa = Roupa.objects.get(pk=id_roupa)
    tamanho = req.GET.get("tamanho")
    usuario = req.user
    carrinho_instance, _ = Carrinho.objects.get_or_create(usuario=usuario, pago=False)
    CarrinhoItem.objects.create(
        carrinho=carrinho_instance,
        roupa=roupa,
        tamanho=tamanho,
        quantidade=1,
    )

    return HttpResponseRedirect(f"/produto/{id_roupa}/")


@login_required(login_url="/accounts/login/")
def carrinho_del(req, id_roupa):
    try:
        item_carrinho = CarrinhoItem.objects.get(id=id_roupa)
        item_carrinho.delete()
    except Exception as error:
        print(error)

    return HttpResponseRedirect(f"/carrinho/")


@login_required(login_url="/accounts/login/")
def entrega(req):
    carrinho_instance = Carrinho.objects.get(pago=False, usuario=req.user)
    carrinho_itens = CarrinhoItem.objects.filter(carrinho=carrinho_instance)
    carrinho_valor = sum([i.roupa.valor for i in carrinho_itens])
    lavagem_preco = sum([i.roupa.precoLavagem for i in carrinho_itens])

    return render(
        request=req,
        template_name="site/entrega.html",
        context={
            "carrinho_preco": carrinho_valor,
            "carrinho_lavagem": lavagem_preco
        }
    )


@login_required(login_url="/accounts/login/")
def entrega_reg(req):
    numero_telefone = req.GET.get("numero_telefone")
    carrinho_instance = Carrinho.objects.get(pago=False, usuario=req.user)
    carrinho_itens = CarrinhoItem.objects.filter(carrinho=carrinho_instance)

    carrinho_valor = sum([i.roupa.valor for i in carrinho_itens])

    try:
        Pedido.objects.create(
            carrinho=carrinho_instance,
            preco_total=carrinho_valor,
            numero_cliente=numero_telefone
        )
        carrinho_instance.pago = True
        carrinho_instance.save()
    except Exception as error:
        return HttpResponseServerError(error)

    return HttpResponseRedirect("/obrigado/")


class MyView(LoginRequiredMixin):
    login_url = "/login/"
    redirect_field_name = "redirect_to"


def obrigado(req):

    return render(
        request=req,
        template_name="site/obrigado.html"
    )