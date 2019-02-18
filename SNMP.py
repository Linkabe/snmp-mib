import os
from tkinter import scrolledtext, ttk
from tkinter import *
from datetime import datetime


def raise_frame(frame):
    frame.tkraise()


window = Tk()
window.title("Network Management TNP")
window.geometry('800x400')

f6 = Frame(window)
f7 = Frame(window)

DNow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

for frame in (f6, f7):
    frame.place(width=800, height=400)


def sysUp():
    f = os.popen('snmpget -c public -v 1 localhost .1.3.6.1.2.1.1.3.0')
    for line in f:
        line = line.strip()
        if line:
            txt6.insert("end", line + "\n")
        txt6.bind("<Return>", sysUp)
    f.close()


def sysDesc():
    f = os.popen('snmpget -c public -v 1 localhost .1.3.6.1.2.1.1.1.0')
    for line in f:
        line = line.strip()
        if line:
            txt6.insert("end", line + "\n")
        txt6.bind("<Return>", sysDesc)
    f.close()


def sysContact():
    f = os.popen('snmpget -c public -v 1 localhost .1.3.6.1.2.1.1.4.0')
    for line in f:
        line = line.strip()
        if line:
            txt6.insert("end", line + "\n")
        txt6.bind("<Return>", sysContact)
    f.close()

def sysName():
    f = os.popen('snmpget -c public -v 1 localhost .1.3.6.1.2.1.1.5.0')
    for line in f:
        line = line.strip()
        if line:
            txt6.insert("end", line + "\n")
        txt6.bind("<Return>", sysName)
    f.close()


def sysBulk():
    f = os.popen('snmpbulkget -c public -v 2c localhost .1.3.6.1.2.1.1.0')
    for line in f:
        line = line.strip()
        if line:
            txt6.insert("end", line + "\n")
        txt6.bind("<Return>", sysBulk)
    f.close()

def sysCPU():
    f = os.popen('snmpwalk -v 2c -c public localhost .1.3.6.1.2.1.25.3.3.1.2')
    for line in f:
        line = line.strip()
        if line:
            txt6.insert("end", line + "\n")
        txt6.bind("<Return>", sysCPU)
    f.close()

def sysCPUSuse():
    f = os.popen('snmpbulkget -v2c -cpublic localhost .1.3.6.1.2.1.25.5.1.1.1')
    for line in f:
        line = line.strip()
        if line:
            txt6.insert("end", line + "\n")
        txt6.bind("<Return>", sysCPUSuse)
    f.close()

def sysRAM():
    f = os.popen('snmpget -v 2c -c public localhost .1.3.6.1.2.1.25.2.2.0')
    for line in f:
        line = line.strip()
        if line:
            txt6.insert("end", line + "\n")
        txt6.bind("<Return>", sysRAM)
    f.close()

def sysRAMuse():
    f = os.popen('snmpwalk -v1 -cpublic localhost 1.3.6.1.2.1.25.2.3.1.4')
    for line in f:
        line = line.strip()
        if line:
            txt6.insert("end", line + "\n")
        txt6.bind("<Return>", sysRAMuse)
    f.close()

def sysStore():
    f = os.popen('snmpwalk -v1 -cpublic localhost 1.3.6.1.2.1.25.2.3.1.5')
    for line in f:
        line = line.strip()
        if line:
            txt6.insert("end", line + "\n")
        txt6.bind("<Return>", sysStore)
    f.close()

def sysStoreUs():
    f = os.popen('snmpwalk -v1 -cpublic localhost 1.3.6.1.2.1.25.2.3.1.5')
    for line in f:
        line = line.strip()
        if line:
            txt6.insert("end", line + "\n")
        txt6.bind("<Return>", sysStoreUs)
    f.close()

def sysStoreBulk():
    f = os.popen('snmpbulkget -v2c -cpublic localhost 1.3.6.1.2.1.25.2.3.1.4')
    for line in f:
        line = line.strip()
        if line:
            txt6.insert("end", line + "\n")
        txt6.bind("<Return>", sysStoreBulk)
    f.close()

def btnhelp():
    f = open('./Help.txt', 'r')
    for line in f:
        line = line.strip()
        if line:
            txt7.insert("end", line + "\n")
        txt7.bind("<Return>", sysStoreBulk)
    f.close()
    txt7.insert(INSERT, "Your help options Have been printed to the console!!")


def snmpget():
    snmpAgent = e1A.get()
    snmpVersion = e3V.get()
    snmpOp = e4Op.get()
    snmpName = e1N.get()
    snmpOID = e5OID.get()
    f = os.popen('snmpget -v' + snmpVersion + ' -' + snmpOp + ' ' + snmpName + ' ' + snmpAgent + ' ' + snmpOID)
    for line in f:
        line = line.strip()
        if line:
            txt7.insert("end", line + "\n")
        txt7.bind("<Return>", snmpgetbulk)
    f.close()

def snmpwalk():
    snmpAgent = e1A.get()
    snmpVersion = e3V.get()
    snmpOp = e4Op.get()
    snmpName = e1N.get()
    snmpOID = e5OID.get()
    f = os.popen('snmpwalk -v' + snmpVersion + ' -' + snmpOp + ' ' + snmpName + ' ' + snmpAgent + ' ' + snmpOID)
    for line in f:
        line = line.strip()
        if line:
            txt7.insert("end", line + "\n")
        txt7.bind("<Return>", snmpgetbulk)
    f.close()

def snmpgetbulk():
    snmpAgent = e1A.get()
    snmpVersion = e3V.get()
    snmpOp = e4Op.get()
    snmpName = e1N.get()
    snmpOID = e5OID.get()
    f = os.popen('snmpbulkget -v'+snmpVersion+' -'+snmpOp+' '+snmpName+' '+snmpAgent+' '+snmpOID)
    for line in f:
        line = line.strip()
        if line:
            txt7.insert("end", line + "\n")
        txt7.bind("<Return>", snmpgetbulk)
    f.close()


def clearbtn():
    txt6.delete(1.0, END)
    txt7.delete(1.0, END)


def printdiag():
    Diag = txt6.get("1.0", "end-1c")
    f = open("./MIB-Printout.txt", "w+")
    f.write("Print Out of Your Information in: " + DNow + "\n" + "\n" + Diag)
    f.close()
    clearbtn()
    txt6.insert(INSERT, "Your Network Information has been Writen" + "\n" + "  MIB-Printout.txt" + "\n" + "Located: ./MIB-Printout.txt")


txt6 = scrolledtext.ScrolledText(f6, width=85, height=10)
txt6.place(x=60, y=80)
Button(f6, text='SNMP System Requests', font=("Arial Bold", 10), command=lambda:raise_frame(f6)).place(x=10, y=2)
Button(f6, text='SNPM MIB Browser', font=("Arial", 10), command=lambda:raise_frame(f7)).place(x=175, y=2)
Label(f6, text="SNMP System Requests", font=("Arial Bold", 25)).place(relx=0.5, rely=0.13, anchor=CENTER)
btnPrint = Button(f6, text="Print", font=("Arial", 14), bg="Blue", fg="black", command=printdiag)
btnPrint.place(x=100, y=57, anchor=CENTER)
btnDesc = Button(f6, text="System Description", font=("Arial", 12), bg="Green", fg="black", command=sysDesc)
btnDesc.place(x=150, y=280, anchor=CENTER)
btnDesc = Button(f6, text="Get Bulk System", font=("Arial", 12), bg="Green", fg="black", command=sysBulk)
btnDesc.place(x=150, y=325, anchor=CENTER)
btnSBulk = Button(f6, text="Get Bulk Storage", font=("Arial", 12), bg="Green", fg="black", command=sysStoreBulk)
btnSBulk.place(x=150, y=365, anchor=CENTER)

btnContact = Button(f6, text="System Contact", font=("Arial", 12), bg="Green", fg="black", command=sysContact)
btnContact.place(x=300, y=280, anchor=CENTER)
btnDesc = Button(f6, text="CPU Temp", font=("Arial", 12), bg="Green", fg="black", command=sysCPU)
btnDesc.place(x=300, y=365, anchor=CENTER)
btnDesc = Button(f6, text="CPU Speed & Use", font=("Arial", 12), bg="Green", fg="black", command=sysCPUSuse)
btnDesc.place(x=300, y=325, anchor=CENTER)

btnName = Button(f6, text="System Name", font=("Arial", 12), bg="Green", fg="black", command=sysName)
btnName.place(x=435, y=280, anchor=CENTER)
btnRAM = Button(f6, text="RAM Size", font=("Arial", 12), bg="Green", fg="black", command=sysRAM)
btnRAM.place(x=435, y=325, anchor=CENTER)
btnRAMUS = Button(f6, text="RAM Use", font=("Arial", 12), bg="Green", fg="black", command=sysRAMuse)
btnRAMUS.place(x=435, y=365, anchor=CENTER)

btnUptime = Button(f6, text="System Uptime", font=("Arial", 12), bg="Green", fg="black", command=sysUp)
btnUptime.place(x=570, y=280, anchor=CENTER)
btnStore = Button(f6, text="Storage Size", font=("Arial", 12), bg="Green", fg="black", command=sysStore)
btnStore.place(x=570, y=325, anchor=CENTER)
btnStoreUs = Button(f6, text="Storage Used", font=("Arial", 12), bg="Green", fg="black", command=sysStoreUs)
btnStoreUs.place(x=570, y=365, anchor=CENTER)

btnClear = Button(f6, text="Clear", font=("Arial Bold", 12), bg="Red", fg="black", command=clearbtn)
btnClear.place(x=725, y=280, anchor=CENTER)


txt7 = scrolledtext.ScrolledText(f7, width=85, height=10)
txt7.place(x=60, y=80)
btnPrint = Button(f7, text="Print", font=("Arial", 14), bg="Blue", fg="black", command=printdiag)
btnPrint.place(x=100, y=57, anchor=CENTER)
Button(f7, text='SNMP System Requests', font=("Arial", 10), command=lambda:raise_frame(f6)).place(x=10, y=2)
Button(f7, text='SNMP MIB Browser', font=("Arial Bold", 10), command=lambda:raise_frame(f7)).place(x=175, y=2)
Label(f7, text="SNMP MIB Browser", font=("Arial Bold", 25)).place(relx=0.5, rely=0.13, anchor=CENTER)

btnGet = Button(f7, text="SNMP  Get", font=("Arial", 12), bg="Green", fg="black", command=snmpget)
btnGet.place(x=390, y=320, anchor=CENTER)

btnWalk = Button(f7, text="SNMP Walk", font=("Arial", 12), bg="Green", fg="black", command=snmpwalk)
btnWalk.place(x=500, y=320, anchor=CENTER)

btnBulk = Button(f7, text="SNMP Bulk Get", font=("Arial", 12), bg="Green", fg="black", command=snmpgetbulk)
btnBulk.place(x=440, y=360, anchor=CENTER)

btnHelp = Button(f7, text="Help", font=("Arial Bold", 14), bg="Red", fg="black", command=btnhelp)
btnHelp.place(x=720, y=300, anchor=CENTER)
btnClear = Button(f7, text="Clear", font=("Arial Bold", 14), bg="Red", fg="black", command=clearbtn)
btnClear.place(x=720, y=360, anchor=CENTER)


Label(f7, text="Configuration", font=("Arial Bold", 9)).place(x=80, y=250)
#'snmpwalk -v'+e3V+' -'+e4Op+' '+e1N+' '+e1A+' '+e5O
Label(f7, text="Profile Name:", font=("Arial", 8)).place(x=90, y=270)
e1N = Entry(f7, width=10)
e1N.insert(0, 'public')
e1N.place(x=170, y=270)

Label(f7, text="Agent Address or Name:", font=("Arial", 8)).place(x=40, y=360)
e1A = Entry(f7, width=10)
e1A.insert(0, 'localhost')
e1A.place(x=170, y=360)

Label(f7, text="Options:", font=("Arial", 8)).place(x=90, y=330)
e4Op = Entry(f7, width=10)
e4Op.insert(0, 'c')
e4Op.place(x=170, y=330)

Label(f7, text="Version [1/2c/3]:", font=("Arial", 8)).place(x=70, y=300)
e3V = Entry(f7, width=10)
e3V.insert(0, '2c')
e3V.place(x=170, y=300)

Label(f7, text="Enter Your OID:", font=("Arial Bold", 12)).place(x=370, y=250)
e5OID = Entry(f7, width=40)
e5OID.insert(0, '')
e5OID.place(x=320, y=275)

raise_frame(f6)
window.mainloop()
