from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    CategoryListView,
    CategoryDetailView,
    SignUpView,
    PostCreateView,
    PostUpdateView,
)


app_name = "blog"

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    # Place the specific route before the slug route to avoid capture
    path("post/new/", PostCreateView.as_view(), name="post_create"),
    path("post/<slug:slug>/edit/", PostUpdateView.as_view(), name="post_edit"),
    path("post/<slug:slug>/", PostDetailView.as_view(), name="post_detail"),
    path("categories/", CategoryListView.as_view(), name="categories"),
    path("category/<slug:slug>/", CategoryDetailView.as_view(), name="category_detail"),
    path("accounts/signup/", SignUpView.as_view(), name="signup"),
]
