from django.shortcuts import render
from .models import exercisecal
from .serializers import exerciseserializer
from rest_framework import generics, mixins, status
from rest_framework.response import Response

# Create your views here.


class exercise_detail_list(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                           mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class = exerciseserializer
    queryset = exercisecal.objects.all()
    lookup_field = 'exercise_name'

    def get(self, request, exercise_name=None):

        if exercise_name:
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
                "msg": "invalid data"
            }
            return Response(data=response, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

    def put(self, request, exercise_name=None):
        return self.update(request, exercise_name)

    def delete(self, request, exercise_name):
        return self.destroy(request, exercise_name)
