'''
Created on Nov 23, 2015

@author: sayed.hussain
'''
class BookedFlight:
    
    def __init__(self,flightid,dateoftravel,passengername,noofchild,noofadults):
        
        self.__flightid=flightid;
        self.__dateoftravel=dateoftravel;
        self.__passengername=passengername;
        self.__noofchild=noofchild;
        self.__noofadults=noofadults;
    
   

    def get_flightid(self):
        return self.__flightid

    def get_dateoftravel(self):
        return self.__dateoftravel

    def get_passengername(self):
        return self.__passengername

    def get_noofchild(self):
        return self.__noofchild

    def get_noofadults(self):
        return self.__noofadults

    def set_flightid(self, value):
        self.__flightid = value

    def set_dateoftravel(self, value):
        self.__dateoftravel = value

    def set_passengername(self, value):
        self.__passengername = value

    def set_noofchild(self, value):
        self.__noofchild = value

    def set_noofadults(self, value):
        self.__noofadults = value

        