from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.slug} - {self.updated}'

    def get_absolute_url(self):
        return reverse('post_detail', args=(self.id, self.slug))

    def liks_count(self):
        return self.plikepost.count()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ucomment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='pcomment')
    replay = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name='rcomment', blank=True, null=True)
    is_replay = models.BooleanField(default=False)
    body = models.TextField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.body [:30]}'


class LikePost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ulikepost')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='plikepost')

    def __str__(self):
        return f'{self.user} liked {self.post.slug}'


