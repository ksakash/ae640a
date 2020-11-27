import numpy as np
import matplotlib.pyplot as plt
import time

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

(x0, y0) = readInput ('temp0.plan')
(x1, y1) = readInput ('temp1.plan')
(x2, y2) = readInput ('temp2.plan')
(x3, y3) = readInput ('temp3.plan')

initialx = [x0[0], x1[0], x2[0], x3[0]]
initialy = [y0[0], y1[0], y2[0], y3[0]]

plt.scatter (initialx, initialy, c=['r','b','g','y'])
plt.ylim ((-1, 5))
plt.xlim ((-1, 5))
plt.pause (1)

for i in range (0, len (x0), 1):
    plt.plot (x0[i:i+2], y0[i:i+2], 'r--')
    plt.plot (x1[i:i+2], y1[i:i+2], 'b--')
    plt.plot (x2[i:i+2], y2[i:i+2], 'g--')
    plt.plot (x3[i:i+2], y3[i:i+2], 'y--')
    plt.pause (1)

plt.show ()
