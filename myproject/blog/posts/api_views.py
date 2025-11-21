from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Topic, Post
from .serializers import CategoryModelSerializer, TopicModelSerializer, PostModelSerializer

@api_view(["GET", "POST"])
def category_list(request):
    if request.method == "GET":
        q = request.query_params.get("q")
        qs = Category.objects.all()
        if q:
            qs = qs.filter(name__icontains=q)
        s = CategoryModelSerializer(qs, many=True)
        return Response(s.data)
    s = CategoryModelSerializer(data=request.data)
    if s.is_valid():
        s.save()
        return Response(s.data, status=status.HTTP_201_CREATED)
    return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def category_search(request):
    q = request.query_params.get("q", "")
    qs = Category.objects.filter(name__icontains=q)
    s = CategoryModelSerializer(qs, many=True)
    return Response(s.data)

@api_view(["GET", "PUT", "DELETE"])
def category_detail(request, pk):
    try:
        obj = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        s = CategoryModelSerializer(obj)
        return Response(s.data)
    if request.method == "PUT":
        s = CategoryModelSerializer(obj, data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
    obj.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["GET", "POST"])
def topic_list(request):
    if request.method == "GET":
        q = request.query_params.get("q")
        qs = Topic.objects.all()
        if q:
            qs = qs.filter(name__icontains=q)
        s = TopicModelSerializer(qs, many=True)
        return Response(s.data)
    s = TopicModelSerializer(data=request.data)
    if s.is_valid():
        s.save()
        return Response(s.data, status=status.HTTP_201_CREATED)
    return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def topic_search(request):
    q = request.query_params.get("q", "")
    qs = Topic.objects.filter(name__icontains=q)
    s = TopicModelSerializer(qs, many=True)
    return Response(s.data)

@api_view(["GET", "PUT", "DELETE"])
def topic_detail(request, pk):
    try:
        obj = Topic.objects.get(pk=pk)
    except Topic.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        s = TopicModelSerializer(obj)
        return Response(s.data)
    if request.method == "PUT":
        s = TopicModelSerializer(obj, data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
    obj.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["GET", "POST"])
def post_list(request):
    if request.method == "GET":
        q = request.query_params.get("q")
        qs = Post.objects.all()
        if q:
            qs = qs.filter(title__icontains=q)
        s = PostModelSerializer(qs, many=True)
        return Response(s.data)
    s = PostModelSerializer(data=request.data)
    if s.is_valid():
        s.save()
        return Response(s.data, status=status.HTTP_201_CREATED)
    return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def post_detail(request, pk):
    try:
        obj = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        s = PostModelSerializer(obj)
        return Response(s.data)
    if request.method == "PUT":
        s = PostModelSerializer(obj, data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
    obj.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
