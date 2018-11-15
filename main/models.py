from django.db import models
from django.utils import timezone

class Noticia(models.Model):
	autor = models.ForeignKey('auth.user', on_delete=models.CASCADE)
	titulo = models.CharField(max_length=40)
	texto = models.TextField()
	data_criacao = models.DateTimeField(default=timezone.now)
	data_publicacao = models.DateTimeField(blank=True, null=True)

	def publicar(self):
		self.data_publicacao = timezone.now()
		self.save()

	def __str__(self):
		return self.titulo


class Atracao(models.Model):
	autor = models.ForeignKey('auth.user', on_delete=models.CASCADE)
	titulo = models.CharField(max_length=40)
	descricao = models.TextField()

