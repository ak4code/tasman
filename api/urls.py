from django.urls import path, include
from rest_framework.routers import DefaultRouter
from projects.views import ProjectViewSet, BoardViewSet, CardViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'boards', BoardViewSet)
router.register(r'cards', CardViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
