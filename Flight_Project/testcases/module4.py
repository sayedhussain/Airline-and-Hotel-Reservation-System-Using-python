'''
Created on Nov 25, 2015

@author: shaik.b
'''
from validations.validate_bookhotel import validate_bookedid
from validations.validate_bookhotel import validate_bookedhotelid
from validations.validate_bookhotel import validate_location
from exceptions.BookedHotelException import BookingidInvalidException
from exceptions.BookedHotelException import HotelidInvalidException
from exceptions.BookedHotelException import LocationInvalidException

print("Positive test case","expected result-True\n",validate_bookedid(1))
print("Positive test case","expected result-True\n",validate_bookedhotelid('H1001'))
print("Positive test case","expected result-True\n",validate_location('Delhi'))
try:
    print("\nNegative test case","Invalid bookingid",validate_bookedid('99'))
except BookingidInvalidException as e:
    print(e) 
    
try:
    print("\nNegative test case","Invalid hotelid",validate_bookedhotelid('H111'))
except HotelidInvalidException as e:
    print(e)
    
try:
    print("\nNegative test case","Invalid Location",validate_location('goa'))
except LocationInvalidException as e:
    print(e)