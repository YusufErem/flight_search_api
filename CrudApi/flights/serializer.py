from rest_framework import serializers
from flights.models import *

class HavaalanlariSerializer(serializers.ModelSerializer):
    class Meta:
        model = Havaalanlari
        fields = '__all__'

class UcuslarSerializer(serializers.ModelSerializer):
    kalkis_havaalani = HavaalanlariSerializer()
    varis_havaalani = HavaalanlariSerializer()

    class Meta:
        model = Ucuslar
        fields = '__all__'

    


        
            
