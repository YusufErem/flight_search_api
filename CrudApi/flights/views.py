from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.shortcuts import render
from flights.serializer import HavaalanlariSerializer, UcuslarSerializer
from flights.models import Havaalanlari, Ucuslar
from rest_framework import status
from django.shortcuts import get_object_or_404
# Create your views here.
@api_view(['POST'])
def airport_create(req):
    serialize = HavaalanlariSerializer(data = req.data)
    if serialize.is_valid():
        serialize.save()
        return Response(serialize.data)
    else:
        return Response(serialize.errors)

@api_view(['POST'])
def flight_create(req):
    pass

@api_view(['GET'])
def search_airport(req):
    
    Havaalanlari_query = req.query_params.get('havaalani').capitalize()

    if Havaalanlari_query:
        queryset = Havaalanlari.objects.filter(sehir = Havaalanlari_query)
        serializer = HavaalanlariSerializer(queryset,many= True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        queryset = Havaalanlari.objects.all()
        serializer = HavaalanlariSerializer(queryset,many= True)
        return Response(serializer.data)


@api_view(['GET'])
def search_flight(request):
    kalkis_havaalani1 = request.query_params.get('kalkis_havaalani')
    if kalkis_havaalani1:
        havaalanii =get_object_or_404(Havaalanlari,sehir=kalkis_havaalani1)
        queryset = Ucuslar.objects.filter(kalkis_havaalani= havaalanii)
        serializer = UcuslarSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Kalkış havaalanı belirtilmedi'}, status=status.HTTP_400_BAD_REQUEST)


def update(req):
    pass

def delete(req):
    pass