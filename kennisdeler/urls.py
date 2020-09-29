"""
Core URL patterns
"""
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("kennisbank/", include("articles.urls")),
    # path("profile/", include("profiles.urls")),
    path("", include("core.urls")),
]
