from rest_framework import serializers
from .models import Post, Comment
from . import services as likes_services

from django.contrib.auth.models import User


class FanSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "username",
            "full_name",
        )

    def get_full_name(self, obj):
        return obj.get_full_name()


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Comment


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    link = serializers.SerializerMethodField()

    def get_link(self, obj):
        return obj.get_absolute_url()

    class Meta:
        fields = (
            "id",
            "body",
            "title",
            "created_at",
            "total_likes",
            "comments",
            "link",
            "author"
        )
        model = Post

    def get_is_fan(self, obj) -> bool:
        """Проверяет, лайкнул ли `request.user` твит (`obj`).
        """
        user = self.context.get("request").user
        return likes_services.is_fan(obj, user)
