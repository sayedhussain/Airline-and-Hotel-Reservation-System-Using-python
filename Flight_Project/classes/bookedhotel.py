'''
Created on Nov 24, 2015

@author: sayed.hussain
'''
class bookedhotel:
    def __init__(self,hotelid,bookingid,noofdays,noofadults,noofchild,noofdeluxerooms,noofexecutiverooms,customername):
        self.__hotelid=hotelid;
        self.__bookingid=bookingid;
        self.__noofdays=noofdays;
        self.__noofadults=noofadults;
        self.__noofchild=noofchild;
        self.__noofdeluxerooms;
        self.__noofexecutiverooms;
        self.__customername;

    def get_hotelid(self):
        return self.__hotelid

    def get_bookingid(self):
        return self.__bookingid

    def get_noofdays(self):
        return self.__noofdays

    def get_noofadults(self):
        return self.__noofadults

    def get_noofchild(self):
        return self.__noofchild

    def get_noofdeluxerooms(self):
        return self.__noofdeluxerooms

    def get_noofexecutiverooms(self):
        return self.__noofexecutiverooms

    def get_customername(self):
        return self.__customername

    def set_hotelid(self, value):
        self.__hotelid = value

    def set_bookingid(self, value):
        self.__bookingid = value

    def set_noofdays(self, value):
        self.__noofdays = value

    def set_noofadults(self, value):
        self.__noofadults = value

    def set_noofchild(self, value):
        self.__noofchild = value

    def set_noofdeluxerooms(self, value):
        self.__noofdeluxerooms = value

    def set_noofexecutiverooms(self, value):
        self.__noofexecutiverooms = value

    def set_customername(self, value):
        self.__customername = value
