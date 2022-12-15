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
    data = []
    c = 0
    for x in range(len(serializer.data)):
        data.append(dict(serializer.data[x]))
        time_slots = ''
        for y in models.TimeSlot.objects.filter(booking = data[c]['id']):
            time_slots += str(y.timeslot) +', '

        data[c]['time_slot'] = time_slots
        c += 1

    return Response(data)

@login_required
@api_view(['GET'])
def approve(request,id,flag):
    if request.method == 'GET':
        if request.user.is_superuser:
            if int(flag)<0 or int(flag)>1 :
                flag = None
            book = models.Booking.objects.get(id=id)
            times = []
            for x in models.TimeSlot.objects.filter(booking= book):
                times.append(x.timeslot)
            temp = models.Booking.objects.raw(f'''select * from Booking b inner join time_slot t on b.id = t.booking_id where b.date = "{book.date}" and b.room_id ={book.id_room} and t.timeslot in {tuple(times)} and  b.approval=1;''')
            if len(temp)>0:
                return Response(status=status.HTTP_409_CONFLICT)
            
            # if flag != None and 
            
            book.approval = flag
            book.approver = request.user
            book.save()
            return Response(status=status.HTTP_200_OK)
        else: Response(status=status.HTTP_401_UNAUTHORIZED)


@login_required
@api_view(['POST'])
def free_room(request):
    date = request.data['date']
    time_slot = request.data['time_slot'].split(',')
    if time_slot[-1] == '' or time_slot[-1] == ' ':time_slot.pop(-1)
    
    temp = models.Booking.objects.raw(f'''select id from Room where id not in(select b.room_id from Booking b inner join time_slot t on b.id = t.booking_id where b.date = "{date}"  and t.timeslot in {tuple(time_slot)} and b.approval =1 )''')
    frees = []
    for x in temp: 
        frees.append(x.id)
    rooms = models.Room.objects.filter(id__in=frees)
    serializer = serializers.FreeRoomSerializer(rooms, many =1 )

    

    return Response(serializer.data)


            
