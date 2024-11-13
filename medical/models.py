from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Doctor(models.Model):
    """Модель врачей"""

    name = models.CharField(max_length=255, verbose_name="ФИО врача")
    age = models.PositiveIntegerField(verbose_name="Возраст", **NULLABLE)
    specialization = models.CharField(max_length=255, verbose_name="Специальность")
    qualification = models.CharField(
        max_length=255, verbose_name="Категория", **NULLABLE
    )
    experience = models.PositiveIntegerField(verbose_name="Стаж", **NULLABLE)
    avatar = models.ImageField(upload_to="medical/doctors", **NULLABLE)
    education = models.TextField(verbose_name="Образование", **NULLABLE)
    comment = models.TextField(verbose_name="Дополинительные сведения", **NULLABLE)

    class Meta:
        verbose_name = "Врач"
        verbose_name_plural = "Врачи"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Service(models.Model):
    """модель услуг"""

    service_name = models.CharField(max_length=255, verbose_name="Название услуги")
    price = models.PositiveIntegerField(verbose_name="Цена")
    description = models.TextField(verbose_name="Описание услуги", **NULLABLE)

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
        ordering = ["service_name"]

    def __str__(self):
        return f"{self.service_name} - {self.price} руб."


class Appointment(models.Model):
    """Модель записи"""

    date = models.DateField(verbose_name="Дата записи")
    time = models.TimeField(verbose_name="Время записи")
    doctor = models.ForeignKey(
        Doctor, max_length=100, on_delete=models.CASCADE, verbose_name="Врач"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создана")
    owner = models.ForeignKey(
        User, verbose_name="Пользователь", on_delete=models.SET_NULL, **NULLABLE
    )

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

    def __str__(self):
        return (
            f"{self.owner}, Вы записаны к "
            f"{self.doctor.name} на {self.date} в {self.time}"
        )


class Result(models.Model):
    """Модель результатов исследований"""

    date = models.DateField(auto_now_add=True, verbose_name="Дата исследования")
    test = models.CharField(max_length=200, verbose_name="Название исследования")
    result = models.CharField(max_length=150, verbose_name="Результат")
    units_of_measurement = models.CharField(
        max_length=100, verbose_name="Единицы измерения", **NULLABLE
    )
    reference_values = models.CharField(
        max_length=100, verbose_name="Референсные значения", **NULLABLE
    )
    owner = models.ForeignKey(
        User, verbose_name="Пользователь", on_delete=models.SET_NULL, **NULLABLE
    )

    class Meta:
        verbose_name = "Результат"
        verbose_name_plural = "Результаты"
        ordering = ["-date"]

    def __str__(self):
        return (
            f"Тест: {self.test}, "
            f"Результат: {self.result}, Единицы измерения: {self.units_of_measurement}"
        )


class Contact(models.Model):
    """Модель обратной связи"""

    name = models.CharField(
        max_length=100,
        verbose_name="Имя",
    )
    phone = models.CharField(
        max_length=50,
        verbose_name="Телефон",
        null=True,
        blank=True,
    )
    message = models.TextField(
        verbose_name="Сообщение",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"


class Static(models.Model):
    """Модель статичной страницы компании"""

    company = models.TextField(verbose_name="О компании")
    about = models.TextField(verbose_name="О нас", **NULLABLE)
    history = models.TextField(verbose_name="История", **NULLABLE)
    values = models.TextField(verbose_name="Ценности", **NULLABLE)
    address = models.TextField(max_length=255, verbose_name="Адрес", **NULLABLE)
    phone = models.CharField(max_length=255, verbose_name="Телефон", **NULLABLE)
    email = models.EmailField(verbose_name="Электронная почта", **NULLABLE)
    map = models.ImageField(upload_to="medical/maps", **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создана")

    def __str__(self):
        return self.company

    class Meta:
        verbose_name = "Статика"
        verbose_name_plural = "Статика"
