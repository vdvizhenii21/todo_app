from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter

from .views import TaskViewSet

router_v1 = DefaultRouter()

router_v1.register('tasks', TaskViewSet)

urlpatterns = [
    path(
        '', include(router_v1.urls),
    ),
    ]