from os import read
from turtle import st
from rest_framework import serializers
from .models import Students

class StudentSerializer(serializers.ModelSerializer):
    classes = serializers.CharField(source='classes.title', read_only=True)

    class Meta:
        model = Students
        fields = '__all__'
    

    def update(self, instance, validated_data):
        classes_student = validated_data.pop('classes')
        student = instance.classes

        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.mail = validated_data.get('mail', instance.mail)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.address = validated_data.get('address', instance.address)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.photo = validated_data.get('photo', instance.photo)

        student.title = classes_student.get('title', student.title)
        student.save()
        return instance


class MultipleMailSerializer(serializers.Serializer):

    title = serializers.CharField(max_length=255)
    text = serializers.CharField(max_length=500)