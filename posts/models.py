from django.db import models

from accounts.models import UserProfile


class Post(models.Model):
    location = models.CharField(max_length=20, blank=False)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='posts',
    )

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}, {self.location}, {self.description}'


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField(blank=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
