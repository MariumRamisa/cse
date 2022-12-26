
from django.shortcuts import render
from .models import burned_cal_detail
from .serializers import burned_calserializer
from rest_framework import generics, mixins, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class burned_cal(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class = burned_calserializer
    queryset = burned_cal_detail.objects.all()
    lookup_field = 'user_id'

# view data
    def get(self, request, user_id=None):

        if user_id:
            return self.retrieve(request)

        else:
            return self.list(request)
# add data

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            return Response(data=data, status=status.HTTP_201_CREATED)
        else:
            response = {
                "msg": "invalid data"
            }
            return Response(data=response, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
# update data

    def put(self, request, user_id=None):
        data = request.data
        val = burned_cal_detail.objects.get(user_id=user_id)
        serializer = self.serializer_class(val, data=data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            return Response(data=data, status=status.HTTP_202_ACCEPTED)
        else:
            response = {
                "msg": "invalid data"
            }
            return Response(data=response, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
# delete data

    def delete(self, request, user_id):
        return self.destroy(request, user_id)
