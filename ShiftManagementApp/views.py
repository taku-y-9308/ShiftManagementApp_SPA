from rest_framework import viewsets
from ShiftManagementApp.models import User
from ShiftManagementApp.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer