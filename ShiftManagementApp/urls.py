from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ShiftManagementApp import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', views.UserViewSet,basename="users")
router.register(r'shifts',views.ShiftViewSet,basename="shifts")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]