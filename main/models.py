from django.db import models
from django.utils import timezone

class Noticia(models.Model):
	autor = models.ForeignKey('auth.user', on_delete=models.CASCADE)
	titulo = models.CharField(max_length=60)
	texto = models.TextField()
	imagem = models.ImageField(upload_to='media', null=True, blank=True)
	data_publicacao = models.DateTimeField(default=timezone.now)

class Atracao(models.Model):
	autor = models.ForeignKey('auth.user', on_delete=models.CASCADE)
	titulo = models.CharField(max_length=60)
	descricao = models.TextField()
	imagem = models.ImageField(upload_to='media', null=True, blank=True)
	data_inicio = models.DateTimeField(default=timezone.now)
	data_fim = models.DateTimeField(default=timezone.now)

