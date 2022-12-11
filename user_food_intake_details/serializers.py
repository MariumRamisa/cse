from rest_framework import serializers
from .models import user_food_intake_detail


class food_intakeserializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        representation = super(food_intakeserializer,
                               self).to_representation(instance)
        representation['food_name'] = instance.food_name.food_name
        representation['quantity'] = instance.quantity
        representation['cal_cup'] = instance.food_name.calorie
        representation['total_calorie_gained'] = instance.total_cal

        return representation

    class Meta:
        model = user_food_intake_detail
        fields = ['user_id', 'meal_type', 'date']
