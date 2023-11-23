from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Profile, Posts, Feed, Messages, Media, Follows
import django.contrib.auth.password_validation as validation
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

class UserSerializer (serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, attrs):
        password = attrs.pop('password')
        password_confirmation = attrs.pop('password_confirmation')

        if password != password_confirmation:
            raise ValidationError({'detail':'Password and Confirmation do not match'})

        try:
            validation.validate_password(password=password)
        except ValidationError as err:
            raise ValidationError({'password': err})

        attrs['password'] = make_password(password)

        return attrs
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'password', 'password_confirmation']

class GroupSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ProfileSerializer (serializers.ModelSerializer):
    # user = UserSerializer()
    class Meta:
        model = Profile
        fields = '__all__'
    # def create(self, validated_data):
    #     user_data = validated_data.pop('user')
    #     profile = Profile.objects.create(**validated_data)
    #     User.objects.create(profile=profile, **user_data)
    #     return profile

# class MediaSerializer (serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Media
#         fields = '__all__'

class PostsSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'

class FeedSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Feed
        fields = '__all__'

class MessagesSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Messages
        fields = '__all__'

class FollowsSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Follows
        fields = '__all__'

class MediaSerializer (serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'
