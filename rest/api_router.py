# -*- coding: utf-8 -*-
from rest_framework.routers import DefaultRouter

from rest.views import PostViewSet

router = DefaultRouter()

router.register(r'post', PostViewSet)
