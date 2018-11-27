from django.contrib import admin
from .models import Edicao
from .models import Atracao
from .models import Estande
from .models import Modalidade
from .models import Visitante
from .models import Inscricao
from .models import Noticia
from .models import Foto
from .models import Patrocinador

admin.site.register(Edicao)
admin.site.register(Atracao)
admin.site.register(Estande)
admin.site.register(Modalidade)
admin.site.register(Visitante)
admin.site.register(Inscricao)
admin.site.register(Noticia)
admin.site.register(Foto)
admin.site.register(Patrocinador)
