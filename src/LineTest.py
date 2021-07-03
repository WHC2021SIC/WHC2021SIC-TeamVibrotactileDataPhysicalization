import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk as NavigationToolbar2TkAgg
import multiprocessing
import random
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle

from syntacts import *
from time import sleep, time
from math import sin
from math import pi

#Create a window
root=Tk()

sensor = Tk()
sensor.title("Sensors")
canvasTest = Canvas(sensor, width=450, height=230, borderwidth=0, highlightthickness=0)
canvasTest.grid()

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
canvasTest.create_circle = _create_circle

root.wm_title("WHC 2021")
root.geometry("950x950")

image = plt.imread('1x/circle.png') #root.image
#print(image.shape)
clickOn=False
xMin=0.4773
yMin=0.4093

s = Session()
s.open()

#print(DataManagement.max_min_by_country_by_year('Colombia', 2020))

def rgbtohex(rgb):
    r = int(rgb[0]*255.0)
    g = int(rgb[1]*255.0)
    b = int(rgb[2]*255.0)
    return f'#{r:02x}{g:02x}{b:02x}'

def renderSensorScreen(Tou, radius):
    #print(radius)
    sensor1 = canvasTest.create_circle(canvasTest, 55, 55, radius[0]+1.5, fill=rgbtohex(Tou[0][0]), outline="#DDD", width=0)
    sensor2 = canvasTest.create_circle(canvasTest, 165, 55, radius[1]+1.5, fill=rgbtohex(Tou[0][1]), outline="#DDD", width=0)
    sensor3 = canvasTest.create_circle(canvasTest, 275, 55, radius[2]+1.5, fill=rgbtohex(Tou[0][2]), outline="#DDD", width=0)
    sensor4 = canvasTest.create_circle(canvasTest, 385, 55, radius[3]+1.5, fill=rgbtohex(Tou[0][3]), outline="#DDD", width=0)
    sensor5 = canvasTest.create_circle(canvasTest, 55, 165, radius[4]+1.5, fill=rgbtohex(Tou[1][0]), outline="#DDD", width=0)
    sensor6 = canvasTest.create_circle(canvasTest, 165, 165, radius[5]+1.5, fill=rgbtohex(Tou[1][1]), outline="#DDD", width=0)
    sensor7 = canvasTest.create_circle(canvasTest, 275, 165, radius[6]+1.5, fill=rgbtohex(Tou[1][2]), outline="#DDD", width=0)
    sensor8 = canvasTest.create_circle(canvasTest, 385, 165, radius[7]+1.5, fill=rgbtohex(Tou[1][3]), outline="#DDD", width=0)

class RenderVibration:
    def __init__(self):
        self.listBefore = 'Not', 'Not', 'Not', 'Not', 'Not', 'Not', 'Not', 'Not'
        self.countryBefore ='Not'
        self.ValMaxSom=1.0
        self.som = Sine(250) * Envelope(500)
        self.t0=time()-self.som.length
        self.TimeMont=2000
        self.modeMonth=True
        self.MontCount=0
        self.listRadius=[0]*8
        self.radiusMax=50.0

    def Countrys(self,listCount):
        #res = [x for x in listCount if x not in self.listBefore]      
        #print(listCount)       
        res = [count if count != self.listBefore[x] else 'Not' for x,count in enumerate(listCount)]
        #print(res)
        val=False
        for i in res:
            if i !='Not':
                val=True
        if val:
            #print(listCount)
            #print("diff")
            self.ValCountry(res)
            self.listBefore = listCount
            if ((time() - self.t0) >= self.som.length):
                self.start_all()
                self.t0=time()
                #print("startSom")
                

    def ValCountry(self, listCount):
        for i,country in enumerate(listCount):
            if(country !='Not'):
                MaxG=1
                if country == 'Out':
                    countVal=0.0
                else:
                    countVal=1-country
                    
                ValCountr = countVal * self.ValMaxSom
                self.listRadius[i] = countVal * self.radiusMax
                #print("Act {}: Country {}, Render: {}".format(i,countVal,ValCountr))
                self.Actuators(i,ValCountr)
                
    def Actuators(self,Indx,value):        
        if(Indx < 4):
            ActNum = Indx * 2 + 1
        else:
            ActNum = (Indx - 4) * 2
        self.render(ActNum, value)
    
    def render(self,indx,value):
        s.set_volume(indx,value)
        #print("Vib {}: Render {}".format(indx,value))

    def start_all(self):
        s.play(0, self.som)
        s.play(1, self.som)
        s.play(2, self.som)
        s.play(3, self.som)
        s.play(4, self.som)
        s.play(5, self.som)
        s.play(6, self.som)
        s.play(7, self.som)
    
    def stop_all(self):
        s.stop(0)
        s.stop(1)
        s.stop(2)
        s.stop(3)
        s.stop(4)
        s.stop(5)
        s.stop(6)
        s.stop(7)
        self.t0 = time()-self.som.length
        self.listBefore = 'Not', 'Not', 'Not', 'Not', 'Not', 'Not', 'Not', 'Not'
        self.MontCount = 0

    def stop_sound(self):
        s.stop(0)
        s.stop(1)
        s.stop(2)
        s.stop(3)
        s.stop(4)
        s.stop(5)
        s.stop(6)
        s.stop(7)
    
    def render_all(self,value):
        s.set_volume(0,value)
        s.set_volume(1,value)
        s.set_volume(2,value)
        s.set_volume(3,value)
        s.set_volume(4,value)
        s.set_volume(5,value)
        s.set_volume(6,value)
        s.set_volume(7,value)
    
    def start_value(self, som):
        s.play(0, som)
        s.play(1, som)
        s.play(2, som)
        s.play(3, som)
        s.play(4, som)
        s.play(5, som)
        s.play(6, som)
        s.play(7, som)

renderVib = RenderVibration()
        

def ModeTotal(PixNow):
    NearCoun,colors=NearestPixels(PixNow)
    #print(colors)
    renderVib.Countrys(NearCoun)
    canvasTest.delete("all")
    renderSensorScreen(colors,renderVib.listRadius)

def NearestPixels(PixNow):
    t0=[0]*2
    NearCoun=[]
    colors = [[0,0,0,0],[0,0,0,0]]
    for i in range(2):
        for j in range(4):
            t0[0]=PixNow[0]+i
            t0[1]=PixNow[1]+j
            if(t0[0]>=image.shape[0] or t0[1]>=image.shape[1]):
                NearCoun.append("Out")
                continue
            Tou0=image[t0[0], t0[1],:]

            colors[i][j] = Tou0
            NearCoun.append(Tou0[0])
    
    return NearCoun, colors

def reset_all():
    renderVib.stop_all()
    renderVib.MontCount=0
    renderVib.countryBefore='Not'

def on_click(event):
    #print('click')
    global clickOn
    if event.inaxes is not None:
        #print(clickOn)
        clickOn=True
        t01=[int(event.ydata+yMin), int(event.xdata+xMin)]
        ModeTotal(t01)
        

def off_click(event):
    global clickOn
    clickOn=False
    canvasTest.delete("all")
    colBlack=[0., 0., 0., 1.]
    renderSensorScreen([[colBlack]*4]*2,[0.0]*8)
    reset_all()

def on_move(event):
    if event.inaxes is not None:
        #print(clickOn)
        if clickOn==True:
            t01=[int(event.ydata+yMin), int(event.xdata+xMin)]
            ModeTotal(t01)


def plot():    #Function to create the base plot, make sure to make global the lines, axes, canvas and any part that you would want to update later
        
    #fig.add_subplot(1, 2, 2)
    fig2 = plt.figure()    
    fig2.canvas.callbacks.connect('button_press_event', on_click)
    fig2.canvas.callbacks.connect('motion_notify_event', on_move)
    fig2.canvas.callbacks.connect('button_release_event', off_click)

    im = plt.imshow(image) # later use a.set_data(new_data) image2
    
    canvas2 = FigureCanvasTkAgg(fig2, master=root)
    canvas2.draw()
    #canvas2.get_tk_widget().grid(row=1, column=1)
    canvas2.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    canvas2._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)


def main():

    #Create the base plot
    plot()
    print('Start...')
    root.mainloop()
    print ('Done')


if __name__ == '__main__':
    main()