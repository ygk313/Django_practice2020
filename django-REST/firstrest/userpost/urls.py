from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('user', views.UserPostViewSet)
urlpatterns=[
    path('', include(router.urls))
]