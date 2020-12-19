from django.urls import path

from posts.views import feed, post_likes, post_comments, post_delete, post_edit, add_photo

urlpatterns = [
    path('', feed, name='feed'),
    path('likes/<int:pk>/', post_likes, name='post like'),
    path('comments/<int:pk>/', post_comments, name='post comments'),
    path('edit/<int:pk>/', post_edit, name='post edit'),
    path('delete/<int:pk>/', post_delete, name='post delete'),
    path('add/', add_photo, name='add photo'),
]
