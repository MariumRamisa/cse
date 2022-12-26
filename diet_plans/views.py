from django.shortcuts import render
from .models import diet_plan
from .serializers import diet_plan_serializer
from rest_framework import generics, mixins

# Create your views here.


class diet_list(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class = diet_plan_serializer
    queryset = diet_plan.objects.all()
    lookup_field = 'id'
# view data

    def get(self, request, id=None):

        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
# add data

    def post(self, request):
        return self.create(request)
# update data

    def put(self, request, id=None):
        return self.update(request, id)
# delete data

    def delete(self, request, id):
        return self.destroy(request, id)
