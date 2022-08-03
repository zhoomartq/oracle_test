from .models import Classes
from .serializers import ClassesSerializer
from rest_framework import generics



class ClassesListAPIView(generics.ListAPIView):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer