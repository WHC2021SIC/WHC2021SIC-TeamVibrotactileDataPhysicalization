import numpy as np
from syntacts import Library

#dataset colors of image sudamericaLowRes.png
ColColombia=[1., 0.56863, 0., 1.]
ColVen=[0.94902,  0.58431, 0.88235, 1.]
ColEcuador=[0.01176 ,0.,         0.71373,  1.        ]
ColPeru=[0.71373  ,0.,         0.01176, 1.]
ColBolivia=[0.23137 ,0.82353  ,0.63529 ,1.        ]
colParaguai=[0.99216, 0.         ,0.34902, 1.        ]
Colchile=[0.,         0.43137, 0.71373,  1.        ]
colArg=[0.5098, 0.11765, 0.50588,  1.        ]
Colguyana=[0.30980393, 0.13333334, 0.03529412, 1.        ]
ColSuri=[0.03529412, 0.20784314, 0.30980393, 1.        ]
French=[1.,         0.27058825, 0.27058825, 1.        ]
ColBrasil=[1.,        0.8666667, 0.        ,1.       ]
ColUruguai=[0.3098,  0.61961, 0.15294, 1.     ]
ColBack=[0.0,  0.0, 0.0, 0.]

class ColorCountry:
    def __init__(self, name,color):
        self.color=color
        self.name=name
        
    def collisionDetect(self,color):
        #print(color)
        res=np.dot(self.color-color,self.color-color)        
        if(res<0.05):
            return True
        else:
            return False

class Continent:
    # creating list
    def __init__(self):
        self.list = []
        self.objAntname="Init"
        # appending instances to list 
        self.list.append( ColorCountry('Colombia',ColColombia) )
        self.list.append( ColorCountry('Venezuela',ColVen))
        self.list.append( ColorCountry('Ecuador',ColEcuador))
        self.list.append( ColorCountry('Peru',ColPeru))
        self.list.append( ColorCountry('Bolivia',ColBolivia))
        self.list.append( ColorCountry('Paraguay',colParaguai))
        self.list.append( ColorCountry('Chile',Colchile) )
        self.list.append( ColorCountry('Argentina',colArg))
        self.list.append( ColorCountry('Guyana',Colguyana) )
        self.list.append( ColorCountry('Suriname',ColSuri) )
        self.list.append( ColorCountry('french',French) )
        self.list.append( ColorCountry('Brazil',ColBrasil) )
        self.list.append( ColorCountry('Uruguay',ColUruguai) )
        self.list.append( ColorCountry('Background',ColBack) )

    def CollisionDetect(self,color):
        col=-1
        for obj in self.list:         
            if(obj.collisionDetect(color)):
                #print( obj.name, sep =' ' )
                return True, obj.name
        if(col==-1):
            return False,-1

# Function to make sure export/import works
def check(signal):
    if signal is not None:
        print('Pass')
    else:
        print('Fail') 

Jan = Library.import_signal('months/jan.wav')
Feb = Library.import_signal('months/feb.wav')
Mar = Library.import_signal('months/mar.wav')
Apr = Library.import_signal('months/apr.wav')
May = Library.import_signal('months/may.wav')
Jun = Library.import_signal('months/jun.wav')
Jul = Library.import_signal('months/jul.wav')
Aug = Library.import_signal('months/aug.wav')
Sep = Library.import_signal('months/sep.wav')
Oct = Library.import_signal('months/oct.wav')
Nov = Library.import_signal('months/nov.wav')
Dec = Library.import_signal('months/dec.wav')

'''check(Jan)
check(Feb)
check(Mar)
check(Apr)
check(May)
check(Jun)
check(Jul)
check(Aug)
check(Sep)
check(Oct)
check(Nov)
check(Dec)'''

MonthsAudio=[Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec ]