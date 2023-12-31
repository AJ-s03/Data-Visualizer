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

#
def input_info(chart):
     info = {}
     #if chart == 1:
          
     pass

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
def ChartVariad(x,y,df, chart):
     info = {}
     for i in range(len(y)):
          if (chart == 1):
               print("Enter Some Additional Info About The Chart : \n")
               info = input_info(chart, y);
               plt.plot(df[x], df[y[i]])
          elif (chart == 2):
               if i == 0:
                    adj = np.arange(len(df[x]))
               else:
                    adj = adj + .15
               print("Enter Some Additional Info About The Chart : \n")
               info = input_info(chart, y);
               if i == 0:
                    plt.bar(df[x], df[y[i]], width = .15)
               else:
                    plt.bar(adj, df[y[i]], width = .15)
          elif (chart == 3):
               print("Enter Some Additional Info About The Chart : \n")
               info = input_info(chart);
               plt.scatter(df[x], df[y[i]])
          elif (chart == 4):
               print("Enter Some Additional Info About The Chart : \n")
               info = input_info(chart);
               plt.pie(df[y], labels = df[x])
               break
          elif (chart == 5):
               print0("Enter Some Additional Info About The Chart : \n")
               info = input_info(chart);
               plt.hist(df[y], bins = 20)
               break
          elif (chart == 6):
               print("Enter Some Additional Info About The Chart : \n")
               info = input_info(chart);
               plt.boxplot(df[y])
               break
     plt.show()
     return 0

#Function to import data from a CSV file.
def CSV(op):
     #Function for similar charts
     def CSVxy(chart):
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
          ChartVariad(x,y,df, chart)
          plt.show()
          return 0
          
     #Funtion for pie chart
     def CSV360(chart):
          y = []
          path = input("Enter File Path : ")
          df = pd.read_csv(path)
          print("Choose Which Column Should Represent The Slices\n")
          print(df.columns)
          slices = input(" : ")
          SearchColumn(slices, df.columns)
          #y = df.loc[0:,[y]]
          print("Choose Which Column Should Represent Labels\n")
          labels = input(" : ")
          SearchColumn(labels, df.columns)
          #x = df.loc[0:,[x]]
          ChartVariad(labels, slices,df, chart)
          plt.show()
          return 0
     
     #Funtion for histogram/box chart
     def CSVhist(chart):
          data = []
          path = input("Enter File Path : ")
          df = pd.read_csv(path)
          print(df.columns)
          times.c = int(input("How Many Columns To Summarize : "))
          #value = input("Enter The Column Which Is To Be Summarised: ")
          #data.append(value)
          #SearchColumn(data[0], df.columns)
          if times.c <= 1 and times.c > 0:
               col = input(" : ")
               SearchColumn(col, df.columns)
               y.append(col)
          else:
               y = variad(times.c, df)
          #x = df.loc[0:,[x]]
          ChartVariad(0, data, df, chart)
          plt.show()
          return 0
  
     if op == 1 or op == 2 or op == 3:
          CSVxy(op)
     elif op == 4:
          CSV360(op)
     elif op == 5:
          CSVhist(op)
     elif op == 6:
          CSVhist(op)
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
def ChartVariadII(x, y, chart):
     for i in range(len(y)):
          if (chart == 1):
               print("Enter Some Additional Info About The Chart : \n")
               info = input_info(chart);
               plt.plot(x, y[i])
          elif (chart == 2):
               if i == 0:
                    adj = np.arange(len(x))
               else:
                    adj = adj + .15
               print("Enter Some Additional Info About The Chart : \n")
               info = input_info(chart);
               plt.bar(x, y[i])
               if i == 0:
                    plt.bar(x, y[i], width = .15)
               else:
                    plt.bar(adj, y[i], width = .15)
          elif (chart == 3):
               print("Enter Some Additional Info About The Chart : \n")
               info = input_info(chart);
               plt.scatter(x, y[i])
          elif (chart == 4):
               print("Enter Some Additional Info About The Chart : \n")
               info = input_info(chart);
               plt.pie(y[i], labels = x)
               break
          elif (chart == 5):
               print("Enter Some Additional Info About The Chart : \n")
               info = input_info(chart);
               plt.hist(y, bins = 20)
               break
          elif (chart == 6):
               print("Enter Some Additional Info About The Chart : \n")
               info = input_info(chart);
               plt.boxplot(y)
               break      
     plt.show()
     return 0

#Funtion to input data manually
def manual(op):
     
     #Funtion for similar charts
     def manualxy(chart):
          try:
               times = count()
               y = []
               times.c = int(input("How Many Columns For Y-axis? :"))
               print("Enter The Number Of Values For Y-axis : ")
               limy = float(input(" : "))
               if times.c <= 1 and times.c > 0:
                    y.append(get_manual_data(limy))
               else:
                    for i in range(times.c):
                         y.append(variadII(limy))
                    
               print("Enter The Number Of Values For X-axis : ")
               limx = float(input(" : "))
               x = get_manual_data(limx)
               ChartVariadII(x, y, chart)
          
          except(ValueError):
               print("ERROR Detected Check The Following:\
                     \n*Dimensions Of Both of The axis Must Be Same.\
                     \n*Enter Correct Inputs.")
          return 0

     #Funtion for pie charts
     def manual360(chart):
          try:
               times = count()
               slices = []
               print("Enter The Number Of Values For The Slices : ")
               limy = float(input(" : "))
               slices.append(get_manual_data(limy))     
               print("Enter The Number Of Labels : ")
               limx = float(input(" : "))
               labels = get_manual_data(limx)
               ChartVariadII(labels, slices, chart)
          except(ValueError):
               print("ERROR Detected Check The Following:\
                     \n*Dimensions Of Both of The axis Must Be Same.\
                     \n*Enter Correct Inputs.")
          return 0
     
     #Function for histogram/box charts
     def manualhist(chart):
          try:
               times = count()
               data = []
               times.c = int(input("How Many Columns To Summarise :"))
               print("Enter The Total Number Of Values : ")
               limy = float(input(" : "))
               if (times.c <= 1 and times.c > 0):# or chart == 6:
                    data.append(get_manual_data(limy))
               else:
                    for i in range(times.c):
                         data.append(variadII(limy))
               ChartVariadII(0, data, chart)
          except(ValueError):
               print("ERROR Detected Check The Following:\
                     \n*Dimensions Of Both of The axis Must Be Same.\
                     \n*Enter Correct Inputs.")
          return 0
     if op == 1 or op == 2 or op == 3:
          manualxy(op)
     elif op == 4:
          manual360(op)
     elif op == 5:
          manualhist(op)
     elif op == 6:
          manualhist(op)
     return 0
     
#Funtion to get data from the database
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

#Funtion to variad arguments for charts from database
def variadIII(c,ydf):
     li = []
     for i in range(c):
          value = input()
          SearchColumn(value, ydf.columns)
          li.append(value)
     return li.copy()

#Funtion for preparnig charts.
def ChartVariadIII(x, y, xdf, ydf, chart):
     info = {}
     for i in range(len(y)):
          if (chart == 1):
               print("Enter Some Additional Info About The Chart : \n")
               info = input_info(chart);
               plt.plot(xdf[x], ydf[y[i]])
          elif (chart == 2):
               if i == 0:
                    adj = np.arange(len(xdf[x]))
               else:
                    adj = adj + .15
               print("Enter Some Additional Info About The Chart : \n")
               info = input_info(chart);
               if i == 0:
                    plt.bar(xdf[x], ydf[y[i]], width = .15)
               else:
                    plt.bar(adj, ydf[y[i]], width = .15)
          elif (chart == 3):
               print("Enter Some Additional Info About The Chart : \n")
               info = input_info(chart);
               plt.scatter(xdf[x], ydf[y[i]])
          elif (chart == 4):
               print("Enter Some Additional Info About The Chart : \n")
               info = input_info(chart);
               plt.pie(ydf[y[i]], labels = xdf[x])
               break
          elif (chart == 5):
               print("Enter Some Additional Info About The Chart : \n")
               info = input_info(chart);
               plt.hist(ydf[y], bins = 20)
               break
          elif (chart == 6):
               print("Enter Some Additional Info About The Chart : \n")
               info = input_info(chart);
               plt.boxplot(ydf[y])
               break
     plt.show()
     return 0


#Funtiion to import data from a database (MySQL)
def db(op):
     passwd = input("Enter The Password : ")
     try:
          db = input("Enter The Name Of The Database : ")
          user = input("Enter The User Name : ") 
          host = input("Enter The Hosy Name : ") 
          Dbcon = sqltor.connect(host = host, user = user, passwd = passwd ,database = db)
          if Dbcon.is_connected():
               time.sleep(2)
               print("Connection Established.")
          else:
               print("Connection Failed.")

     except(sqltor.errors.ProgrammingError):
          print("ERROR Detected Check The Following:\
                \n*Database Name.")
          return 0

     #Funtion for similar charts
     def dbxy(chart):
          times = count()
          y = []
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
          ChartVariadIII(x, y, xdf, ydf, chart)
          return 0

     #Funtion for pie charts
     def db360(chart):
          slices = []
          #For slices
          print("Input Qeury For The Values Of The Slices : \n");
          slicesdf = get_relation(Dbcon)
          print(slicesdf.columns)
          print("Choose Which Column Should Represent Y-axis: \n")
          col = input()
          SearchColumn(col, slicesdf.columns)
          slices.append(col)
               
          #For X axis
          print("\n\nInput Qeury For The Values Of The Labels : \n");
          labeldf = get_relation(Dbcon)
          print(labeldf.columns)
          label = input("Enter Col For Labels: ")
          SearchColumn(label, labeldf.columns)
          ChartVariadIII(label, slices, labeldf, slicesdf, chart)
          return 0

     #Function for histogram/box chart
     def dbhist(chart):
          times = count()
          data = []
          #For data
          times.c = int(input("How Many Columns For The Summarisation? :"))
          print("Input Qeury For The Summarisation Of The Data : \n");
          datadf = get_relation(Dbcon)
          print(datadf.columns)
          print("Choose Which Column Should Represent Y-axis: \n")
          if (times.c <= 1 and times.c > 0): #or chart == 6:
               col = input()
               SearchColumn(col, datadf.columns)
               data.append(col)         
          else:
               data = variadIII(times.c, datadf)
          ChartVariadIII(0, data, 0, datadf, chart)
          return 0
          
     if op == 1 or op == 2 or op == 3:
          dbxy(op)
     elif op == 4:
          db360(op)
     elif op == 5:
          dbhist(op)
     elif op == 6:
          dbhist(op)
     return 0

#Main
def Input_data():
     try :
          op = int(input("What Type Of Chart Would Like To Make: \n 1)Line chart \n 2)Bar chart \n 3)Scatter plot \n 4)Pie chart \n 5)Histogram chart \n 6)BoxPlot chart \n:"))
          if op < 1 or op > 6:
               raise ValueError
          print("Please Enter How Would You Like To Upload Data\n1)CSV\n2)Manual\n3)Database(MySql)\n")
          inp = int(input(":"))
          if inp == 1:
               CSV(op)
          elif inp == 2:
               manual(op)  
          elif inp == 3:
                db(op)
          else:
               print("Please Enter A Valid Choice.")
     except(ValueError):
          print("ERROR Detected Check The Following:\
                     \n*Input Values.\
                     \n*Check Dimensions.\
                     \n*Values Of Slices Must Be Integers")
Input_data()

