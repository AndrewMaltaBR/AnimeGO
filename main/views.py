from django.shortcuts import render
from django.utils import timezone
from .models import Noticia

def index(request):
	noticias = Noticia.objects.filter(data_publicacao__lte=timezone.now()).order_by('data_publicacao')
	return render(request, 'main/index.html', {'noticias': noticias})
