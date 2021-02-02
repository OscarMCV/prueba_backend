from rest_framework import serializers

from backend_test_api import models


class HelloSerializer(serializers.Serializer):
    """Create a serializer for a request in my HelloApiView"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)


class CreateClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CreateClass
        fields = '__all__'


class CreateCourserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CreateCourse
        fields = '__all__'


class CreateLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CreateLesson
        fields = '__all__'


class CreateQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CreateQuestion
        fields = '__all__'
