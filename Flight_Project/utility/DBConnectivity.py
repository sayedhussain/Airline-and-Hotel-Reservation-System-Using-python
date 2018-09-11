'''
Created on Jul 29, 2015

@author: Deepak_M05
'''
import cx_Oracle
def create_connection():
    return cx_Oracle.Connection('t714077/t714077@10.123.79.60/georli05')

def create_cursor(con):
    return cx_Oracle.Cursor(con)

