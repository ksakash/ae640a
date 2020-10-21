import numpy as np
import matplotlib.pyplot as plt
import time

x0 = [0, 1, 2, 2, 1, 0]
y0 = [0, 1, 2, 3, 3, 4]

x1 = [0, 0, 0, 0, 0, 0]
y1 = [1, 2, 3, 2, 1, 0]

x2 = [1, 2, 3, 4, 4, 4]
y2 = [0, 1, 1, 2, 1, 0]

x3 = [1, 2, 3, 3, 4, 4]
y3 = [1, 2, 3, 4, 3, 4]

obsx = [2, 3, 1, 3, 1, 2]
obsy = [0, 0, 2, 2, 4, 4]

initialx = [0, 0, 1, 1]
initialy = [0, 1, 0, 1]

plt.scatter (initialx, initialy, c=['r','b','g','y'])
plt.scatter (obsx, obsy, c=['k','k','k','k','k','k'])
plt.ylim ((-1, 5))
plt.xlim ((-1, 5))
plt.pause (1)

for i in range (0, len (x0), 1):
    plt.plot (x0[i:i+2], y0[i:i+2], 'ro-')
    plt.plot (x1[i:i+2], y1[i:i+2], 'bo-')
    plt.plot (x2[i:i+2], y2[i:i+2], 'go-')
    plt.plot (x3[i:i+2], y3[i:i+2], 'yo-')
    plt.pause (1)

plt.show ()
