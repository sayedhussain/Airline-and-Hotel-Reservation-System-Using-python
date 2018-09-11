'''
Created on Nov 23, 2015

@author: sayed.hussain
'''




from database import DBCon
from exceptions.CustomExceptions import SourceInvalidException
from exceptions.CustomExceptions import DestinationInvalidException
from exceptions.CustomExceptions import DepttimeInvalidException
from exceptions.CustomExceptions import FlightInvalidException
def validate_flight(source,destination,depttime):
    if source.isalpha():
        pass
    else:
        raise SourceInvalidException()
    if destination.isalpha() :
        pass
    else:
        raise DestinationInvalidException()
    
    list_of_source = [];
    list_of_source=DBCon.get_source(source);
    if source not in list_of_source:
        raise SourceInvalidException;
 
    list_of_destination = [];
    list_of_destination=DBCon.get_destination(destination);
    if destination not in list_of_destination:
        raise DestinationInvalidException;
    if len(depttime) != 5:
        raise DepttimeInvalidException;
        
    if depttime[2] != ':':
        raise DepttimeInvalidException;
    else:
        h = depttime[0] + depttime[1];
        m = depttime[3] + depttime[4];
        if int(h) >= 24 or int(m) >= 60 :
            raise DepttimeInvalidException;
    
    list_of_flights = []
    list_of_flights = DBCon.get_values(source, destination, depttime);
    if len(list_of_flights) == 0 :
        raise FlightInvalidException;
    print("Available Flights are :");
    print("------------------------------------------------------------------------");
    for i in list_of_flights:
        print(i.get_flightid(),i.get_flightname(),i.get_duration(),i.get_adultfare(),i.get_childfare());
    