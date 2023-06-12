from django.urls import path, include
from rest_framework import routers

from .views import TestViewSet

router = routers.SimpleRouter()
router.register(r"tests", TestViewSet, basename="tests")

urlpatterns = [
    path("api/", include(router.urls)),
]