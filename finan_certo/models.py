from django.db import models

class CadastroUsuario(models.Model):
    USUARIO_ID = models.IntegerField(primary_key=True)
    USUARIO_NOME_COMPLETO = models.CharField(max_length=200)
    USUARIO_EMAIL = models.EmailField(max_length=200, null=False, blank=False)
    USUARIO_SENHA = models.CharField(max_length=50, null=False, blank=False)
    USUARIO_CRIADO_EM = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.USUARIO_ID)
    
    class Meta:
        db_table = 'fc_usuarios'
