#Django rest_framework
from rest_framework.permission import BasePermission

#models
from users_manage_api.models import UserProfile


class IsStandardUser(BasePermission):
    """Allow acces to answer questions"""

    def has_permission(slef, request, view):
        try:
            user = UserProfile.objects.get
            email = request.user,
            is_recruiter = False
            )
        except UserProfile.DoesNotExist:
            return False
        return True

