from django.db import models
# from .company import Company
# from .Employee import Employee

class Department(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    ruler = models.OneToOneField(
        'company.Employee',
        related_name='this_ruller',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Руководитель',
    )
    company = models.ForeignKey(
        'company.Company',
        on_delete=models.CASCADE,
        verbose_name='Компания',
        default='',
        null=True,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/main/department/{pk}'.format(pk=self.pk)
