from rest_framework import serializers
from .models import GeneratedImage

class GenerateImageSerializer(serializers.Serializer):
    text_prompts = serializers.ListField(child=serializers.CharField(), required=True)
    image_size=serializers.CharField(required=True)

class GeneratedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model= GeneratedImage
        fields=['id','text_prompt', 'image_data','created_at']