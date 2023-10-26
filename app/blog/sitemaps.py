from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Post


class PostSitemap(Sitemap):
    """Sitemap for posts."""

    changefreq = "monthly"
    priority = 0.9
    protocol = "https"

    def items(self):
        """Define a list of posts."""
        return Post.objects.all()

    def lastmod(self, obj):
        """Define the time of the last update of the post."""
        return obj.time_update


class StaticSitemap(Sitemap):
    """Sitemap for static pages."""

    def items(self):
        """Define a list of static pages."""
        return ["home"]

    def location(self, item):
        """Define a URL for a static page."""
        return reverse(item)
