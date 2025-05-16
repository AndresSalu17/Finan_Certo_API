from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from finan_certo.models import CustomUser, FinancasUsuario, UsuarioMeta

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("id", "email", "first_name", "last_name","is_active", "is_staff")
    ordering = ("id",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Informações Pessoais", {
         "fields": ("first_name", "last_name" )}),
        ("Permissões", {"fields": ("is_active", "is_staff",
         "is_superuser", "groups", "user_permissions")}),
        ("Datas Importantes", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "first_name", "last_name", "password1", "password2", "role", "calculator_access", "is_active", "is_staff", "is_superuser"),
        }),
    )

    search_fields = ("email", "first_name", "last_name")

class FinancasUsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'FINANCAS_RECEITAS', 'FINANCAS_DESPESAS', 
                    'FINANCAS_BALANCO','MES_ATUAL','FINANCAS_CRIADO_EM')
    list_filter = ('id',)
    search_fields = ('id', 'FINANCAS_RECEITAS','FINANCAS_CRIADO_EM')
admin.site.register(FinancasUsuario, FinancasUsuarioAdmin)

class LoginAdmin(admin.ModelAdmin):
    list_display = ('USUARIO_EMAIL', 'USUARIO_SENHA')
    list_filter = ('USUARIO_EMAIL',)
    search_fields = ('USUARIO_NOME_COMPLETO', 'USUARIO_EMAIL')

admin.register(LoginAdmin)

class UsuarioMetaAdmin(admin.ModelAdmin):
    list_display = ('ID_USUARIO', 'USUARIO_META','USUARIO_ENTRADA',
                    'MES_ATUAL', 'ANO_META', 'META_CRIADO_EM', 'ATUALIZADO_EM')
    list_filter=('id',)
    search_fields=('id', 'USUARIO_META', 'META_CRIADO_EM')
    
admin.site.register(UsuarioMeta, UsuarioMetaAdmin)
