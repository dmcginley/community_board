from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Category name (e.g., "Technology", "Health")
    slug = models.SlugField(unique=True, blank=True)  # URL-friendly identifier
    description = models.TextField(blank=True, null=True)  # Optional description

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Post(models.Model):
    DRAFT = 'draft'
    PUBLISHED = 'published'

    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='posts')  # Added related_name
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts')
    slug = models.SlugField(max_length=250, unique=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,default=DRAFT)

    class Meta:
        verbose_name_plural = "posts"
        ordering = ['-created_at'] 

    def save(self, *args, **kwargs):
        if not self.slug:  # Create slug only if it doesn't exist
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('community_board_app:post_detail', kwargs={'slug': self.slug})
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming users are logged in
    email = models.EmailField(blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author.username}'
    
    class Meta:
        ordering = ['created_at']

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['post', 'user'], name='unique_post_like')
        ]

    def __str__(self):
        return f'{self.user.username} likes "{self.post.title}"'


class SiteDescription(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    num_posts = models.PositiveIntegerField(default=0)
    num_members = models.PositiveIntegerField(default=0)


    def save(self, *args, **kwargs):
        """Ensure only one instance exists"""
        if not SiteDescription.objects.exists():
            super().save(*args, **kwargs)
        else:
            self.pk = SiteDescription.objects.first().pk
            super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Site Description"
        verbose_name_plural = "Site Description"

    def num_posts(self):
        """Returns the number of published posts."""
        return Post.objects.filter(status=Post.PUBLISHED).count()

    def num_users(self):
        """Returns the total number of registered users."""
        return User.objects.count()