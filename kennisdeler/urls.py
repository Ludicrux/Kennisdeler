"""
Core URL patterns
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from django.conf import settings


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("kennisbank/", include("articles.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    # Change pathing through user profiles
    path("berichten/", include("comments.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
