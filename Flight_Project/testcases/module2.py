'''
Created on Nov 25, 2015

@author: shaik.b
'''
from validations.validate_bookflight import validate_bookflight
from exceptions.BookingFlightException import FlightIdInvalidException,DateInvalidException,NoOfChildrenInvalidException,NoOfAdultsInvalidException
print("Positive test case","SP101","expected result-True\n",validate_bookflight('SP101','12-12-16',1,1))
try:
    print("\nNegative test case","SG101","expected result-The flight Id does not exist")
    validate_bookflight('SG101','12-12-16',1,1) 
except FlightIdInvalidException as e:
     print(e)
try:
    print("Negative test case","20/11/15","expected result-Enter valid date format")
    validate_bookflight('SP101','2/11/15',1,1)
except DateInvalidException as e:
     print(e)
try:
    print("Negative test case","6","expected result-Enter valid children number")
    validate_bookflight('SP101','12-12-16',6,1)
except NoOfChildrenInvalidException as e:
     print(e)
try:
    print("Negative test case","0","expected result-Enter valid Adults number")
    validate_bookflight('SP101','12-12-16',1,0)
except NoOfAdultsInvalidException as e:
     print(e)