"""
URL routing to Articles
url: /kennisbank/
"""
from django.urls import path

from articles import views
from articles.forms import ArticleFormPage1, ArticleFormPage2


app_name = "articles"
urlpatterns = [
    path(
        "<str:order_by>/pagina<int:page>/",
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
        "kennis/<slug:slug>/like",
        views.like_article,
        name="article-like"
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
        "nieuwekennis/pagina<int:num>",
        views.ArticleCreateView.as_view([ArticleFormPage1, ArticleFormPage2]),
        name="article-create-page"
    ),
    path(
        "nieuwekennis/",
        views.ArticleCreateView.as_view([ArticleFormPage1, ArticleFormPage2]),
        name="article-create"
    ),
]
