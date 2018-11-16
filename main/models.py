from django.db import models
from django.utils import timezone

class Noticia(models.Model):
	autor = models.ForeignKey('auth.user', on_delete=models.CASCADE)
	titulo = models.CharField(max_length=60)
	texto = models.TextField()
	imagem = models.ImageField(null=True)
	data_publicacao = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.titulo

class Atracao(models.Model):
	autor = models.ForeignKey('auth.user', on_delete=models.CASCADE)
	titulo = models.CharField(max_length=60)
	descricao = models.TextField()
	imagem = models.ImageField(null=True)
	data_inicio = models.DateTimeField(default=timezone.now)
	data_fim = models.DateTimeField(default=timezone.now)


