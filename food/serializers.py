from rest_framework import serializers
from .models import foodCalories


class foodserializer(serializers.ModelSerializer):
    class Meta:
        model = foodCalories
        fields = ['id', 'food_name', 'quantity',
                  'quantity_gm', 'calorie']

# Validation of data

    def validate(self, data):
        data = super(foodserializer, self).validate(data)

        if (data.get('calorie') < 0):
            raise serializers.ValidationError("calorie cannot be negative")
        elif (data.get('quantity') < 0):
            raise serializers.ValidationError("quantity cannot be negative")
        elif (data.get('quantity_gm') < 0):
            raise serializers.ValidationError("quantity cannot be negative")
        elif (data.get('food_name').exists()):
            raise serializers.ValidationError("change food name")
        else:
            return data
