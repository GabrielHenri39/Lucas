from django import template
from datetime import datetime,date

register = template.Library()

@register.filter
def idade(data_nascimento):
    
    data = data_nascimento
   
    hoje = date.today()
    idade =hoje.year - data.year - ((hoje.month, hoje.day) < (data.month, data.day))
    texto = 'Anos'
    if idade == 1:
        texto = 'Ano'
    return f"{idade} {texto}."

    
@register.filter
def mask_cpf(value):
    cpf = str(value)
    cpf_masked = '.'.join([cpf[:3], cpf[3:6], cpf[6:9]]) + '-' + cpf[9:]
    return cpf_masked