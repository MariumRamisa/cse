from django.shortcuts import render
from .models import user
from django.contrib import messages
from .serializers import userserializer
from rest_framework import generics, mixins, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class user(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin,
           mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class = userserializer
    queryset = user.objects.all()
    lookup_field = ['id', 'name']

    def get(self, request, name=None):

        if name:
            if name:
                response = {
                    "message": "User found",
                }
                return Response(data=response, status=status.HTTP_302_FOUND)
            else:
                response = {
                    "message": "User Not found",
                }
                return Response(data=response, status=status.HTTP_404_NOT_FOUND)
        else:
            return self.list(request)

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if (serializer.is_valid()):
            serializer.save()
            response = {
                "message": "User Created Successfully",
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        response = {
            "message": "User exists",
        }
        return Response(data=response, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, name=None):
        return self.update(request, name)

    def delete(self, request, name):
        return self.destroy(request, name)
