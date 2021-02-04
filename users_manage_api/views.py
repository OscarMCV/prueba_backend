# Django REST Framework
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Serializers
from users_manage_api.serializers import UserLoginSerializer, UserProfileModelSerializer

# Models
from users_manage_api.models import UserProfile


class UserAPIView(APIView):
    #Only active users, inspect in model for more information about the fields
    queryset = UserProfile.objects.filter(is_active=True)
    ##############Why is this the properly reference?
    serializer_class = UserProfileModelSerializer

    def get(self, request):
        #Only shows active users
        user = UserProfile.objects.filter(is_active=True)
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
        }
        return Response(data, status=status.HTTP_201_CREATED)
