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
while i < Ndados:
    # Read all the ADC channel values in a list.
    
    # Read the specified ADC channel using the previously set gain value.
    F0[i] = adc.read_adc(0, gain=GAIN)
    F1[i] = adc.read_adc(1, gain=GAIN)
    F2[i] = adc.read_adc(2, gain=GAIN)
    F3[i] = adc.read_adc(3, gain=GAIN)
    
    #myData= [F0, F1, F2,F3]
    i=i+1
#print(F0)
myData= [F0, F1, F2,F3]
#myData.transpose()
with myFile:
    writer = csv.writer(myFile, dialect='myDialect')
    writer.writerows(myData)

   
    