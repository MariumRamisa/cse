from rest_framework import serializers
from .models import diet_plan


class diet_plan_serializer(serializers.ModelSerializer):
    class Meta:
        model = diet_plan
        fields = ['id', 'goal_weight', 'diet_plan']
