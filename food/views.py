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
    lookup_field = ['id', 'calorie']

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
            data = serializer.data
            return Response(data=data, status=status.HTTP_201_CREATED)
        else:
            response = {
                "msg": "calorie can never be negative "
            }
            return Response(data=response, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)
