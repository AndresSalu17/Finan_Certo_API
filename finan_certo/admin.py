from django.contrib import admin

from finan_certo.models import CadastroUsuario

class CadastroUsuarioAdmin(admin.ModelAdmin):
    list_display = ('USUARIO_ID', 'USUARIO_NOME_COMPLETO', 'USUARIO_EMAIL', 'USUARIO_SENHA')
    list_filter = ('USUARIO_ID',)
    search_fields = ('USUARIO_ID', 'USUARIO_NOME_COMPLETO')
admin.site.register(CadastroUsuario, CadastroUsuarioAdmin)
