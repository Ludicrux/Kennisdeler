"""
Article admin view
"""
from django.contrib import admin
from .models import Subject, Tag, Article, Like, Favorite


admin.site.register(Subject)
admin.site.register(Tag)
admin.site.register(Article)
admin.site.register(Like)
admin.site.register(Favorite)
