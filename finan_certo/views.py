from urllib import response
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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

class LoginViewSet(viewsets.ViewSet):

    # queryset = CadastroUsuario.objects.all()
    # permission_classes = [IsAuthenticated]
    def create(self, request):
        email = request.data.get('USUARIO_EMAIL')
        senha = request.data.get('USUARIO_SENHA')

        if not email or not senha:
            return Response({'error': 'Email e senha são obrigatórios!'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            usuario = CadastroUsuario.objects.get(USUARIO_EMAIL=email)
            if usuario.USUARIO_SENHA == senha:
                return Response({'message': 'Login realizado com sucesso!'}, status=status.HTTP_200_OK)
            
            else:
                return Response({'error': 'Senha incorreta!'}, status=status.HTTP_401_UNAUTHORIZED)

        except CadastroUsuario.DoesNotExist:
            return Response({'error': 'Usuário não encontrado!'}, status=status.HTTP_404_NOT_FOUND)
        