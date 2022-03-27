

from django.contrib.auth import get_user_model
from rest_framework import viewsets


from .serializers import CustomUserDetailsSerializer


class UserList(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = CustomUserDetailsSerializer
