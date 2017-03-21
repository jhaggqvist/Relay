from Tkinter import *
import os

root = Tk()


def date():
    f = os.popen('date')
    now = f.read()
    print "the date is: ", now   


def uptime():
    a = os.popen('uptime')
    now = a.read()
    print "the uptime is: ", now
    
def ifconfig():
    b = os.popen('ifconfig')
    now = b.read()
    print "ifconfig return: ", now
    
button_1 = Button(root, text="see the date", command=date)
button_2 = Button(root, text="See the uptime", command=uptime)
button_3=Button(root, text="See ifconfig return", command=ifconfig)
button_1.pack()
button_2.pack()
button_3.pack()


root.mainloop()
