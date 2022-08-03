from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin


class TeacherManager(BaseUserManager):
    use_in_migration = True

    def create_user(self, email, phone_number, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, *extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Teacher(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(unique=True, error_messages={'unique': 'Такой пользователь уже зарегистрирован'}, null=True)
    phone_number = models.IntegerField(null=True, unique=True)
    class_name = models.CharField(max_length=255, verbose_name='Название предмета', blank=True, null=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)


    objects = TeacherManager()

    USERNAME_FIELD: str = 'phone_number'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name_plural = 'Учителя'

    def __str__(self):
        return str(self.phone_number)