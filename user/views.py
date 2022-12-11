from django.shortcuts import render
from .models import user
from .serializers import userserializer
from rest_framework import generics, mixins, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class user_list(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class = userserializer
    queryset = user.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):

        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "User Created Successfully",
                "data": serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)
