
"""
Forms for articles
"""
from django import forms
# from django.forms import ClearableFileInput
from articles.models import Article, Subject


class ArticleFormPage1(forms.ModelForm):
    title = forms.CharField(label='Titel', max_length=120)
    short_desc = forms.CharField(label="Korte omschrijving", max_length=120)
    image = forms.ImageField(label="Upload afbeelding")
    long_desc = forms.CharField(
        label="Geef hier een lange beschrijving (optioneel)",
        widget=forms.Textarea
    )
    uploaded_file = forms.FileField(
        label="Upload hier je bestanden (optioneel"
    )

    class Meta:
        model = Article
        fields = [
            'title',
            'short_desc',
            'image',
            'long_desc',
            "uploaded_file",
        ]


class ArticleFormPage2(forms.ModelForm):
    subject = forms.ModelChoiceField(
        label="Opleiding",
        queryset=Subject.objects.all(),
    )
    level = forms.IntegerField(
        label="Niveau"
    )
    file_type = forms.CharField(
        label="Soort document"
    )
    is_public = forms.BooleanField(label="Openbaar")

    class Meta:
        model = Article
        fields = [
            'subject',
            'level',
            'file_type',
            'is_public',
        ]
        exclude = [
            "author"
        ]


class ArticleForm(forms.ModelForm):
    """
    Create or update an article
    """
    class Meta:
        model = Article
        fields = [
            'title',
            'short_desc',
            'long_desc',
            'image',
            "uploaded_file",
            'subject',
            'level',
            'is_public',
        ]
        exclude = ["author"]

        # Future Feature: Multiple files
        # widgets = {
        #    'uploaded_file': ClearableFileInput(attrs={'multiple': True}),
        # }
