'''
Created on Nov 23, 2015

@author: sayed.hussain
'''
class FlightIdInvalidException(Exception):
    def __init__(self):
        super().__init__("Flight id does not exist");
class DateInvalidException(Exception):
    def __init__(self):
        super().__init__("Enter Valid date format");
class NoOfChildrenInvalidException(Exception):
    def __init__(self):
        super().__init__("Enter Valid Children Number");
class NoOfAdultsInvalidException(Exception):
    def __init__(self):
        super().__init__("Enter Valid Adults Number");