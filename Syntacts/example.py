from syntacts import *
from time import sleep
from math import sin
from math import pi

s = Session()
s.open()

x = Sine(440) * Triangle(20) * ASR(1,2,3)
y = Square(440, 1000) * ADSR(1,1,1,1)
z = Pwm(500,0.5) * Envelope(1)

s.play(2, x)
sleep(x.length)



