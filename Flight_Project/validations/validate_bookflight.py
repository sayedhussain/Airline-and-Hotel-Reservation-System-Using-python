'''
Created on Nov 23, 2015

@author: sayed.hussain
'''

from database import DBCon
from database import BookingDB
from exceptions.BookingFlightException import FlightIdInvalidException
from exceptions.BookingFlightException import DateInvalidException
from exceptions.BookingFlightException import NoOfChildrenInvalidException
from exceptions.BookingFlightException import NoOfAdultsInvalidException

def validate_bookflight(flightid,date,noofchildren,noofadults):
    list_of_flightid = []
    list_of_flightid = BookingDB.get_flightid(flightid);
    if flightid not in list_of_flightid:
        raise FlightIdInvalidException;
    if len(date)!=8 and date[2]!='-' and date[5]!='-':
        raise DateInvalidException;
    if int(noofchildren)<0 or int(noofchildren)>4:
        raise NoOfChildrenInvalidException;
    if int(noofadults)<1 or int(noofadults)>4:
        raise NoOfAdultsInvalidException;