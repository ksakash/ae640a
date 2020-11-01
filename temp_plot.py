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

initialx = [x0[0]]
initialy = [y0[0]]

plt.scatter (initialx, initialy, c=['r'])
plt.ylim ((-1, 5))
plt.xlim ((-1, 5))
# plt.pause (1)

for i in range (0, len (x0), 1):
    plt.plot (x0[i:i+2], y0[i:i+2], 'ro-')
    # plt.pause (1)

plt.show ()
