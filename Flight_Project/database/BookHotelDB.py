'''
Created on Nov 24, 2015

@author: sayed.hussain
'''
import cx_Oracle
from utility.DBConnectivity import create_connection
from utility.DBConnectivity import create_cursor
from utility import DBConnectivity

def get_bookingid(bookingid):
    '''Returns list containing bookingid from bookedflight table'''
    try:
        con = DBConnectivity.create_connection();
        cur = DBConnectivity.create_cursor(con);
        list_of_bookingid=[];
        cur.execute("select bookingid from bookedflight where bookingid =: bookingid",{"bookingid":bookingid});
        for row in cur:
            list_of_bookingid.append(row[0]);
        return list_of_bookingid
    
    except Exception as e:
        print("Sorry some system error occurred")
        print(e)
    
    finally:
        cur.close();
        con.close();

def get_location(location):
    '''Returns list containing location from hotel table'''
    try:
        con = DBConnectivity.create_connection();
        cur = DBConnectivity.create_cursor(con);
        list_of_location=[];
        cur.execute("select location from hotel where location =: location",{"location":location});
      
        for row in cur:
            list_of_location.append(row[0]);
     
        
        return list_of_location
    
    except Exception as e:
        print("Sorry some system error occurred")
        print(e)
    
    finally:
        cur.close();
        con.close();

def get_hotelid(hotelid):
    '''Returns list containing hotelid from hotel table'''
    try:
        con = DBConnectivity.create_connection();
        cur = DBConnectivity.create_cursor(con);
        list_of_hotelid=[];
        cur.execute("select hotelid from hotel where hotelid =: hotelid",{"hotelid":hotelid});
        for row in cur:
            list_of_hotelid.append(row[0]);
        return list_of_hotelid
    
    except Exception as e:
        print("Sorry some system error occurred")
        print(e)
    
    finally:
        cur.close();
        con.close();

def get_fare(hotelid):
    try:
        con = DBConnectivity.create_connection();
        cur = DBConnectivity.create_cursor(con);
        list_of_fare = [];
        cur.execute("select deluxefare,executivefare from hotel where hotelid =: hotelid",{"hotelid":hotelid});
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
        
def insert_booking(hotelid,noofdays,noofadults,noofchild,noofdeluxerooms,noofexecutiverooms,customername,totalfare):
    try:
        count= 1
        con = DBConnectivity.create_connection();
        cur = DBConnectivity.create_cursor(con);
        cur2 = DBConnectivity.create_cursor(con)
        cur2.execute("select * from bookedhotel")
        for row in cur2:
            count +=1;
        hbookingid = count;
        cur.execute("insert into bookedhotel values(:hotelid,:hbookingid,:noofdays,:noofadults,:noofchild,:noofdeluxerooms,:noofexecutiverooms,:customername,:totalfare)"
                    ,{"hotelid":hotelid,"hbookingid":hbookingid,"noofdays":noofdays,"noofadults":noofadults,"noofchild":noofchild,"noofdeluxerooms":noofdeluxerooms,"noofexecutiverooms":noofexecutiverooms,"customername":customername,"totalfare":totalfare});
        con.commit();
        return hbookingid;
    
    except Exception as e:
        print("Sorry some system error occurred")
        print(e)
    
    finally:
        cur.close();
        con.close();            
