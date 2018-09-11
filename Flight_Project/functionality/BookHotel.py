'''
Created on Nov 24, 2015

@author: sayed.hussain
'''


from validations.validate_bookhotel import validate_bookedid,validate_bookedhotelid,validate_location
from database.BookHotelDB import get_fare, insert_booking
from exceptions.BookedHotelException import BookingidInvalidException
from exceptions.BookedHotelException import HotelidInvalidException
from exceptions.BookedHotelException import LocationInvalidException

def book_hotel(noofadults,noofchild,noofdeluxerooms,noofexecutiverooms,flag): #validating No of bookings and No of rooms
    try:
        print("Enter the Hotel id")
        hotelid = input();
            
        print("Enter no of days")
        noofdays=input()
        print("Enter name under which booking should be made");
        customername=input()
        
        
        if hotelid.isdigit():
      
            raise HotelidInvalidException
        
        
        validate_bookedhotelid(hotelid)
        list_of_fare = []
        list_of_fare = get_fare(hotelid)
        total_fare = list_of_fare[0] * int(noofdays) + list_of_fare[1] * int(noofdays)
        print('Total Fare :',total_fare)
        bookingid = insert_booking(hotelid,int(noofdays),int(noofadults),int(noofchild),int(noofdeluxerooms),int(noofexecutiverooms),customername,total_fare);
        print("Your hotel accomodation has been booked with booking id",bookingid)
        
    except BookingidInvalidException as e:
        print(e)
    
    except HotelidInvalidException as e:
        print(e)
        
    except LocationInvalidException as e:
        print(e)
      
  
    