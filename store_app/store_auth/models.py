from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
# from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.db import models


class StoreUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.

        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class StoreUser(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(
        unique=True,
        max_length=25,
        blank=False,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    # USER_TYPE_CHOICES = (
    #     (1, 'publisher'),
    #     (2, 'customer'),
    # )
    #
    # user_type = models.BooleanField(choices=USER_TYPE_CHOICES)

    USERNAME_FIELD = 'email'

    object = StoreUserManager()

