from django.shortcuts import render
from .models import nutrient_list
from .serializers import nutritionserializer
from rest_framework import generics, mixins

# Create your views here.


class nutrition_list(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class = nutritionserializer
    queryset = nutrient_list.objects.all()
    lookup_field = 'food_name'

# view data

    def get(self, request, food_name=None):

        if food_name:
            return self.retrieve(request)
        else:
            return self.list(request)

# add date

    def post(self, request):
        return self.create(request)

# update data

    def put(self, request, food_name=None):
        return self.update(request, food_name)

# delete data

    def delete(self, request, food_name):
        return self.destroy(request, food_name)
