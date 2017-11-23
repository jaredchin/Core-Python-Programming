import math
from random import random
import pylab
import numpy
# %pylab inline --no-import-all
import numpy import matplotlib
from matplotlib import pylab, mlab, pyplot np = numpy plt = pyplot from IPython.display import display from IPython.core.pylabtools import figsize, getfigs
from pylab import * from numpy import *
pylab.rcParams['figure.figsize'] = (12, 6)

width = 2048; height = 1024
world = numpy.zeros((height+1, width+1, 3))
world[:,:,2] = 0.75

draw = lambda img: plt.imshow(img); plt.show()
draw(world)