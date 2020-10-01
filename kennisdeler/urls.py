"""
Core URL patterns
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from . import base as settings


urlpatterns = [
    path("admin/", admin.site.urls),
    path("kennisbank/", include("articles.urls")),
    # path("profile/", include("profiles.urls")),
    path("", include("core.urls")),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)