import matplotlib.pyplot as plt
import numpy as np
from math import *

# Definimos variables fijas
ti = 0
tf = 10
Δt = 0.5
A = 1200
Q = 500
y0 = 0

# Definimos la funcion
def eqn(a):
    # a = t
    return 3*(Q/A)*(sin(a)**2)-(Q/A)


n = int((tf-ti)/Δt)

t = np.zeros(n+1)
y = np.zeros(n+1)

t[0] = ti
y[0] = y0

f = np.zeros(n+1)

print(" t   |   y   |   f   |")
for i in range(n):
    t[i+1] = float(t[i] + Δt)
    f[i] = eqn(t[i])
    y[i+1] = y[i] + ( f[i] * Δt )

for i in range(n+1):
    print("-----+-------+-------+")
    print(t[i],"    ",y[i]," ",f[i])


