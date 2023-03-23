from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import date, datetime
from django.utils.dateparse import parse_date
from .models import Paciente
from django.contrib import messages
from django.contrib.messages import constants
# Create your vews here.

@login_required(login_url="auth/login/")#type: ignore
def home(request):
    if request.method == "GET":
        pacientes = Paciente.objects.filter(fisio=request.user)
        return render(request, 'index.html', {'pacientes': pacientes})


@login_required(login_url="auth/login/")#type: ignore 
def novo_paciente(request):
    if request.method == "GET":
        return render(request, "novo_paciente.html")
    # elif request.method == "POST":
    #         nome = request.POST.get('nome')
    #         sexo = request.POST.get('sexo')
    #         data = request.POST.get('data')
    #         dataf=parse_date(data)
    #         cpf = request.POST.get('cpf')
    #         telefone = request.POST.get('telefone')
    #         print(dataf,type(dataf))

    #         if (len(nome.strip()) == 0) or (len(sexo.strip()) == 0)  or (len(telefone.strip()) == 0):
    #             messages.add_message(request, constants.ERROR,
    #                                 'Preencha todos os campos')
    #             return redirect('/')

    #         # if not idade.isnumeric():
    #         #     messages.add_message(request, constants.ERROR,
    #         #                          'Digite uma idade válida')
    #         #     return redirect('/')

    #         pacientes = Paciente.objects.filter(telefone=telefone)
    #         if pacientes.exists():
    #             messages.add_message(request, constants.ERROR,
    #                                 'Já existe um paciente com esse E-mail')
    #             return redirect('/')
    #         try:
    #             paciente = Paciente(nome_do_paciente=nome,
    #                                 sexo=sexo,
    #                                 data_de_nacimento=dataf,
    #                                 cpf=cpf,
    #                                 telefone=telefone,
    #                                 fisio=request.user)

    #             paciente.save()

    #             messages.add_message(request, constants.SUCCESS,
    #                                 'Paciênte cadastrado com sucesso')
    #             return redirect('/')
    #         except :
    #             messages.add_message(request, constants.ERROR,
    #                                 'Erro interno do sistema')
    #             return redirect('/')