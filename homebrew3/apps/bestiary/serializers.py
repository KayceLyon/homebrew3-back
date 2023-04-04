from rest_framework import serializers

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

class CreaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creature
        fields = ('id', 'name') 

class KeepersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keeper
        fields = ('id', 'name')

class AberrationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aberration
        fields = ('id', 'name')

class BeastsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beast
        fields = ('id', 'name')

class CelestialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Celestial
        fields = ('id', 'name')

class ConstructsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Construct
        fields = ('id', 'name')

class DragonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dragon
        fields = ('id', 'name')

class ElementalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elemental
        fields = ('id', 'name')

class FeySerializer(serializers.ModelSerializer):
    class Meta:
        model = Fey
        fields = ('id', 'name')

class FiendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fiend
        fields = ('id', 'name')

class GiantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Giant
        fields = ('id', 'name')

class HumanoidsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Humanoid
        fields = ('id', 'name')

class Monstrositieserializer(serializers.ModelSerializer):
    class Meta:
        model = Monstrositie
        fields = ('id', 'name')

class OozesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ooze
        fields = ('id', 'name')

class PlantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ('id', 'name')

class SwarmOfLargeBeastsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwarmOfLargeBeast
        fields = ('id', 'name')

class SwarmOfLargeUndeadsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwarmOfLargeUndead
        fields = ('id', 'name')

class SwarmOfMediumBeastsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwarmOfMediumBeast
        fields = ('id', 'name')

class SwarmOfMediumConstructsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwarmOfMediumConstruct
        fields = ('id', 'name')

class UndeadsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Undead
        fields = ('id', 'name')

class VehiclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('id', 'name')