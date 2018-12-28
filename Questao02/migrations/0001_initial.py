# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-12-28 13:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('carga_horaria', models.IntegerField()),
                ('ementa', models.CharField(max_length=200)),
                ('valor', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=100)),
                ('valor_hora_aula', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_incio', models.DateField()),
                ('data_terminio', models.DateField()),
                ('hora_incio', models.TimeField()),
                ('hora_terminio', models.TimeField()),
                ('chave', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Questao02.Curso')),
                ('chave1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Questao02.Professor')),
            ],
        ),
    ]
