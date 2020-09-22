"""Core Views"""
from django.views.generic import ListView
from articles.models import Subject


class HomePageListView(ListView):
    model = Subject
