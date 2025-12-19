
from django.contrib import admin
from django.urls import path, include
from web_project.views import SystemView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("", include("apps.dashboard.urls")),
]
