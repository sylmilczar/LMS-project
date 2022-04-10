from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import Group, PermissionsMixin
from django.db import models


class CustomAccountManager(BaseUserManager):
    def create_user(self, email, fullname, password=None):
        if not email:
            raise ValueError('Users must provide the email.')
        user = self.model(
            email=self.normalize_email(email),
            fullname=fullname
        )

        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        if not user.is_instructor:
            students_group = Group.objects.get(name='students')
            user.groups.add(students_group)
        return user

    def create_superuser(self, email, fullname, password=None):
        user = self.create_user(email=email, fullname=fullname, password=password)

        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=60, unique=True, verbose_name='email')
    fullname = models.CharField(max_length=30, unique=True)
    is_instructor = models.BooleanField(default=False)
    date_join = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = CustomAccountManager()

    def __str__(self):
        return self.email
