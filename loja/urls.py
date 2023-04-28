"""from django.contrib import admin
from django.urls import path, include
from cad_roupas import views

urlpatterns = [
    path("admin", admin.site.urls),
    path("", views.home, name="home"),
    path("todos-vestido-noiva/", views.noiva, name='noiva'),
    path("todos-vestido-formatura/", views.formatura, name='formatura'),
    path("todos-vestido-festa/", views.festa, name='festa'),
    
    
    
    
    path("cadastro-vestido-noiva/", views.cadastroNoiva, name='cadastroNoiva'),
    
    
    
    path("todos-noiva-teste/", views.todosNoiva, name='todosNoiva'),
    path("todos-formatura-teste/", views.todosFormatura, name='todosFormatura'),
    
    
    path("login/", views.login, name='login'),
    #path('', include('usuarios.urls'))
]
"""
from django.contrib import admin
from django.urls import path
from cad_roupas import views

urlpatterns = [
    path("admin", admin.site.urls),
    path(route='', view=views.home),
    path(route='produto/<id>/', view=views.produto),
    path(route='categoria/<cat>/', view=views.categoria),
    path(route='carrinho/', view=views.carrinho),
    path(route='entrega/', view=views.entrega),
    path("todos-vestido-noiva/", views.noiva, name='noiva'),
]