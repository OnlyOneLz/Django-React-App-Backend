from django.contrib.auth.models import User, Group
from .models import Cat, Dog, Bird
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, GroupSerializer, DogSerializer, CatSerializer, BirdSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    permission_classes = [permissions.IsAuthenticated]

class DogViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    permission_classes = [permissions.IsAuthenticated]

class BirdViewSet(viewsets.ModelViewSet):
    queryset = Bird.objects.all()
    serializer_class = BirdSerializer
    permission_classes = [permissions.IsAuthenticated]