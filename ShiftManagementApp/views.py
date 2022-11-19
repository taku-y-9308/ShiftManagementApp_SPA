from rest_framework import viewsets
from ShiftManagementApp.models import User,Shift
from ShiftManagementApp.serializers import UserSerializer,ShiftSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters 


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ShiftFilter(filters.FilterSet):
    date_gte = filters.DateFilter(field_name="date",lookup_expr="gte")
    date_lte = filters.DateFilter(field_name="date",lookup_expr="lte")

    class Meta:
        model = Shift
        fields = ['date_gte','date_lte','user']


class ShiftViewSet(viewsets.ModelViewSet):
    serializer_class = ShiftSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ShiftFilter
    
    def get_queryset(self):
        if self.request.user.is_staff == True:
            return Shift.objects.all().order_by('begin')
        else:
            return Shift.objects.filter(publish=True).order_by('begin') | Shift.objects.filter(user=self.request.user).order_by('begin')

    """ 
    def get_queryset(self):
        
       #クエリパラメータuserの有無で返すquerysetを変える
        if self.request.query_params.get('user') is not None:

             #クエリパラメータでuserのシフトを要求したユーザーが本人か、そうでないかで返すquertsetを変える
            if self.request.user.id == int(self.request.query_params.get('user')):
                return Shift.objects.filter(id=int(self.request.query_params.get('user'))).order_by('begin')
            else:
                return Shift.objects.filter(id=int(self.request.query_params.get('user')),publish=True).order_by('begin')
        else:
            return Shift.objects.all()
    """
