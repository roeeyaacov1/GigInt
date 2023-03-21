from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'', ReviewsViewSet)
router.register(r'comment', CommentsViewSet)
router.register(r'like', LikesViewSet)


urlpatterns = [
    path('', include(router.urls)),
]