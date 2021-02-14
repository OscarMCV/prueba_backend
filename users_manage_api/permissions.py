#Django rest_framework
from rest_framework.permissions import BasePermission


#Permissions in REST framework are always defined as a list of permission classes.
#models
from users_manage_api.models import UserProfile


class IsStudent(BasePermission):
    """Allow acces to answer questions and view content"""
    #https://www.django-rest-framework.org/api-guide/permissions/#custom-permissions
    def has_permission(self, request, view):
        #the has_permission and has_object_permission are 
        #reserved methods for the BasePermission classes
        try:
            user = UserProfile.objects.get(
                email=request.user,
                is_student=True
            )
            #the request.user gives the user through the given token
            #If forget ho reques.user works:
            # https://www.django-rest-framework.org/api-guide/authentication/#authentication
        except UserProfile.DoesNotExist:
            return False
        return True


class IsTeacher(BasePermission):
    message = "Stundets can't perform this action"

    def has_permission(self, request, view):
        try:
            user = UserProfile.objects.get(
                email=request.user,
                is_teacher=True
            )
        except UserProfile.DoesNotExist:
            return False
        return True

