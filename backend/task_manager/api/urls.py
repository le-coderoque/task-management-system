from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdvertViewSet, TaskViewSet

router = DefaultRouter()
router.register('tasks', TaskViewSet, basename='tasks')
router.register('adverts', AdvertViewSet, basename='adverts')

urlpatterns = [
    path('', include(router.urls)),
]
