from django.db import models
from .uttils import validate_cpf, remove_mask_cpf 
from  autenticacao.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver

choice_de_sexo = (
    ('f', 'Feminino'),
    ('m', 'Masculino')
)


class Paciente(models.Model):
    nome_do_paciente = models.CharField(max_length=50, verbose_name='Nome de Paciente')
    telefone = models.CharField(max_length=19)
    cpf = models.CharField(verbose_name='CPF' ,max_length=14 ,validators=[validate_cpf])
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

class EscalaDeEva(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    valor = models.IntegerField(verbose_name='Valor da EVA')
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Escalas de EVA'
        ordering = ['-data']

    def __str__(self):
        return f'{self.paciente} - {self.valor}'




@receiver(pre_save, sender=Paciente)
def remove_cpf_mask(sender, instance, **kwargs):
    instance.cpf = remove_mask_cpf(instance.cpf)
