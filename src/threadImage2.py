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

from DataManagement import DataManagement
from ContinentColor import Continent

#Create a window
root=Tk()

root.wm_title("WHC 2021")
#root.geometry("450x350")

image = plt.imread('sudamericaLowRes.png') #root.image
#print(image.shape)
clickOn=False
xMin=0.4773
yMin=0.4093



continent=Continent()

print(DataManagement.max_min_by_country_by_year('Colombia', 2020))

class RenderVibration:
    def __init__(self):
        self.listBefore = 'Not', 'Not', 'Not', 'Not', 'Not', 'Not', 'Not', 'Not'        
        self.MaxGlobal, self.MinGlobal = DataManagement.global_values()
        self.ValMaxFreq=500

    def Countrys(self,listCount):
        #res = [x for x in listCount if x not in self.listBefore]
        if(Tot_Mounth.get()):
        
            res = [count if count != self.listBefore[x] else 'Not' for x,count in enumerate(listCount)]

            print(res)
            val=False
            for i in res:
                if i !='Not':
                    val=True
            if val:
                #print("diff")
                self.start(res)
                self.listBefore = listCount
            else:
                print("equal")

    def start(self, listCount):
        for i,country in enumerate(listCount):
            if(country !='Not'):
                if country != 'Background':
                    countVal,_=DataManagement.max_min_by_country(country)        
                else:
                    countVal=0.0
                ValCountr = countVal * (self.ValMaxFreq / self.MaxGlobal)
                #print("Act {}: Country {}, Render: {}".format(i,countVal,ValCountr))
                self.Actuators(i,ValCountr)
                
    def Actuators(self,Indx,value):        
        if(Indx < 4):
            ActNum = Indx * 2
        else:
            ActNum = (Indx - 4) * 2 + 1
        self.render(ActNum, value)
    
    def render(self,indx,value):        
        print("Vib {}: Render {}".format(indx,value))
        



renderVib = RenderVibration()


def NearestPixels(PixNow):
    t0=[0]*2
    NearCoun=[]
    for i in range(2):
        for j in range(4):
            t0[0]=PixNow[0]+i
            t0[1]=PixNow[1]+j
            if(t0[0]>=image.shape[0] or t0[1]>=image.shape[1]):
                NearCoun.append("Out")
                continue
            Tou0=image[t0[0], t0[1],:]
            Collision,Country=continent.CollisionDetect(Tou0)
            if(Collision):
                NearCoun.append(Country)
            else:
                if(i==0 and j==0):
                    NearCoun.append('Background')    
                    continue
                NearCoun.append(NearCoun[-1])
            
    return NearCoun
    

def on_click(event):
    #print('click')
    global clickOn, circ
    if event.inaxes is not None:
        #print(clickOn)
        clickOn=True        
        t01=[int(event.ydata+yMin), int(event.xdata+xMin)]
        NearCoun=NearestPixels(t01)
        renderVib.Countrys(NearCoun)
        #print(NearCoun)

def off_click(event):
    global clickOn, circ
    clickOn=False

def on_move(event):
    if event.inaxes is not None:
        #print(clickOn)
        if clickOn==True:
            t01=[int(event.ydata+yMin), int(event.xdata+xMin)]
            NearCoun=NearestPixels(t01)
            print(NearCoun)


def ActDeath():
    print("death")
    

def plot():    #Function to create the base plot, make sure to make global the lines, axes, canvas and any part that you would want to update later
    global Death_Cas, Tot_Mounth
        
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
    Tot_Mounth.set(True)


def main():
    #Create the base plot
    plot()
    print('Start...')
    root.mainloop()
    print ('Done')


if __name__ == '__main__':
    main()