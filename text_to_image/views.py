from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from .task import generate_image
from rest_framework.response import Response
from rest_framework import status
from .serializers import GeneratedImageSerializer, GenerateImageSerializer
from .models import GeneratedImage
# Create your views here.

class GenrateImageAPIView(APIView):

    def get_queryset(self,request):
        try:
            image_data= GeneratedImage.objects.all()
            print(image_data)
        except GeneratedImage.DoesNotExist:
            content = {
                'status': 'Support not found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return image_data


    def get(self,request):
        data=self.get_queryset(request)
        serializor=GeneratedImageSerializer(data, many=True)
        print(serializor)
        return Response(serializor.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer=GenerateImageSerializer(data=request.data)
        if serializer.is_valid():
            tasks=[]
            text_prompts=serializer.validated_data['text_prompts']
            for text_prompt in text_prompts:
                image_size = serializer.validated_data['image_size']
                width, height = image_size.split('x')
                task = generate_image(text_prompt, int(width), int(height))
                tasks.append(task)
            return Response({'message:' f'Image Generation Request is submitted. Request ID {tasks}'},status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
