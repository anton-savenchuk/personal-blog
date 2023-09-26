from core.settings import PAGINATION_RANGE

menu = [
    {"title": "/Все посты", "url_name": "home"},
    {"title": "/О сайте", "url_name": "home"},
    {"title": "/Обратная связь", "url_name": "home"},
]


class DataMixin:
    """A mixin that can be used as a template context."""

    paginate_by = PAGINATION_RANGE

    def get_user_context(self, **kwargs):
        """Return a dictionary to use as a template context."""
        context = kwargs
        context["menu"] = menu

        return context
