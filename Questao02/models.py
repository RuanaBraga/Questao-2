from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=200)
    carga_horaria = models.IntegerField()
    ementa = models.CharField(max_length=200)
    valor = models.FloatField()



class Professor(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=100)
    valor_hora_aula = models.CharField(max_length=100)


class Turma(models.Model):
    data_incio = models.DateField()
    data_terminio = models.DateField()
    hora_incio = models.TimeField()
    hora_terminio = models.TimeField()
    Curso = models.ForeignKey(Curso)
    chave1 = models.ForeignKey(Professor)
