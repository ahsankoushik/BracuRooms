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
from datetime import datetime

# Create your views here.


BASE_DIR = Path(__file__).resolve().parent.parent

class Entrypoint(generics.GenericAPIView):
    def get(self,request):
        dic = {'login':'/api/login'}
        return Response(dic)



#-----------------------------------------------------------Syed Hasnat Jami-----------------------------------------------------------------#


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
#         models.Room.yyyyobjects.filter(room_type='lab',seats__lt=31)
        


@login_required
@api_view(['GET','POST'])
def booking(request):
    if request.method == 'GET':
        bookings = models.Booking.objects.all()   
        # select * from booking;
        serializer = serializers.BookingSerialzer(bookings, many= 1)
        # print(type(serializer.data))
        return Response(serializer.data)
    elif request.method == 'POST':
        if request.user.is_staff:
            serializer = serializers.BookingAddSerialzer(data = request.data)
            #insert into Booking(date,room,reason) values(request.date,request.room,request.reason)

            if serializer.is_valid():
                temp = serializer.save()
                temp.user = request.user 
                # update booking set user_id = request.user.id 
                temp.save()
                booking = models.Booking.objects.get(id=temp.id)
                for x in request.data['time_slot'].split(',')[:-1]:

                    time = models.TimeSlot(booking=booking,timeslot=x)
                    #insert into time_slot(booking,timeslot) values({booking},{timeslot})
                    time.save()
                
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        else: return Response(status=status.HTTP_401_UNAUTHORIZED)


@login_required
@api_view(['GET'])
def get_booking_approval(request):
    bookings = models.Booking.objects.filter(approval = None)
    #select * from booking where approal != null
    serializer = serializers.BookingApprovalSerializer(bookings,many= True)
    data = []
    c = 0
    for x in range(len(serializer.data)):
        data.append(dict(serializer.data[x]))
        time_slots = ''
        for y in models.TimeSlot.objects.filter(booking = data[c]['id']):
            # select * from time_slot where booking = {data[c]['id']}
            time_slots += str(y.timeslot) +', '

        data[c]['time_slot'] = time_slots
        c += 1

    return Response(data)


#-----------------------------------------------------------Md Ahsan Hasib------------------------------------------------------------------#


@login_required
@api_view(['GET'])
def approve(request,id,flag):
    if request.method == 'GET':
        if request.user.is_superuser:
            if int(flag)<0 or int(flag)>1 :
                flag = None
            book = models.Booking.objects.get(id=id)
            # select * from booking where id = {id};
            times = []
            for x in models.TimeSlot.objects.filter(booking= book):
                # select * from time_slot where booking_id = {book_id}
                times.append(x.timeslot)
            temp = models.Booking.objects.raw(f'''select * from Booking b inner join time_slot t on b.id = t.booking_id where b.date = "{book.date}" and b.room_id ={book.id_room} and t.timeslot in {tuple(times)} and  b.approval=1;''')
            if len(temp)>0:
                return Response(status=status.HTTP_409_CONFLICT)
            
            # if flag != None and 
            
            book.approval = flag    # update booking set approval = {flag} where id = {id};
            book.approver = request.user # update booking set approver = {request.user} where id = {id};
            book.save()
            return Response(status=status.HTTP_200_OK)
        else: Response(status=status.HTTP_401_UNAUTHORIZED)


@login_required
@api_view(['POST'])
def free_room_teacher(request):
    date = request.data['date']
    today = False
    if date == str(datetime.now())[:10]: today = 1
    time_slot = request.data['time_slot'].strip()
    time_str = '(' + str(time_slot) 
    if time_str[-1] == ',': time_str = time_str[:-1]
    time_str += ')'
    # print(time_str)
    if time_slot[-1] == '' or time_slot[-1] == ' ':time_slot.pop(-1)
    if today:
        st_book = models.Room.objects.raw("select * from Room where booked > 0")
        booked = []
        for x in st_book :
            booked.append(x.id)


    temp = models.Booking.objects.raw(f'''select id from Room where id not in
                                            (select b.room_id from Booking b inner join time_slot t on b.id = t.booking_id 
                                            where b.date = "{date}"  and t.timeslot in {time_str} and b.approval =1 )''')
    # print(temp)
    frees = []
    for x in temp: 
        if   today:
            if x.id in booked:
                continue
        frees.append(x.id)
    rooms = models.Room.objects.filter(id__in=frees)
    # select * from Room where id in {frees}
    serializer = serializers.FreeRoomSerializer(rooms, many =1 )
    return Response(serializer.data)


@login_required
@api_view(['POST'])
def free_room_st(request):
    date = request.data['date']
    time_slot = request.data['time_slot'].strip()
    time_str = '(' + str(time_slot) 
    if time_str[-1] == ',': time_str = time_str[:-1]
    time_str += ')'
    if time_slot[-1] == '' or time_slot[-1] == ' ':time_slot.pop(-1)
    st_book = models.Room.objects.raw("select * from Room where booked = seats")
    booked = []
    for x in st_book :
        booked.append(x.id)
    temp = models.Booking.objects.raw(f'''select id from Room where id not in(select b.room_id from Booking b inner join time_slot t on b.id = t.booking_id where b.date = "{date}"  and t.timeslot in {time_str} and b.approval =1 )''')
    frees = []
    for x in temp: 
        if x.id in booked:
            continue
        frees.append(x.id)
    rooms = models.Room.objects.filter(id__in=frees)
    # select * from Room where id in {frees}
    serializer = serializers.FreeRoomSerializer(rooms, many =1 )

    return Response(serializer.data)







#----------------------------------------------------------------- Archana Das-----------------------------------------------------------#


@login_required
@api_view(['GET'])
def book_a_seat(request,room):
    try: 
        seat = models.RequestsForSeats.objects.get(user = request.user)
        # select * from request_for_seat where user_id = {request.user.id}
        if seat.seats_requested == 1:
            return Response(status=status.HTTP_409_CONFLICT,data='You have already one seat booked')
    except:
        seat = models.RequestsForSeats(user=request.user)
        # insert into request_for_seat(user_id = {request.user.id});
    r = models.Room.objects.get(id = room)
    # select * from Room where id = {room}

    if r.booked == r.seats:
        return Response('class full')
    seat.Room_number = r 
    seat.seats_requested = 1
    # update request_for_seat set Room_number = {r}, seats_requested = 1 where id = {request.user.id} 
    r.booked += 1
    #update room set booked = booked+1
    r.save()
    seat.save()

    return Response(status=status.HTTP_200_OK)

    



@login_required
@api_view(['GET'])
def remove_seat(request):
    seat = models.RequestsForSeats.objects.get(user=request.user)
    # select * from request_for_seat where user_id = {request.user.id}
    r = models.Room.objects.get(id = seat.Room_number.id)
    # select * from Room where id = {room}
    r.booked -= 1
    #update room set booked = booked-1
    seat.Room_number = None
    seat.seats_requested = 0 
    # update request_for_seat set Room_number = null, seats_requested = 0 where id = {request.user.id} 
    r.save()
    seat.save()
    return Response(status=status.HTTP_200_OK)