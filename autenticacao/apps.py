from django.apps import AppConfig


class AutenticacaoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'autenticacao'


    class Meta:
        varbose_name='Autenticação'