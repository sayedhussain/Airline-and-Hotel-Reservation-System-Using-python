'''
Created on Nov 25, 2015

@author: shaik.b
'''
from validations.validate_flight import validate_flight
from exceptions.CustomExceptions import SourceInvalidException,DestinationInvalidException,DepttimeInvalidException,FlightInvalidException
print("Positive test case","expected result-True\n",validate_flight('delhi','banglore','10:00'))
try:
    print("\nNegative test case","Chennai","expected result-The Source is invalid")
    validate_flight('chennai','delhi','10:00') 
except SourceInvalidException as e:
    print(e)
try:
    print("\nNegative test case","Chennai","expected result-The Destination is invalid")
    validate_flight('delhi','chennai','10:00') 
except DestinationInvalidException as e:
    print(e)
try:
    print("\nNegative test case","9:00","expected result-Departure time is invalid")
    validate_flight('mumbai','delhi','9:00') 
except DepttimeInvalidException as e:
    print(e)
try:
    print("\nNegative test case","Banglore,Mumbai,10:00","expected result-No Flights are found,Try different search value")
    validate_flight('banglore','mumbai','09:00') 
except FlightInvalidException as e:
    print(e)
