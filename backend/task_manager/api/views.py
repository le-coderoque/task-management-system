from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.db.models import F
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Advert, Task
from .serializers import (AdvertSerializer, TaskDetailSerializer, 
                          TaskListSerializer)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get_serializer_class(self):
        if self.action == 'list':
            return TaskListSerializer
        return TaskDetailSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User(username=username)

        if User.objects.filter(username=username).exists():
            return Response({'detail': 'A user with this username already exists.'},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            user.set_password(password)
            user.save()
        except IntegrityError:
            return Response({'detail': 'Registration failed. Username might already be taken.'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is None:
            return Response({'error': 'Invalid username or password'},
                            status=status.HTTP_400_BAD_REQUEST)

        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key},
                        status=status.HTTP_200_OK)


class LogoutView(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        token_header = request.headers.get('Authorization')
        if not token_header or 'Token' not in token_header:
            return Response({'detail': 'Authentication credentials were not provided.'},
                            status=status.HTTP_400_BAD_REQUEST)

        token_string = token_header.split('Token ')[1]
        token = Token.objects.filter(key=token_string).first()
        if token:
            token.delete()
            return Response({'detail': 'Successfully logged out.'},
                            status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid token.'},
                            status=status.HTTP_400_BAD_REQUEST)


class AdvertViewSet(viewsets.ModelViewSet):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer
    permission_classes = [AllowAny]

    def retrieve(self, request, *args, **kwargs):
        advert = self.get_object()
        Advert.objects.filter(pk=advert.pk).update(views=F('views') + 1)
        advert.refresh_from_db()
        serializer = self.get_serializer(advert)
        return Response(serializer.data)
