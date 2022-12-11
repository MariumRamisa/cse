from rest_framework import serializers
from .models import exercisecal


class exerciseserializer(serializers.ModelSerializer):
    class Meta:
        model = exercisecal
        fields = ['id', 'exercise_name', 'quantity', 'calorie']
