from django.shortcuts import render
from .models import user
from django.contrib import messages
from .serializers import userserializer, LoginSerializer
from rest_framework import generics, mixins, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class user(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
           mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class = userserializer
    queryset = user.objects.all()
    lookup_field = 'name'
    permission_classes = [IsAuthenticated]

#  def get(self, request, name=None):
    # def get(self, request):

#        if name:
    # if name:

#            return self.retrieve(request)
    # else:
    #    response = {
    #       "message": "User Not found",
    #  }
    # return Response(data=response, status=status.HTTP_404_NOT_FOUND)
 #       else:
 #           return self.list(request)
# view user

    def get(self, request, name=None):

        if name:
            if name:
                return self.retrieve(request)
        else:
            return self.list(request)
# add user

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

# update user

    def put(self, request, name=None):
        return self.update(request, name)

# delete user

    def delete(self, request, name):
        return self.destroy(request, name)

# user login


class LoginView(generics.GenericAPIView):

    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'user': serializer.data,
            "message": "User found",
        }

        return Response(data=response,
                        status=status.HTTP_202_ACCEPTED)
