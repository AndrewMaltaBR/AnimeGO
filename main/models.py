from django.db import models
from django.utils import timezone

class Noticia(models.Model):
	usuario = models.ForeignKey('auth.user', on_delete=models.CASCADE)
	titulo = models.CharField(max_length=60)
	texto = models.TextField()
	imagem = models.ImageField(upload_to='media', null=True, blank=True)
	data_publicacao = models.DateTimeField(default=timezone.now)

class Atracao(models.Model):
	usuario = models.ForeignKey('auth.user', on_delete=models.CASCADE)
	titulo = models.CharField(max_length=60)
	descricao = models.TextField()
	imagem = models.ImageField(upload_to='media', null=True, blank=True)
	nome_responsavel = models.CharField(max_length=120, null=True)
	local = models.CharField(max_length=120, null=True)
	data_inicio = models.DateTimeField(default=timezone.now)
	data_fim = models.DateTimeField(default=timezone.now)

class Estande(models.Model):
	usuario = models.ForeignKey('auth.user', on_delete=models.CASCADE)
	nome = models.CharField(max_length=60)
	descricao = models.TextField()
	imagem = models.ImageField(upload_to='media', null=True, blank=True)
	nome_responsavel = models.CharField(max_length=120, null=True)
	local = models.CharField(max_length=120, null=True)

class Foto(models.Model):
	usuario = models.ForeignKey('auth.user', on_delete=models.CASCADE)
	imagem = models.ImageField(upload_to='media', null=True, blank=True)
	descricao = models.TextField()
