from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors137631ViewSet

router = DefaultRouter()
router.register(
    "testconnectors137631", Testconnectors137631ViewSet, basename="testconnectors137631"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
