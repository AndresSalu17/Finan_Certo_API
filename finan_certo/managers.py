from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Gerenciador de usuários personalizado para o modelo de usuário.
    Este gerenciador fornece métodos para criar usuários e superusuários
    com validações específicas.
    Métodos:
        create_user(email, password=None, **extra_fields):
            Cria e retorna um usuário com o email e senha fornecidos.
            Levanta um ValueError se o email não for fornecido.
        create_superuser(email, password=None, **extra_fields):
            Cria e retorna um superusuário com permissões administrativas.
            Garante que os campos `is_staff` e `is_superuser` sejam definidos como True.
            Levanta um ValueError se essas condições não forem atendidas.
    """
    def create_user(self, email, password=None, **extra_fields):
        """
        Cria e retorna um novo usuário com o email e senha fornecidos.

        Args:
            email (str): O endereço de email do usuário. Este campo é obrigatório.
            password (str, opcional): A senha do usuário. Pode ser None.
            **extra_fields: Campos adicionais para o modelo de usuário.

        Raises:
            ValueError: Se o email não for fornecido.

        Returns:
            user: A instância do usuário criada.
        """
        if not email:
            raise ValueError('O email é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Cria e retorna um superusuário com o email e senha fornecidos.
        Este método define os campos padrão `is_staff`, `is_superuser` e `is_active` como True.
        Ele também valida que os campos `is_staff` e `is_superuser` sejam True, 
        caso contrário, uma exceção será levantada.
        Args:
            email (str): O endereço de email do superusuário.
            password (str, opcional): A senha do superusuário. Padrão é None.
            **extra_fields: Campos adicionais para o superusuário.
        Raises:
            ValueError: Se `is_staff` não for True.
            ValueError: Se `is_superuser` não for True.
        Returns:
            User: O objeto de superusuário criado.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser precisa ter is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser precisa ter is_superuser=True.")

        return self.create_user(email, password, **extra_fields)