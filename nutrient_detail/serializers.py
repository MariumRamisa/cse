from rest_framework import serializers
from .models import nutrient_list
from food.serializers import foodserializer


class nutritionserializer(serializers.ModelSerializer):
    class Meta:
        model = nutrient_list
        fields = ['food_name', 'quantity', 'protien', 'carbohydrate',
                  'fiber', 'sugar', 'saturated_fat', 'polyunsaturated_fat', 'monounsaturated_fat',
                  'trans_fat', 'cholestrol', 'sodium', 'potassium', 'calcium', 'vitaminA', 'vitaminC', 'iron']

    def to_representation(self, instance):
        representation = super(foodserializer,
                               self).to_representation(instance)
        representation['food_id'] = instance.food_name.id

        return representation
