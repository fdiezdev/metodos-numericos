import matplotlib.pyplot as plt
import numpy as np

m = 68.1
c = 12.5
g = 9.8
ti = 0
tf = 12
dt = 2 # Este es el "paso" que tomo

n = int(((tf-ti)/dt))
# print("n: "+ str(n))

v = np.zeros(n)
t = np.zeros(n)

for i in range(n-1):
    print(i)
    t[i+1] = t[i] + dt
    v[i+1] = v[i]+g-(c/m*v[i])*(t[i+1]-t[i])
    print(t[i+1], v[i+1])

plt.plot(t, v)
plt.show()