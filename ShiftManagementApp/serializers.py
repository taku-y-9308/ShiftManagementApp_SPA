from rest_framework import serializers
from ShiftManagementApp.models import User,Shift

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'shop_id',
            'username',
            'default_position',
            'email',
            'is_edit_mode',
            'is_staff',
            'is_active',
            'is_pwa_user',
            'date_joined'
            ]

class ShiftSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Shift
        fields = [
            'id',
            'user',
            'username',
            'date',
            'begin',
            'finish',
            'position',
            'publish'
        ]