import matplotlib.pyplot as pt
import numpy as np

x=np.arange(1,11)
y=10*x+14
pt.plot(x,y,"b--",linewidth=2,marker='o',mec='k',mfc='r')
pt.show()