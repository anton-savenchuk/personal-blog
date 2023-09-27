from django.urls import path

from . import views

urlpatterns = [
    path("", views.PostListView.as_view(), name="home"),
    path(
        route="post/<slug:post_slug>/",
        view=views.PostDetailView.as_view(),
        name="post",
    ),
    path(
        route="category/<slug:category_slug>/",
        view=views.CategoryPostListView.as_view(),
        name="category",
    ),
    path(
        route="tag/<slug:tag_slug>/",
        view=views.TagPostListView.as_view(),
        name="tag",
    ),
]
