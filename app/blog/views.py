from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Post

menu = [
    {"title": "/Все посты", "url_name": "home"},
    {"title": "/О сайте", "url_name": "home"},
    {"title": "/Обратная связь", "url_name": "home"},
]


class PostListView(ListView):
    """Post model view."""

    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        """Return a dictionary to use as a template context."""
        context = super().get_context_data(**kwargs)
        context["title"] = "Все посты"
        context["menu"] = menu

        return context

    def get_queryset(self):
        """Return the list of items for this view."""
        return Post.objects.filter(is_published=True)


class PostDetailView(DetailView):
    """Single post model view."""

    model = Post
    template_name = "blog/single.html"
    context_object_name = "post"
    slug_url_kwarg = "post_slug"

    def get_context_data(self, **kwargs):
        """Return a dictionary to use as a template context."""
        context = super().get_context_data(**kwargs)
        context["title"] = self.object.title
        context["menu"] = menu

        return context
