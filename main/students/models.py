from django.db import models
from classes.models import Classes
from .helpers import post_send_email_for_student
from django.db.models.signals import post_save



GENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other')
)


class Students(models.Model):
    full_name = models.TextField()
    mail = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=255)
    gender = models.CharField(max_length=80, choices=GENDER)
    photo = models.ImageField(upload_to='images/',  verbose_name='Фото', blank=True, null=True)
    classes = models.ForeignKey(Classes, related_name='student_class', on_delete=models.SET_NULL, null=True, verbose_name='Класс')

    class Meta:
        verbose_name = 'Ученика'
        verbose_name_plural = 'Ученик'

    def __str__(self):
        return self.full_name

post_save.connect(post_send_email_for_student, Students)