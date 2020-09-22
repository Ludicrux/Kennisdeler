"""
Core URL patterns
"""
from django.contrib import admin
from django.urls import include, path

from . import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("article/", include("articles.urls")),
    # path("profile/", include("profiles.urls")),
    path("", views.HomePageListView.as_view(), name="Homepage")
]
