from rest_framework import serializers
from .models import Spells

class SpellsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spells
        fields = ('id', 'name') 