import numpy as np
import math
import time
import matplotlib.pyplot as plt

I = np.array ([[1,0,0],
               [0,1,0],
               [0,0,1]])

R0 = np.array ([[1,0,0],
                [0,1,0],
                [0,0,1]])

J = np.array ([[1,0,0],
               [0,1,0],
               [0,0,2]])

Kp = 10
Kd = 10

PI = 3.14285714286

def getWErr (curr, des, R, Rd):
    err = curr - (R.transpose ().dot (Rd)).dot (des)
    return err

def getRotErr (curr, des):
    err = (des.transpose ().dot (curr) - curr.transpose ().dot (des))/2
    return err

def getVMap (a_hat):
    ret = np.array ([a_hat[2][1], a_hat[0][2], a_hat[1][0]])
    return ret

def getHatMap (a):
    ax = np.array ([[0,-a[2],a[1]],
                    [a[2],0,-a[0]],
                    [-a[1],a[0],0]])
    return ax

def getControlInput (er, ew, Kp, Kd):
    u = -Kp * getVMap (er) - Kd * ew
    return u

def getTargetRot (W, step, Rd):
    return getExp (W, step).dot (Rd)

def getTargetW (t, f):
    ret = np.array ([math.sin (2*PI*f*t), math.sin (2*PI*f*t), 0])
    return ret

def getAxTheta (W):
    norm = np.linalg.norm (W)
    if norm == 0:
        return (0, np.array ([0,0,0]))
    unit = W/norm
    return (norm, unit)

def getRot (step, W, R):
    return getExp (W, step).dot (R)

def getW (u, J, W, step):
    temp = np.cross (J.dot (W), W) + u
    J_inv = np.linalg.inv (J)
    w_dot = J_inv.dot (temp)
    new_w = W + w_dot * step
    return new_w

def getExp (W, step):
    (theta, a) = getAxTheta (step * W)
    ax = getHatMap (a)
    ret = I + math.sin (theta) * ax + (1 - math.cos (theta)) * ax.dot (ax)
    return ret

f = 20

start = 0
end = 1.5/f
step = 0.005

num = int ((end - start) / step)

R = R0
W = np.array ([0, 0, 0])
Rd = R0

W_array = []
Wd_array = []
time_array = []

for i in range (num):
    t = start + i * step
    Wd = getTargetW (t, f)
    Rd = getTargetRot (Wd, step, Rd)
    ew = getWErr (W, Wd, R, Rd)
    er = getRotErr (R, Rd)
    u = getControlInput (er, ew, Kp, Kd)
    W_ = getW (u, J, W, step)
    R = getRot (step, W_, R)
    W = W_
    W_array.append (np.linalg.norm (W))
    Wd_array.append (np.linalg.norm (Wd))
    time_array.append (t)

plt.plot (time_array, W_array, label = "|W|")
plt.plot (time_array, Wd_array, label = "|Wd|")

plt.legend ()
plt.show ()
