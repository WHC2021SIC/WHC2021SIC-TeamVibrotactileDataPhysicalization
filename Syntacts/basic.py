from syntacts import *
from time import sleep
from math import sin
from math import pi

s = Session()
s.open()

x = Sine(446) * Envelope(0.9)

s.play(0, x)
s.play(1, x)
s.play(2, x)
s.play(3, x)
s.play(4, x)
s.play(5, x)
s.play(6, x)
s.play(7, x)

