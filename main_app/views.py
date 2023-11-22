from django.contrib.auth.models import User, Group
from .models import Profile, Posts, Feed, Messages, Media
from rest_framework import viewsets, permissions, generics, status, parsers
from .serializers import UserSerializer, GroupSerializer, ProfileSerializer, PostsSerializer, FeedSerializer, MessagesSerializer, MediaSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser, FormParser

# import uuid
# import boto3
# import os


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # permission_classes = [permissions.IsAuthenticated]

# class ProfileViewSet(generics.ListCreateAPIView):
#     model = Profile
#     serializer_class = ProfileSerializer
#     def get_queryset(self):
#         id = self.kwargs['id']
#         queryset = Profile.objects.filter(user= id)
#         return queryset
    
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    # def retrieve(self, request, *args, **kwargs):
    #     # The Primary Key of the object is passed to the retrieve method through self.kwargs
    #     user = self.kwargs['pk']

# def media(request, profile_id):
#     # photo-file will be the "name" attribute on the <input type="file">
#     photo_file = request.FILES.get('photo-file', None)
#     if photo_file:
#         s3 = boto3.client('s3')
#         # need a unique "key" for S3 / needs image file extension too
#         key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
#         # just in case something goes wrong
#         try:
#             bucket = os.environ['S3_BUCKET']
#             s3.upload_fileobj(photo_file, bucket, key)
#             # build the full url string
#             url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
#             # we can assign to cat_id or cat (if you have a cat object)
#             media.objects.create(url=url, profile_id=profile_id)
#         except Exception as e:
#             print('An error occurred uploading file to S3')
#             print(e)
    



class PostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    # permission_classes = [permissions.IsAuthenticated]

class FeedViewSet(viewsets.ModelViewSet):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
    # permission_classes = [permissions.IsAuthenticated]

class MessagesViewSet(viewsets.ModelViewSet):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer
    # permission_classes = [permissions.IsAuthenticated]

class HomeView(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self, request):
        content = {'message': 'Welcome to the JWT Authentication page using React Js and Django!'}
        return Response(content)


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CreateProfile(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    parser_classes = [MultiPartParser, FormParser]  # Add these parser classes to handle file uploads

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    # def post(self, request, format=None):
    #     user = UserSerializer(user = self.request.user)
    #     user.save()
    #     return Response(status=status.HTTP_201_created)

class ProfileDeleteViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class userDeleteViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class addMediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    http_method_names = ['get', 'post', 'patch', 'delete']

class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer