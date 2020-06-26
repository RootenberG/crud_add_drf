import schedule
import time
import threading

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType


class Like(models.Model):
    user = models.ForeignKey(User,
                             related_name="likes", on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = GenericRelation(Like)

    title = models.CharField(max_length=50)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return f"{settings.DOMAIN_NAME}api/v1/posts/{self.id}"

    def __str__(self):
        return self.title

    @property
    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post,
                             related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}-{}".format(self.post.title, str(self.author.username))


def reset_upvotes():
    t = threading.Thread(target=cleaner)
    t.setDaemon(True)
    t.start()
    return True


def del_all():
    queryset = Like.objects.all()
    for i in queryset:
        i.delete()


def cleaner():
    schedule.every(10).seconds.do(del_all)
    while True:
        schedule.run_pending()
        time.sleep(1)


# reset_upvotes()
