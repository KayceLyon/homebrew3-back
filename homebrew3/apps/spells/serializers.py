from rest_framework import serializers

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

class CantripsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cantrip
        fields = ('id', 'name')

class LevelOneSpellsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LevelOneSpell
        fields = ('id', 'name') 

class LevelTwoSpellsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LevelTwoSpell
        fields = ('id', 'name') 

class LevelThreeSpellsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LevelThreeSpell
        fields = ('id', 'name') 

class LevelFourSpellsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LevelFourSpell
        fields = ('id', 'name') 

class LevelFiveSpellsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LevelFiveSpell
        fields = ('id', 'name') 

class LevelSixSpellsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LevelSixSpell
        fields = ('id', 'name') 

class LevelSevenSpellsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LevelSevenSpell
        fields = ('id', 'name') 

class LevelEightSpellsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LevelEightSpell
        fields = ('id', 'name') 

class LevelNineSpellsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LevelNineSpell
        fields = ('id', 'name') 