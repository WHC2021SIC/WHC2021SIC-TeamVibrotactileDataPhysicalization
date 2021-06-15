#Import the library
from tkinter import *

#Create an instance of tkinter frame
win= Tk()

#Define the geometry of window
win.geometry("600x400")

#Create a canvas object
c= Canvas(win)
c.pack()

#Draw an Oval in the canvas
c.create_oval(60,60,210,210,fill="blue")

win.mainloop()