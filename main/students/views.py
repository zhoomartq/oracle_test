from .models import Students
from .serializers import StudentSerializer, MultipleMailSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.core.mail import send_mail
from decouple import config
from rest_framework.generics import CreateAPIView






class StudentViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['full_name', 'mail', 'address', 'gender']

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data, many=True).data
        if serializer.is_valid():
            photo = self.request.FILES['photo']
            author = request.author
            author.photo = photo
            author.save()

            return Response({'photo' : request.build_absolute_uri(author.photo.url) if author.photo else None}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    
class MultipleMailView(CreateAPIView):

    serializer_class = MultipleMailSerializer

    def post(self, request, *args, **kwargs):
        serializer = MultipleMailSerializer(data=request.data)
        student = Students.objects.all()
        email = [i.mail for i in student]
        if serializer.is_valid():
            text = serializer.validated_data['text']
            title = serializer.validated_data['title']
            for i in email:
                send_mail("{}".format(title), "{}".format(text), config('EMAIL_HOST_USER'), [i])
            return Response('Сообщение успешно отправлено всем ученикам!', status=status.HTTP_200_OK)
        return Response('Сообщение не отправлено', status=status.HTTP_400_BAD_REQUEST)



