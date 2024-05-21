from django.contrib.auth.models import Group, User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from usuario.serializer import UserSerializer, UserRegistrationSerializer, ChangePasswordSerializer
from usuario.models import CustomUser

class MyProfileView(RetrieveAPIView):
    """
    Return data from the current logged user
    """

    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        instance = self.request.user
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
class ChangeMyPasswordUpdateView(UpdateAPIView):
    """
    Change the password of current logged user
    """

    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

    def update(self, request, *args, **kwargs):
        instance_logged = self.request.user
        serializer = self.get_serializer(instance_logged, data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)

        user = serializer.instance
        token, created = Token.objects.get_or_create(user=user)
        data = serializer.data
        data["token"] = token.key

        return Response(data, status=status.HTTP_200_OK)


class UserRegistrationAPIView(CreateAPIView):
    """
    Register a new user in database
    """

    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        user = serializer.instance
        token, created = Token.objects.get_or_create(user=user)
        data = serializer.data
        data["token"] = token.key

        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)