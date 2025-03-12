from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from finan_certo.models import CadastroUsuario

class CadastroUsuarioViewSet(viewsets.ModelViewSet):
    queryset = CadastroUsuario.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CadastroUsuario
    ordering_fields = ('USUARIO_ID',)
    filterset_fields = ('USUARIO_ID', 'USUARIO_NOME_COMPLETO', 'USUARIO_EMAIL') 
