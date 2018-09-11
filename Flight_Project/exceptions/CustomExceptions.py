'''
Created on Nov 23, 2015

@author: sayed.hussain
'''
class SourceInvalidException(Exception):
    def __init__(self):
        super().__init__("The source is invalid");

class DestinationInvalidException(Exception):
    def __init__(self):
        super().__init__("The destination is invalid");
        
class DepttimeInvalidException(Exception):
    def __init__(self):
        super().__init__("Departure time is invalid");
        
class FlightInvalidException(Exception):
    def __init__(self):
        super().__init__("No Flights are found,Try different search value");


    