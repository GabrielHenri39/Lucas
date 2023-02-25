from django.db import models
from  autenticacao.models import User

choice_de_sexo = (
    ('f', 'Feminino'),
    ('m', 'Masculino')
)


class Paciente(models.Model):
    nome_do_paciente = models.CharField(max_length=50, verbose_name='Nome de Paciente')
    telefone = models.CharField(max_length=19)
    cpf = models.CharField(max_length=15, null=True, blank=True, unique=True ,verbose_name='CPF')
    data_de_nacimento = models.DateField(verbose_name='Data de Nascimento')
    sexo = models.CharField(max_length=1, choices=choice_de_sexo)
    fisio = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateField(verbose_name='Data de início do tratamento')
    hma = models.TextField()
    queixa_principal = models.TextField()
    objetivo = models.TextField()

    class Meta:
        verbose_name_plural = 'Pacientes'
        ordering = ['nome_do_paciente']

    def __str__(self):
        return f'{self.nome_do_paciente}'


class DadosPaciente(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    altura = models.DecimalField(max_digits=3, decimal_places=2)
    pa = models.CharField(max_length=7)
    bpm=models.IntegerField()
    
    



    def __str__(self):
        return f"Paciente({self.paciente}, {self.peso})"

# class EscalaDeEva(models.Model):
#     pass