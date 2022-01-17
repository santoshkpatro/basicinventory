from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from . base import BaseModel


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        if not first_name:
            raise ValueError('Users must have first name')

        user = User(
            email=self.normalize_email(email),
            first_name=first_name,
            password=password
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, password=None):
        user = self.create_user(
            email,
            first_name,
            password
        )
        user.is_admin = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, BaseModel):
    email = models.EmailField(verbose_name='Email address', unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    avatar_url = models.CharField(max_length=200, blank=True, null=True)

    is_email_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    password_reset_required = models.BooleanField(default=False)
    password_reset_token = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )
    password_reset_expiry = models.DateTimeField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    objects = UserManager()

    class Meta:
        db_table = 'users'

    def __str__(self) -> str:
        return self.email

    # For Django Admin Panel
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
