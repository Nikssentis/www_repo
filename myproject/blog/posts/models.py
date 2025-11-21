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
    title = models.CharField(max_length=150)
    text = models.TextField()
    topic = models.ForeignKey('posts.Topic', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created_at"]  # od najnowszych

    def __str__(self):
        words = self.text.split()
        head = " ".join(words[:5])
        return head + ("..." if len(words) > 5 else "")
