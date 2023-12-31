import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import mysql.connector as sqltor
import time
class count:
     c = 0
'''
def listextend(df):
     list = []
     for i in df'''


#Funtion to check validity of entered column
def SearchColumn(col, cols):
     if col not in cols:
          print("Error: Data Does Not Contain Specified Column")
     return 0


#Funtion for accepting variable columns
def variad(c, df):
     li = []
     print("Enter Columns\Values Serial Wise: ")
     for i in range(c):
          col = input()
          SearchColumn(col, df.columns)
          li.append(col)
     return li.copy()

#Funtion to plot variable columns
def ChartVariad(x,y,df, graph):
     for i in range(len(y)):
          if (graph == 1):
               plt.plot(df[x], df[y[i]])
     plt.show()
     return 0

#Function to import data from a CSV file.
def CSV():
     times = count()
     y = []
     path = input("Enter File Path : ")
     df = pd.read_csv(path)
     times.c = int(input("How Many Columns For Y-axis? : "))
     print("Choose Which Column Should Represent Y-axis\n")
     print(df.columns)
     if times.c <= 1 and times.c > 0:
          col = input(" : ")
          SearchColumn(col, df.columns)
          y.append(col)
     else:
          y = variad(times.c, df)
     #y = df.loc[0:,[y]]
     print("Choose Which Column Should Represent X-axis\n")
     x = input(" : ")
     SearchColumn(x, df.columns)
     #x = df.loc[0:,[x]]
     if times.c <= 1 and times.c > 0:
          plt.plot(df[x], df[y[i]])
     else:
          plotvariad(x,y,df)
     plt.show()
     return 0

#Function to get manual input limit.
def get_manual_data(lim):
     li = []
     ch = 0
     print("Enter The Values\nNumerical(1)\Character or String (0) : ")
     ch = int(input())
     if ch == 1:
          for i in range(int(lim)):
               value = eval(input())
               li.append(value)
          return li
     elif ch == 0:
          for i in range(int(lim)):
               value = input()
               li.append(value)
          return li
#
def variadII(c):
     li = []
     print("Enter Columns\Values Serial Wise: ")
     for i in range(int(c)):
          col = int(input())
          li.append(col)
     return li.copy()
#
def ChartVariadII(x,y):
     for i in range(len(y)):
          plt.plot(x, y[i])
     plt.show()
     return 0

#Funtion to input data manually
def manual():
     try:
          times = count()
          y = []
          times.c = int(input("How Many Columns For Y-axis? :"))
          print("Enter The Number Of Values For Y-axis : ")
          limy = float(input(" : "))
          if times.c <= 1 and times.c > 0:
               y.extend(get_manual_data(limy))
          else:
               for i in range(times.c):
                    y.append(variadII(limy))
                    
          print("Enter The Number Of Values For X-axis : ")
          limx = float(input(" : "))
          x = get_manual_data(limx)
          if times.c <= 1 and times.c > 0:
               plt.plot(x,y)
               plt.show()
          else:
               plotvariadII(x,y)
          
     except(ValueError):
          print("ERROR Detected Check The Following:\
                \n*Dimensions Of Both of The axis Must Be Same.\
                \n*Enter Correct Inputs.")
          return 0
     return 0
#
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
#
def variadIII(c,ydf):
     li = []
     for i in range(c):
          value = input()
          SearchColumn(value, ydf.columns)
          li.append(value)
     return li.copy()

#
def ChartVariadIII(x, y, xdf, ydf):
     for i in range(len(y)):
          plt.plot(xdf[x], ydf[y[i]])
     plt.show()
     return 0

#Funtiion to import data from a database (MySQL)
def db():
     times = count()
     y = []
     passwd = input("Enter The Password : ")
     try:
          db = input("Enter The Name Of The Database : ")
          user = input("Enter The User Name : ")
          Dbcon = sqltor.connect(host = "localhost", user = user, passwd =  passwd,database = db)
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
     times.c = int(input("How Many Columns For Y-axis? :"))
     print("Choose Which Column Should Represent Y-axis: \n")
     if times.c <= 1 and times.c > 0:
          col = input()
          SearchColumn(col, ydf.columns)
          y.append(col)
     else:
          y = variadIII(times.c, ydf)
          
     
     #For X axis
     print("\n\nInput Qeury For The Values Of X-axis : \n");
     xdf = get_relation(Dbcon)
     print(xdf.columns)
     x = input("Enter Col For X-axis: ")
     SearchColumn(x, xdf.columns)
     if times.c <= 1 and times.c > 0:
          plt.plot(xdf[x], ydf[y[0]])
          plt.show()
     else:
          ChartvariadIII(x, y, xdf, ydf)
     return 0

#Main
def Input_data():
     print("Please Enter How Would You Like To Upload Data\n1)CSV\n2)Manual\n3)Database(MySql)\n")
     try :
          inp = int(input(":"))
          if inp == 1:
               CSV()
          elif inp == 2:
               manual()  
          elif inp == 3:
                db()     
          else:
               print("Please Enter A Valid Choice.")
     except(ValueError):
          print("ERROR Detected Check The Following:\
                     \n*Input Value.\
                     \n*Check Dimensions.")

