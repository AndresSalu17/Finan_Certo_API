from urllib import request
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from finan_certo.models import CustomUser, FinancasUsuario, UsuarioMeta
from finan_certo.serializers import FinancasUsuarioSerializer, UserSerializer, UsuarioMetaSerializer

User = get_user_model()
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class FinancasUsuarioViewSet(viewsets.ModelViewSet):
    queryset = FinancasUsuario.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = FinancasUsuarioSerializer
    ordering_fields = ('id', )
    filterset_fields = ('id',)

class LoginViewSet(viewsets.ModelViewSet):

    def create(self, request):
        email = request.data.get('USUARIO_EMAIL')
        senha = request.data.get('USUARIO_SENHA')

        if not email or not senha:
            return Response({'error': 'Email e senha são obrigatórios!'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            usuario = CustomUser.objects.get(USUARIO_EMAIL=email)
            if usuario.USUARIO_SENHA == senha:
                return Response({'message': 'Login realizado com sucesso!'}, status=status.HTTP_200_OK)
            
            else:
                return Response({'error': 'Senha incorreta!'}, status=status.HTTP_401_UNAUTHORIZED)

        except CustomUser.DoesNotExist:
            return Response({'error': 'Usuário não encontrado!'}, status=status.HTTP_404_NOT_FOUND)
        
class UsuarioMetaViewSet(viewsets.ModelViewSet):
    queryset = UsuarioMeta.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UsuarioMetaSerializer

    @action(detail=False, methods=['post'])
    def criar_ou_atualizar_meta(self, request):
        usuario_id = request.data['ID_USUARIO']
        usuario = CustomUser.objects.get(id=usuario_id)
        mes = request.data['MES_ATUAL']
        ano = request.data['ANO_META']
        
        try:
            meta = UsuarioMeta.objects.get(ID_USUARIO=usuario, MES_ATUAL=mes, ANO_META=ano)
            meta.USUARIO_META = request.data['USUARIO_META']
            meta.USUARIO_ENTRADA = request.data['USUARIO_ENTRADA']
            meta.save()
            return Response({'mensagem': 'Meta atualizada com sucesso'})
        except UsuarioMeta.DoesNotExist:
            UsuarioMeta.objects.create(
                ID_USUARIO=usuario,
                MES_ATUAL=mes,
                ANO_META=ano,
                USUARIO_META=request.data['USUARIO_META'],
                USUARIO_ENTRADA=request.data['USUARIO_ENTRADA']
            )
            return Response({'mensagem': 'Meta criada com sucesso'})






