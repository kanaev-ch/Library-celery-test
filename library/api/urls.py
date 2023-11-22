from django.urls import path, include
from rest_framework import routers

from .views import BookViewset


router = routers.DefaultRouter()
router.register(r'books', BookViewset, basename='users')

name = 'api'
urlpatterns = [
    path('', include(router.urls)),
]
