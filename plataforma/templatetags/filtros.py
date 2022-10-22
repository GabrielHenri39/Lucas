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