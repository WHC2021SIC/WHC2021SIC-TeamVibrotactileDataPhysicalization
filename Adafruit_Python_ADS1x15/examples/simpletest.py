# Simple demo of reading each analog input from the ADS1x15 and printing it to
# the screen.
# Author: Tony DiCola
# License: Public Domain
import time

# Import the ADS1x15 module.
import Adafruit_ADS1x15
from decimal import *
getcontext().prec = 2
# Create an ADS1115 ADC (16-bit) instance.
#adc = Adafruit_ADS1x15.ADS1115()

# Or create an ADS1015 ADC (12-bit) instance.
#adc = Adafruit_ADS1x15.ADS1015()

# Note you can change the I2C address from its default (0x48), and/or the I2C
# bus by passing in these optional parameters:
adc = Adafruit_ADS1x15.ADS1015(address=0x49, busnum=1)

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
GAIN = 1

print('Reading ADS1x15 values, press Ctrl-C to quit...')
# Print nice channel column headers.
print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*range(4)))
print('-' * 37)
# Main loop.

offset = [0]*4
offset[0]  = adc.read_adc(0, gain=GAIN)
offset[1]  = adc.read_adc(1, gain=GAIN)
offset[2]  = adc.read_adc(2, gain=GAIN)
offset[3]  = adc.read_adc(3, gain=GAIN)

print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*offset))


while True:
    # Read all the ADC channel values in a list.
    values = [0]*4
    for i in range(4):
        # Read the specified ADC channel using the previously set gain value.
        values[i] = round(adc.read_adc(i, gain=GAIN) - offset[i],2)
        # Note you can also pass in an optional data_rate parameter that controls
        # the ADC conversion time (in samples/second). Each chip has a different
        # set of allowed data rate values, see datasheet Table 9 config register
        # DR bit values.
        #values[i] = adc.read_adc(i, gain=GAIN, data_rate=128)
        # Each value will be a 12 or 16 bit signed integer value depending on the
        # ADC (ADS1015 = 12-bit, ADS1115 = 16-bit).
    # Print the ADC values.
#     Sx_Num=(-1/values[0])+(1/values[1])+(1/values[2])-(1/values[3])
#     Sx_Den=(1/values[0])+(1/values[1])+(1/values[2])+(1/values[3])
#     Sy_Num=(-1/values[0])-(1/values[1])+(1/values[2])+(1/values[3])
#     Sx=Sx_Num/Sx_Den
#     Sy=Sy_Num/Sx_Den
    print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*values))
   
    #if values[0] > 100 or values[1] > 100 or values[2] > 100 or values[3] > 100 or values[0] < -100 or values[1] < -100 or values[2] < -100 or values[3] < -100:
     #   offset[0]  = adc.read_adc(0, gain=GAIN)
     #   offset[1]  = adc.read_adc(1, gain=GAIN)
     #   offset[2]  = adc.read_adc(2, gain=GAIN)
     #   offset[3]  = adc.read_adc(3, gain=GAIN)
   
   
    if values[0] > 14 and values[0] < 74:
        if values[1] > -28 and values[1] < 38:
            if values[2] > -16 and values[2] < 44:
                if values[3] > -52 and values[3] < 8:
                   print ('BRAZIL')
   
    if values[0] > -8 and values[0] < 52:
        if values[1] > 23 and values[1] < 83:
            if values[2] > -46 and values[2] < 14:
                if values[3] > -27 and values[3] < 33:
                   print ('PERU')
   
    if values[0] > 31 and values[0] < 91:
        if values[1] > 50 and values[1] < 120:
            if values[2] > -37 and values[2] < 27:
                if values[3] > -48 and values[3] < 18:
                   print ('ARGENTINA') 
   
    time.sleep(0.1)
