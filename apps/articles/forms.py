
"""
Forms for articles
"""
from django import forms
# from django.forms import ClearableFileInput
from articles import models
from articles.models import Article, Subject


class ArticleFormPage1(forms.ModelForm):
    """First part of Article Creation form"""
    title = forms.CharField(label='Titel', max_length=120)
    short_desc = forms.CharField(label="Korte omschrijving", max_length=120)
    image = forms.ImageField(label="Upload afbeelding")
    long_desc = forms.CharField(
        label="Geef hier een lange beschrijving (optioneel)",
        widget=forms.Textarea,
        required=False
    )
    uploaded_file = forms.FileField(
        label="Upload hier je bestanden (optioneel)",
        required=False
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
    """Second part of Article Creation form"""
    subject = forms.ModelChoiceField(
        label="Opleiding",
        queryset=Subject.objects.all(),
        empty_label=None
    )
    level = forms.ChoiceField(
        label="Niveau",
        choices=models.LEVEL_CHOICES
    )
    file_type = forms.ChoiceField(
        label="Soort document",
        choices=models.FILE_TYPE_CHOICES
    )
    is_public = forms.ChoiceField(
        widget=forms.RadioSelect,
        label="",
        choices=models.PUBLIC_SETTING_CHOICES,
        initial=1
    )

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
    """Article edit form"""
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
