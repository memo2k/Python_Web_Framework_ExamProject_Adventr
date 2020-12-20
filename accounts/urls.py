from django.urls import path, include

from accounts.views import user_profile, signup_profile, signout_user

urlpatterns = (
    path('', include('django.contrib.auth.urls')),
    path('profile/', user_profile, name='current user profile'),
    path('profile/<int:pk>/', user_profile, name='user profile'),
    path('signup/', signup_profile, name='signup profile'),
    path('signout/', signout_user, name='signout user'),
)
