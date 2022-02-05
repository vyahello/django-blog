from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    """User post model (post table)."""

    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)

    def published(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approve_comments=True)

    def get_absolute_url(self):
        """
        Go to that post of details page with a primary key of the post
        you've just created.
        """
        return reverse('post_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    """User comment model (comment table) connects to the user post model."""

    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        """After adding comment return to a list of comments."""
        return reverse('post_list')

    def __str__(self):
        return self.text
