'''
Created on Nov 25, 2015

@author: sayed.hussain
'''
import cx_Oracle
from utility.DBConnectivity import create_connection
from utility.DBConnectivity import create_cursor

from utility import DBConnectivity

def check(src,dest):
    try:
        
        con1=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con1)
        #cur2=DBConnectivity.create_cursor(con1)
        flag=False
        cur.execute("select flightid, depttime, duration, source, destination from flight where lower(source) =:source and lower(destination) =:destination",{"source":src.lower(),"destination":dest.lower()})
        
        print("non-stop flight")
        print("FLIGHTID    DEPARTURETIME    DURATION    SOURCE    DESTINATION")
        for row in cur:
            flag=True
            
            
                
            print("--------------------------------------------------------------")
            print(row[0],"        ",row[1],"        ", row[2],"      ", row[3],"      ",row[4])
            
        if(flag==False):
            print("NO FLIGHTS AVAILABLE")   
        print("--------------------------------------------------------------")
        
        
        flag=False
        cur.execute("select f1.flightid, f1.depttime, f1.duration,f1.source,f1.destination, f2.flightid, f2.depttime, f2.duration, f2.source,f2.destination from flight f1, flight f2 where f1.source=:source AND f1.destination=f2.source AND f2.destination=:destination AND (TO_NUMBER(SUBSTR(f1.DEPTTIME,1,2))+F1.DURATION) < TO_NUMBER(SUBSTR(F2.DEPTTIME,1,2))",{"source":src,"destination":dest})
        print("flights with one-stop")
        for row in cur:
            flag= True
            print("FLIGHTID    DEPARTURETIME    DURATION    SOURCE    DESTINATION")
            print("--------------------------------------------------------------")
            print(row[0],"        ",row[1],"        ", row[2],"      ", row[3],"      ",row[4])
            print(row[5],"        ", row[6],"        ", row[7],"      ", row[8],"      ", row[9])
        
        if(flag==False):
            print("NO FLIGHTS AVAILABLE")   
        print("--------------------------------------------------------------")
        
        flag=False
        cur.execute("select f1.flightid, f1.depttime, f1.duration, f1.source,f1.destination, f2.flightid, f2.depttime, f2.duration,f2.source,f2.destination, f3.flightid, f3.depttime, f3.duration,F3.SOURCE,F3.DESTINATION from flight f1,flight f2 ,FLIGHT F3 where lower(f1.source)=:source AND f1.DESTINATION=f2.SOURCE AND f2.DESTINATION=F3.SOURCE AND f1.source<>f2.destination and lower(F3.DESTINATION)=:destination and TO_NUMBER(SUBSTR(f1.depttime,1,2))+F1.DURATION<TO_NUMBER(SUBSTR(f2.depttime,1,2)) and TO_NUMBER(SUBSTR(f2.depttime,1,2))+F2.DURATION <TO_NUMBER(SUBSTR(F3.depttime,1,2))",{"source":src.lower(),"destination":dest.lower()})
        
        print("flights with two-stops")
        for row in cur:
            flag=True
        
        
            print("FLIGHTID    DEPARTURETIME    DURATION    SOURCE    DESTINATION")
            print("--------------------------------------------------------------")
            print(row[0],"        ",row[1],"        ", row[2],"      ", row[3],"      ",row[4])
            print(row[5],"        ", row[6],"        ", row[7],"      ", row[8],"      ", row[9])
            print(row[10],"        ", row[11],"        ", row[12],"      ", row[13],"      ", row[14])
        if(flag==False):
            print("NO FLIGHTS AVAILABLE")   
        print("--------------------------------------------------------------")
                
    
    finally:
        cur.close()
        #cur2.close()
        con1.close()
        