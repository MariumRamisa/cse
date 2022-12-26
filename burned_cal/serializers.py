
from rest_framework import serializers
from .models import burned_cal_detail


class burned_calserializer(serializers.ModelSerializer):

    # representing values of the fields taken from another class
    def to_representation(self, instance):
        representation = super(burned_calserializer,
                               self).to_representation(instance)
        representation['exercise_name'] = instance.exercise_name.exercise_name
        representation['quantity'] = instance.quantity
        representation['cal_per'] = instance.exercise_name.calorie
        representation['burned_cal'] = instance.burned_cal

        return representation

    class Meta:
        model = burned_cal_detail
        fields = '__all__'

    # checking validation
    def validate(self, data):
        data = super(burned_calserializer, self).validate(data)

        if (data.get('quantity') < 0):
            raise serializers.ValidationError("quantity cannot be negative")

        else:
            return data
