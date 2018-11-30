from django.db import models
# from .department import Department


class Employee(models.Model):
    fio = models.CharField(
        max_length=255,
        verbose_name="ФИО"
    )
    phone = models.CharField(
        max_length=14,
        verbose_name="Номер"
    )
    address = models.CharField(
        max_length=255,
        verbose_name="Адрес"
    )
    department = models.ForeignKey(
        'company.Department',
        # related_name='my_department',
        on_delete=models.CASCADE,
        verbose_name='Департамент',
    )

    def __str__(self):
        return self.fio

    def get_absolute_url(self):
        return '/main/employee/{pk}'.format(pk=self.pk)
