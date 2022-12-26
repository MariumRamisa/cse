from rest_framework import serializers
from .models import exercisecal


class exerciseserializer(serializers.ModelSerializer):
    class Meta:
        model = exercisecal
        fields = ['id', 'exercise_name', 'quantity', 'calorie']

# checking data validation

    def validate(self, data):
        data = super(exerciseserializer, self).validate(data)

        if (data.get('quantity') < 0):
            raise serializers.ValidationError("quantity cannot be negative")

        else:
            return data
