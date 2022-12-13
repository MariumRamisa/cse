import os
import base64
import io
import logging

from django.conf import settings
from django.shortcuts import _get_queryset
from django.core.exceptions import ValidationError

from rest_framework import serializers

from source.exceptions import CustomNotFoundError


def get_object_or_404(klass, *args, **kwargs):

    queryset = _get_queryset(klass)
    try:
        return queryset.get(*args, **kwargs)
    except queryset.model.DoesNotExist:
        model = queryset.model._meta.object_name
        raise CustomNotFoundError(f"{model} not found")


def annotation_validator(value):
    if value is not None:
        try:
            start_index = int(value.pop('start_index'))
            end_index = int(value.pop('end_index'))
            if (start_index <= 0 and end_index <= 0) or (start_index > end_index):
                raise ValueError
        except (KeyError, ValueError, TypeError):
            raise ValidationError(
                message="Invalid Annotation",
                params={'value': value},
            ) from None
    return value
