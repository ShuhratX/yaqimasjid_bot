from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(verbose_name="Ism", max_length=100)
    username = models.CharField(verbose_name="Telegram username", max_length=100, null=True)
    telegram_id = models.BigIntegerField(verbose_name='Telegram ID', unique=True, default=1)

    class Meta:
        db_table = "users"

    def __str__(self):
        return f"{self.id} - {self.telegram_id} - {self.full_name}"


class Mosque(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="Masjid nomi", max_length=150)
    latitude = models.CharField(verbose_name="Kenglik", max_length=150)
    longtitude = models.CharField(verbose_name="Uzunlik", max_length=150)

    class Meta:
        db_table = "mosques"

    def __str__(self):
        return f"{self.id} - {self.name}"