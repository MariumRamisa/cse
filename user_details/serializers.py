from rest_framework import serializers
from .models import user_details


class user_detailserializer(serializers.ModelSerializer):
    class Meta:
        model = user_details
        fields = ['user_id', 'height', 'weight', 'age', 'gender',
                  'location', 'goal_weight', 'activity_level', 'weekly_goal', 'bmi', 'net_goal']
