import re
from django.forms import ValidationError
from rest_framework import serializers

from finan_certo.models import CadastroUsuario, FinancasUsuario, UsuarioMeta

class CadastroUsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = CadastroUsuario
        fields = '__all__'

    
    def validate_email(self,value):

        if CadastroUsuario.objects.filter(USUARIO_EMAIL=value).exists():
            raise serializers.ValidationError('Email já cadastrado!')

        return value

    def validate(self, data):
    
        if len(data['USUARIO_SENHA']) < 8:
            raise serializers.ValidationError('Senha fraca!')
            
        if not re.search(r'[A-Z]', data['USUARIO_SENHA']):
            raise serializers.ValidationError('A USUARIO_SENHA deve conter pelo menos uma letra maiúscula')
            
        if not re.search(r'[a-z]', data['USUARIO_SENHA']):
            raise serializers.ValidationError('A senha deve conter pelo menos uma letra minúscula')
            
        if not re.search(r'[0-9]', data['USUARIO_SENHA']):
            raise serializers.ValidationError("A senha deve conter pelo menos um número.")

        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', data['USUARIO_SENHA']):
            raise serializers.ValidationError('A senha deve conter pelo menos um caractere especial.')
        
        return data

class FinancasUsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = FinancasUsuario
        fields = '__all__'

class UsuarioMetaSerializer(serializers.ModelSerializer):

    class Meta:
        model = UsuarioMeta
        fields = '__all__'
