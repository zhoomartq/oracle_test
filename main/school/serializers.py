from rest_framework import serializers
from .models import School
from classes.serializers import ClassesSerializer


class SchoolSerializer(serializers.ModelSerializer):
    school_class = ClassesSerializer(many=True, read_only=True)

    class Meta:
        model = School
        fields = '__all__'

