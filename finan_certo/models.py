from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser

from finan_certo.managers import CustomUserManager

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return str(self.id)
    
class FinancasUsuario(models.Model):
    TIPO_MES = (
        (1,'Janeiro'),
        (2,'Fevereiro'),
        (3,'Março'),
        (4,'Abril'),
        (5,'Maio'),
        (6,'Junho'),
        (7,'Julho'),
        (8,'Agosto'),
        (9,'Setembro'),
        (10,'Outubro'),
        (11,'Novembro'),
        (12,'Dezembro')
    )

    MES_ATUAL = models.IntegerField(choices=TIPO_MES)
    ID_USUARIO = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    FINANCAS_RECEITAS = models.FloatField(null=False, blank=False)
    FINANCAS_DESPESAS = models.FloatField(null=False, blank=False)
    FINANCAS_BALANCO = models.FloatField(null=False, blank=True)
    FINANCAS_CRIADO_EM = models.DateTimeField(auto_now=True)
    FINANCAS_ANO =  models.IntegerField(null=False)

    @property
    def ano(self):
        return self.FINANCAS_CRIADO_EM.year if self.FINANCAS_CRIADO_EM else timezone.now().year
    
    def save(self, *args, **kwargs):

        self.FINANCAS_BALANCO = self.FINANCAS_RECEITAS - self.FINANCAS_DESPESAS

        self.FINANCAS_ANO = self.FINANCAS_CRIADO_EM.year if self.FINANCAS_CRIADO_EM else timezone.now().year

        balancoExistente = FinancasUsuario.objects.filter(
            ID_USUARIO=self.ID_USUARIO, 
            MES_ATUAL=self.MES_ATUAL
            
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
        return f"{self.ID_USUARIO} - {self.get_MES_ATUAL_display()} ({self.ano})"
    
    class Meta:
        db_table = "fc_financas_usuario"

class UsuarioMeta(models.Model):
    TIPO_MES = (
        (1,'Janeiro'),
        (2,'Fevereiro'),
        (3,'Março'),
        (4,'Abril'),
        (5,'Maio'),
        (6,'Junho'),
        (7,'Julho'),
        (8,'Agosto'),
        (9,'Setembro'),
        (10,'Outubro'),
        (11,'Novembro'),
        (12,'Dezembro')
    )

    MES_ATUAL = models.IntegerField(choices=TIPO_MES)
    ID_USUARIO = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    ANO_META = models.IntegerField(null=False)
    USUARIO_META = models.FloatField(null=False, blank=False)
    USUARIO_ENTRADA = models.FloatField(null=True, blank=True)
    META_CRIADO_EM = models.DateTimeField(auto_now_add=True)
    ATUALIZADO_EM = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        metaExistente = UsuarioMeta.objects.filter(
            ID_USUARIO=self.ID_USUARIO,
            MES_ATUAL=self.MES_ATUAL,
            ANO_META=self.ANO_META,
            USUARIO_META=self.USUARIO_META,
            USUARIO_ENTRADA=self.USUARIO_ENTRADA
        ).first()

        if metaExistente:
                
            UsuarioMeta.objects.filter(pk=metaExistente.pk).update(
                USUARIO_META=self.USUARIO_META,
                USUARIO_ENTRADA=self.USUARIO_ENTRADA,
                MES_ATUAL=self.MES_ATUAL,
                ANO_META=self.ANO_META,
                ATUALIZADO_EM=timezone.now()
            )
            return
        else:    
            super(UsuarioMeta, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.ID_USUARIO} - {self.get_MES_ATUAL_display()} ({self.ANO_META})"
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['ID_USUARIO', 'MES_ATUAL', 'ANO_META'], name='unique_usuario_meta')
        ]
        db_table = "fc_meta_usuario"
