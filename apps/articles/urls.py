"""
URL routing to Articles
"""
from django.urls import path

from articles import views


app_name = "articles"
urlpatterns = [
    path(
        "kennis/<slug:slug>/bewerken",
        views.ArticleEditView.as_view(),
        name="article-edit"
    ),
    path(
        "kennis/<slug:slug>/favorite",
        views.FavoriteArticle,
        name="article-favorite"
    ),
    path(
        "kennis/<slug:slug>/comment",
        views.CreateComment,
        name="article-comment"
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
