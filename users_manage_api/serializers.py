#Django
from django.contrib.auth import password_validation, authenticate

# Django REST Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

# Models
from users_manage_api import models


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ['email', 'password', 'name', ]
        


#Serializer class for the model
class UserProfileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ['email', 'password', ]


#Serializer class for the login
class UserLoginSerializer(serializers.Serializer):
    #Fields to be requiered
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    # Validating data, tthe method validate() is reserved to make validations with the fields given
    #It has tu have this structure and return "data"
    def validate(self, data):
        #authenticate get the credentials, if they are valid return the user object
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('The credentials are invalid')

        #Save the user whit the context in order to create and recover the token
        self.context['user'] = user
        return data

    def create(self, data):
        """Generate o recover a token"""
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key


#Serializer for create a new user (help)
