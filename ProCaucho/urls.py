
from django.contrib import admin
from django.urls import path
from django.urls import include, path

import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls', namespace="entries")),
]