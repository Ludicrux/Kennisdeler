"""
URL routing to Articles
url: /kennisbank/
"""
from django.urls import path

from articles import views


app_name = "articles"
urlpatterns = [
    path("", views.redirect_to_list_view, name="redirect"),
    path(
        "<order_by>/",
        views.ArticleListView.as_view(),
        name="article-list"
        ),
    path(
        "kennis/<slug:slug>/bewerken",
        views.ArticleEditView.as_view(),
        name="article-edit"
    ),
    path(
        "kennis/<slug:slug>/favorite",
        views.favorite_article,
        name="article-favorite"
    ),
    path(
        "kennis/<slug:slug>/comment",
        views.create_comment,
        name="article-comment"
    ),
    path(
        "kennis/<slug:slug>/",
        views.ArticleDetailView.as_view(),
        name="article-detail"
    ),
    path(
        "nieuwekennis",
        views.ArticleCreateView.as_view(),
        name="article-create"
    ),
]
