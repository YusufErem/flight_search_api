from flights.serializer import HavaalanlariSerializer, UcuslarSerializer
from flights.models import Havaalanlari, Ucuslar
from rest_framework import status,viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.
class HavaalaniViewset(viewsets.ModelViewSet):
    serializer_class = HavaalanlariSerializer

    def get_queryset(self):
        queryset = Havaalanlari.objects.all()
        city = self.request.GET.get('sehir')
        if city: 
            queryset = queryset.filter(sehir__icontains = city)
        return queryset
    
class UcuslarViewset(viewsets.ModelViewSet):
    serializer_class = UcuslarSerializer
    queryset = Ucuslar.objects.all()
    
    def list(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def create(self, request):
        print("Error ver")
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    @action(detail=False, methods=['get'], url_path='list')
    def list_ucus(self,request):
        queryset = Ucuslar.objects.all()
        kalkis_yeri = self.request.GET.get('kalkis-yeri')
        varis_yeri = self.request.GET.get('varis-yeri')
        kalkis_tarihi = self.request.GET.get('kalkis-tarihi')
        donus_tarihi = self.request.GET.get('donus-tarihi')

        if kalkis_yeri:
            queryset = queryset.filter(kalkis_havaalani__sehir__icontains=kalkis_yeri)
        if varis_yeri:
            queryset = queryset.filter(varis_havaalani__sehir__icontains=varis_yeri)
        if kalkis_tarihi:
            queryset = queryset.filter(kalkis_zamani__date__gte=kalkis_tarihi)
        if donus_tarihi:
            queryset = queryset.filter(donus_zamani__date__lte=donus_tarihi)

        serializer = self.get_serializer(queryset, many=True)
        return  Response(serializer.data)

    @action(detail=False, methods=['post'], url_path='create')
    def create_ucus(self, request):
        kalkis_yeri = request.data.get('kalkis_havaalani')
        inis_yeri = request.data.get('varis_havaalani')
        kalkis_zamani = request.data.get('kalkis_zamani')
        donus_zamani = request.data.get('donus_zamani')
        
        if kalkis_yeri == inis_yeri:
            return Response(
                    {"detail": "Kalkis Havaalani ile Varis Havaalani Ayni Sehirde Olamaz."},
                    status=status.HTTP_400_BAD_REQUEST)

           
        if kalkis_zamani and donus_zamani:
            print(f"{kalkis_yeri,kalkis_zamani,donus_zamani,inis_yeri}TEST")

            if kalkis_zamani >= donus_zamani:
                return Response(
                    {"detail": "Kalkış tarihi dönüş tarihinden büyük veya eşit olamaz."},
                    status=status.HTTP_400_BAD_REQUEST)
            
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
