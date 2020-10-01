from django.forms import ModelForm

from articles.models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'short_desc',
            'long_desc',
            'image',
            'uploaded_file',
            'subject',
            'level',
            'is_public',
        ]
