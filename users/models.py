from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    """модель пользователя"""

    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    name = models.CharField(max_length=100, verbose_name="ФИО")
    phone = models.CharField(max_length=35, verbose_name="Телефон", **NULLABLE)
    birth_date = models.DateField(verbose_name="Дата рождения", **NULLABLE)
    avatar = models.ImageField(
        upload_to="users/avatars/", verbose_name="Аватар", **NULLABLE
    )
    token = models.CharField(max_length=100, verbose_name="Токен", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
