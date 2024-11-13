# Generated by Django 5.0.7 on 2024-11-02 14:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("medical", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="appointment",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь",
            ),
        ),
        migrations.AddField(
            model_name="appointment",
            name="doctor",
            field=models.ForeignKey(
                max_length=100,
                on_delete=django.db.models.deletion.CASCADE,
                to="medical.doctor",
                verbose_name="Врач",
            ),
        ),
        migrations.AddField(
            model_name="result",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь",
            ),
        ),
    ]