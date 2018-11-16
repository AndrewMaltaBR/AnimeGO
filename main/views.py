from django.shortcuts import render
from django.utils import timezone
from .models import Noticia

def index(request):
	array_noticias = []
	noticias = Noticia.objects.filter(data_publicacao__lte=timezone.now()).order_by('data_publicacao')[:6]
	cont = 0
	i = 0
	for noticia in noticias:
		if(cont == 0):
			array_noticias.append([])

		if(len(noticia.texto) > 165):
			noticia.texto = noticia.texto[:165]+"..."

		array_noticias[i].append(noticia)
		cont += 1

		if(cont == 3):
			cont = 0
			i += 1

	return render(request, 'main/index.html', {'array_noticias': array_noticias})
