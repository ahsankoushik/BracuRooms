from pathlib import Path
from rest_framework import permissions, generics
from rest_framework.decorators import api_view, parser_classes
from django.contrib.auth.decorators import login_required
# from rest_framework.parsers import JSONParser, FormParser, FileUploadParser
from rest_framework.response import Response

# from rest_framework.authtoken.serializers import AuthTokenSerializer
# from django.contrib.auth import login
from . import serializers
from rooms import models

# Create your views here.


BASE_DIR = Path(__file__).resolve().parent.parent

class Entrypoint(generics.GenericAPIView):
    def get(self,request):
        dic = {'login':'/api/login'}
        return Response(dic)


@login_required
@api_view(['GET'])
def rooms(request):
    if request.method == 'GET':
        rooms = models.Room.objects.all()
        serializer = serializers.RoomSerializer(rooms, many = True)
        return Response(serializer.data)