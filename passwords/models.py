from django.db import models
from users.models import User


class Password(models.Model):
    """
        Model for storing passwords associated with users and services.
    """

    user = models.ForeignKey(User, verbose_name='Владелец', on_delete=models.CASCADE, related_name='passwords')
    password = models.CharField(max_length=255, verbose_name='Пароль')
    service_name = models.CharField(max_length=50, verbose_name='Сервис')

    def __str__(self):
        return f"Пароль {self.user} от {self.service_name}"

    class Meta:
        verbose_name = 'Пароль'
        verbose_name_plural = 'Пароли'
        db_table = 'passwords'



