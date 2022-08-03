from rest_framework import serializers
from .models import Teacher
from classes.serializers import ClassesSerializer


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, write_only=True)
    

    class Meta:
        model = Teacher
        fields = ('email', 'phone_number', 'password', 'class_name')


    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        phone_number = validated_data.get('phone_number')
        class_name = validated_data.get('class_name')
        user = Teacher.objects.create_user(email=email, phone_number=phone_number, password=password, class_name=class_name)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    phone_number = serializers.IntegerField()
    password = serializers.CharField()
    class_name = serializers.CharField()

    class Meta:
        fields = ('email', 'phone_number', 'password', 'class_name')


class TeacherListSerializer(serializers.ModelSerializer):
    teacher_class = ClassesSerializer(many=True, read_only=True)

    class Meta:
        model = Teacher
        fields = ('phone_number', 'class_name', 'teacher_class')