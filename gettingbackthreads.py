import os
from tkinter import scrolledtext, ttk
from tkinter import *
from random import *
from datetime import datetime
from pandas import DataFrame
import matplotlib.animation as animation
import time
import threading
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np

DNow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

i=0



def save_to_graph():
    while True:
        global i
        rad= randint(20, 40)
        rad=str(rad)
        print (rad)
        f = open(".Graphs.txt", "a")
        i=str(i)
        f.write(i)
        f.write(",")
        f.write(rad)
        f.write("\n")
        print(i)
        i=int(i)
        i=i+1
        f.close()
        time.sleep(1)

def animate(i):
    save_to_graph()
    pullData = open("Graphs.txt", "r").read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    for eachLine in dataArray:
        if len(eachLine) > 1:
            x, y = eachLine.split(',')
            xar.append(int(x))
            yar.append(int(y))
    ax1.clear()
    ax1.plot(xar, yar)





window = Tk()
window.title("Network Management TNP")
window.geometry('800x400')
Label(window, text="SNMP Graphs.txt", font=("Arial Bold", 25)).place(relx=0.5, rely=0.13, anchor=CENTER)
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()




btnCPUTemp = Button(window, text="CPU Temp", font=("Arial", 12), bg="Green", fg="black", command=animate)
btnCPUTemp.place(x=550, y=280, anchor=CENTER)



window.mainloop()
