#Django rest_framework
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsStandardUser
from rest_framework.response import Response
from rest_framework.views import APIView
#models
from teachers_site_api import models
from teachers-site_api import serializers


# Create your views here.
class WhatchClasses(APIView):

    def get_permissions(self):
        permission_classes = [IsAuthenticated, IsStandardUser]
        return [permission() for permission in permission_classes]

    def get(self, request):
        