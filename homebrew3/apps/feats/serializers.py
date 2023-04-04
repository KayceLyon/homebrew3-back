from rest_framework import serializers
from .models import Feat

class FeatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feat
        fields = ('id', 'name') 