'''
Created on Nov 23, 2015

@author: sayed.hussain
'''
from validations.validate_flight import validate_flight
from functionality.Bookflight import book_flight
from exceptions.CustomExceptions import SourceInvalidException
from exceptions.CustomExceptions import DestinationInvalidException
from exceptions.CustomExceptions import DepttimeInvalidException
from exceptions.CustomExceptions import FlightInvalidException
def search_flight():
    try:
        print('Enter the source');
        source = input();
        print('Enter the destination');
        destination = input();
        print('Enter the time');
        depttime = input();
        validate_flight(source.lower(),destination.lower(),depttime.lower()); #valiadtion for source,destination and departure time
        print('Do you wish to continue booking? Enter Y or N');
        choice=input();
        if choice == 'Y':
            print("Enter the flight id:")
            flight_id = input();
            book_flight(flight_id);
        elif choice == 'N':
            pass
    except SourceInvalidException as e:
        print(e)
    
    except DestinationInvalidException as e:
        print(e)
        
    except DepttimeInvalidException as e:
        print(e)
        
    except FlightInvalidException as e:
        print(e)
        
    except Exception as e:
        print("Sorry some system error occurred")
        print(e)
