# coding: utf-8
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from blog.models import Post
from rest.serializers import PostSerializer


class PostViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    queryset = Post.objects.all()
    serializer_class = PostSerializer