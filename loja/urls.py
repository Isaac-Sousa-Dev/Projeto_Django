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