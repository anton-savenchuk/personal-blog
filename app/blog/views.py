from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Category, Post

PAGINATION_RANGE = 3

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
    paginate_by = PAGINATION_RANGE

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


class CategoryPostListView(ListView):
    """Category post model view."""

    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    allow_empty = False
    paginate_by = PAGINATION_RANGE

    def get_context_data(self, **kwargs):
        """Return a dictionary to use as a template context."""
        context = super().get_context_data(**kwargs)
        context["title"] = f"Посты из категории: {self.category.title}"
        context["menu"] = menu

        return context

    def get_queryset(self):
        """Return the list of items for this view."""
        self.category = Category.objects.get(slug=self.kwargs["category_slug"])

        return Post.objects.all().filter(
            category__slug=self.category.slug,
            is_published=True,
        )
