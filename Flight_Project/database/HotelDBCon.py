'''
Created on Nov 24, 2015

@author: sayed.hussain
'''
import cx_Oracle
from utility.DBConnectivity import create_connection
from utility.DBConnectivity import create_cursor

from utility import DBConnectivity
from classes.Hotel import Hotel


def get_noofpeople(bookingid):
    '''Functions get No of child and No of adults from user'''
    try:
        con = DBConnectivity.create_connection();
        cur = DBConnectivity.create_cursor(con);
        list_of_passenger = [];
        cur.execute("select noofchild,noofadults from bookedflight  where bookingid =:bookingid",{"bookingid":bookingid});
        for row in cur:
            list_of_passenger.append(row[0]);
            list_of_passenger.append(row[1]);
        return list_of_passenger;
    
    except Exception as e:
        print("Sorry some system error occurred")
        print(e)
    
    finally:
        cur.close();
        con.close();
def get_bookingid(bookingid):
    '''Returns list containg bookingid from bookedflight table'''
    try:
        con = DBConnectivity.create_connection();
        cur = DBConnectivity.create_cursor(con);
        list_of_bookedid=[];
        cur.execute("select bookingid from bookedflight");
        for row in cur:
            list_of_bookedid.append(row[0]);
        
        return list_of_bookedid
    
    except Exception as e:
        print("Sorry some system error occurred")
        print(e)
    
    finally:
        cur.close();
        con.close();

def get_location():
    '''Returns list containg location from hotel table'''
    try:
        con = DBConnectivity.create_connection();
        cur = DBConnectivity.create_cursor(con);
        list_of_location=[];
        cur.execute("select location from hotel");
        for row in cur:
            list_of_location.append(row[0].lower());
        
        return list_of_location
    
    except Exception as e:
        print("Sorry some system error occurred")
        print(e)
    
    finally:
        cur.close();
        con.close();

def get_hotel(location):
    '''Returns list containing details of hotel in location'''
    try:
        con = DBConnectivity.create_connection();
        cur = DBConnectivity.create_cursor(con);
        list_of_hotel=[];
        cur.execute("select * from hotel where lower(location) =: location",{"location":location});
        for row in cur:
            hotel = Hotel(row[0],row[1],row[2],row[3],row[4]);
            list_of_hotel.append(hotel);
      
        return list_of_hotel
    
    except Exception as e:
        print("Sorry some system error occurred")
        print(e)
    
    finally:
        cur.close();
        con.close();