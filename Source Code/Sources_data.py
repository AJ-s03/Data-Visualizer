import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import mysql.connector as sqltor
import time
class count:
     count = 0
'''
def listextend(df):
     list = []
     for i in df'''


#Funtion to check validity of entered column
def SearchColumn(col, cols):
     if col not in cols:
          print("Error: Data Does Not Contain Specified Column")
     return 0

#Function to get manual input limit.
def get_manual_data(lim):
     li = []
     print("Enter The Values : ")
     for i in range(int(lim)):
          value = float(input())
          li.extend([value])
     return li

#Function to import data from a CSV file.
def getfile():
     path = input("Enter File Path : ")
     df = pd.read_csv(path)
     print("Choose Which Column Should Represent Y-axis\n")
     print(df.columns)
     y = input(" : ")
     SearchColumn(y, df.columns)
     #y = df.loc[0:,[y]]
     print("Choose Which Column Should Represent X-axis\n")
     x = input(" : ")
     SearchColumn(x, df.columns)
     #x = df.loc[0:,[x]]
     plt.plot(df[x], df[y]) 
     plt.show()
     return 0

#Funtion to input data manually
def manual():
     try:
          print("Enter The Number Of Values For Y-axis : ")
          limy = float(input(" : "))
          print("Enter The Number Of Values For X-axis : ")
          limx = float(input(" : "))
          y = get_manual_data(limy)
          x = get_manual_data(limx)
          plt.plot(x,y)
          plt.show()
     except(ValueError):
          print("ERROR Detected Check The Following:\
                \n*Dimensions Of Both of The axis Must Be Same.\
                \n*Enter Correct Inputs.")
          return 0
     return 0

def get_relation(Dbcon):
     fix = input("Input All The Data From Only A Table?(Y/N): ")
     if fix == 'Y':
          table = input("Input Table: ")
          query = "Select * From " + table
          df = pd.read_sql(query,Dbcon)
     else:
          print("Input Desired Qeury: ")
          query = input()
          df = pd.read_sql(query,Dbcon)
     return df

#Funtiion to import data from a database (MySQL)
def db():
     passwd = input("Enter The Password : ")
     user = input("Enter Yout User Name : ")
     try:
          db = input("Enter The Name Of The Database : ")
          Dbcon = sqltor.connect(host = "localhost", user = user, passwd = passwd ,database = db)
          if Dbcon.is_connected():
               time.sleep(2)
               print("Connection Established.")
          else:
               print("Connection Failed.")

     except(sqltor.errors.ProgrammingError):
          print("ERROR Detected Check The Following:\
                \n*Database Name.")
          return 0
     #For Y axis
     print("Input Qeury For The Values Of Y-axis : \n");
     ydf = get_relation(Dbcon)
     print(ydf.columns)
     y = input("Enter Col For Y-axis: ")
     SearchColumn(y, ydf.columns)

     #For X axis
     print("\n\nInput Qeury For The Values Of X-axis : \n");
     xdf = get_relation(Dbcon)
     print(xdf.columns)
     x = input("Enter Col For X-axis: ")
     SearchColumn(x, xdf.columns)

     plt.plot(xdf[x], ydf[y])
     plt.show()
     return 0


print("Please Enter How Would You Like To Upload Data\n1)CSV\n2)Manual\n3)Database(MySql)\n")
try :
     inp = int(input(":"))
     if inp == 1:
          getfile()
     elif inp == 2:
          manual()  
     elif inp == 3:
           db()     
     else:
          print("Please Enter A Valid Choice.")
except(ValueError):
     print("ERROR Detected Check The Following:\
                \n*Input Value.")

