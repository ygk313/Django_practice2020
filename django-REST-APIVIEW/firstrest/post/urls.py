from django.urls import path, include
from . import views

urlpatterns=[
    path('post/', views.PostList.as_view()),
    path('post/<int:pk>/', views.PostDetail.as_view()),
]