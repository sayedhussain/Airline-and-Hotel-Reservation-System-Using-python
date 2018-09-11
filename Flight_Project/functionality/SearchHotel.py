'''
Created on Nov 24, 2015

@author: sayed.hussain
'''
from database.HotelDBCon import get_noofpeople
from validations.validate_hotel import validate_hotel, validate_bookingid
from functionality.BookHotel import book_hotel
from exceptions.HotelExceptions import BookingIdInvalidException
from exceptions.HotelExceptions import NoofRoomsInvalidException
from exceptions.HotelExceptions import NoofpeopleInvalidException
from exceptions.HotelExceptions import LocationInvalidException
from exceptions.HotelExceptions import NoHotelException
def search_hotel(flag):
    try:
        print("Do you have the flight booking id ? Enter Y or N");
        choice = input();
        if choice == 'Y':
            print("Enter the booking id")
            bookingid = input();
            validate_bookingid(bookingid);
            list_of_passenger =[]
            list_of_passenger = get_noofpeople(bookingid);
            noofchild = list_of_passenger[0]
            noofadults = list_of_passenger[1]
        elif choice == 'N':
            bookingid = None;
            print("Enter the number of children")
            noofchild = input()
            print("Enter the number of adults")
            noofadults = input()
        
        print("Enter the number of deluxe rooms");
        noofdeluxeroom = input();
        print("Enter the number of executive rooms")
        noofexecutiverooms = input();
        print("Enter location")
        location = input()
        #validating user data as No of peoples and No of rooms booked
        validate_hotel(bookingid,int(noofadults),int(noofexecutiverooms),int(noofdeluxeroom),int(noofchild),location.lower(),flag)
        
       
        if flag == False:
            print("Do you wish to book a hotel? Enter Y or N")
            choice = input()
            if choice == 'Y':
                book_hotel(noofadults,noofchild,noofdeluxeroom,noofexecutiverooms,flag);
        else:
             book_hotel(noofadults,noofchild,noofdeluxeroom,noofexecutiverooms,flag);
    
    except BookingIdInvalidException as e:
        print(e)
            
    except NoofRoomsInvalidException as e:
        print(e)
            
    except NoofpeopleInvalidException as e:
        print(e)
            
    except LocationInvalidException as e:
        print(e)
        
    except NoHotelException as e:
        print(e)
        
    except Exception as e:
        print("Some system error occurred")
        print(e)    