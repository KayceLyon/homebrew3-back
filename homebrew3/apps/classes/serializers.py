from rest_framework import serializers

from .models import Archetype
from .models import Classe
from .models import Subclasse

class ArchetypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archetype
        fields = ('id', 'name') 

class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classe
        fields = ('id', 'name') 

class SubclassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subclasse
        fields = ('id', 'name') 