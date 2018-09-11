'''
Created on Nov 23, 2015

@author: sayed.hussain
'''
from validations.validate_bookflight import validate_bookflight
from database.BookingDB import get_fare, insert_booking
from classes.BookedFlight import BookedFlight
from functionality.SearchHotel import search_hotel
from exceptions.BookingFlightException import FlightIdInvalidException
from exceptions.BookingFlightException import DateInvalidException
from exceptions.BookingFlightException import NoOfChildrenInvalidException
from exceptions.BookingFlightException import NoOfAdultsInvalidException
def book_flight(flightid):
    try:
        print("Enter the date of travel:");
        date = input();
        print("Enter the number of children:");
        noofchildren = input();
        print("Enter the number of adults:");
        noofadults = input();
        print("Enter name of primary passenger:");
        passengername = input()
        validate_bookflight(flightid,date,noofchildren,noofadults);
        list_of_fare = []
        list_of_fare = get_fare(flightid);
        total_fare = 0;
        adultfare = list_of_fare[0];
        childfare = list_of_fare[1];
        total_fare = adultfare * int(noofadults) + childfare * int(noofchildren);
        print("Total Fare :",total_fare);
        bookedflight = BookedFlight(flightid,date,passengername,noofchildren,noofadults);
        bookingid = insert_booking(flightid,date,passengername,int(noofchildren),int(noofadults),int(total_fare));
        print("The ticket is successfully booked with id :",bookingid);
        print("Do you want to search the Hotel? Enter Y or N")
        choice = input()
        if choice == 'Y':
            search_hotel(True);
        elif choice == 'N':
            return
    
    except FlightIdInvalidException as e:
        print(e)
        
    except DateInvalidException as e:
        print(e)
        
    except NoOfChildrenInvalidException as e:
        print(e)
        
    except NoOfAdultsInvalidException as e:
        print(e)
        
    except Exception as e:
        print("Some system error occurred")
        print(e)