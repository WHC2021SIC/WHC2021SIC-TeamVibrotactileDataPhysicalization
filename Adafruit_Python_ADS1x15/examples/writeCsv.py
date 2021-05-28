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

import numpy as np

CoordX=15
CoordY=15
Ndados=5000

F1 = np.empty(Ndados, dtype=object)
F2 = np.empty(Ndados, dtype=object)
F3 = np.empty(Ndados, dtype=object)
F0 = np.empty(Ndados, dtype=object)
xR = np.empty(Ndados, dtype=object)
yR = np.empty(Ndados, dtype=object) 

csv.register_dialect('myDialect', delimiter=',', quoting=csv.QUOTE_NONE)

myFile = open('posNewTouchedData/'+str(CoordX)+','+str(CoordY)+'.csv', 'w')
# with myFile:
#    writer = csv.writer(myFile, dialect='myDialect')
#    writer.writerows(myData)
Nda=0

Nmean=5
print("start..")
while Nda<Ndados:
    # Read all the ADC channel values in a list.
    
    # Read the specified ADC channel using the previously set gain value.
    values = [0]*4
    mean10=np.empty((Nmean,4)) 
    for j in range(Nmean):
        for i in range(4):
            # Read the specified ADC channel using the previously set gain value.
            values[i] = adc.read_adc(i, gain=GAIN)
        mean10[j,:]=values
        
    meanT=np.mean(mean10, axis=0)
    #print(meanT)
    F0[Nda] = meanT[0]
    F1[Nda] = meanT[1]
    F2[Nda] = meanT[2]
    F3[Nda] = meanT[3]
    xR[Nda]=CoordX
    yR[Nda]=CoordY
    Nda=Nda+1
    if(Nda%100==0):
        print(Nda)
    #myData= [F0, F1, F2,F3]
    
#print(F0)
myData=np.array([F0, F1, F2,F3,xR,yR])
myData=myData.T
with myFile:
    writer = csv.writer(myFile, dialect='myDialect')
    writer.writerows(myData)
print("finish")
