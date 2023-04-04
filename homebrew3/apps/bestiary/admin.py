from django.contrib import admin

from .models import Creature
from .models import Keeper
from .models import Aberration
from .models import Beast
from .models import Celestial
from .models import Construct
from .models import Dragon
from .models import Elemental
from .models import Fey
from .models import Fiend
from .models import Giant
from .models import Humanoid
from .models import Monstrositie
from .models import Ooze
from .models import Plant
from .models import SwarmOfLargeBeast
from .models import SwarmOfLargeUndead
from .models import SwarmOfMediumBeast
from .models import SwarmOfMediumConstruct
from .models import Undead
from .models import Vehicle

# Register your models here.

admin.site.register(Creature)
admin.site.register(Keeper)
admin.site.register(Aberration)
admin.site.register(Beast)
admin.site.register(Celestial)
admin.site.register(Construct)
admin.site.register(Dragon)
admin.site.register(Elemental)
admin.site.register(Fey)
admin.site.register(Fiend)
admin.site.register(Giant)
admin.site.register(Humanoid)
admin.site.register(Monstrositie)
admin.site.register(Ooze)
admin.site.register(Plant)
admin.site.register(SwarmOfLargeBeast)
admin.site.register(SwarmOfLargeUndead)
admin.site.register(SwarmOfMediumBeast)
admin.site.register(SwarmOfMediumConstruct)
admin.site.register(Undead)
admin.site.register(Vehicle)