from rest_framework import serializers
from apiCNN import models

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'image',
            'label',
            'probability',
        )
        model = models.Image