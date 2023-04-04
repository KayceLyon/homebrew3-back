from django.contrib import admin

from .models import AdventuringGear
from .models import ArmorAndShield
from .models import CoinsAndGemstone
from .models import Weapon
from .models import WonderousItem

# Register your models here.

admin.site.register(AdventuringGear)
admin.site.register(ArmorAndShield)
admin.site.register(CoinsAndGemstone)
admin.site.register(Weapon)
admin.site.register(WonderousItem)