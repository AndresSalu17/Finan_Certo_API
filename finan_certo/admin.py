from django.contrib import admin

from finan_certo.models import CadastroUsuario

class CadastroUsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'USUARIO_NOME_COMPLETO', 'USUARIO_EMAIL', 'USUARIO_SENHA')
    list_filter = ('id',)
    search_fields = ('id', 'USUARIO_NOME_COMPLETO')
admin.site.register(CadastroUsuario, CadastroUsuarioAdmin)
