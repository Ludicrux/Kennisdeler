"""
Views for Core
"""
from django.views import generic
from django.shortcuts import render, redirect
from django.db.models import Count

from articles.models import Article, Subject
from users.forms import CustomUserCreationForm
from users.models import User, Profile

from django.contrib.auth import authenticate, login


class HomePageView(generic.View):
    """List all subjects and most popular items"""
    template_name = "core/homepage.html"

    def get(self, request, *args, **kwargs):
        """Return all subjects and most popular items"""
        subject = Subject.objects.all()
        article = Article.objects.annotate(
            num_likes=Count("user_likes")
        ).order_by("-num_likes")[:3]

        context = {
            "subject_list": subject,
            "article_list": article
        }

        return render(request, self.template_name, context)


class CreateUserView(generic.View):
    """Create new user"""
    template_name = "registration/register.html"

    def get(self, request, *args, **kwargs):
        form = CustomUserCreationForm()
        context = {"form": form}

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST, request.FILES)

        if form.is_valid():
            user = User.objects.create_user(
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password1"]
            )
            profile = Profile(
                user=user,
                job=form.cleaned_data["job"],
                organization=form.cleaned_data["organization"],
                profile_picture=form.cleaned_data["profile_picture"],
            )
            profile.save()
            user = authenticate(
                request,
                username=user.email,
                password=user.password
            )
            if user is not None:
                login(request, user)

            return redirect("core:homepage")

        context = {"form": form}

        return render(request, self.template_name, context)
