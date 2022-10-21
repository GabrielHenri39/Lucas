# Generated by Django 4.0.5 on 2022-10-09 15:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_do_paciente', models.CharField(max_length=50, verbose_name='Nome do Paciente')),
                ('cpf', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('data_de_nacimento', models.DateField(verbose_name='Data de Nascimento')),
                ('sexo', models.CharField(choices=[('f', 'Feminino'), ('m', 'Masculino')], max_length=1)),
                ('fisio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Pacientes',
                'ordering': ['nome_do_paciente'],
            },
        ),
        migrations.CreateModel(
            name='DadosPaciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('peso', models.IntegerField()),
                ('altura', models.IntegerField()),
                ('pa', models.IntegerField()),
                ('bpm', models.IntegerField()),
                ('hma', models.TextField()),
                ('queixa_principal', models.TextField()),
                ('objetivo', models.TextField()),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plataforma.paciente')),
            ],
        ),
    ]
