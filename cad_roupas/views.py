"""from django.shortcuts import render
from .models import VestidoNoiva, VestidoFormatura, VestidoFesta


# Create your views here.
def home(request):
    return render(request, 'site/home.html')

def noiva(request):
    vestidosN = VestidoNoiva.objects.all()
    return render(request, 'app/feminino/noiva.html', {'vestidosN': vestidosN})

def formatura(request):
    vestidosForm = VestidoFormatura.objects.all()
    return render(request, 'app/feminino/formatura.html', {'vestidosForm': vestidosForm})


def festa(request):
    vestidosFesta = VestidoFesta.objects.all()
    return render(request, 'app/feminino/festa.html', {'vestidosFesta': vestidosFesta})








def cadastroNoiva(request):
    return render(request, 'app/cadastro/vestidos/noiva.html',)








def todosNoiva(request):
    vestidosN = VestidoNoiva.objects.all()
    return render(request, 'site/todos_noiva.html', {'vestidosN': vestidosN})

def todosFormatura(request):
    vestidosForm = VestidoFormatura.objects.all()
    return render(request, 'site/todos_formatura.html', {'vestidosForm': vestidosForm})









#def formatura(request):
 #   return render(request, 'app/feminino/formatura.html')




def login(request):
    return render(request, 'site/login.html')
"""


from django.shortcuts import render
from django.http import HttpResponse
from .models import VestidoNoiva, VestidoFormatura, VestidoFesta

# Create your views here.
def home(req):
   return render(
      request=req,
      template_name='site/home.html',
      context={'name': 'Pesro'}
   )
def produto(req, id):
   return render(
      request=req,
      template_name='site/produto.html',
      context={'produto': 'Pesro'}
   )
def categoria(req, cat):
   vestidosN = ''
   if(cat == '1'):
      vestidosN = VestidoNoiva.objects.all() 
   elif(cat == '2'):
      vestidosN = VestidoFormatura.objects.all()
   elif(cat == '3'):
      vestidosN = VestidoFesta.objects.all()
   return render(
      request=req,
      template_name='site/pesquisar_categorias.html',
      context={'vestidosN': vestidosN}
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
   
def noiva(request):
    vestidosN = VestidoNoiva.objects.all()
    return render(request, 'app/feminino/noiva.html', {'vestidosN': vestidosN})
