from rest_framework import serializers

from .models import Race
from .models import Subrace

class RacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = ('id', 'name') 

class SubracesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subrace
        fields = ('id', 'name') 