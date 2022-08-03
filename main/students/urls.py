from django.urls import path
from .views import MultipleMailView


urlpatterns = [
    path("multiple-mail/", MultipleMailView.as_view(), name="multiple_mail")
]