from django.urls import include, path
from rest_framework import routers
from .views import ApiViewSet

router = routers.DefaultRouter()

router.register('api', ApiViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
