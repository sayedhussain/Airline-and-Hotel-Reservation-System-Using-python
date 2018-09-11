'''
Created on Nov 23, 2015

@author: sayed.hussain
'''
class Flight:
    def __init__(self,flightid,flightname,duration,adultfare,childfare):
        self.__flightid= flightid;
        self.__flightname = flightname;
        '''self.__source = source;
        self.__destination = destination;
        self.__depttime = depttime;'''
        self.__duration = duration;
        self.__adultfare = adultfare;
        self.__childfare = childfare;

    def get_flightid(self):
        return self.__flightid


    def get_flightname(self):
        return self.__flightname


    def get_source(self):
        return self.__source


    def get_destination(self):
        return self.__destination


    def get_depttime(self):
        return self.__depttime


    def get_duration(self):
        return self.__duration


    def get_adultfare(self):
        return self.__adultfare


    def get_childfare(self):
        return self.__childfare


   

  

    
    