from django.urls import path

from posts.views import feed, post_details, post_likes

urlpatterns = [
    path('', feed, name='feed'),
    path('details/<int:pk>/', post_details, name='post details'),
    path('likes/<int:pk>/', post_likes, name='post like'),
]
