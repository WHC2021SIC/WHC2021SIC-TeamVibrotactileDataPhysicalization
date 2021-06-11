import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk as NavigationToolbar2TkAgg
import multiprocessing
import time
import random
from tkinter import *


#Create a window
window=Tk()

def simulation(q):
    iterations = range(100)
    for i in iterations:
        if not i % 10:
            time.sleep(1)
                #here send any data you want to send to the other process, can be any pickable object
            q.put(random.randint(1,10))
    q.put('Q')


def plot():    #Function to create the base plot, make sure to make global the lines, axes, canvas and any part that you would want to update later
    global line,ax,canvas
    fig = matplotlib.figure.Figure()
    fig.canvas.callbacks.connect('button_press_event', on_click)
    ax = fig.add_subplot()
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)
    line, = ax.plot([1,2,3], [1,2,10])


def on_click(event):
    if event.inaxes is not None:
        print ("x:{},y:{}".format(event.x, event.y))
    else:
        print ('Clicked ouside axes bounds but inside plot window')


def updateplot(q):
    try:       #Try to check if there is data in the queue
        result=q.get_nowait()

        if result !='Q':
             print ("R: {}".format(result))
                 #here get crazy with the plotting, you have access to all the global variables that you defined in the plot function, and have the data that the simulation sent.
             line.set_ydata([1,result,10])
             ax.draw_artist(line)
             canvas.draw()
             window.after(500,updateplot,q)
        else:
             print ('doneN')
    except:
        print ("emptyN")
        window.after(500,updateplot,q)

def main():
    #Create a queue to share data between process
    q = multiprocessing.Queue()

    #Create and start the simulation process
    simulate=multiprocessing.Process(None,simulation,args=(q,))
    simulate.start()

    #Create the base plot
    plot()

    #Call a function to update the plot when there is new data
    updateplot(q)
    print('hola')
    window.mainloop()
    print ('Done')



if __name__ == '__main__':
    main()