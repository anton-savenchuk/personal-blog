from core.settings import PAGINATION_RANGE

menu = [
    {"title": "/Все посты", "url_name": "home"},
    {"title": "/Обо мне", "url_name": "about"},
]


class DataMixin:
    """A mixin that can be used as a template context."""

    paginate_by = PAGINATION_RANGE

    def get_user_context(self, **kwargs):
        """Return a dictionary to use as a template context."""
        context = kwargs
        context["menu"] = menu

        return context
