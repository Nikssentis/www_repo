import graphene
from graphene_django import DjangoObjectType
from posts.models import Category, Topic, Post


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = "__all__"


class TopicType(DjangoObjectType):
    class Meta:
        model = Topic
        fields = "__all__"


class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = "__all__"


class Query(graphene.ObjectType):
    all_categories = graphene.List(CategoryType)
    all_topics = graphene.List(TopicType)
    all_posts = graphene.List(PostType)
    post_by_id = graphene.Field(PostType, id=graphene.Int(required=True))
    posts_by_title = graphene.List(PostType, substr=graphene.String(required=True))
    posts_by_text = graphene.List(PostType, substr=graphene.String(required=True))
    post_count_by_user = graphene.Int(user_id=graphene.Int(required=True))
    posts_by_topic = graphene.List(PostType, topic_id=graphene.Int(required=True))
    posts_by_user = graphene.List(PostType, user_id=graphene.Int(required=True))

    def resolve_all_categories(root, info):
        return Category.objects.all()

    def resolve_all_topics(root, info):
        return Topic.objects.all()

    def resolve_all_posts(root, info):
        return Post.objects.all()

    def resolve_post_by_id(root, info, id):
        try:
            return Post.objects.get(pk=id)
        except Post.DoesNotExist:
            raise Exception("Post not found")

    def resolve_posts_by_title(root, info, substr):
        return Post.objects.filter(title__icontains=substr)

    def resolve_posts_by_text(root, info, substr):
        return Post.objects.filter(text__icontains=substr)

    def resolve_post_count_by_user(root, info, user_id):
        return Post.objects.filter(created_by_id=user_id).count()

    def resolve_posts_by_topic(root, info, topic_id):
        return Post.objects.filter(topic_id=topic_id)

    def resolve_posts_by_user(root, info, user_id):
        return Post.objects.filter(created_by_id=user_id)

class CreatePost(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        text = graphene.String(required=True)
        topic_id = graphene.Int(required=True)
        slug = graphene.String(required=True)
        user_id = graphene.Int(required=True)

    post = graphene.Field(PostType)

    def mutate(root, info, title, text, topic_id, slug, user_id):
        post = Post.objects.create(
            title=title,
            text=text,
            topic_id=topic_id,
            slug=slug,
            created_by_id=user_id
        )
        return CreatePost(post=post)


class UpdatePost(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        title = graphene.String()
        text = graphene.String()

    post = graphene.Field(PostType)

    def mutate(root, info, id, title=None, text=None):
        post = Post.objects.get(id=id)
        if title:
            post.title = title
        if text:
            post.text = text
        post.save()
        return UpdatePost(post=post)


class DeletePost(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    ok = graphene.Boolean()

    def mutate(root, info, id):
        Post.objects.filter(id=id).delete()
        return DeletePost(ok=True)


class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()
    update_post = UpdatePost.Field()
    delete_post = DeletePost.Field()

schema = graphene.Schema(query=Query)
schema = graphene.Schema(query=Query, mutation=Mutation)

