"""
Core URL patterns
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

# from settings import base
from kennisdeler.settings import base


urlpatterns = [
    path("admin/", admin.site.urls),
    path("kennisbank/", include("articles.urls")),
    # path("profile/", include("profiles.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)
# urlpatterns += static(base.STATIC_URL, document_root=base.STATIC_ROOT)
