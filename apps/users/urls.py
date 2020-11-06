"""
URL routing to Users
url: /profiel/
"""
from django.urls import path

from users import views

app_name = "users"
urlpatterns = [
    path("", views.UserProfileView.as_view(), name="user-profile"),
    path(
        "<slug:slug>",
        views.UserArticleListView.as_view(),
        name="user-article-list"
    ),
]
