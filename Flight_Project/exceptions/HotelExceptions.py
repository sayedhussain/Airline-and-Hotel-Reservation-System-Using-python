'''
Created on Nov 24, 2015

@author: sayed.hussain
'''
class BookingIdInvalidException(Exception):
    def __init__(self):
        super().__init__("Invalid booking id");
        
class NoofRoomsInvalidException(Exception):
    def __init__(self):
        super().__init__("Number of adults should not be less than number of executive rooms");

class NoofpeopleInvalidException(Exception):
    def __init__(self):
        super().__init__("Number of people should be equals to the number of rooms");

class LocationInvalidException(Exception):
    def __init__(self):
        super().__init__("Location is invalid");

class NoHotelException(Exception):
    def __init__(self):
        super().__init__("No hotel hotel is matching the search criteria");