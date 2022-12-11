from rest_framework import serializers
from .models import foodCalories


class foodserializer(serializers.ModelSerializer):
    class Meta:
        model = foodCalories
        fields = ['id', 'food_name', 'quantity',
                  'quantity_gm', 'calorie']
