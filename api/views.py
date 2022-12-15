from pathlib import Path
from rest_framework import permissions, generics, status
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
@api_view(['GET','POST'])
def rooms(request):
    if request.method == 'GET':
        rooms = models.Room.objects.all()
        serializer = serializers.RoomSerializer(rooms, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        if request.user.is_superuser:
            serializer = serializers.RoomSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else: return Response(status=status.HTTP_401_UNAUTHORIZED)


# @login_required
# @api_view(['POST'])
# def book_a_cmputer(request):
#     if request.method == 'POST':
#         models.Room.objects.filter(room_type='lab',seats__lt=31)
        


@login_required
@api_view(['GET','POST'])
def booking(request):
    if request.method == 'GET':
        bookings = models.Booking.objects.all()
        serializer = serializers.BookingSerialzer(bookings, many= 1)
        # print(type(serializer.data))
        return Response(serializer.data)
    elif request.method == 'POST':
        if request.user.is_staff:
            serializer = serializers.BookingAddSerialzer(data = request.data)
                
            if serializer.is_valid():
                temp = serializer.save()
                temp.user = request.user
                temp.save()
                booking = models.Booking.objects.get(id=temp.id)
                for x in request.data['time_slot'].split(',')[:-1]:

                    time = models.TimeSlot(booking=booking,timeslot=x)
                    time.save()
                
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        else: return Response(status=status.HTTP_401_UNAUTHORIZED)


@login_required
@api_view(['GET'])
def get_booking_approval(request):
    bookings = models.Booking.objects.filter(approval = None)
    serializer = serializers.BookingApprovalSerializer(bookings,many= True)
    return Response(serializer.data)

@login_required
@api_view(['GET'])
def approve(request,id,flag):
    if request.method == 'GET':
        if request.user.is_superuser:
            book = models.Booking.objects.get(id=id)
            if int(flag)<0 or int(flag)>1 :
                flag = None
            book.approval = flag
            book.save()
            return Response(status=status.HTTP_200_OK)
        else: Response(status=status.HTTP_401_UNAUTHORIZED)


            
