from posts.models import Category, Topic, Post



Category.objects.all()

Category.objects.get(id=3)

Category.objects.filter(name\_\_istartswith='A')

Topic.objects.values\_list('category\_\_name', flat=True).distinct()

Post.objects.order\_by('-title').values\_list('title', flat=True)

Category.objects.create(name='Nowa kategoria', description='Opis testowy')



