from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length=60)

    category = models.ForeignKey('posts.Category', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
