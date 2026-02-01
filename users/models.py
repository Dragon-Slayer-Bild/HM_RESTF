from django.contrib.auth.models import AbstractUser
from django.db import models
from lms.models import Сourse, Lesson


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True, verbose_name="Email", help_text="Укажите почту"
    )
    phone = models.CharField(
        max_length=35,
        verbose_name="Телефон",
        blank=True,
        null=True,
        help_text="Введите номер телефона",
    )
    avatar = models.ImageField(
        upload_to="users/avatar",
        verbose_name="Аватар",
        blank=True,
        null=True,
        help_text="Загрузите аватар",
    )
    city = models.CharField(
        max_length=255, verbose_name="Город", help_text="Введите город проживания"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


class Payments(models.Model):
    payment_method = (('cash', 'Наличные'), ('transfer_to_account', 'Перевод на счет'))

    user = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Пользователь', related_name='payments',
                             null=True)
    date = models.DateField(auto_now_add=True, verbose_name='Дата оплаты')
    paid_course = models.ForeignKey(Сourse, on_delete=models.SET_NULL, verbose_name='Курс для оплаты', related_name='payments', blank=True, null=True)
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, verbose_name='Урок для оплаты',
                                    related_name='payments', blank=True, null=True)
    amount = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='Сумма оплаты', blank=True, null=True)
    method = models.CharField(max_length=30, choices=payment_method, verbose_name='Способ оплаты', blank=True, null=True)

    def __str__(self):
        return f'{self.method} {self.amount}'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
