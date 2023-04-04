from django.contrib import admin

from .models import Cantrip
from .models import LevelOneSpell
from .models import LevelTwoSpell
from .models import LevelThreeSpell
from .models import LevelFourSpell
from .models import LevelFiveSpell
from .models import LevelSixSpell
from .models import LevelSevenSpell
from .models import LevelEightSpell
from .models import LevelNineSpell

# Register your models here.

admin.site.register(Cantrip)
admin.site.register(LevelOneSpell)
admin.site.register(LevelTwoSpell)
admin.site.register(LevelThreeSpell)
admin.site.register(LevelFourSpell)
admin.site.register(LevelFiveSpell)
admin.site.register(LevelSixSpell)
admin.site.register(LevelSevenSpell)
admin.site.register(LevelEightSpell)
admin.site.register(LevelNineSpell)

