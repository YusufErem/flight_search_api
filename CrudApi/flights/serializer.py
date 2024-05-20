from rest_framework import serializers
from flights.models import *

class HavaalanlariSerializer(serializers.ModelSerializer):
    class Meta:
        model = Havaalanlari
        fields = ['id','sehir']


class UcuslarSerializer(serializers.ModelSerializer):
    kalkis_havaalani = serializers.PrimaryKeyRelatedField(queryset=Havaalanlari.objects.all())
    varis_havaalani = serializers.PrimaryKeyRelatedField(queryset=Havaalanlari.objects.all())
    
    
  
    class Meta: 
        model = Ucuslar
        fields = ['id','kalkis_havaalani', 'varis_havaalani', 'kalkis_zamani', 'donus_zamani', 'fiyat']
        

    


        
            
