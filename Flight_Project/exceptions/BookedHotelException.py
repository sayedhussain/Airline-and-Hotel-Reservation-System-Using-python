'''
Created on Nov 24, 2015

@author: sayed.hussain
'''
class BookingidInvalidException(Exception):
    def __init__(self):
        super().__init__('Booking Id not valid')

class HotelidInvalidException(Exception):
    def __init__(self):
        super().__init__('Hotel Id not valid')
        
class LocationInvalidException(Exception):
    def __init__(self):
        super().__init__('Location not found')