from syntacts import *
from time import sleep,time
from math import sin
from math import pi
import keyboard  # using module keyboard

# Function to make sure export/import works
def check(signal):
    if signal is not None:
        print('Pass')
    else:
        print('Fail') 
#------------------------------------------

def printMenu():
    print('############### Menu ################')
    print('Press the key to listen to the signal')
    print(' z ==> signal_1')
    print(' x ==> signal_2')
    print(' c ==> signal_3')
    print(' v ==> signal_4')
    print(' b ==> signal_5')
    print(' n ==> signal_6')
    print(' m ==> signal_7')
    print(' a ==> signal_8')
    print(' s ==> signal_9')
    print(' d ==> signal_10')
    print(' f ==> signal_11')
    print(' g ==> signal_12')
    print(' h ==> signal_13')
    print(' j ==> signal_14')
    print(' Space ==> Stop')
    print(' Esc ==> End')
    print('#####################################')
#------------------------------------------


session = Session()

session.open()

# JSON format
sig1 = Library.import_signal('signals/signal_1.json')
print('Signal 1')
check(sig1)

sig2 = Library.import_signal('signals/signal_2.json')
print('Signal 2')
check(sig2)

sig3 = Library.import_signal('signals/signal_3.json')
print('Signal 3')
check(sig3)

sig4 = Library.import_signal('signals/signal_4.json')
print('Signal 4')
check(sig4)

sig5 = Library.import_signal('signals/signal_5.json')
print('Signal 5')
check(sig5)

sig6 = Library.import_signal('signals/signal_6.json')
print('Signal 6')
check(sig6)

sig7 = Library.import_signal('signals/signal_7.json')
print('Signal 7')
check(sig7)

sig8 = Library.import_signal('signals/signal_8.json')
print('Signal 8')
check(sig8)

sig9 = Library.import_signal('signals/signal_9.json')
print('Signal 9')
check(sig9)

sig10 = Library.import_signal('signals/signal_10.json')
print('Signal 10')
check(sig10)

sig11 = Library.import_signal('signals/signal_11.json')
print('Signal 11')
check(sig11)

sig12 = Library.import_signal('signals/signal_12.json')
print('Signal 12')
check(sig12)

sig13 = Library.import_signal('signals/signal_13.json')
print('Signal 13')
check(sig13)

sig14 = Library.import_signal('signals/signal_14.json')
print('Signal 14')
check(sig14)

printMenu()

# measure wall time
t0 = time()
flagT=True

totalTime = 4

brazil = Sine(446) * Envelope(totalTime,1)
colombia = Sine(84) * Envelope(totalTime,1)
peru = Sine(67) * Envelope(totalTime,1)
paraguay = Sine(8) * Envelope(totalTime,1)
argentina = Sine(74) * Envelope(totalTime,1)
bolivia = Sine(13) * Envelope(totalTime,1)

while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown        
        if(flagT):
            print('time: {},{}'.format(time() - t0, float(brazil.length)) )
            if ((time() - t0) >= brazil.length-0.1):
                session.play(0, brazil)
                session.play(1, brazil)
                session.play(2, brazil)
                session.play(3, brazil)
                session.play(4, brazil)
                session.play(5, brazil)
                session.play(6, brazil)
                session.play(7, brazil)
                print('Signal 2')
                t0=time()
#             session.play(0, brazil)     
#             sleep(brazil.length)
#         if keyboard.is_pressed('x'):  
#             print('Signal 2')
#             session.play(0, sig2)
#         if keyboard.is_pressed('c'):  
#             print('Signal 3')
#             session.play(0, sig3)
#         if keyboard.is_pressed('v'):  
#             print('Signal 4')
#             session.play(0, sig4)
#         if keyboard.is_pressed('b'):  
#             print('Signal 5')
#             session.play(0, sig5)
#         if keyboard.is_pressed('n'):  
#             print('Signal 6')
#             session.play(0, sig6)
#         if keyboard.is_pressed('m'):  
#             print('Signal 7')
#             session.play(0, sig7)
#         if keyboard.is_pressed('a'):  
#             print('Signal 8')
#             session.play(0, sig8)
#         if keyboard.is_pressed('s'):  
#             print('Signal 9')
#             session.play(0, sig9)
#         if keyboard.is_pressed('d'):  
#             print('Signal 10')
#             session.play(0, sig10)
#         if keyboard.is_pressed('f'):  
#             print('Signal 11')
#             session.play(0, sig11)
#         if keyboard.is_pressed('g'):  
#             print('Signal 12')
#             session.play(0, sig12)
#         if keyboard.is_pressed('h'):  
#             print('Signal 13')
#             session.play(0, sig13)
#         if keyboard.is_pressed('j'):  
#             print('Signal 14')
#             session.play(0, sig14)
#         if keyboard.is_pressed('space'):  
#             print('Stop')
#             session.stop(0)
#             printMenu()
#         if keyboard.is_pressed('esc'):  
#             print('Finished')
#             session.stop(0)
#             session.close()
#             break  # finishing the loop
    except:
        break  # if user pressed a key other than the given key the loop will break
