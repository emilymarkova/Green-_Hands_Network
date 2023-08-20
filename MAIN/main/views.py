from django.shortcuts import render, get_object_or_404
from .models import Author, Category, Post
from .utils import update_views


def main(request):
    return render(request, "main.html", {})


def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        "post": post
    }
    update_views(request, post)
    return render(request, "detail.html", context)


def mission(request):
    return render(request, "mission.html", {})


def forum(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(approved=True, categories=category)
    context = {
        "posts": posts,
    }
    return render(request, "forum.html", context)
