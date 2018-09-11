'''
Created on Nov 24, 2015

@author: sayed.hussain
'''
from database.AdvanceSearchDB import check
def advanced_search():
    try:
        source=input("Enter the source: ")
        destination=input("Enter the destinaton: ")
        check(source,destination)
    except Exception as e:
        print("some error")
        print(e)