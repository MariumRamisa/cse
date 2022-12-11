from django.shortcuts import render
from .models import exercisecal
from .serializers import exerciseserializer
from rest_framework import generics, mixins

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
        return self.create(request)

    def put(self, request, exercise_name=None):
        return self.update(request, id)

    def delete(self, request, exercise_name):
        return self.destroy(request, exercise_name)
