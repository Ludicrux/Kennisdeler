from django import forms

from .models import Article, Subject
import django_filters


class ArticleFilter(django_filters.FilterSet):
    subject = django_filters.ModelMultipleChoiceFilter(
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Article
        fields = ["subject", "level", "file_type", ]
