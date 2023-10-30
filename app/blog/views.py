import requests
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Category, Post, Tag
from .utils import DataMixin, menu


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
        return (
            Post.objects.filter(is_published=True)
            .select_related("category")
            .prefetch_related("tag")
        )


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

        return (
            Post.objects.all()
            .filter(
                category__slug=self.category.slug,
                is_published=True,
            )
            .select_related("category")
            .prefetch_related("tag")
        )


class TagPostListView(DataMixin, ListView):
    """Tag post model view."""

    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    allow_empty = False

    def get_context_data(self, **kwargs):
        """Return a dictionary to use as a template context."""
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(
            title=f"Посты по тегу: {self.tag.title}",
        )

        return context | user_context

    def get_queryset(self):
        """Return the list of items for this view."""
        self.tag = Tag.objects.get(slug=self.kwargs["tag_slug"])
        return (
            Post.objects.all()
            .filter(
                tag__slug=self.tag.slug,
                is_published=True,
            )
            .select_related("category")
            .prefetch_related("tag")
        )


def get_about_page(request):
    """About page."""
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    }
    url = "https://raw.githubusercontent.com/anton-savenchuk/anton-savenchuk/main/README.md"
    description = requests.get(url, headers=headers, timeout=6).text

    return render(
        request=request,
        template_name="blog/static.html",
        context={
            "title": "Обо мне",
            "menu": menu,
            "description": description,
        },
    )


def badRequest(request, exception):
    """Handle 400 error."""
    return render(
        request=request,
        template_name="blog/errors/error_page.html",
        status=400,
        context={
            "title": "Bad request: 400",
            "menu": menu,
            "error_message": "Неправильный запрос.",
        },
    )


def pageForbidden(request, exception):
    """Handle 403 error."""
    return render(
        request=request,
        template_name="blog/errors/error_page.html",
        status=403,
        context={
            "title": "Page forbidden: 403",
            "menu": menu,
            "error_message": "Доступ к этой странице ограничен.",
        },
    )


def pageNotFound(request, exception):
    """Handle 404 error."""
    return render(
        request=request,
        template_name="blog/errors/error_page.html",
        status=404,
        context={
            "title": "Page not found: 404",
            "menu": menu,
            "error_message": "К сожалению такая страница не найдена, или перемещена.",
        },
    )


def internalServerError(request):
    """Handle 500 error."""
    return render(
        request=request,
        template_name="blog/errors/error_page.html",
        status=500,
        context={
            "title": "Internal Server Error: 500",
            "menu": menu,
            "error_message": "Внутренняя ошибка сайта, вернитесь на главную страницу, отчёт об ошибке направлен администрации сайта.",
        },
    )
