from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', view=views.cadastro, name='cadastro'), #type: ignore
    path('login/', views.login, name='login'), # type: ignore
    path('sair/', views.sair, name='sair'),
]
