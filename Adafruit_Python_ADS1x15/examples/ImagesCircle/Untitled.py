import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from time import time,sleep
from itertools import count
import random

t0=time()

#plt.axis([0, 10, 0, 1])
y=[]
x=[]

index=count()

def animate(i):
    x.append(next(index))
    y.append(random.randint(0,5))
    plt.cla()
    plt.plot(x,y)
    plt.tight_layout()


def on_mouse_move(event):
    print('Event received:',event.x,event.y)


#ani = FuncAnimation(plt.gcf(), animate, interval=1000)
plt.connect('motion_notify_event',on_mouse_move)

for i in range(10):
    #print(i)
    x.append(next(index))
    y.append(random.randint(0,5))
    plt.cla()
    plt.plot(x,y)
    #plt.tight_layout()
    #sleep(0.1)    
    t2=time()
    plt.pause(0.001)
    print(time()-t2)

plt.show()