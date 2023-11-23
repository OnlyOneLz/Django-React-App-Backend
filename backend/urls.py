from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from main_app import views
from rest_framework_simplejwt import views as jwt_views
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'profile', views.ProfileViewSet)
router.register(r'profile', views.ProfileDeleteViewSet)
router.register(r'userDelete', views.userDeleteViewSet)
router.register(r'posts', views.PostsViewSet)
router.register(r'feed', views.FeedViewSet)
router.register(r'messages', views.MessagesViewSet)
router.register(r'add_media', views.addMediaViewSet)
router.register(r'media', views.MediaViewSet)
router.register(r'follows', views.FollowsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.CreateUser.as_view(), name='signup'),
    path('create_profile/', views.CreateProfile.as_view(), name='create_profile'),
    path('add_message/', views.CreateMessages.as_view(), name='create_message'),
    path('create_follow/', views.CreateFollows.as_view(), name='create_follow'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    # Remove the line below as it's not valid
    # path('profile_pics/', views.(), name='profile_pics'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Add the following line to serve media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
