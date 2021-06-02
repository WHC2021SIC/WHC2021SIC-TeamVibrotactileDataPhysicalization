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

# with myFile:
#    writer = csv.writer(myFile, dialect='myDialect')
#    writer.writerows(myData)
i=0
NmeanNew=np.array([408.942958,138.473131,394.008856,308.599539,0.548101,-0.518616])
NstadNew=np.array([106.510489,204.268260,128.503499,149.708490,0.429971,0.476176])

loaded_model = tf.keras.models.load_model('xyForcePlateN2/')

class Country:
    def __init__(self, name,x,y,radius):
        self.name = name 
        self.Pos = np.array([x,y])
        self.radius = radius

class Continent:
    # creating list
    def __init__(self):
        self.list = [] 
        # appending instances to list 
        self.list.append( Country('Brasil', 10.5,7.5,3.0) )
        self.list.append( Country('Colombia', 3.0,3.0,2.0) )
        self.list.append( Country('Peru', 2.25,6.75,1.7) )
        self.list.append( Country('Bolivia', 6.0,9.0,1.7) )
        self.list.append( Country('paraguai', 7.5,11.25,1.7) )
        self.list.append( Country('Argentina', 6.0,15,2.2) )
        
    def CollisionDetect(self,xp,yp):
        for obj in self.list:
            dist=obj.Pos-np.array([xp,yp])            
            if(np.dot(dist,dist)<=(obj.radius*obj.radius)):
                print( obj.name, sep =' ' )
        
    

def normNew(x):
    return ((x - NmeanNew) / NstadNew)

def ratioSxSy(x):
        Sxnum=-(1/x[0])+(1/x[1])+(1/x[2])-(1/x[3])   
        Synum=-(1/x[0])-(1/x[1])+(1/x[2])+(1/x[3])
        Sden=(1/x[0])+(1/x[1])+(1/x[2])+(1/x[3])
        Sx = Sxnum/Sden
        Sy = Synum/Sden
        return np.array([Sx,Sy])
    
def resultCon(x):
    SxSy = ratioSxSy(x)
    val=np.concatenate((x,SxSy))
    return normNew(val)

def lengthVal(x):
    return np.sqrt(np.sum(np.power(x,2)))
    

# def unorm(n):
#     x=n[0] * 5.332927 + 8.400000
#     y=n[1] * 7.823059 + 12.000000
#     return np.array((x,y))

Nmean=5
values = [0]*4
mean10=np.empty((Nmean,4)) 
for j in range(Nmean):
    for i in range(4):
        #Read the specified ADC channel using the previously set gain value.
        values[i] = adc.read_adc(i, gain=GAIN)
    mean10[j,:]=values
meanT=np.mean(mean10, axis=0)

dataSqrtInit=lengthVal(resultCon(meanT))

print("dataSqrtInit: {}".format(dataSqrtInit))

continent = Continent() 

while True:
    # Read all the ADC channel values in a list.
    
    # Read the specified ADC channel using the previously set gain value.
    
    #mean10=np.empty((Nmean,4)) 
    #for j in range(Nmean):
    for i in range(4):
    # Read the specified ADC channel using the previously set gain value.
        values[i] = adc.read_adc(i, gain=GAIN)

    
    resultC=resultCon(np.array(values))
    #print("dataSqrtInit: {}".format(abs(lengthVal(resultC)-dataSqrtInit)))
    
    Pos=loaded_model.predict(resultC.reshape((1,6)))
    
    continent.CollisionDetect(float(Pos[0]),float(Pos[1]))
    
#     if lengthVal(resultC) > (dataSqrtInit+10):
#         #resultC=resultCon(np.array(values))
#         #Pos=loaded_model.predict(resultC.reshape((1,6)))
#         print("touch")
#     else:
#         print("NO touch")
        
    #Unpos=unorm(Pos)
    #print(Pos)
#     print(Unpos.shape)
    print("x: {}, y: {}".format(float(Pos[0]),float(Pos[1])))
    

   
    