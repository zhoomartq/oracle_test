from django.urls import path
from .views import ClassesListAPIView

urlpatterns = [
    path('', ClassesListAPIView.as_view())
]