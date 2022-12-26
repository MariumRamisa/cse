from django.shortcuts import render

from .models import user_calorie_detail
from .serializers import usercalorieserializer
from rest_framework import generics, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class user_calorie_list(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin):

    serializer_class = usercalorieserializer
    queryset = user_calorie_detail.objects.all()
    lookup_field = 'user_id'

# view data

    def get(self, request, user_id=None):

        if user_id:
            return self.retrieve(request)

        else:
            return self.list(request)

# add data

    def post(self, request):
        return self.create(request)

# update data

    def put(self, request, user_id=None):
        return self.update(request, user_id)

# delete data

    def delete(self, request, user_id):
        return self.destroy(request, user_id)
