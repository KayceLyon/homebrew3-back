from rest_framework import serializers

from .models import ArmorAndShield
from .models import AdventuringGear
from .models import CoinsAndGemstone
from .models import Weapon
from .models import WonderousItem

class ArmorAndShieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArmorAndShield
        fields = ('id', 'name') 

class AdventuringGearSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdventuringGear
        fields = ('id', 'name') 

class CoinsAndGemstonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinsAndGemstone
        fields = ('id', 'name') 

class WeaponsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = ('id', 'name') 

class WonderousItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WonderousItem
        fields = ('id', 'name') 