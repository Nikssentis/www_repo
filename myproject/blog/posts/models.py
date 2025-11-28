from django.conf import settings
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["name"]  # sortowanie alfabetycznie

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=60)
    category = models.ForeignKey('posts.Category', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]  # sortowanie alfabetycznie

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        related_name='posts'
    )

    class Meta:
        permissions = [
            ('can_edit_others_posts', 'Can edit posts created by other users'),
        ]

    def __str__(self):
        return self.title
