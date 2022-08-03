from django.contrib import admin
from django.db import models
from .models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'email']
    ordering = ('email',)

    fieldsets = (
        (None, {
            'fields': ('email', 'phone_number', 'password', 'class_name', 'is_staff', 'is_superuser')
        }),
    )
    add_fieldsets = (
        (None, {
            'fields': ('email', 'phone_number', 'password', 'class_name', 'is_staff', 'is_superuser')
        }),
    )


admin.site.register(Teacher, TeacherAdmin)