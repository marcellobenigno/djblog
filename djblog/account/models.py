from django.contrib.auth.models import (
    AbstractBaseUser, UserManager as BaseUserManager, PermissionsMixin
)
from django.db import models
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


class UserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField('Nome Completo', max_length=100)
    email = models.EmailField('E-mail', unique=True)
    phone = models.CharField('Telefone', max_length=14, blank=True)

    # admin
    is_staff = models.BooleanField('Equipe', default=False)
    is_active = models.BooleanField('Ativo', default=True)
    criado = models.DateTimeField('Criado em', auto_now_add=True)
    modificado = models.DateTimeField('Modificado em', auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_full_name(self):
        return str(self)

    def get_short_name(self):
        return str(self).split(" ")[0]

    def uidb64(self):
        return urlsafe_base64_encode(force_bytes(self.pk))
