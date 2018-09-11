'''
Created on Nov 25, 2015

@author: shaik.b
'''
from validations.validate_hotel import validate_hotel
from validations.validate_hotel import validate_bookingid
from exceptions.HotelExceptions import BookingIdInvalidException
from exceptions.HotelExceptions import NoofRoomsInvalidException
from exceptions.HotelExceptions import NoofpeopleInvalidException 
from exceptions.HotelExceptions import LocationInvalidException
from exceptions.HotelExceptions import NoHotelException

print("Positive test case",validate_hotel(1,1,1,1,1,'banglore',False))
try:
    print("\nNegative test case","booking id not present","expected result-Invalid booking id")
    validate_bookingid(13) 
except BookingIdInvalidException as e:
     print(e)
try:
    print("\nNegative test case","No of rooms invalid","expected result-Number of adults should not be less than number of executive rooms")
    validate_hotel(1,1,2,1,1,'banglore',False)
except NoofRoomsInvalidException as e:
    print(e)
try:
    print("\nNegative test case","No of rooms equals to No of people","expected result-Number of people should be equals to the number of rooms")
    validate_hotel(1,1,1,1,2,'banglore',False)
except NoofpeopleInvalidException as e:
    print(e)
try:
    print("\nNegative test case","Location is invalid","expected result-Location is invalid")
    validate_hotel(1,1,1,1,1,'goa',False)
except LocationInvalidException as e:
    print(e) 