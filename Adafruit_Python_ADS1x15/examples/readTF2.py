from syntacts import *
from time import sleep, time
from math import sin
from math import pi

import Adafruit_ADS1x15
import csv
import tensorflow as tf
from decimal import *
getcontext().prec = 2

adc = Adafruit_ADS1x15.ADS1015(address=0x49, busnum=1)

GAIN = 1

offset = [0]*4
offset[0]  = adc.read_adc(0, gain=GAIN)
offset[1]  = adc.read_adc(1, gain=GAIN)
offset[2]  = adc.read_adc(2, gain=GAIN)
offset[3]  = adc.read_adc(3, gain=GAIN)

import numpy as np

s = Session()
s.open()

# measure wall time
t0 = time()
flagT=True

# with myFile:
#    writer = csv.writer(myFile, dialect='myDialect')
#    writer.writerows(myData)
i=0
#NmeanNew=np.array([408.942958,138.473131,394.008856,308.599539,0.548101,-0.518616])
#NstadNew=np.array([106.510489,204.268260,128.503499,149.708490,0.429971,0.476176])

NmeanNew=np.array([82.669758,126.453971,83.662616,85.599579,311.351552,-0.157280,0.038515])
NstadNew=np.array([106.510489,204.268260,128.503499,149.708490,179.464143,45.116143,9.908787])

print("please don't touch the board!..")
loaded_model = tf.keras.models.load_model('Models/xyForcePlateN6/')

totalTime = 10

brazil = Sine(446) * Envelope(totalTime,1)

class Country:
    def __init__(self, name,x,y,radius,fsom,tsom):
        self.name = name 
        self.Pos = np.array([x,y])
        self.radius = radius
        self.som=Sine(fsom) * Envelope(tsom,1)

class Continent:
    # creating list
    def __init__(self):
        self.t0=time()-totalTime
        self.timeSom=totalTime
        self.list = []
        self.objAntname="Init"
        # appending instances to list 
        self.list.append( Country('Brasil', 10.5,7.5,3.0,446,self.timeSom) )
        self.list.append( Country('Colombia', 3.0,3.0,2.0,84,self.timeSom) )
        self.list.append( Country('Peru', 2.25,6.75,1.7,67,self.timeSom) )
        self.list.append( Country('Bolivia', 6.0,9.0,1.5,13,self.timeSom) )
        self.list.append( Country('paraguai', 7.5,11.25,1.5,8,self.timeSom) )
        self.list.append( Country('Argentina', 6.0,15,2.2,74,self.timeSom) )
        self.list.append( Country('Argentina', 6.0,12.0,1.5,74,self.timeSom) )
        
    def CollisionDetect(self,xp,yp):
        for obj in self.list:
            dist=obj.Pos-np.array([xp,yp])            
            if(np.dot(dist,dist)<=(obj.radius*obj.radius)):
                print( obj.name, sep =' ' )
                #s.play_all(obj.som)
                
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
                
                    
def normNew(x):
    return ((x - NmeanNew) / NstadNew)

def ratioSxSy(x):
    try:
        Sxnum=-(1/x[0])+(1/x[1])+(1/x[2])-(1/x[3])   
        Synum=-(1/x[0])-(1/x[1])+(1/x[2])+(1/x[3])
        Sden=(1/x[0])+(1/x[1])+(1/x[2])+(1/x[3])
        Sx = Sxnum/Sden
        Sy = Synum/Sden
        return np.array([Sx,Sy])
    except:        
        return np.array([-1,-1])
    
def resultCon(x):
    SxSy = ratioSxSy(x)
    val=np.concatenate((x,SxSy))
    return normNew(val)

def lengthVal(x):
    return np.sqrt(np.sum(np.power(x,2)))
    

Nmean=5
values = [0]*4
mean10=np.empty((Nmean,4)) 
for j in range(Nmean):
    for i in range(4):
        #Read the specified ADC channel using the previously set gain value.
        values[i] = adc.read_adc(i, gain=GAIN)
    mean10[j,:]=values
valInit=np.mean(mean10, axis=0)

#dataSqrtInit=lengthVal(resultCon(meanT))

#print("dataSqrtInit: {}".format(dataSqrtInit))

continent = Continent()



print("Start")
while True:
    
    #mean5=np.empty((Nmean,4)) 
    #for j in range(Nmean):
    for i in range(4):
        #Read the specified ADC channel using the previously set gain value.
        values[i] = adc.read_adc(i, gain=GAIN)
    #mean5[j,:]=values
    #valCur=np.mean(mean5, axis=0)

    ActVal= values-valInit
    LenVal=lengthVal(ActVal)
    
    if (LenVal>10.0 and LenVal<190.0):
        #res=np.array([ActVal,LenVal])
        res=np.append(ActVal,LenVal)
        #print("{}".format(res))
        resultC=resultCon(res)
        Pos=loaded_model.predict(resultC.reshape((1,7)))
        continent.CollisionDetect(float(Pos[0]),float(Pos[1]))
        print("x: {}, y: {}, f:{}".format(float(Pos[0]),float(Pos[1]), LenVal))
#         print("touch")
    elif(LenVal>190.0):        
        print("forca excessiva")
    else:
        s.stop(0)
        s.stop(1)
        s.stop(2)
        s.stop(3)
        s.stop(4)
        s.stop(5)
        s.stop(6)
        s.stop(7)
        continent.t0=time()-continent.timeSom
        
    #Unpos=unorm(Pos)
    #print(Pos)
#     print(Unpos.shape)
    #print("x: {}, y: {}".format(float(Pos[0]),float(Pos[1])))
    

   
    