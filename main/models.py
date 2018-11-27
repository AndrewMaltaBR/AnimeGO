from django.db import models
from django.utils import timezone

class Edicao(models.Model):
	admin = models.ForeignKey('auth.user', on_delete=models.CASCADE)
	data_inicio = models.DateTimeField(default=timezone.now)
	data_fim = models.DateTimeField(default=timezone.now)
	local = models.CharField(max_length=120)
	data_inicio_incricoes = models.DateTimeField(default=timezone.now)
	data_fim_incricoes = models.DateTimeField(default=timezone.now)

class Atracao(models.Model):
	admin = models.ForeignKey('auth.user', on_delete=models.CASCADE)
	edicao = models.ForeignKey('Edicao', on_delete=models.CASCADE)
	titulo = models.CharField(max_length=60)
	descricao = models.TextField()
	imagem = models.ImageField(null=True, blank=True)
	nome_responsavel = models.CharField(max_length=120, null=True)
	local = models.CharField(max_length=120, null=True)
	data_inicio = models.DateTimeField(default=timezone.now)
	data_fim = models.DateTimeField(default=timezone.now)

class Estande(models.Model):
	admin = models.ForeignKey('auth.user', on_delete=models.CASCADE)
	edicao = models.ForeignKey('Edicao', on_delete=models.CASCADE)
	nome = models.CharField(max_length=60)
	descricao = models.TextField()
	imagem = models.ImageField(null=True, blank=True)
	nome_responsavel = models.CharField(max_length=120, blank=True, null=True)
	local = models.CharField(max_length=120, blank=True, null=True)

class Modalidade(models.Model):
	admin = models.ForeignKey('auth.user', on_delete=models.CASCADE)
	edicao = models.ForeignKey('Edicao', on_delete=models.CASCADE)
	nome = models.CharField(max_length=60)
	preco = models.FloatField()
	limite = models.IntegerField(null=True, blank=True)
	atracoes = models.BooleanField()
	palestras = models.BooleanField()
	workshops = models.BooleanField()
	torneios = models.BooleanField()

class Visitante(models.Model):
	nome_completo = models.CharField(max_length=120)
	email = models.CharField(max_length=60)
	cpf = models.CharField(max_length=14)

class Inscricao(models.Model):
	modalidade = models.ForeignKey('Modalidade', on_delete=models.CASCADE)
	visitante = models.ForeignKey('Visitante', on_delete=models.CASCADE)	

class Noticia(models.Model):
	admin = models.ForeignKey('auth.user', on_delete=models.CASCADE)
	titulo = models.CharField(max_length=60)
	texto = models.TextField()
	imagem = models.ImageField(null=True, blank=True)
	data_publicacao = models.DateTimeField(default=timezone.now)

class Foto(models.Model):
	admin = models.ForeignKey('auth.user', on_delete=models.CASCADE)
	imagem = models.ImageField(null=True, blank=True)
	descricao = models.TextField()

class Patrocinador(models.Model):
	admin = models.ForeignKey('auth.user', on_delete=models.CASCADE)
	nome = models.CharField(max_length=60)
	imagem = models.ImageField(null=True, blank=True)
	site = models.URLField(max_length=120, null=True, blank=True)