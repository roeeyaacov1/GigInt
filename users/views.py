from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    # specify serializer to be used
    serializer_class = UserSerializer

    @action(detail=True, methods=['get'])
    def get_user_summary(self, username):
        user = get_object_or_404(User, username=username)
        serializer = self.get_serializer(user)
        data = serializer.data

        return Response(data)
