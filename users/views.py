from django.contrib.auth.models import User

from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from users.permissions import IsOwner
from users.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser, IsOwner]

# def create_user(request):
#     user = User.objects.create_user(
#
#     )
#     return
