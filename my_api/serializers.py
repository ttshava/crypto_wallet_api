from rest_framework import serializers
from .models import Btc , Eth

class BtcSerializer(serializers.ModelSerializer):
    class Meta:
        model = Btc
        fields = '__all__'

class EthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eth
        fields = '__all__'

