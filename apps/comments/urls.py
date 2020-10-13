"""
URL routing to comments
url: /bedankje/
"""
from django.urls import path

from comments import views

app_name = "comments"
urlpatterns = [
    path(
        "",
        views.CommentListView.as_view(),
        name="comment-list"
    )
]
