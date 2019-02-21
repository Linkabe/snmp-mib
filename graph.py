from matplotlib import pyplot as plt
import matplotlib.animation as animation
import time
import os

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)


def nohup():

    os.popen("python C:/Users/niall/Documents/College/NetworkManagment/SNMP-App/savetograph1.pyw")


def animate(i):
    # global i
    # print("test1")
    pullData = open("./Graphstest1.txt", "r").read()
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
    print("Time in seconds", i)
    i = i + 1

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
