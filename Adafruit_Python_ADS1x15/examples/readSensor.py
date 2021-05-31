import Adafruit_ADS1x15
import csv
from decimal import *
getcontext().prec = 2

adc = Adafruit_ADS1x15.ADS1015(address=0x49, busnum=1)

GAIN = 1

import numpy as np

while True:
    # Read all the ADC channel values in a list.
    
    # Read the specified ADC channel using the previously set gain value.
    values = [0]*4

    for i in range(4):
        # Read the specified ADC channel using the previously set gain value.
        values[i] = adc.read_adc(i, gain=GAIN)
    print(values)
        


