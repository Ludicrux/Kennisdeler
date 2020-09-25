"""URL routing to Articles"""
from django.urls import path

from . import views


app_name = "articles"
urlpatterns = [
    path(
        '<order_by>/',
        views.ArticleListView.as_view(),
        name="article_list_new"
        ),
    path(
        "<slug:slug>/",
        views.ArticleDetailView.as_view(),
        name="article_detail"
    ),
]
