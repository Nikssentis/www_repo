from django.urls import path
from . import api_views

urlpatterns = [
    path("categories/", api_views.category_list),
    path("categories/search/", api_views.category_search),
    path("categories/<int:pk>/", api_views.category_detail),

    path("topics/", api_views.topic_list),
    path("topics/search/", api_views.topic_search),
    path("topics/<int:pk>/", api_views.topic_detail),

    path("posts/", api_views.post_list),
    path("posts/<int:pk>/", api_views.post_detail),

    path('posts-secure/', api_views.PostSecureList.as_view()),
    path('posts-secure/<int:pk>/', api_views.PostSecureDetail.as_view()),
    path('posts-secure/<int:pk>/', api_views.PostSecureDetail.as_view(), name='post-secure-detail'),
]
