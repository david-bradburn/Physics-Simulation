import numpy as np

import math
import matplotlib.pyplot as plt

delta_t = 0.01
g = -9.81
v_initial = 0
d_initial = 0

def force_to_acceleration(force, mass):
    return force/mass


def velocity_update(v_0, a, delta_t):
    return v_0 + a*delta_t


def position_update(d_0, v_0, a, delta_t):
    return d_0 + velocity_update(v_0, a, delta_t)*delta_t



v_cur = v_initial
d_cur = d_initial

for i in range(100):
    plt.figure(1)
    v_new = velocity_update(v_cur, g, delta_t)
    plt.plot(, '-')
    v_cur = v_new


    plt.figure(2)
    d_new = position_update(d_cur, v_cur, g, delta_t)
    plt.plot(d_new, 'x')
    d_cur = d_new

plt.show()





