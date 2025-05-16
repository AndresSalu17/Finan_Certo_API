import re
from django.forms import ValidationError
from rest_framework import serializers

from finan_certo.models import FinancasUsuario, UsuarioMeta

from django.contrib.auth import get_user_model

User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True, min_length=8)
    
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    class Meta:
        model = User
        fields = '__all__'
class FinancasUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancasUsuario
        fields = '__all__'
class UsuarioMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioMeta
        fields = '__all__'

