from django.shortcuts import render
from .models import burned_cal_detail
from .serializers import burned_calserializer
from rest_framework import generics, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class burned_cal(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class = burned_calserializer
    queryset = burned_cal_detail.objects.all()
    lookup_field = 'user_id'

    def get(self, request, user_id=None):

        if user_id:
            return self.retrieve(request)

        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, user_id=None):
        return self.update(request, user_id)

    def delete(self, request, user_id):
        return self.destroy(request, user_id)
