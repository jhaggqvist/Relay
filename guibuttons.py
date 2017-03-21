from Tkinter import *

root = Tk() #window?

topFrame = Frame(root) #creates a frame that will be used to add to the top of gui
topFrame.pack() #Shows frame
bottomFrame = Frame(root) #crates a frame that will be used to add to the bottom of gui
bottomFrame.pack(side=BOTTOM) #shows the frame

button1 = Button(topFrame, text="Button 1", fg="red") #Creates 4 buttoms (whichframe, name, textColor)
button2 = Button(topFrame, text="Button 2", fg="blue")
button3 = Button(topFrame, text="Button 3", fg="green")
button4 = Button(bottomFrame, text="button 4", fg="purple")



button1.pack(side=LEFT) #shows buttons and where to place them.
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)


root.mainloop() #to keep the window from closing. 
