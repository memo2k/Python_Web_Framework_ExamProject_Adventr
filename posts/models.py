from django.db import models


class Post(models.Model):
    location = models.CharField(max_length=20, blank=False)
    description = models.TextField()
    image_url = models.URLField()

    def __str__(self):
        return f'{self.id}, {self.location}, {self.description}'


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)