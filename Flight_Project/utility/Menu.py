'''
Created on Jul 29, 2015

@author: Deepak_M05
'''
from validations import validate_flight
from functionality.Search_flight import search_flight
from functionality.Bookflight import book_flight
from functionality.SearchHotel import search_hotel
from functionality.BookHotel import book_hotel
from functionality.AdvanceSearch import advanced_search

'''
This module displays a menu to the user.
'''

print("Welcome to Integrated Travel Services!!")
print("***************************************")

print("Choose an option from below:\n")

end=False


while(end==False):
    print("1. Search a Flight")
    print("2. Book a Flight")
    print("3. Search a Hotel")
    print("4. Book a Hotel")
    print("5. Advanced Flight search")
    print("6. Exit")
    option=input()
    if(option.isdigit() and (int(option)>=1 or int(option)<=6)):
        if(int(option)==1):
            print("Let us search a flight")
            search_flight();
           
        if(int(option)==2):
            print("Let us book a flight")
            print("Enter Flight id")
            flightid = input()
            book_flight(flightid);
        if(int(option)==3):
            print("Let us search a hotel")
            flag = False
            search_hotel(flag);
        if(int(option)==4):
            print("Let us book a hotel")
            flag = True
            search_hotel(flag);
        if(int(option)==5):
            print("Advanced Search")
            advanced_search();
        if(int(option)==6):
            print("Thank you!")
            end=True
    else:
        print("Please enter a valid option ( 1,2,3,4,5,6 )")
    