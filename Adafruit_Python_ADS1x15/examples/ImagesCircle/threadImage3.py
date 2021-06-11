import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk as NavigationToolbar2TkAgg
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import multiprocessing
import time
import random
from tkinter import *
import numpy as np
from matplotlib.patches import Circle, Rectangle

#Create a window
root=Tk()

root.wm_title("minimal example")

root.image = plt.imread('Recurso 3.png')

clickOn=False

Heigth=15.0
Length=15.0
radius=1.5

HRelation=Heigth/root.image.shape[0]
LRelation=Length/root.image.shape[1]

Brazil=[12.0,10.0,3.0]
Brazil2=[8.2,7.45,2.0]
Peru=[3.7,9.0,1.7]
bolivia=[7.0,11.0,1.7]
colombia=[3.9,5.0,1.5]
venezuela=[6.4,3.3,1.5]
paraguai=[8.8,14.0,1.7]

BtnCase=[0.99,11.24,1.4]
BtnDeath=[1.35,14.4,1.4]
BtnGMax=[13.7,0.6,1.4]
BtnGMin=[13.9,3.8,1.4]
Btn20=[5.4,0.0,1.4]
Btn21=[9.1,0.0,1.4]

Country=[Brazil,Brazil2,Peru, bolivia,colombia,venezuela,paraguai]

circ=Circle((0,0),50)

def on_click(event):
    #print('click')
    global clickOn, circ, rectColi
    if event.inaxes is not None:
        #print(clickOn)
        clickOn=True
        Hreal=event.xdata*HRelation
        Lreal=event.ydata*LRelation
        radPix=radius*(1/HRelation)
        print ("x:{},y:{}".format(event.x, event.y))
        print ("x:{},y:{}".format(event.xdata, event.ydata))
        print ("radius:{}".format(radPix))
        print ("x:{},y:{}".format(Hreal, Lreal))
        
        circ = Circle((int(event.xdata), int(event.ydata)),radPix)
        ax.add_patch(circ)
        canvas.draw()        
        #print (im.cmap(im.norm(root.image[int(event.ydata), int(event.xdata)])))

        print("Collison: {}".format(rectColi.collisionDetect(Hreal,Lreal)))
    

def off_click(event):
    global clickOn, circ
    clickOn=False
    circ.remove()
    canvas.draw()    

def on_move(event):
    if event.inaxes is not None:
        #print(clickOn)
        if clickOn==True:
            Hreal=event.xdata*HRelation
            Lreal=event.ydata*LRelation
            print ("x:{},y:{}".format(event.x, event.y))
            print ("x:{},y:{}".format(event.xdata, event.ydata))
            print ("x:{},y:{}".format(Hreal, Lreal))
            print (im.cmap(im.norm(root.image[int(event.ydata), int(event.xdata)])))
    '''else:
        print ('Clicked ouside axes bounds but inside plot window')'''


fig = plt.figure()
#binding_id = plt.connect('motion_notify_event', on_move)
fig.canvas.callbacks.connect('button_press_event', on_click)
fig.canvas.callbacks.connect('motion_notify_event', on_move)
fig.canvas.callbacks.connect('button_release_event', off_click)

global im

im = plt.imshow(root.image) # later use a.set_data(new_data)
ax = plt.gca()
ax.set_aspect('equal')

# Now, loop through coord arrays, and create a circle at each x,y pair
for xx,yy,r in Country:    
    print("x: {}, y: {},r: {}".format(xx,yy,r))
    circC = Circle((xx*(1/HRelation),yy*(1/HRelation)),r*(1/HRelation),fill=False)
    ax.add_patch(circC)

ax.set_xticklabels([]) 
ax.set_yticklabels([])

class Rectan:
    def __init__(self, c,ang,E): 
        rotAxisH=np.array([np.cos(np.deg2rad(ang)),np.sin(np.deg2rad(ang))])
        rotAxisL=np.array([-rotAxisH[1],rotAxisH[0]])       
        self.c = c
        self.U = np.array([rotAxisH,rotAxisL])
        self.E = E  
        self.posDraw = c-(rotAxisH*E[0])-(rotAxisL*E[1])

    def collisionDetect(self,x,y):
        d=np.array([x,y])-self.c
        q=self.c
        cont=0
        for i in range(2):
            dist=np.dot(d,self.U[i])
            print("Dist:{}".format(dist))
            if (dist<self.E[i]) and (dist>-self.E[i]):
                cont=cont+1
        if cont>1:
            return True
        else:
            return False


ang=45.0
rotAxisH=np.array([np.cos(np.deg2rad(ang)),np.sin(np.deg2rad(ang))])
rotAxisL=np.array([-rotAxisH[1],rotAxisH[0]])
RectLen=np.array([2.0,1.5])
RectCent=np.array([3.9,5.0])

RectPosC=RectCent-(rotAxisH*RectLen[0])-(rotAxisL*RectLen[1])

print("RectC:{}".format(RectPosC))

rect=Rectangle(RectPosC*(1/HRelation),RectLen[0]*(1/HRelation)*2.0,RectLen[1]*(1/HRelation)*2.0,ang)
ax.add_patch(rect)

'''print("shape:{}".format(rotAxisH))
print("shape:{}".format(np.array([rotAxisH,rotAxisL])[0]))'''

rectColi = Rectan(RectCent,ang,RectLen)



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
    print(root.image.shape)
    root.mainloop()
    print ('Done')


if __name__ == '__main__':
    main()