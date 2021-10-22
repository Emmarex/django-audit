from django.contrib import admin
from django.urls import path

from .views import TestView

urlpatterns = [
    path("admin/", admin.site.urls)
]
