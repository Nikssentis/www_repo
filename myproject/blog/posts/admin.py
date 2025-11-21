from django.contrib import admin
from .models import Category, Topic, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")
    search_fields = ("name",)


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category")
    list_select_related = ("category",)
    search_fields = ("name", "category__name")
    list_filter = ("category", "category__name")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at",)
    list_display = (
        "id",
        "title",
        "topic_with_category",
        "created_by",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "topic",
        "topic__category",
        "created_by",
        "topic__name",
        "topic__category__name",
    )
    search_fields = ("title", "text", "topic__name", "topic__category__name")
    list_select_related = ("topic", "topic__category", "created_by")
    prepopulated_fields = {"slug": ("title",)}

    @admin.display(description="Temat (Kategoria)")
    def topic_with_category(self, obj: Post):
        return f"{obj.topic.name} ({obj.topic.category.name})"
