from django.contrib import admin

from finan_certo.models import CadastroUsuario, FinancasUsuario

class CadastroUsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'USUARIO_NOME_COMPLETO', 'USUARIO_EMAIL', 'USUARIO_SENHA')
    list_filter = ('id',)
    search_fields = ('id', 'USUARIO_NOME_COMPLETO')
admin.site.register(CadastroUsuario, CadastroUsuarioAdmin)

class FinancasUsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'FINANCAS_RECEITAS', 'FINANCAS_DESPESAS', 
                    'FINANCAS_BALANCO','ID_MES','FINANCAS_CRIADO_EM')
    list_filter = ('id',)
    search_fields = ('id', 'FINANCAS_RECEITAS','FINANCAS_CRIADO_EM')
admin.site.register(FinancasUsuario, FinancasUsuarioAdmin)

class LoginAdmin(admin.ModelAdmin):
    list_display = ('USUARIO_EMAIL', 'USUARIO_SENHA')
    list_filter = ('USUARIO_EMAIL',)
    search_fields = ('USUARIO_NOME_COMPLETO', 'USUARIO_EMAIL')

admin.register(LoginAdmin)

