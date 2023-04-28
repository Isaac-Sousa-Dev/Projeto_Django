from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('', views, name="")
    path('login-teste/', auth_views.LoginView.as_view(
        template_name = 'usuarios/login.html'
    ), name="login-teste")
]
