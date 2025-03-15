from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from finan_certo.models import CadastroUsuario, FinancasUsuario, Meses
from finan_certo.serializers import CadastroUsuarioSerializer, FinancasUsuarioSerializer, MesesSerializer

class CadastroUsuarioViewSet(viewsets.ModelViewSet):
    queryset = CadastroUsuario.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CadastroUsuarioSerializer
    ordering_fields = ('id',)
    filterset_fields = ('id', 'USUARIO_NOME_COMPLETO', 'USUARIO_EMAIL') 

class MesesViewSet(viewsets.ModelViewSet):
    queryset = Meses.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = MesesSerializer
    ordering_fields = ('id',)
    filterset_fields = ('id', 'MES_ATUAL')

class FinancasUsuarioViewSet(viewsets.ModelViewSet):
    queryset = FinancasUsuario.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = FinancasUsuarioSerializer
    ordering_fields = ('id', )
    filterset_fields = ('id', 'ID_MES')
