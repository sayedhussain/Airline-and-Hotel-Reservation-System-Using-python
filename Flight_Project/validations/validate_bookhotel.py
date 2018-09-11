'''
Created on Nov 24, 2015

@author: sayed.hussain
'''
from database.BookHotelDB import get_bookingid, get_location,get_hotelid
from exceptions.BookedHotelException import BookingidInvalidException
from exceptions.BookedHotelException import HotelidInvalidException
from exceptions.BookedHotelException import LocationInvalidException

def validate_bookedid(bookingid):
    list_of_bookingid = [];
    list_of_bookingid=get_bookingid(bookingid);
    if int(bookingid) not in list_of_bookingid:
        raise BookingidInvalidException;
    
def validate_bookedhotelid(hotelid):
    list_of_hotelid = [];
    list_of_hotelid=get_hotelid(hotelid);
    if hotelid not in list_of_hotelid:
        raise HotelidInvalidException;

def validate_location(location):
    list_of_location = [];
    list_of_location=get_location(location);
    print(list_of_location)
    if location not in list_of_location:
        raise LocationInvalidException;