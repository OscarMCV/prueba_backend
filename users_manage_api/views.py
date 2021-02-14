# Django REST Framework
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Serializers
from users_manage_api.serializers import UserLoginSerializer, UserProfileModelSerializer, CreateUserSerializer

# Models
from users_manage_api.models import UserProfile


class CreateUser(APIView):
    queryset = UserProfile.objects.all()
    #Retrieve all the users
    serializer_class = CreateUserSerializer
    #Default serializer for the view

    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response("Invalid Input")
        data = {
            'user': serializer.data,
        }
        return Response(data, status=status.HTTP_201_CREATED)


class UserAPIView(APIView):
    #Only active users, inspect in model for more information about the fields
    queryset = UserProfile.objects.filter(is_active=True, is_student=True)
    ##############Why is this the properly reference?
    serializer_class = UserProfileModelSerializer

    def get(self, request):
        #Only shows active users and students
        user = UserProfile.objects.filter(is_active=True, is_student=True)
        serializer = UserProfileModelSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request):
        """User sign in."""
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            #Return an object instance, based on the validated data and assigns this to user and token
            user, token = serializer.save()
        else:
            return Response("Invalid input")
        data = {
            'user': UserProfileModelSerializer(user).data,
            'access_token': token,
            'api_message': 'login completed successfully'
            'This is '
        }
        return Response(data, status=status.HTTP_201_CREATED)
