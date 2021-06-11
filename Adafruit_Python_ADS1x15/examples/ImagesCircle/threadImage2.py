import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk as NavigationToolbar2TkAgg
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import multiprocessing
import time
import random
from tkinter import *

#Create a window
root=Tk()

root.wm_title("minimal example")

root.image = plt.imread('proverbs.jpg')
fig = plt.figure(figsize=(5,4))
im = plt.imshow(root.image) # later use a.set_data(new_data)
ax = plt.gca()
ax.set_xticklabels([]) 
ax.set_yticklabels([])

# a tk.DrawingArea
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)


def rotate(*args):
    print ('rotate button press...')
    root.image = ndimage.rotate(root.image, 90)
    im.set_data(root.image)
    canvas.draw()


def main():

    print('hola')
    root.mainloop()
    print ('Done')


if __name__ == '__main__':
    main()