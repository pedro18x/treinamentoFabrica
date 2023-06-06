from rest_framework import viewsets
from .models import Camisa, Calca, Tenis, Casaco
from .serializers import CamisaSerializer, CalcaSerializer, TenisSerializer, CasacoSerializer

class CamisaViewSet(viewsets.ModelViewSet):
    queryset = Camisa.objects.all()
    serializer_class = CamisaSerializer

class CalcaViewSet(viewsets.ModelViewSet):
    queryset = Calca.objects.all()
    serializer_class = CalcaSerializer

class TenisViewSet(viewsets.ModelViewSet):
    queryset = Tenis.objects.all()
    serializer_class = TenisSerializer

class CasacoViewSet(viewsets.ModelViewSet):
    queryset = Casaco.objects.all()
    serializer_class = CasacoSerializer