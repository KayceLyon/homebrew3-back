from django.contrib import admin

from .models import Archetype
from .models import Classe
from .models import Subclasse

# Register your models here.

admin.site.register(Archetype)
admin.site.register(Classe)
admin.site.register(Subclasse)