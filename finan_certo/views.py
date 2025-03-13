from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from finan_certo.models import CadastroUsuario
from finan_certo.serializers import CadastroUsuarioSerializer

class CadastroUsuarioViewSet(viewsets.ModelViewSet):
    queryset = CadastroUsuario.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CadastroUsuarioSerializer
    ordering_fields = ('id',)
    filterset_fields = ('id', 'USUARIO_NOME_COMPLETO', 'USUARIO_EMAIL') 
