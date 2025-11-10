from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.db.models import Count, Q
from .models import Post, Category
from .forms import CommentForm, SignUpForm, PostForm
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class PostListView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
    paginate_by = 10

    def get_queryset(self):
        return (
            Post.objects.filter(status=Post.Status.PUBLISHED)
            .exclude(published_at__isnull=True)
            .order_by("-published_at")
        )

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["categories"] = (
            Category.objects.annotate(
                posts_count=Count(
                    "posts",
                    filter=Q(posts__status=Post.Status.PUBLISHED) & Q(posts__published_at__isnull=False),
                )
            )
            .filter(posts_count__gt=0)
            .order_by("name")
        )
        return ctx


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["comments"] = self.object.comments.filter(is_approved=True).select_related("user")
        ctx["comment_form"] = CommentForm()
        return ctx

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.user = request.user
            comment.save()
            messages.success(request, "Comment posted.")
            return redirect("blog:post_detail", slug=self.object.slug)
        ctx = self.get_context_data()
        ctx["comment_form"] = form
        return self.render_to_response(ctx)


class CategoryListView(ListView):
    model = Category
    template_name = "blog/categories.html"
    context_object_name = "categories"

    def get_queryset(self):
        return Category.objects.annotate(
            posts_count=Count(
                "posts",
                filter=Q(posts__status=Post.Status.PUBLISHED) & Q(posts__published_at__isnull=False),
            )
        ).order_by("name")


class CategoryDetailView(ListView):
    template_name = "blog/category_detail.html"
    context_object_name = "posts"
    paginate_by = 10

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs.get("slug"))
        return (
            Post.objects.filter(
                categories=self.category,
                status=Post.Status.PUBLISHED,
            )
            .exclude(published_at__isnull=True)
            .order_by("-published_at")
        )

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["category"] = self.category
        return ctx


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "registration/signup.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, "Welcome! Your account has been created.")
        return redirect("blog:index")


class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def test_func(self):
        return self.request.user.is_staff

    def form_valid(self, form):
        messages.success(self.request, "Post created successfully.")
        response = super().form_valid(form)
        return response

    def get_success_url(self):
        return reverse("blog:post_detail", kwargs={"slug": self.object.slug})
