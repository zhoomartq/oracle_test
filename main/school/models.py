from django.db import models


class School(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название Школы')

    class Meta:
        verbose_name = 'Школа'

    def __str__(self):
        return self.title



