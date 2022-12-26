from rest_framework import serializers
from .models import user_calorie_detail


class usercalorieserializer(serializers.ModelSerializer):

    # representing data from another tables

    def to_representation(self, instance):
        representation = super(usercalorieserializer,
                               self).to_representation(instance)
        representation['calorie_intake'] = instance.calorie_intake.total_cal
        representation['burned_calorie'] = instance.burned_calorie.burned_cal
        representation['goal_calorie'] = instance.goal_calorie.net_goal
        representation['remain_cal'] = representation['goal_calorie'] - \
            representation['calorie_intake']+representation['burned_calorie']
        return representation

    class Meta:
        model = user_calorie_detail
        fields = ['user_id']
