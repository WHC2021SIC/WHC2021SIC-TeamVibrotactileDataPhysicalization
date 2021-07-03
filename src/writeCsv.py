import Adafruit_ADS1x15
import csv
from decimal import *
getcontext().prec = 2

adc = Adafruit_ADS1x15.ADS1015(address=0x49, busnum=1)

GAIN = 1

offset = [0]*4
offset[0]  = adc.read_adc(0, gain=GAIN)
offset[1]  = adc.read_adc(1, gain=GAIN)
offset[2]  = adc.read_adc(2, gain=GAIN)
offset[3]  = adc.read_adc(3, gain=GAIN)

print("please don't touch the board!..")

import numpy as np

CoordX=7.5
CoordY=5.25
Ndados=10000
minF=10.0
maxF=170.0

F1 = np.empty(Ndados, dtype=object)
F2 = np.empty(Ndados, dtype=object)
F3 = np.empty(Ndados, dtype=object)
F0 = np.empty(Ndados, dtype=object)
xR = np.empty(Ndados, dtype=object)
yR = np.empty(Ndados, dtype=object)
Fdist = np.empty(Ndados, dtype=object)
NmeanNow = np.empty(Ndados, dtype=object) 

csv.register_dialect('myDialect', delimiter=',', quoting=csv.QUOTE_NONE)

myFile = open('posFinalTouch/'+str(CoordX)+','+str(CoordY)+'.csv', 'w')

#NmeanRest=np.array([-326.27320,12.01916,-310.34624,222.99996])

def lengthVal(x):
    return np.sqrt(np.sum(np.power(x,2)))

Nda=0

Nmean=10

values = [0]*4
mean10=np.empty((Nmean,4)) 
for j in range(Nmean):
    for i in range(4):
        #Read the specified ADC channel using the previously set gain value.
        values[i] = adc.read_adc(i, gain=GAIN)
    mean10[j,:]=values
valInit=np.mean(mean10, axis=0)

print("start..")
while Nda<Ndados:
    # Read all the ADC channel values in a list.
    
    # Read the specified ADC channel using the previously set gain value.
    values = [0]*4
    #mean10=np.empty((Nmean,4)) 
    #for j in range(Nmean):
    for i in range(4):
        # Read the specified ADC channel using the previously set gain value.
        values[i] = adc.read_adc(i, gain=GAIN)
    #mean10[j,:]=values
        
    #meanT=np.mean(mean10, axis=0)
    #print(meanT)
    FdistC=lengthVal(values-valInit)
    
    if(FdistC>minF and FdistC<maxF):
        F0[Nda] = values[0]
        F1[Nda] = values[1]
        F2[Nda] = values[2]
        F3[Nda] = values[3]
        xR[Nda]=CoordX
        yR[Nda]=CoordY        
        NmeanNow[Nda]=valInit
        Fdist[Nda]=FdistC
        Nda=Nda+1
        if(Nda%100==0):
            print(Nda)
    elif(FdistC>maxF):        
        print("forca excessiva")
    else:        
        print("noTouch")
    #myData= [F0, F1, F2,F3]
    
#print(F0)
myData=np.array([F0, F1, F2,F3,xR,yR,NmeanNow,Fdist])
myData=myData.T
with myFile:
    writer = csv.writer(myFile, dialect='myDialect')
    writer.writerows(myData)
print("finish")
