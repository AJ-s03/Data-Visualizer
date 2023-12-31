import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Funtion for repetitive string inputs
def rep_string(c):
     info = {}
     info["temp"]=[]
     for i in range(len(c)):
          print(i + 1," : ")
          info["temp"].append(input())
     return info["temp"].copy()

#Funtion for repetitive number inputs
def rep_number(c):
     info = {}
     info["temp"]=[]
     for i in range(len(c)):
          print(i + 1," : ")
          info["temp"].append(float(input()))s
     return info["temp"].copy()          

def input_info(chart, c):
     info = {}
     #For line chart
     if chart == 1:
          print("\n Enter color\nFor line")
          info["clr"] = rep_string(c)
          print("\n Enter linewidth\nFor line")
          info["lnwidth"] = rep_number(c)
          print("\n Enter line style\nFor line")
          info["lnstyle"] = rep_string(c)
          print("\n Enter marker style\nFor line")
          info["mkr"] = rep_string(c)
          print("\n Enter marker size\nFor line")
          info["mkrsize"] = rep_number(c)
          print("\n Enter marker edge color\nFor line")
          info["mkredgecolor"] = rep_string(c)

     #For bar chart    
     elif chart == 2:
          print("\n Enter width\nFor bar")
          info["width"] = rep_number(c)
          print("\n Enter color\nFor bar")
          info["clr"] = rep_string(c)

     #For scatter chart     
     elif chart == 3:
          print("\n Enter color\nFor line")
          info["clr"] = rep_string(c)
          print("\n Enter marker style\nFor line")
          info["mkr"] = rep_string(c)
          print("\n Enter marker size\nFor line")
          info["mkrsize"] = rep_number(c)

     #For pie chart
     elif chart == 4:
          info["autopct"] = input("\Formatted slice percentage (True -> 1/ False -> 0) : ")
          print("\nEnter color\nFor slice")
          info["clr"] = rep_string(c)
          ch = input("Exploding slices? (True -> 1/ False -> 0) : ")     
          if ch == 1:
               print("\nEnter units\nFor slice")
               info["xplode"] = rep_number(c)
          return info

     #For histogram chart
     elif chart == 5:
          info["bins"] = int(input("\Enter bins : "))
          info["cum"] = int(input("\nCumulative (True -> 1/ False -> 0) : "))
          info["type"] = input("Enter Hist Type : ")
          info["orientation"] = input("Vertical or horizontal : ")
          return info

     #For box chart
     elif chart == 6:
          info["notch"] = int(input("Notched Box (True -> 1/ False -> 0) : "))
          info["vert"] = int(input("Vertical ? (True -> 1/ False -> 0) : "))
          info["fill"] = int(input("Fill the box ? (True -> 1/ False -> 0) : "))
          print("\nEnter label\nFor box")
          info["label"] = rep_string(c)
          info["means"] = int(input("Show mean ? (True -> 1/ False -> 0) : "))
           if info["means"] == 1:
                    info["meanlne"] = int(input("Meanline ? (True -> 1/ False -> 0) : "))
          return info
     
     #Common types for similar charts
     info["xlabel"] = input("\nEnter the label of x-axis : ")
     info["ylabel"] = input("\nEnter the label of y-axis : ")
     info["fig_x"] = int(input("\nEnter the number of units of x : "))
     info["fig_y"] = int(input("\nEnter the number of units of y : "))
     info["grid"] = int(input("\nGrid requirement (True -> 1/ False -> 0) : "))
     return info

input_info(1,[1,2])
