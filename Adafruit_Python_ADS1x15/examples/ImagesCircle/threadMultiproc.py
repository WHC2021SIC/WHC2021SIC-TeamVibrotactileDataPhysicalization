import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk as NavigationToolbar2TkAgg
import multiprocessing
import time
import random
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
from matplotlib.collections import PatchCollection
from matplotlib.animation import FuncAnimation

#Create a window
root=Tk()

root.wm_title("WHC 2021")
root.geometry("450x350")

'''#Create a canvas object
c= Canvas(root)
c.grid(columnspan=2, rowspan=2)

#Draw an Oval in the canvas
c.create_oval(60,60,210,210,fill="blue")'''

image = plt.imread('sudamericaLowRes.png') #root.image
image2 = plt.imread('Actuators.png')

clickOn=False

Heigth=15.0
Length=15.0
radius=1.5

HRelation=Heigth/image.shape[0]
LRelation=Length/image.shape[1]

HRelationAct=1.0/image2.shape[0]
LRelationAct=1.0/image2.shape[1]

xMin=0.4773
yMin=0.4093

def simulation(q):
    global patches
    iterations = range(100)
    for i in iterations:
        if not i % 10:
            time.sleep(1)
            colors = 100*np.random.rand(8) # random index to color map            
                #here send any data you want to send to the other process, can be any pickable object
            q.put(colors)
            print("sim")
    q.put('Q')

def on_click(event):
    #print('click')
    global clickOn, circ
    if event.inaxes is not None:
        #print(clickOn)
        clickOn=True
        Hreal=event.xdata*HRelationAct
        Lreal=event.ydata*LRelationAct
        #radPix=radius*(1/LRelationAct)
        
        #print ("x:{},y:{}".format(event.x, event.y))        
        
        print ("x:{},y:{}".format(event.xdata + xMin, event.ydata+ yMin))
        #print ("radius:{}".format(radPix))
        print ("x:{},y:{}".format(Hreal, Lreal))
        print (image[int(event.ydata+yMin), int(event.xdata+xMin),:])
        


        '''circ = Circle((int(event.xdata), int(event.ydata)),radPix)1
        ax.add_patch(circ)
        canvas.draw()'''

def off_click(event):
    global clickOn, circ
    clickOn=False
    '''circ.remove()
    canvas.draw()'''

def on_move(event):
    if event.inaxes is not None:
        #print(clickOn)
        if clickOn==True:
            Hreal=event.xdata*HRelation
            Lreal=event.ydata*LRelation
            print ("x:{},y:{}".format(event.x, event.y))
            print ("x:{},y:{}".format(event.xdata, event.ydata))
            print ("x:{},y:{}".format(Hreal, Lreal))
            print (image[int(event.ydata), int(event.xdata),:])
            #print (im.cmap(im.norm(root.image[int(event.ydata), int(event.xdata)])))
    '''else:
        print ('Clicked ouside axes bounds but inside plot window')'''

def animate(i):
    global fig
    colors = 100*np.random.rand(8) # random index to color map     
    p.set_array(colors)
    

def plot():    #Function to create the base plot, make sure to make global the lines, axes, canvas and any part that you would want to update later
    global line,ax,canvas, patches, p, fig

    '''fig = plt.figure()
    #fig = matplotlib.figure.Figure()
    #binding_id = plt.connect('motion_notify_event', on_move)
    #fig.add_subplot(1, 2, 1)
    plt.imshow(image2)

    ax2=plt.gca()

    patches = []
    # Now, loop through coord arrays, and create a circle at each x,y pair
    for xx,yy,r in Actuat:    
        #print("x: {}, y: {},r: {}".format(xx,yy,r))
        circC = Circle((xx*(1/HRelationAct),yy*(1/LRelationAct)),r)
        patches.append(circC)
    ani = FuncAnimation(fig, animate, interval=1000)

    # add these circles to a collection
    p = PatchCollection(patches, facecolors='r', alpha=0.4)
    ax2.add_collection(p)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=1, column=0)
    #canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)'''
        
    #fig.add_subplot(1, 2, 2)
    fig2 = plt.figure()    
    fig2.canvas.callbacks.connect('button_press_event', on_click)
    fig2.canvas.callbacks.connect('motion_notify_event', on_move)
    fig2.canvas.callbacks.connect('button_release_event', off_click)

    global im
    im = plt.imshow(image) # later use a.set_data(new_data) image2
    
    canvas2 = FigureCanvasTkAgg(fig2, master=root)
    canvas2.draw()
    #canvas2.get_tk_widget().grid(row=1, column=1)
    canvas2.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    canvas2._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)

def updateplot(q):
    try:       #Try to check if there is data in the queue
        result=q.get_nowait()
        global line,ax,canvas
        if result !='Q':
             print ("R: {}".format(result))
                 #here get crazy with the plotting, you have access to all the global variables that you defined in the plot function, and have the data that the simulation sent.
             p.set_array(result)
             #canvas.draw()
             root.after(500,updateplot,q)
        else:
             print ('doneN')
    except:
        print ("emptyN")
        root.after(500,updateplot,q)

def main():
    #Create a queue to share data between process
    q = multiprocessing.Queue()

    #Create and start the simulation process
    simulate=multiprocessing.Process(target=simulation,args=(q,))
    simulate.start()

    radi=90
    Act0=[0.265,0.41,radi]
    Act1=[0.295,0.64,radi]
    Act2=[0.395,0.34,radi]
    Act3=[0.395,0.61,radi]
    Act4=[0.52,0.39,radi]
    Act5=[0.515,0.62,radi]
    Act6=[0.635,0.47,radi]
    Act7=[0.615,0.67,radi]
    global Actuat
    Actuat=[Act0,Act1,Act2,Act3,Act4,Act5,Act6,Act7]
    #Create the base plot
    plot()

    #Call a function to update the plot when there is new data
    updateplot(q)
    print('hola')
    root.mainloop()
    print ('Done')



if __name__ == '__main__':
    main()