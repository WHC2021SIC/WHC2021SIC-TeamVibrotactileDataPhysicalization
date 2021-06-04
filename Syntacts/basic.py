from syntacts import *
from time import sleep
from math import sin
from math import pi

s = Session()
s.open()

totalTime = 4

brazil = Sine(446) * Envelope(totalTime,1)
colombia = Sine(84) * Envelope(totalTime,1)
peru = Sine(67) * Envelope(totalTime,1)
paraguay = Sine(8) * Envelope(totalTime,1)
argentina = Sine(74) * Envelope(totalTime,1)
bolivia = Sine(13) * Envelope(totalTime,1)

s.play_all(peru)

sleep(totalTime)

s.play_all(colombia)

sleep(totalTime)

s.play_all(paraguay)

sleep(totalTime)

s.play_all(brazil)

sleep(totalTime)

s.play_all(argentina)

sleep(totalTime)

s.play_all(bolivia)

sleep(totalTime)


