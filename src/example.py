from syntacts import *
from time import sleep
from math import sin
from math import pi

s = Session()
s.open()

# Function to make sure export/import works
def check(signal):
    if signal is not None:
        print('Pass')
    else:
        print('Fail') 

x = Sine(440) * Triangle(20) * ASR(1,2,3)
y = Square(440, 1000) * ADSR(1,1,1,1)
z = Pwm(500,0.5) * Envelope(1)

x = Sine(440) * Envelope(1, 1.0)

s.play(0, x)
print(x.length)
sleep(x.length)
s.play(1, y)
sleep(y.length)

seq = Sequence()

seq << 1 << x << -2 << y
seq.insert(z, 4)

#Library.save_signal(seq,'python')
Library.export_signal(seq, 'music/python2.wav')
loaded = Library.import_signal('music/python2.wav')
check(loaded)

s.play(0,loaded)
sleep(loaded.length)

noise = Noise()
sp = Spatializer(s)
sp.set_position(0, (0,0))
sp.set_position(1, (1,0))
sp.target = (0,0)
sp.radius = 0.5
sp.play(noise)

t = 0
while t < 10:
    xPos = 0.5 + 0.5 * sin(2*pi*t)
    sp.target = (xPos, 0)
    sleep(0.01)
    t += 0.01

del sp