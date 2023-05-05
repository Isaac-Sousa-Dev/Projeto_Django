from django.contrib import admin
from django.urls import path, include
from cad_roupas import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path(route="", view=views.home),
    path(route="produto/<id_roupa>/", view=views.produto),
    path(route="categoria/<cat>/", view=views.categoria),
    path(route="carrinho/", view=views.carrinho),
    path(route="carrinho/add/<id_roupa>/", view=views.carrinho_add),
    path(route="carrinho/del/<id_roupa>/", view=views.carrinho_del),
    path(route="entrega/", view=views.entrega),
    path(route="entrega/reg/", view=views.entrega_reg),
    path(route="obrigado/", view=views.obrigado),
    path("accounts/", include("django.contrib.auth.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
