from django.utils import timezone
from django.db import models

class CadastroUsuario(models.Model):
    USUARIO_NOME_COMPLETO = models.CharField(max_length=200)
    USUARIO_EMAIL = models.EmailField(max_length=200, null=False, blank=False)
    USUARIO_SENHA = models.CharField(max_length=50, null=False, blank=False)
    USUARIO_CRIADO_EM = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.id)
    
    class Meta:
        db_table = 'fc_usuarios'

class Meses(models.Model):
    MES_ATUAL = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.MES_ATUAL

    class Meta:
        db_table = 'fc_mes'

class FinancasUsuario(models.Model):
    ID_USUARIO = models.ForeignKey(CadastroUsuario, on_delete=models.CASCADE)
    FINANCAS_RECEITAS = models.FloatField(null=False, blank=False)
    FINANCAS_DESPESAS = models.FloatField(null=False, blank=False)
    FINANCAS_BALANCO = models.FloatField(null=False, blank=True)
    ID_MES = models.ForeignKey(Meses, on_delete=models.CASCADE, to_field='id')
    FINANCAS_CRIADO_EM = models.DateTimeField(auto_now=True)
    FINANCAS_ANO =  models.IntegerField(null=False)

    @property
    def ano(self):
        return self.FINANCAS_CRIADO_EM.year if self.FINANCAS_CRIADO_EM else timezone.now().year
    
    def save(self, *args, **kwargs):

        self.FINANCAS_BALANCO = self.FINANCAS_RECEITAS - self.FINANCAS_DESPESAS

        self.FINANCAS_ANO = self.FINANCAS_CRIADO_EM.year if self.FINANCAS_CRIADO_EM else timezone.now().year

        balancoExistente = FinancasUsuario.objects.filter(
            ID_USUARIO=self.ID_USUARIO, ID_MES=self.ID_MES
        ).first()

        if balancoExistente:
                
            FinancasUsuario.objects.filter(pk=balancoExistente.pk).update(
                
                FINANCAS_RECEITAS=self.FINANCAS_RECEITAS,
                FINANCAS_DESPESAS=self.FINANCAS_DESPESAS,
                FINANCAS_BALANCO=self.FINANCAS_BALANCO,
                FINANCAS_ANO=self.FINANCAS_ANO,
            )
            return
        else:    
            super(FinancasUsuario, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.ID_USUARIO} - {self.ID_MES.MES_ATUAL} ({self.ano})"
    
    class Meta:
        db_table = "fc_financas_usuario"
