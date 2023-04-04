from django.contrib import admin

from .models import Race
from .models import Subrace

# Register your models here.

admin.site.register(Race)
admin.site.register(Subrace)