import matplotlib.pyplot as plt
import numpy as np

# set a seed to ensure reproducability
np.random.seed(100)

# build a random image
img = np.random.rand(10,10)

# create the image and save the artist 
img_artist = plt.imshow(img, interpolation='nearest')

# plot a red cross to "mark" the pixel in question
plt.plot(5,5,'rx', markeredgewidth=3, markersize=10)


def on_mouse_move(event):
    #print('Event received:',event.xdata,event.ydata)
    if event.inaxes is not None:
        print ("x:{},y:{}".format(event.xdata, event.ydata))
        # get the color at pixel 5,5 (use normalization and colormap)
        print (img_artist.cmap(img_artist.norm(img[int(event.ydata), int(event.xdata)])))
    else:
        print ('Clicked ouside axes bounds but inside plot window')


#ani = FuncAnimation(plt.gcf(), animate, interval=1000)
plt.connect('button_press_event',on_mouse_move)

#fig.canvas.callbacks.connect('button_release_event', off_click)

plt.axis('image')
plt.show()