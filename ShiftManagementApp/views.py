from rest_framework import viewsets
from ShiftManagementApp.models import User,Shift
from ShiftManagementApp.serializers import UserSerializer,ShiftSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ShiftViewSet(viewsets.ModelViewSet):
    serializer_class = ShiftSerializer

    def get_queryset(self):
        queryset = Shift.objects.all().order_by('begin')
        user_id = self.request.query_params.get('user_id')
        if user_id is not None:
            user_id = int(user_id)
            queryset = queryset.filter(user=user_id)
        return queryset