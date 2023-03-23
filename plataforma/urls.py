from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('novo_paciente/', views.novo_paciente, name='novo_paciente' ),

]
