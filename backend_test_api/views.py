from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from backend_test_api import serializers
from backend_test_api import models


class CreateClassView(APIView):
    """Serializer to get the fields"""
    def get(self, request, format=None):
        """Method to get the classes"""
        classes = models.CreateClass.objects.all()
        serializer = serializers.CreateClassSerializer(classes, many=True)
        """The parameter "many=True" tell drf that queryset contains mutiple 
        items (a list of items) so drf needs to serialize each item with serializer 
        class (and serializer.data will be a list)"""
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.CreateClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
