'''
Created on Nov 23, 2015

@author: sayed.hussain
'''
import cx_Oracle
from utility.DBConnectivity import create_connection
from utility.DBConnectivity import create_cursor

from utility import DBConnectivity
from classes.Flight import Flight


def get_source(sources):
    '''Returns list containing source from flight table'''
    try:
        con = DBConnectivity.create_connection();
        cur = DBConnectivity.create_cursor(con);
        list_of_source = [];
        cur.execute("select source from Flight  where Lower(source) =: sources",{"sources":sources});
        for source in cur:
            list_of_source.append(source[0].lower());
        return list_of_source;
    
    except Exception as e:
        print("Sorry some system error occurred")
        print(e)
    
    finally:
        cur.close();
        con.close();

def get_destination(destinations):
    '''Returns list containing destination from flight table'''
    try:
        con = DBConnectivity.create_connection();
        cur = DBConnectivity.create_cursor(con);
        list_of_destination = [];
        
        cur.execute("select destination from flight  where Lower(destination) =: destinations",
                {"destinations":destinations});
        for destination in cur:
            list_of_destination.append(destination[0].lower());
        
        return list_of_destination;
    
    except Exception as e:
        print("Sorry some system error occurred")
        print(e)
    
    finally:
        cur.close();
        con.close();
        
def get_values(sources,destinations,depttimes):
    '''Returns list containing flights detail having matched conditions'''
    try:
        con = DBConnectivity.create_connection();
        cur = DBConnectivity.create_cursor(con);
        list_of_flights = [];
        cur.execute("select * from flight where Lower(destination) =: destinations and Lower(source) =: sources and Lower(depttime) >: depttimes" 
                    ,{"destinations":destinations,"sources":sources,"depttimes":depttimes});
        for row in cur:
            flight = Flight(row[0],row[1],row[5],row[6],row[7]);
            list_of_flights.append(flight);
        return list_of_flights;
    
    except Exception as e:
        print("Sorry some system error occurred")
        print(e)
    
    finally:
        cur.close();
        con.close();

