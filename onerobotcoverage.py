import numpy as np
import matplotlib.pyplot as plt
import time

x0 = []
y0 = []

f = open ('robotx0.plan', 'r')
lines = f.readlines()
f.close ()

for line in lines:
    (x, y) = (int (line.split(' ')[0]), int (line.split(' ')[1]))
    x0.append (x)
    y0.append (y)

print (x0)
print (y0)

obsx = [2, 3, 1, 3, 1, 2]
obsy = [0, 0, 2, 2, 4, 4]

initialx = [0]
initialy = [0]

plt.scatter (initialx, initialy, c=['r'])
plt.scatter (obsx, obsy, c=['k','k','k','k','k','k'])
plt.ylim ((-1, 5))
plt.xlim ((-1, 5))
plt.pause (1)

for i in range (0, len (x0), 1):
    plt.plot (x0[i:i+2], y0[i:i+2], 'ro-')
    plt.pause (1)

plt.show ()
