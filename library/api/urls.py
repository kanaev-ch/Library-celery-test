from django.urls import path, include
from rest_framework import routers

from .views import BookViewset, UserViewset


router = routers.DefaultRouter()
router.register(r'books', BookViewset, basename='books')
router.register(r'users', UserViewset, basename='users')

name = 'api'
urlpatterns = [
    path('', include(router.urls))
]
