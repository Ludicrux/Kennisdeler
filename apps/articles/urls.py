"""
URL routing to Articles
"""
from django.urls import path

from . import views


app_name = "articles"
urlpatterns = [
    path(
        "kennis/<slug:slug>/bewerken",
        views.ArticleEditView.as_view(),
        name="article-edit"
    ),
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
    path(
        'nieuwekennis',
        views.ArticleCreateView.as_view(),
        name="article-create"
    ),
]
