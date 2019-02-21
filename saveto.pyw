from datetime import datetime
from random import *
import time
i=0



def save_to_graph():
    while True:
        global i
        rad= randint(20, 40)
        rad=str(rad)
        print (rad)
        f = open("./Graphs.txt", "a")
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


save_to_graph()


