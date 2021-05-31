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
Ndados = 5000

F1 = np.empty(Ndados, dtype=object)
F2 = np.empty(Ndados, dtype=object)
F3 = np.empty(Ndados, dtype=object)
F0 = np.empty(Ndados, dtype=object) 

csv.register_dialect('myDialect', delimiter=',', quoting=csv.QUOTE_NONE)

myFile = open('positionsTouchedData/3,0.csv', 'w')
# with myFile:
#    writer = csv.writer(myFile, dialect='myDialect')
#    writer.writerows(myData)
i=0
NmeanNew=np.array([385.350284,132.483951,366.454000,355.273467])
NstadNew=np.array([109.484312,185.298980,176.520386,201.882096])

loaded_model = tf.keras.models.load_model('xyForcePlate6/')

def normNew(x):
    return ((x - NmeanNew) / NstadNew)

# def unorm(n):
#     x=n[0] * 5.332927 + 8.400000
#     y=n[1] * 7.823059 + 12.000000
#     return np.array((x,y))

Nmean=5

while True:
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
    #print(values)
    valueN=normNew(meanT)
    #valueN=normNew(np.array(values))
    #print(valueN)
    #valueN=meanT
    #print(valueN)
    Pos=loaded_model.predict(valueN.reshape((1,4)))
    #Unpos=unorm(Pos)
    #print(Pos)
#     print(Unpos.shape)
    print("x: {}, y: {}".format(Pos[0],Pos[1]))
#     F0[i] = adc.read_adc(0, gain=GAIN)
#     F1[i] = adc.read_adc(1, gain=GAIN)
#     F2[i] = adc.read_adc(2, gain=GAIN)
#     F3[i] = adc.read_adc(3, gain=GAIN)
    
    #myData= [F0, F1, F2,F3]
#print(F0)
# myData= [F0, F1, F2,F3]
# #myData.transpose()
# with myFile:
#     writer = csv.writer(myFile, dialect='myDialect')
#     writer.writerows(myData)

   
    