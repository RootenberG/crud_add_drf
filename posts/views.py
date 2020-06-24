from rest_framework import viewsets


from .mixins import LikedMixin

from .models import Post, Comment
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class PostViewSet(LikedMixin, viewsets.ModelViewSet):
    # permission_classes = (IsAuthorOrReadOnly,)
    permission_classes = (IsAuthenticatedOrReadOnly, )

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

