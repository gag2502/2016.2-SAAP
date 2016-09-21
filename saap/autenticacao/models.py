# coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import *


# Create your models here.

class Usuario_saap(User):

    data_de_nascimento = models.DateField()
    sexo = models.CharField(max_length=10)
    municipio = models.CharField(max_length=250)
    uf = models.CharField(max_length=2)

    @classmethod
    def busca_nome(cls, nome):
        return Usuario_saap.objects.filter(first_name__startswith(nome))

    @classmethod
    def deleta_usuario(cls, idArg):
        Usuario_saap.objects.get(id=idArg).delete()

    @classmethod
    def busca_username(cls, username):
        return Usuario_saap.objects.filter(username__startswith(username))

    @classmethod
    def get_usuario_por_username(cls, username):
        return Usuario_saap.objects.filter(username = username)


class Gabinete_saap(models.Model):

    participantes = models.ManyToManyField(Usuario_saap)
    nome_gabinete = models.CharField(max_length=100)
    municipio = models.CharField(max_length=250)
    uf = models.CharField(max_length=2)


class Ticket(models.Model):

    envio_identificado = models.BooleanField(default=False)
    titulo = models.CharField(max_length=100)
    corpo_texto = models.CharField(max_length=500)
    remetente = Usuario_saap()
    gabinete_destino = Gabinete_saap()
    data_publicacao = models.DateField('data_de_publicacao', auto_now=True)
    tipo_ticket = models.CharField(max_length=30)
    file = models.FileField()

    # @classmethod
    # def current_date(self):
    #     return datetime.datetime.now()

class Cidadao(Usuario_saap):

    pass


class OrganizadorContatos(Usuario_saap):

    pass