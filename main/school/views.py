from .models import School
from .serializers import SchoolSerializer
from rest_framework import generics


class SchoolListAPIView(generics.ListAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
