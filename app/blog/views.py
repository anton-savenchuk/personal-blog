from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Category, Post
from .utils import DataMixin


class PostListView(DataMixin, ListView):
    """Post model view."""

    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        """Return a dictionary to use as a template context."""
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(title="Все посты")

        return context | user_context

    def get_queryset(self):
        """Return the list of items for this view."""
        return Post.objects.filter(is_published=True)


class PostDetailView(DataMixin, DetailView):
    """Single post model view."""

    model = Post
    template_name = "blog/single.html"
    context_object_name = "post"
    slug_url_kwarg = "post_slug"

    def get_context_data(self, **kwargs):
        """Return a dictionary to use as a template context."""
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(title=self.object.title)

        return context | user_context


class CategoryPostListView(DataMixin, ListView):
    """Category post model view."""

    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    allow_empty = False

    def get_context_data(self, **kwargs):
        """Return a dictionary to use as a template context."""
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(
            title=f"Посты из категории: {self.category.title}",
        )

        return context | user_context

    def get_queryset(self):
        """Return the list of items for this view."""
        self.category = Category.objects.get(slug=self.kwargs["category_slug"])

        return Post.objects.all().filter(
            category__slug=self.category.slug,
            is_published=True,
        )
