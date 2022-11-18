from rest_framework import viewsets
from ShiftManagementApp.models import User,Shift
from ShiftManagementApp.serializers import UserSerializer,ShiftSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ShiftViewSet(viewsets.ModelViewSet):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer