from posts.models import Category, Topic, Post

from posts.serializers import TopicBasicSerializer, CategoryModelSerializer, TopicModelSerializer, PostModelSerializer

from django.contrib.auth import get\_user\_model

from rest\_framework.renderers import JSONRenderer



User = get\_user\_model()



cat = Category.objects.create(name="Filmy", description="Opis")

top = Topic.objects.create(name="Batman", category=cat)

usr = User.objects.first() or User.objects.create\_user(username="tester", password="x")



s1 = TopicBasicSerializer(top)

JSONRenderer().render(s1.data)



s2 = CategoryModelSerializer(cat)

JSONRenderer().render(s2.data)



s3 = TopicModelSerializer(top)

JSONRenderer().render(s3.data)



p = Post.objects.create(title="Pierwszy post", text="To jest testowy post do DRF", topic=top, slug="pierwszy-post", created\_by=usr)

s4 = PostModelSerializer(p)

JSONRenderer().render(s4.data)



payload = {"name": "Superman", "category": cat.pk}

s5 = TopicBasicSerializer(data=payload)

s5.is\_valid()

s5.save()



q = {"title": "Nowy post", "text": "Treść", "topic": top.pk, "slug": "nowy-post", "created\_by": usr.pk}

s6 = PostModelSerializer(data=q)

s6.is\_valid()

obj = s6.save()

JSONRenderer().render(PostModelSerializer(obj).data)



