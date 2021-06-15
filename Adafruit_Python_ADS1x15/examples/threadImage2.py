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
#root.geometry("450x350")

'''#Create a canvas object
c= Canvas(root)
c.grid(columnspan=2, rowspan=2)

#Draw an Oval in the canvas
c.create_oval(60,60,210,210,fill="blue")'''

image = plt.imread('sudamericaLowRes.png') #root.image
image2 = plt.imread('Actuators.png')

print(image.shape)

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

ColColombia=[1., 0.56863, 0., 1.]
ColVen=[0.94902,  0.58431, 0.88235, 1.]
ColEcuador=[0.01176 ,0.,         0.71373,  1.        ]
ColPeru=[0.71373  ,0.,         0.01176, 1.]
ColBolivia=[0.23137 ,0.82353  ,0.63529 ,1.        ]
colParaguai=[0.99216, 0.         ,0.34902, 1.        ]
Colchile=[0.,         0.43137, 0.71373,  1.        ]
colArg=[0.5098, 0.11765, 0.50588,  1.        ]
Colguyana=[0.30980393, 0.13333334, 0.03529412, 1.        ]
ColSuri=[0.03529412, 0.20784314, 0.30980393, 1.        ]
French=[1.,         0.27058825, 0.27058825, 1.        ]
ColBrasil=[1.,        0.8666667, 0.        ,1.       ]
ColUruguai=[0.3098,  0.61961, 0.15294, 1.     ]
ColBack=[0.0,  0.0, 0.0, 0.]

class ColorCountry:
    def __init__(self, name,color):
        self.color=color
        self.name=name
        
    def collisionDetect(self,color):
        #print(color)
        res=np.dot(self.color-color,self.color-color)        
        if(res<0.05):
            return True
        else:
            return False

class Continent:
    # creating list
    def __init__(self):
        self.list = []
        self.objAntname="Init"
        # appending instances to list 
        self.list.append( ColorCountry('colombia',ColColombia) )
        self.list.append( ColorCountry('Venezuela',ColVen))
        self.list.append( ColorCountry('ecuador',ColEcuador))
        self.list.append( ColorCountry('peru',ColPeru))
        self.list.append( ColorCountry('bolivia',ColBolivia))
        self.list.append( ColorCountry('paraguai',colParaguai))
        self.list.append( ColorCountry('chile',Colchile) )
        self.list.append( ColorCountry('argentina',colArg))
        self.list.append( ColorCountry('guyana',Colguyana) )
        self.list.append( ColorCountry('suri',ColSuri) )
        self.list.append( ColorCountry('french',French) )
        self.list.append( ColorCountry('Brasil',ColBrasil) )
        self.list.append( ColorCountry('Uruaguai',ColUruguai) )
        self.list.append( ColorCountry('Background',ColBack) )

    def CollisionDetect(self,color):
        col=-1
        for obj in self.list:         
            if(obj.collisionDetect(color)):
                #print( obj.name, sep =' ' )
                #print(np.dot(obj.color-color,obj.color-color))
                return True, obj.name
        if(col==-1):
            return False,-1
    

def on_click(event):
    #print('click')
    global clickOn, circ
    if event.inaxes is not None:
        #print(clickOn)
        clickOn=True
        Hreal=event.xdata*HRelationAct
        Lreal=event.ydata*LRelationAct
        
        t01=[int(event.ydata+yMin), int(event.xdata+xMin)]
        t0=[0]*2
        NearCoun=[]
        for i in range(2):
            for j in range(4):
                t0[0]=t01[0]+i
                t0[1]=t01[1]+j
                if(t0[0]>=image.shape[0] or t0[1]>=image.shape[1]):
                    NearCoun.append("Out")
                    continue
                Tou0=image[t0[0], t0[1],:]
                Collision,Country=continent.CollisionDetect(Tou0)
                if(Collision):
                    NearCoun.append(Country)
        
        print(NearCoun)

        #t1=[int(event.ydata+yMin), int(event.xdata+xMin)]

        #radPix=radius*(1/LRelationAct)
        
        #print ("x:{},y:{}".format(event.x, event.y))        
        
        '''print ("x:{},y:{}".format(event.xdata + xMin, event.ydata+ yMin))
        #print ("radius:{}".format(radPix))
        print ("x:{},y:{}".format(Hreal, Lreal))
        print (image[int(event.ydata+yMin), int(event.xdata+xMin),:])'''

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
            colorTouch=image[int(event.ydata+yMin), int(event.xdata+xMin),:]
            continent.CollisionDetect(colorTouch)
            '''print ("x:{},y:{}".format(event.x, event.y))
            print ("x:{},y:{}".format(event.xdata, event.ydata))
            print ("x:{},y:{}".format(Hreal, Lreal))
            print (image[int(event.ydata), int(event.xdata),:])'''
            #print (im.cmap(im.norm(root.image[int(event.ydata), int(event.xdata)])))
    '''else:
        print ('Clicked ouside axes bounds but inside plot window')'''

def ActDeath():
    print("death")
    

def plot():    #Function to create the base plot, make sure to make global the lines, axes, canvas and any part that you would want to update later
    global line,ax,canvas, patches, p, fig
        
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

    Death_Cas=IntVar()
    c = Checkbutton(root, text = "On:Death/Off:Cases", variable=Death_Cas, justify=LEFT).pack(side=LEFT)
    
    Tot_Mounth=IntVar()
    c2 = Checkbutton(root, text = "On:Total/Off:Mounthoy", variable=Tot_Mounth, justify=LEFT).pack(side=RIGHT)

    '''TotBtn=Button(root,text="Total")
    TotBtn.pack(side=RIGHT)
    MonBtn=Button(root,text="Mountly")
    MonBtn.pack(side=RIGHT)'''

continent=Continent()

def main():
    #Create the base plot
    plot()
    print('Start...')
    root.mainloop()
    print ('Done')



if __name__ == '__main__':
    main()