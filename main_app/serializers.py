from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Bird, Dog, Cat

class UserSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups ']
class GroupSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
class CatSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cat
        fields = '__all__'
class DogSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dog
        fields = '__all__'
class BirdSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bird
        fields = '__all__'
