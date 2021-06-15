import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk as NavigationToolbar2TkAgg
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import multiprocessing
import random
from tkinter import *
import numpy as np
from matplotlib.patches import Circle, Rectangle

from syntacts import *
from time import sleep, time
from math import sin
from math import pi

import numpy as np

s = Session()
s.open()

#Create a window
root=Tk()

root.wm_title("WHC 2021")

root.image = plt.imread('Recurso 3_1.png')

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

totalTime = 10

def on_click(event):
    #print('click')
    global clickOn, circ, rectColi
    if event.inaxes is not None:
        #print(clickOn)
        clickOn=True
        Hreal=event.xdata*HRelation
        Lreal=event.ydata*LRelation
        radPix=radius*(1/HRelation)
#         print ("x:{},y:{}".format(event.x, event.y))
#         print ("x:{},y:{}".format(event.xdata, event.ydata))
#         print ("radius:{}".format(radPix))
#         print ("x:{},y:{}".format(Hreal, Lreal))
        continent.CollisionDetect(Hreal,Lreal)
        circ = Circle((int(event.xdata), int(event.ydata)),radPix)
        ax.add_patch(circ)
        canvas.draw()        
        #print (im.cmap(im.norm(root.image[int(event.ydata), int(event.xdata)])))

        #print("Collison: {}".format(rectColi.collisionDetect(Hreal,Lreal)))
    
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
            continent.CollisionDetect(Hreal,Lreal)
#             print ("x:{},y:{}".format(event.x, event.y))
#             print ("x:{},y:{}".format(event.xdata, event.ydata))
#             print ("x:{},y:{}".format(Hreal, Lreal))
#             print (im.cmap(im.norm(root.image[int(event.ydata), int(event.xdata)])))
            
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

class Country:
    def __init__(self, name,x,y,radius,fsom,tsom):
        self.name = name 
        self.Pos = np.array([x,y])
        self.radius = radius
        self.som=Sine(fsom) * Envelope(tsom,1)
        
    def collisionDetect(self,x,y):
        dist=self.Pos-np.array([x,y])            
        if(np.dot(dist,dist)<=(self.radius*self.radius)):
            return True
        else:
            return False
        
        
class Edge:
    def __init__(self,name,cx,cy,H,L,ang):
        self.name = name
        rotAxisH=np.array([np.cos(np.deg2rad(ang)),np.sin(np.deg2rad(ang))])
        rotAxisL=np.array([-rotAxisH[1],rotAxisH[0]])       
        self.c = np.array([cx,cy])
        self.U = np.array([rotAxisH,rotAxisL])
        self.E = np.array([H,L])  
        self.posDraw = self.c-(rotAxisH*H)-(rotAxisL*L)

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
        
class Continent:
    # creating list
    def __init__(self):
        self.t0=time()-totalTime
        self.timeSom=totalTime
        self.list = []
        self.objAntname="Init"
        # appending instances to list 
        self.list.append( Country('Brasil', 12.0,10.0,3.0,446,self.timeSom) )
        self.list.append( Country('Brasil', 8.2,7.45,2.0,446,self.timeSom) )
        self.list.append( Country('Colombia', 3.9,5.0,1.5,84,self.timeSom) )
        self.list.append( Country('Peru', 3.7,9.0,1.7,67,self.timeSom) )
        self.list.append( Country('Bolivia', 7.0,11.0,1.7,13,self.timeSom) )
        self.list.append( Country('Paraguai', 8.8,14.0,1.7,8,self.timeSom) )
        self.list.append( Country('Venezuela', 6.4,3.3,1.5,8,self.timeSom) )
        self.list.append( Country('Cases', 1.35,10.9,1.4,8,self.timeSom) )
        self.list.append( Country('Death', 1.3,13.6,1.4,8,self.timeSom) )
        self.list.append( Country('Total', 13.7,1.3,1.4,8,self.timeSom) )
        self.list.append( Country('Month', 13.7,4.0,1.4,8,self.timeSom) )
        self.list.append( Country('Btn20', 6.4,0.0,1.4,8,self.timeSom) )
        self.list.append( Country('Btn21', 9.1,0.0,1.4,8,self.timeSom) )
        self.listRect = []
        self.listRect.append( Edge('Col_Ven',5.0,4.0,1.5,0.5,45.0) )
        self.listRect.append( Edge('Bol_Bra',8.0,10.0,1.6,0.5,45.0) )
        self.listRect.append( Edge('Par_Bra',9.8,12.6,1.5,0.5,45.0) )
        self.listRect.append( Edge('Per_Bra',5.0,8.5,1.3,0.5,45.0) )
        self.listRect.append( Edge('Per_Col',3.3,6.7,1.0,0.6,10.0) )
        self.listRect.append( Edge('Col_Bra',5.3,6.1,0.8,0.5,-45.0) )
        self.listRect.append( Edge('Per_Bol',5.4,10.2,1.2,0.5,-45.0) )
        self.listRect.append( Edge('Vol_Par',7.9,12.5,0.8,0.5,-45.0) )
        self.listRect.append( Edge('Ven_Bra',7.3,4.5,0.8,0.5,-45.0) )
        
    def CollisionDetect(self,xp,yp):
#         for obj in self.listRect:         
#             if(obj.collisionDetect(xp,yp)):
#                 print( obj.name, sep =' ' )
#                 return
                #sleep(obj.som.length)
        for obj in self.list:         
            if(obj.collisionDetect(xp,yp)):
                print( obj.name, sep =' ' )
                
                if(self.objAntname!=obj.name):
                    #print("diff")
                    self.objAntname=obj.name
                    s.stop(0)
                    s.stop(1)
                    s.stop(2)
                    s.stop(3)
                    s.stop(4)
                    s.stop(5)
                    s.stop(6)
                    s.stop(7)
                    self.t0 = time()- self.timeSom                            
                                    
                if ((time() - self.t0) >= obj.som.length):
                    s.play(0, obj.som)
                    s.play(1, obj.som)
                    s.play(2, obj.som)
                    s.play(3, obj.som)
                    s.play(4, obj.som)
                    s.play(5, obj.som)
                    s.play(6, obj.som)
                    s.play(7, obj.som)
                    #print('Signal 2')
                    self.t0=time()
                #sleep(obj.som.length)
                return

for xx,yy,H,L,ang in CountryRect:
    rotAxisH=np.array([np.cos(np.deg2rad(ang)),np.sin(np.deg2rad(ang))])
    rotAxisL=np.array([-rotAxisH[1],rotAxisH[0]])
    #RectLen=np.array([H,L])
    RectCent=np.array([xx,yy])
    RectPosC=RectCent-(rotAxisH*H)-(rotAxisL*L)
    rect=Rectangle(RectPosC * (1/HRelation), H * (1/HRelation) * 2.0, L * (1/HRelation) * 2.0, ang)
    ax.add_patch(rect)


#ax.add_patch(rect)

'''print("shape:{}".format(rotAxisH))
print("shape:{}".format(np.array([rotAxisH,rotAxisL])[0]))'''

#rectColi = Rectan(RectCent,ang,RectLen)

# a tk.DrawingArea
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)

global continent
continent = Continent()

def main():

    print('hola')
    print(root.image.shape)
    root.mainloop()
    print ('Done')


if __name__ == '__main__':
    main()