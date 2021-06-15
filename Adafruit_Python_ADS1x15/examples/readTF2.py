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

NmeanRest = np.array([326.27320,12.01916,310.34624,222.99996])

NmeanNew=np.array([82.669758,126.453971,83.662616,85.599579,311.351552,-0.157280,0.038515])
NstadNew=np.array([106.510489,204.268260,128.503499,149.708490,179.464143,45.116143,9.908787])

print("please don't touch the board!..")
loaded_model = tf.keras.models.load_model('Models/xyForcePlateN5/')

totalTime = 10

Cases_death=True #Cases:True, Death:False
Total_month=True #Total:True, Month:False

brazil = Sine(446) * Envelope(totalTime,1)

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
    
    if (LenVal>200.0 and LenVal<500.0):
        #res=np.array([ActVal,LenVal])
        res=np.append(ActVal,LenVal)
        #print("{}".format(res))
        resultC=resultCon(res)
        Pos=loaded_model.predict(resultC.reshape((1,7)))
        if(Pos[0]>15.0): Pos[0]=15.0
        if(Pos[1]>15.0): Pos[1]=15.0
        if(Pos[0]<0.0): Pos[0]=0.0
        if(Pos[1]<0.0): Pos[1]=0.0
        continent.CollisionDetect(float(Pos[0]),float(Pos[1]))
        print("x: {}, y: {}, f:{}".format(float(Pos[0]),float(Pos[1]), LenVal))
#         print("touch")
    #elif(LenVal>300.0):
        #print("forca excessiva")
    elif(LenVal<50.0):
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
    

   
    