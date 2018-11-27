from django.shortcuts import render
from django.utils import timezone
import datetime
from random import random
from .models import Edicao
from .models import Atracao
from .models import Estande
from .models import Modalidade
from .models import Visitante
from .models import Inscricao
from .models import Noticia
from .models import Foto
from .models import Patrocinador

def getEdicaoAtual():
	edicao = Edicao.objects.filter(data_inicio__gte=timezone.now()).order_by('data_inicio')[:1]
	if(len(edicao) == 0):
		return None
	return edicao[0]

def getAtracoes(edicao):
	if(edicao == None):
		return []

	datas = []
	for i in range(0, (edicao.data_fim - edicao.data_inicio).days + 1):
		datas.append(edicao.data_inicio + datetime.timedelta(days=i))

	atracoes = Atracao.objects.filter(edicao=edicao.id).order_by('data_inicio')
	array_atracoes = []
	for i in range(0, len(datas)):
		array_atracoes.append([])
		for atracao in atracoes:
			if(atracao.data_inicio.day == datas[i].day and atracao.data_inicio.month == datas[i].month and atracao.data_inicio.year == datas[i].year):
				array_atracoes[i].append(atracao)

	return array_atracoes

def getEstandes(edicao):
	if(edicao == None):
		return []
	estandes = Estande.objects.filter(edicao=edicao.id)
	return estandes

def getNoticias():
	array_noticias = []
	noticias = Noticia.objects.filter(data_publicacao__lte=timezone.now()).order_by('-data_publicacao')[:6]
	cont = 0
	i = 0
	for noticia in noticias:
		if(cont == 0):
			array_noticias.append([])

		array_noticias[i].append(noticia)
		cont += 1

		if(cont == 3):
			cont = 0
			i += 1

	return array_noticias

def getPatrocinadores():
	patrocinadores = Patrocinador.objects.all()
	return patrocinadores

def getModalidades(edicao):
	if(edicao == None):
		return []
	modalidades = Modalidade.objects.filter(edicao=edicao.id)
	return modalidades

def getFotos():
	fotos = list(Foto.objects.all())
	fotos = sorted(Foto.objects.all(), key=lambda x: random())
	return fotos

def index(request):
	edicao = getEdicaoAtual()
	array_atracoes = getAtracoes(edicao)
	estandes = getEstandes(edicao)
	modalidades = getModalidades(edicao)

	array_noticias = getNoticias()
	patrocinadores = getPatrocinadores()
	fotos = getFotos()

	return render(request, 'main/index.html', 
		{'agora': timezone.now(),
		'array_noticias': array_noticias, 
		'edicao': edicao, 
		'array_atracoes': array_atracoes, 
		'estandes': estandes, 
		'patrocinadores': patrocinadores,
		'modalidades': modalidades,
		'fotos': fotos
		})
