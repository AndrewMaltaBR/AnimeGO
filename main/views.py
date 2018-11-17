from django.shortcuts import render
from django.utils import timezone
from .models import Noticia
from .models import Atracao

def index(request):
	# Obtendo notícias
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

	# Obtendo dias de evento
	atracoes = Atracao.objects.filter(data_inicio__gte=timezone.now()).order_by('data_inicio')
	datas = []
	for atracao in atracoes:
		inserir = True
		for data in datas:
			if(atracao.data_inicio.day == data.day and atracao.data_inicio.month == data.month and atracao.data_inicio.year == data.year):
				inserir = False
				break
		if(inserir):
			datas.append(atracao.data_inicio)

	# Obtendo atrações
	array_atracoes = [[]]*len(datas)
	for atracao in atracoes:
		for i in range(0, len(datas)):
			if(atracao.data_inicio.day == datas[i].day and atracao.data_inicio.month == datas[i].month and atracao.data_inicio.year == datas[i].year):
				array_atracoes[i].append(atracao)
	print(array_atracoes)


	return render(request, 'main/index.html', {'array_noticias': array_noticias,'datas': datas, 'atracoes': atracoes})
