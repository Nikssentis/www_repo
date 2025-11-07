from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Category, Topic, Post

User = get_user_model()

class TopicBasicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=60)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    def create(self, validated_data):
        return Topic.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.category = validated_data.get("category", instance.category)
        instance.save()
        return instance

class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "description"]
        read_only_fields = ["id"]

class TopicModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ["id", "name", "category", "created"]
        read_only_fields = ["id", "created"]

class PostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id","title","text","topic","slug","created_at","updated_at","created_by"]
        read_only_fields = ["id","created_at","updated_at"]
