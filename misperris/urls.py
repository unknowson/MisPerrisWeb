from rest_framework import routers
from blog import views
from django.contrib import admin
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pwa.urls')),
    path('', include('blog.urls')),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
