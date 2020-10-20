
"""
Forms for articles
"""
from django import forms 
# from django.forms import ClearableFileInput
from articles.models import Article


class ArticleFormPage1(forms.ModelForm):
    your_name = forms.CharField(label='Your name', max_length=100)

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
