from django.db import models
from registration.models import Teacher
from school.models import School


class Classes(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название класса')
    teacher = models.ForeignKey(Teacher, related_name='teacher_class', on_delete=models.SET_NULL, null=True, verbose_name='Учитель')
    school = models.ForeignKey(School, related_name='school_class', on_delete=models.SET_NULL, null=True, verbose_name='Школа')


    class Meta:
        verbose_name = 'Классы'
        verbose_name_plural = 'Класс'

    def __str__(self):
        return self.title