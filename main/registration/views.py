from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework import status, exceptions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import *


class RegisterView(GenericAPIView):
   serializer_class = RegisterSerializer
   def post(self, request):
       data = request.data
       serializer = RegisterSerializer(data=data, context={'request': request})
       if serializer.is_valid(raise_exception=True):
           user = serializer.save()
           return Response('Регистрация пользователя прошла успешно!', status=status.HTTP_201_CREATED)



class LoginView(GenericAPIView):

    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(email=serializer.validated_data['email'], phone_number=serializer.validated_data['phone_number'], password=serializer.validated_data['password'], class_name=serializer.validated_data['class_name'])
        if not user:
            raise exceptions.AuthenticationFailed('Username or password are incorrect')

        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'phone_number':user.phone_number,
            'class_name': user.class_name,
        })


class TeacherListAPIView(ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherListSerializer
