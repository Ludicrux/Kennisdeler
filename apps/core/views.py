"""
Views for Core
"""
from django.views import generic
from django.shortcuts import render

from articles.models import Subject


class HomePageView(generic.View):
    """List all subjects and most popular items"""
    model = Subject
    template_name = "core/homepage.html"

    def get(self, request, *args, **kwargs):
        """Return all subjects and most popular items"""
        subject = Subject.objects.all()
        context = {
            "subject_list": subject
        }

        return render(request, self.template_name, context)
