from rest_framework import serializers
from .models import GolestanHikayat, Hafez, Khayyam, Moulavi

class GolestanHikayatSerializer(serializers.ModelSerializer):
    class Meta:
        model  = GolestanHikayat
        fields = '__all__'

class HafezSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Hafez
        fields = '__all__'

class KhayyamSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Khayyam
        fields = '__all__'

class MoulaviSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Moulavi
        fields = '__all__'
