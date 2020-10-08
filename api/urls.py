from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'videos', views.VideoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('video_search/', views.SearchAPIView.as_view())
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]