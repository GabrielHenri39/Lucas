from django.core.exceptions import ValidationError


def remove_mask_cpf(value):
    return value.replace('.', '').replace('-', '')



def validate_cpf(value):
    cpf = remove_mask_cpf(value)
    if not cpf.isdigit():
        raise ValidationError('CPF deve conter apenas números.')
    if len(cpf) != 11:
        raise ValidationError('CPF deve ter 11 dígitos.')
    
    cpf = [int(digit) for digit in cpf]
    
    # Cálculo do primeiro dígito verificador
    sum_of_products = sum(cpf[i] * (10-i) for i in range(9))
    remainder = sum_of_products % 11
    if remainder < 2:
        expected_digit = 0
    else:
        expected_digit = 11 - remainder
    if cpf[9] != expected_digit:
        raise ValidationError('CPF inválido.')
    
    # Cálculo do segundo dígito verificador
    sum_of_products = sum(cpf[i] * (11-i) for i in range(10))
    remainder = sum_of_products % 11
    if remainder < 2:
        expected_digit = 0
    else:
        expected_digit = 11 - remainder
    if cpf[10] != expected_digit:
        raise ValidationError('CPF inválido.')
