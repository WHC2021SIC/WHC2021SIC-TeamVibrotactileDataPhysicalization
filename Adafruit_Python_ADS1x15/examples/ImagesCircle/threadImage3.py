import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk as NavigationToolbar2TkAgg
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib import cm
import multiprocessing
import random
from tkinter import *
import numpy as np
from matplotlib.patches import Circle, Rectangle
from matplotlib.collections import PatchCollection
from matplotlib import animation

#Create a window
root=Tk()

root.wm_title("WHC 2021")
#root.geometry("450x350")

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

Brazil=[12.0,10.0,3.0]
Brazil2=[8.2,7.45,2.0]
Peru=[3.7,9.0,1.7]
bolivia=[7.0,11.0,1.7]
colombia=[3.9,5.0,1.5]
venezuela=[6.4,3.3,1.5]
paraguai=[8.8,14.0,1.7]

BtnCase=[1.35,10.9,1.4]
BtnDeath=[1.3,13.6,1.4]
BtnTotal=[13.7,1.3,1.4]
BtnMont=[13.7,4.0,1.4]
Btn20=[5.4,0.0,1.4]
Btn21=[9.1,0.0,1.4]

Country=[Brazil,Brazil2,Peru, bolivia,colombia,venezuela,paraguai]

RectColVen=[5.0,4.0,1.5,0.5,45.0]
RectBolBra=[8.0,10.0,1.6,0.5,45.0]
RectParBra=[9.8,12.6,1.5,0.5,45.0]
RectPerBra=[5.0,8.5,1.3,0.5,45.0]
RectPerCol=[3.3,6.7,1.0,0.6,10.0]
RectColBra=[5.3,6.1,0.8,0.5,-45.0]
RectPerBol=[5.4,10.2,1.2,0.5,-45.0]
RectBolPar=[7.9,12.5,0.8,0.5,-45.0]
RectVezBra=[7.3,4.5,0.8,0.5,-45.0]

CountryRect=[RectColVen,RectBolBra,RectParBra,RectPerBra, RectPerCol, RectColBra, RectPerBol, RectBolPar, RectVezBra]

circ=Circle((0,0),50)
xMin=0.4773
yMin=0.4093

def on_click(event):
    #print('click')
    global clickOn, circ, p
    if event.inaxes is not None:
        #print(clickOn)
        clickOn=True
        Hreal=event.xdata*HRelationAct
        Lreal=event.ydata*LRelationAct
        #radPix=radius*(1/LRelationAct)
        
        #print ("x:{},y:{}".format(event.x, event.y))

        colors = 100*np.random.rand(len(patches)) # random index to color map
        p.set_array(np.array(colors))
        
        print ("x:{},y:{}".format(event.xdata + xMin, event.ydata+ yMin))
        #print ("radius:{}".format(radPix))
        print ("x:{},y:{}".format(Hreal, Lreal))
        print (image[int(event.ydata+yMin), int(event.xdata+xMin),:])
        


        '''circ = Circle((int(event.xdata), int(event.ydata)),radPix)1
        ax.add_patch(circ)
        canvas.draw()'''
        
        #print (im.cmap(im.norm(root.image[int(event.ydata), int(event.xdata)])))
        #print("Collison: {}".format(rectColi.collisionDetect(Hreal,Lreal)))
    
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

radi=90
Act0=[0.265,0.41,radi]
Act1=[0.295,0.64,radi]
Act2=[0.395,0.34,radi]
Act3=[0.395,0.61,radi]
Act4=[0.52,0.39,radi]
Act5=[0.515,0.62,radi]
Act6=[0.635,0.47,radi]
Act7=[0.615,0.67,radi]

Actuat=[Act0,Act1,Act2,Act3,Act4,Act5,Act6,Act7]

fig = plt.figure()
#binding_id = plt.connect('motion_notify_event', on_move)
fig.add_subplot(1, 2, 1)
plt.imshow(image2)

ax2=plt.gca()

patches = []
# Now, loop through coord arrays, and create a circle at each x,y pair
for xx,yy,r in Actuat:    
    #print("x: {}, y: {},r: {}".format(xx,yy,r))
    circC = Circle((xx*(1/HRelationAct),yy*(1/LRelationAct)),r)
    patches.append(circC)

# add these circles to a collection
p = PatchCollection(patches, facecolors='r', alpha=0.4)
ax2.add_collection(p)

'''def animate(i):
    colors = 100*np.random.rand(len(patches)) # random index to color map
    p.set_array(np.array(colors)) # set new color colors
    return p,

ani = animation.FuncAnimation(fig, animate, interval=50)'''

fig.add_subplot(1, 2, 2)
fig.canvas.callbacks.connect('button_press_event', on_click)
fig.canvas.callbacks.connect('motion_notify_event', on_move)
fig.canvas.callbacks.connect('button_release_event', off_click)

global im
im = plt.imshow(image) # later use a.set_data(new_data) image2


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
            #print("Dist:{}".format(dist))
            if (dist<self.E[i]) and (dist>-self.E[i]):
                cont=cont+1
        if cont>1:
            return True
        else:
            return False


'''ax = plt.gca()
ax.set_xticklabels([]) 
ax.set_yticklabels([])
#ax.set_aspect('equal')

# Now, loop through coord arrays, and create a circle at each x,y pair
for xx,yy,r in Country:    
    #print("x: {}, y: {},r: {}".format(xx,yy,r))
    circC = Circle((xx*(1/HRelation),yy*(1/HRelation)),r*(1/HRelation),fill=False)
    ax.add_patch(circC)

for xx,yy,H,L,ang in CountryRect:
    rotAxisH=np.array([np.cos(np.deg2rad(ang)),np.sin(np.deg2rad(ang))])
    rotAxisL=np.array([-rotAxisH[1],rotAxisH[0]])
    #RectLen=np.array([H,L])
    RectCent=np.array([xx,yy])
    RectPosC=RectCent-(rotAxisH*H)-(rotAxisL*L)
    rect=Rectangle(RectPosC * (1/HRelation), H * (1/HRelation) * 2.0, L * (1/HRelation) * 2.0, ang)
    ax.add_patch(rect)'''


#ax.add_patch(rect)

'''print("shape:{}".format(rotAxisH))
print("shape:{}".format(np.array([rotAxisH,rotAxisL])[0]))'''

#rectColi = Rectan(RectCent,ang,RectLen)

# a tk.DrawingArea
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)


button1=Button(root, text="button1", pady=20, padx=30)
button1.pack(side=RIGHT)

def main():

    print('hola')
    print(image.shape)
    root.mainloop()
    print ('Done')


if __name__ == '__main__':
    main()