from rest_framework import serializers
from .models import Camisa, Calca, Tenis, Casaco

class CamisaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camisa
        fields = '__all__'

class CalcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calca
        fields = '__all__'

class TenisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenis
        fields = '__all__'

class CasacoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Casaco
        fields = '__all__'