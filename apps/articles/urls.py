"""URL routing to Articles"""
from django.urls import path

from . import views


app_name = "articles"
urlpatterns = [
    path(
        "kennis/<slug:slug>/",
        views.ArticleDetailView.as_view(),
        name="article-detail"
    ),
    path(
        '<order_by>/',
        views.ArticleListView.as_view(),
        name="article-list"
        ),
]
