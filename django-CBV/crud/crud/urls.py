from django.contrib import admin
from django.urls import path, include 
import classcrud.urls
import classcrud.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('classcrud/',include('classcrud.urls')),
    # path('', classcrud.views.BlogView.as_view(), name="list"),
]
