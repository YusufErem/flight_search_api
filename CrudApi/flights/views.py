from flights.serializer import HavaalanlariSerializer, UcuslarSerializer, UserSerializer
from flights.models import Havaalanlari, Ucuslar, Customer
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

class Register(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Login(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = Customer.objects.filter(email=email).first()
        if user is None:
            return Response(
                {"detail": "Invalid credentials"},
                status=status.HTTP_404_NOT_FOUND
            )
        if not user.check_password(password):
            return Response(
                {"detail": "Invalid credentials"},
                status=status.HTTP_404_NOT_FOUND
            )
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
        )
    
class HavaalaniViewset(viewsets.ModelViewSet):
    serializer_class = HavaalanlariSerializer

    def get_queryset(self):
        queryset = Havaalanlari.objects.all()
        code = self.request.GET.get('code')
        if code: 
            queryset = queryset.filter(code__icontains=code)
        return queryset

class UcuslarViewset(viewsets.ModelViewSet):
    serializer_class = UcuslarSerializer
    queryset = Ucuslar.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = UcuslarSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        kalkis_havaalani = request.data.get('kalkis_havaalani')
        inis_havaalani = request.data.get('inis_havaalani')

        if kalkis_havaalani == inis_havaalani:
            return Response(
                {"detail": "Kalkış havaalanı ile iniş havaalanı aynı olamaz"},
                status=status.HTTP_400_BAD_REQUEST
            )
        kalkis_zamani = request.data.get('kalkis_zamani')
        inis_zamani = request.data.get('inis_zamani')

        if inis_zamani <= kalkis_zamani:
            return Response(
                {"detail": "İniş zamanı kalkış zamanından önce olamaz"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = UcuslarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

    

