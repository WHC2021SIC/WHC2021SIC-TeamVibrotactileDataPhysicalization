import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk as NavigationToolbar2TkAgg
import multiprocessing
import random
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle

from DataManagement import DataManagement
from ContinentColor import Continent

from syntacts import *
from time import sleep, time
from math import sin
from math import pi

#Create a window
root=Tk()

sensor = Tk()
sensor.title("Sensors")
canvasTest = Canvas(sensor, width=400, height=400, borderwidth=0, highlightthickness=0)
canvasTest.grid()


def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
canvasTest.create_circle = _create_circle

sensor1 = canvasTest.create_circle(canvasTest, 50, 50, 50, fill="blue", outline="#DDD", width=4)
sensor2 = canvasTest.create_circle(canvasTest, 150, 50, 50, fill="blue", outline="#DDD", width=4)
sensor3 = canvasTest.create_circle(canvasTest, 250, 50, 50, fill="blue", outline="#DDD", width=4)
sensor4 = canvasTest.create_circle(canvasTest, 350, 50, 50, fill="blue", outline="#DDD", width=4)
sensor5 = canvasTest.create_circle(canvasTest, 50, 150, 50, fill="blue", outline="#DDD", width=4)
sensor6 = canvasTest.create_circle(canvasTest, 150, 150, 50, fill="blue", outline="#DDD", width=4)
sensor7 = canvasTest.create_circle(canvasTest, 250, 150, 50, fill="blue", outline="#DDD", width=4)
sensor8 = canvasTest.create_circle(canvasTest, 350, 150, 50, fill="blue", outline="#DDD", width=4)

root.wm_title("WHC 2021")
#root.geometry("450x350")

image = plt.imread('sudamericaLowRes.png') #root.image
#print(image.shape)
clickOn=False
xMin=0.4773
yMin=0.4093

s = Session()
s.open()

continent=Continent()

#print(DataManagement.max_min_by_country_by_year('Colombia', 2020))

def rgbtohex(rgb):
    r = int(rgb[0]*255)
    g = int(rgb[1]*255)
    b = int(rgb[2]*255)
    return f'#{r:02x}{g:02x}{b:02x}'

def renderSensorScreen(Tou):
    
    # canvasTest = Canvas(sensor, width=400, height=400, borderwidth=0, highlightthickness=0)
    # canvasTest.grid()
    # canvasTest.create_circle = _create_circle

    sensor1 = canvasTest.create_circle(canvasTest, 50, 50, 50, fill=rgbtohex(Tou[0][0]), outline="#DDD", width=4)
    sensor2 = canvasTest.create_circle(canvasTest, 150, 50, 50, fill=rgbtohex(Tou[0][1]), outline="#DDD", width=4)
    sensor3 = canvasTest.create_circle(canvasTest, 250, 50, 50, fill=rgbtohex(Tou[0][2]), outline="#DDD", width=4)
    sensor4 = canvasTest.create_circle(canvasTest, 350, 50, 50, fill=rgbtohex(Tou[0][3]), outline="#DDD", width=4)
    sensor5 = canvasTest.create_circle(canvasTest, 50, 150, 50, fill=rgbtohex(Tou[1][0]), outline="#DDD", width=4)
    sensor6 = canvasTest.create_circle(canvasTest, 150, 150, 50, fill=rgbtohex(Tou[1][1]), outline="#DDD", width=4)
    sensor7 = canvasTest.create_circle(canvasTest, 250, 150, 50, fill=rgbtohex(Tou[1][2]), outline="#DDD", width=4)
    sensor8 = canvasTest.create_circle(canvasTest, 350, 150, 50, fill=rgbtohex(Tou[1][3]), outline="#DDD", width=4)

class RenderVibration:
    def __init__(self):
        self.listBefore = 'Not', 'Not', 'Not', 'Not', 'Not', 'Not', 'Not', 'Not'
        self.countryBefore ='Not'
        self.MaxGlobal, self.MinGlobal = DataManagement.global_values()
        self.ValMaxSom=1.0
        self.som = Sine(450) * Envelope(500)
        self.t0=time()-self.som.length
        self.TimeMont=1000
        self.modeMonth=True
        self.MontCount=0

    def Countrys(self,listCount):
        #res = [x for x in listCount if x not in self.listBefore]             
        res = [count if count != self.listBefore[x] else 'Not' for x,count in enumerate(listCount)]            
        #print(res)
        val=False
        for i in res:
            if i !='Not':
                val=True
        if val:
            print(listCount)
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
                if country != 'Background':
                    countVal=DataManagement.get_sum_country(country)
                else:
                    countVal=0.0
                ValCountr = countVal * (self.ValMaxSom / self.MaxGlobal)
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
    
    def render_all(self,value):
        s.set_volume(0,value)
        s.set_volume(1,value)
        s.set_volume(2,value)
        s.set_volume(3,value)
        s.set_volume(4,value)
        s.set_volume(5,value)
        s.set_volume(6,value)
        s.set_volume(7,value)

renderVib = RenderVibration()

def ModeMonth(PixNow):
    countryPix=CountryPix(PixNow)
    if countryPix!='Background':
        if renderVib.countryBefore == countryPix:
            return
        renderVib.countryBefore = countryPix
        print(countryPix)
        listMonth=DataManagement.get_data_contry_by_year(countryPix, 2020)
        MaxMonth,_=DataManagement.max_min_by_country_by_year(countryPix, 2020)
        simMonth(listMonth,MaxMonth)
        renderVib.start_all()
    else:
        renderVib.stop_all()
        renderVib.MontCount=0
        

def simMonth(listMonth,MaxMonth):    
    if(renderVib.MontCount<len(listMonth) and clickOn):
        valCurr=listMonth[renderVib.MontCount]
        ValCountr = valCurr * (renderVib.ValMaxSom / MaxMonth)
        renderVib.render_all(ValCountr)
        print("mes: {} : {}".format(renderVib.MontCount, ValCountr))        
        root.after(renderVib.TimeMont,simMonth,listMonth,MaxMonth)
    else:
        renderVib.stop_all()
        return
    renderVib.MontCount += 1

def ModeTotal(PixNow):
    NearCoun=NearestPixels(PixNow)
    renderVib.Countrys(NearCoun)
    

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

            Collision,Country=continent.CollisionDetect(Tou0)
            if(Collision):
                NearCoun.append(Country)
            else:
                if(i==0 and j==0):
                    NearCoun.append('Background')    
                    continue
                if(i+j == 4):
                    NearCoun.append(NearCoun[0])
                else:
                    NearCoun.append(NearCoun[-1]) 
    
    canvasTest.delete("all")
    renderSensorScreen(colors)

    return NearCoun


def CountryPix(PixNow):
    colorPix=image[PixNow[0], PixNow[1],:]
    Collision,Country=continent.CollisionDetect(colorPix)
    NearCoun=[]
    if(Collision):            
        NearCoun=Country
    else:                   
        NearCoun='Background'
    return NearCoun

def reset_all():
    renderVib.stop_all()
    renderVib.MontCount=0
    renderVib.countryBefore='Not'


def on_click(event):
    #print('click')
    global clickOn, circ
    if event.inaxes is not None:
        #print(clickOn)
        clickOn=True
        t01=[int(event.ydata+yMin), int(event.xdata+xMin)]
        
        if(Tot_Mounth.get()):
            ModeTotal(t01)
        else:            
            ModeMonth(t01)
        
        #print(NearCoun)

def off_click(event):
    global clickOn, circ
    clickOn=False
    reset_all()

def on_move(event):
    if event.inaxes is not None:
        #print(clickOn)
        if clickOn==True:
            t01=[int(event.ydata+yMin), int(event.xdata+xMin)]
            if(Tot_Mounth.get()):
                ModeTotal(t01)
#             else:            
#                 ModeMonth(t01)
            #print(NearCoun)


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
    Death_Cas.set(True)

    Tot_Mounth=IntVar()
    c2 = Checkbutton(root, text = "On:Total/Off:Monthly", variable=Tot_Mounth, justify=LEFT).pack(side=RIGHT)
    Tot_Mounth.set(True)


def main():

    #Create the base plot
    plot()
    print('Start...')
    root.mainloop()
    print ('Done')


if __name__ == '__main__':
    main()