from django.urls import path
from . import api_views

urlpatterns = [
    path('categories/', api_views.category_list),
    path('categories/<int:pk>/', api_views.category_detail),
    path('categories/search/', api_views.category_search),
    path('topics/', api_views.topic_list),
    path('topics/<int:pk>/', api_views.topic_detail),
    path('topics/search/', api_views.topic_search),
    path('posts/', api_views.PostList.as_view()),
    path('posts/<int:pk>/', api_views.PostDetail.as_view()),
]
