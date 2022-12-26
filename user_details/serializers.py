from rest_framework import serializers
from .models import user_details


class user_detailserializer(serializers.ModelSerializer):

    # representing data from another tables
    def to_representation(self, instance):
        representation = super(user_detailserializer,
                               self).to_representation(instance)
        representation['name'] = instance.user_id.name
        representation['email'] = instance.user_id.email
        representation['password'] = instance.user_id.password

        return representation

    class Meta:
        model = user_details
        fields = ['user_id', 'height', 'weight', 'age', 'gender',
                  'location', 'goal_weight', 'activity_level', 'weekly_goal', 'bmi', 'net_goal']
