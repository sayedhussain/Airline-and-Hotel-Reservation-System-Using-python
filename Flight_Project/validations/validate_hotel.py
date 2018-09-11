'''
Created on Nov 24, 2015

@author: sayed.hussain
'''
from database.HotelDBCon import get_bookingid, get_location,get_hotel
from exceptions.HotelExceptions import BookingIdInvalidException
from exceptions.HotelExceptions import NoofRoomsInvalidException
from exceptions.HotelExceptions import NoofpeopleInvalidException
from exceptions.HotelExceptions import LocationInvalidException
from exceptions.HotelExceptions import NoHotelException
def validate_hotel(bookingid,noofadults,noofexecutiverooms,noofdeluxeroom,noofchild,location,flag):
    
    validate_bookingid(bookingid);
    if noofadults<noofexecutiverooms:
        raise NoofRoomsInvalidException
    
    if noofdeluxeroom+noofexecutiverooms != noofadults+noofchild:
        raise NoofpeopleInvalidException
        
    list_of_location = []
    list_of_location = get_location();
    
    if location not in list_of_location:
        raise LocationInvalidException
    
    list_of_hotels = []
    list_of_hotels = get_hotel(location);
    if len(list_of_hotels) == 0:
        raise NoHotelException
    if flag == False:
        for hotel in list_of_hotels:
            print(hotel.get_hotelid(),hotel.get_hotelname(),hotel.get_deluxefare(),hotel.get_executivefare());
        

def validate_bookingid(bookingid):
    if bookingid is not None :
        list_of_bookingid = []
        list_of_bookingid = get_bookingid(bookingid);
        if int(bookingid) not in list_of_bookingid:
            raise BookingIdInvalidException            
    