'''
Created on Nov 23, 2015

@author: sayed.hussain
'''
class Hotel:
    def __init__(self,hotelid,hotelname,location,deluxefare,executivefare):
        self.__hotelid=hotelid;
        self.__hotelname=hotelname;
        self.__location=location;
        self.__deluxefare=deluxefare;
        self.__executivefare=executivefare;
    
    def get_hotelid(self):
        return self.__hotelid
    
    def get_hotelname(self):
        return self.__hotelname
    
    def get_location(self):
        return self.__location
    
    def get_deluxefare(self):
        return self.__deluxefare
    
    def get_executivefare(self):
        return self.__executivefare
    
    def set_hotelid(self, value):
        self.__hotelid = value
    
    def set_hotelname(self, value):
        self.__hotelname = value
    
    def set_location(self, value):
        self.__location = value
    
    def set_deluxefare(self, value):
        self.__deluxefare = value
    
    def set_executivefare(self, value):
        self.__executivefare = value