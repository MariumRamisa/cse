from django.shortcuts import render
from .models import foodCalories
from .serializers import foodserializer
from rest_framework import generics, mixins, status
from rest_framework.response import Response
# Create your views here.


class food_detail_list(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class = foodserializer
    queryset = foodCalories.objects.all()
    lookup_field = 'food_name'

# view data
    def get(self, request, food_name=None):

        if food_name:
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

    def put(self, request, food_name=None):
        data = request.data
        val = foodCalories.objects.get(food_name=food_name)
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

    def delete(self, request, food_name=None):
        return self.destroy(request, food_name)
