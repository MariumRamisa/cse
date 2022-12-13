from django.shortcuts import render
from source.base import RetrieveUpdateViewSet
from source.utils import get_object_or_404

from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import Account

from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import (
    RegistrationSerializer, LoginSerializer,
    AccountSerializer, PasswordSerializer, ConfigureProfileSerializer
)
# Create your views here.


class RegistrationView(GenericAPIView):
    permission_classes = [AllowAny]

    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        account = serializer.save()
        return Response(status=status.HTTP_201_CREATED)


class LoginView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        account = serializer.validated_data
        refresh_token = get_refresh_tokens(account)
        return Response({"refresh": refresh_token['refresh'],
                         "access": refresh_token['access']},
                        status=status.HTTP_202_ACCEPTED)


class AccountViewSet(RetrieveUpdateViewSet):
    # serializer_class = AccountSerializer

    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'change_password':
            return PasswordSerializer
        elif self.action == 'configure_profile':
            return ConfigureProfileSerializer
        else:
            return AccountSerializer

    def get_queryset(self):
        return Account.objects.filter(pk=self.request.user.pk)

    def get_object(self):
        queryset = self.get_queryset()
        pk = self.request.user.pk
        obj = get_object_or_404(queryset, pk=pk)

        self.check_object_permissions(self.request, obj)
        return obj

    @action(methods=['put'], detail=True, url_path='change-password')
    def change_password(self, request, pk=None):
        serializer = self.get_serializer(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        request.user.set_password(serializer.validated_data['new_password'])
        request.user.save()
        return Response(status=status.HTTP_202_ACCEPTED)

    @parser_classes([MultiPartParser, FormParser])
    @action(methods=['put'], detail=True, url_path='configure-profile')
    def configure_profile(self, request, pk=None):
        account = self.get_object()
        if account.is_first_login is True and account.profile_type is None:
            serializer = self.get_serializer(account, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.validated_data['is_first_login'] = False
            account = serializer.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        account = self.get_object()
        serializer = self.get_serializer(
            account, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        profile_image = account.profile_image

        account = serializer.save()

        if account.profile_image is None and account.has_profile_type('Student'):
            account.profile_image = profile_image
            account.save()
        return Response(self.get_serializer(account).data,
                        status=status.HTTP_202_ACCEPTED)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


def get_refresh_tokens(account):
    refresh = RefreshToken.for_user(account)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }
