# Generated by Django 3.0 on 2021-07-20 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('porteiros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=194, verbose_name='Nome completo')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
                ('data_nascimento', models.DateField(verbose_name='Data de nascimento')),
                ('numero_casa', models.PositiveSmallIntegerField(verbose_name='Númeo da casa a ser visitada')),
                ('placa_veiculo', models.CharField(blank=True, max_length=7, null=True, verbose_name='Placa de veículo')),
                ('horario_chegada', models.DateTimeField(auto_now_add=True, verbose_name='Horário de chegada na portaria')),
                ('horario_saida', models.DateTimeField(blank=True, null=True, verbose_name='Horário de saida do condomínio')),
                ('horario_autorizacao', models.DateTimeField(blank=True, null=True, verbose_name='Horário de autorização de entrada')),
                ('morador_responsavel', models.CharField(blank=True, max_length=194, verbose_name='Nome do morador responsável')),
                ('registrado_por', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='porteiros.Porteiro', verbose_name='Porteiro responsável pelo registro')),
            ],
            options={
                'verbose_name': 'Visitante',
                'verbose_name_plural': 'Visitantes',
                'db_table': 'visitante',
            },
        ),
    ]
