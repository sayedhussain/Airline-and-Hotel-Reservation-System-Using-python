'''
Created on Nov 24, 2015

@author: sayed.hussain
'''
import cx_Oracle
from utility.DBConnectivity import create_connection
from utility.DBConnectivity import create_cursor
from utility import DBConnectivity
from classes.Flight import Flight

def get_flightid(flightid):
    '''Returns list containg flightid from flight table'''
    try:
        con = DBConnectivity.create_connection();
        cur = DBConnectivity.create_cursor(con);
        list_of_flightid = [];
        cur.execute("select flightid from Flight  where flightid =: flightid",{"flightid":flightid});
        for flightid in cur:
            list_of_flightid.append(flightid[0]);
        return list_of_flightid;
    
    except Exception as e:
        print("Sorry some system error occurred")
        print(e)
    
    finally:
        cur.close();
        con.close();

def get_fare(flightid):
    '''calculates total fare depending on flight and no of childs and adults'''
    try:
        con = DBConnectivity.create_connection();
        cur = DBConnectivity.create_cursor(con);
        list_of_fare = [];
        cur.execute("select adultfare,childfare from Flight  where flightid =: flightid",{"flightid":flightid});
        for row in cur:
            list_of_fare.append(row[0]);
            list_of_fare.append(row[1]);
        return list_of_fare;
    
    except Exception as e:
        print("Sorry some system error occurred")
        print(e)
    
    finally:
        cur.close();
        con.close();

def insert_booking(flightid,dateoftravel,passengername,noofchild,noofadults,totalfare):
    '''calculates booking id and insert values in bookedflight table'''
    try:
        count= 1
        con = DBConnectivity.create_connection();
        cur = DBConnectivity.create_cursor(con);
        cur2 = DBConnectivity.create_cursor(con)
        cur2.execute("select * from bookedflight")
        for row in cur2:
            count +=1;
        bookingid = count;
        cur.execute("insert into bookedflight values(:bookingid,:flightid,to_date(:dateoftravel,'dd-mm-yy'),:passengername,:noofchild,:noofadults,:totalfare)",
                    {"bookingid":bookingid,"flightid":flightid,"dateoftravel":dateoftravel,"passengername":passengername,"noofchild":noofchild,"noofadults":noofadults,"totalfare":totalfare})
        con.commit();
        return bookingid
    
    except Exception as e:
        print("Sorry some system error occurred")
        print(e)
    
    finally:
        cur.close();
        con.close();      