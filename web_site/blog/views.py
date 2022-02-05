from blog.forms import CommentForm, PostForm
from blog.models import Comment, Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)


class AboutView(TemplateView):
    template_name = 'about.html'


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        """
        Perform SQL query on the model.

        Grab Post model and filter out all this conditions.
        published_date__lte = published_date field is less than of equal to
        current time and order by -published_date ('-' is desc order).
        https://docs.djangoproject.com/en/4.0/topics/db/queries/

        SELECT * FROM post
        WHERE published_date <= timezone.now() ORDER BY published_date DESC
        """
        return Post.objects.filter(published_date__lte=timezone.now()).order_by(
            '-published_date'
        )


class PostDetailView(DetailView):
    """When I have a list of post I click on one that takes to the blog post."""

    model = Post


class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    # where it actually goes when it is deleted.
    success_url = reverse_lazy('post_list')


class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by(
            'created_date'
        )
