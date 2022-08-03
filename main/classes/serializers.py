from rest_framework import serializers
from .models import Classes
from students.serializers import StudentSerializer


class ClassesSerializer(serializers.ModelSerializer):
    teacher = serializers.CharField(source='teacher.phone_number')
    school = serializers.CharField(source='school.title')
    student_class = StudentSerializer(many=True, read_only=True)


    class Meta:
        model = Classes
        fields = '__all__'
