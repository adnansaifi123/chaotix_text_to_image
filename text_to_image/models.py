from django.db import models

# Create your models here.

class GeneratedImage(models.Model):
    text_prompt=models.CharField(max_length=500)
    image_data=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

