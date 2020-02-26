from django.urls import path
from . import views

app_name = "apps"
urlpatterns =[
    path('create/',views.create, name="create"),
    path('delete/<int:id>',views.delete, name="delete"),
    path('update/<int:id>',views.update, name="update"),
    path('detail/<int:id>',views.detail, name="detail"),
]