import numpy as np
import matplotlib.pyplot as plt
import time

x0 = []
y0 = []

x1 = []
y1 = []

def readInput (filename):
    f = open (filename, 'r')
    lines = f.readlines()
    f.close ()
    x_ = []
    y_ = []

    for line in lines:
        (x, y) = (int (line.split(' ')[0]), int (line.split(' ')[1]))
        x_.append (x)
        y_.append (y)

    return (x_, y_)

(x0, y0) = readInput ('roboty0.plan')
(x1, y1) = readInput ('roboty1.plan')

obsx = [2, 3, 1, 3, 1, 2]
obsy = [0, 0, 2, 2, 4, 4]

initialx = [x0[0], x1[0]]
initialy = [y0[0], y1[0]]

plt.scatter (initialx, initialy, c=['r','g'])
plt.scatter (obsx, obsy, c=['k','k','k','k','k','k'])
plt.ylim ((-1, 5))
plt.xlim ((-1, 5))
plt.pause (1)

for i in range (0, len (x0), 1):
    plt.plot (x0[i:i+2], y0[i:i+2], 'r--')
    plt.plot (x1[i:i+2], y1[i:i+2], 'g--')
    plt.pause (1)

plt.show ()
