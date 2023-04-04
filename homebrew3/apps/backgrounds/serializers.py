from rest_framework import serializers
from .models import Background

class BackgroundsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Background
        fields = ('id', 'name') 