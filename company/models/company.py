from django.db import models

class Company(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    ruler = models.OneToOneField(
        'company.Employee',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Руководитель',
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/main/company/{pk}'.format(pk=self.pk)
