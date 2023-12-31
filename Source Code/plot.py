import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

op = 0;

x = ["A", "B", "C", "D", "E"]
y = [989.34, 878, 34, 909.98, 400]
y2 = [1000, 900, 4, 900, 400]
op = int(input("Enter the choice: \n 1)Line chart \n 2)Bar chart \n 3)Scatter plot \n 4)Pie chart \n 5)Histogram chart \n 6)BoxPlot chart \n:"))
xlabel = input("\nEnter the label of x-axis : ")
ylabel = input("\nEnter the label of y-axis : ")
fig_x = int(input("\nEnter the number of units of x : "))
fig_y = int(input("\nEnter the number of units of y : "))
grid = int(input("\nGrid requirement (True -> 1/ False -> 0) : "))
clr = input("\nEnter the color of line : ")
lnwidth = int(input("\nEnter linewidth : "))
lnstyle = input("\nEnter linestyle : ")
mkr = input("\nEnter the marker style : ")
mkrsize = int(input("\nEnter the marker size : "))
mkredgecolor = input("\nEnter the marker egde color : ")
if op == 1:
     plt.figure(figsize = (fig_x, fig_y))
     plt.grid(grid)
     plt.xlabel(xlabel)
     plt.ylabel(ylabel)
     plt.plot(x, y, clr, linewidth = lnwidth, marker = mkr , markeredgecolor = mkredgecolor, markersize = mkrsize)
     plt.plot(x, y2, linestyle = lnstyle, marker = mkr , markeredgecolor = mkredgecolor, markersize = mkrsize)
elif op == 2:
     plt.figure(figsize = (fig_x, fig_y))
     plt.grid(grid)
     plt.xlabel(xlabel)
     plt.ylabel(ylabel)
     plt.bar(x,y)
plt.show()
