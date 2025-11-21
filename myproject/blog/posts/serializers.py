from django.utils import timezone
from rest_framework import serializers
from .models import Category, Topic, Post

class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "description"]

class TopicModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ["id", "name", "category", "created"]

class PostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "text", "topic", "slug", "created_at", "updated_at", "created_by"]
        read_only_fields = ["updated_at"]

    def validate_title(self, value):
        import re
        if not re.match(r"^[A-Za-zÀ-ÿ\s]+$", value or ""):
            raise serializers.ValidationError("title: tylko litery i spacje")
        return value

    def validate(self, attrs):
        created_at = attrs.get("created_at")
        if created_at and created_at > timezone.now():
            raise serializers.ValidationError({"created_at": "nie może być z przyszłości"})
        return attrs
