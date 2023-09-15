from django.urls import path

from . import views

urlpatterns = [
    path("", views.PostListView.as_view(), name="home"),
    path(
        route="post/<slug:post_slug>/",
        view=views.PostDetailView.as_view(),
        name="post",
    ),
]
