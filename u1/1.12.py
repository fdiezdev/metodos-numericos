import matplotlib.pyplot as plt
import numpy as np
from prettytable import PrettyTable

# * La escala de tiempo esta en dias
ti = 0
tf = 1
Δt = 0.1
k = 5


n = int((tf-ti)/Δt)

# Creamos "una columna" de tiempo que cada fila
# sea un valor de t separado 0.1 del anterior

t = np.zeros(n)

for i in range(n):
    t[i] = i/n


# Definimos la funcion expresada en la ecuacion dc/dt = -kc

def eqn(ke, ce):
    return -ke*ce

# Declaramos la condicion inicial de la ecuacion
# diferencial para que tenga solucion
c = np.zeros(n)
c[0] = 10

# Creamos el vector que alamacenara lo que nos devuelva la ecuacion
# De igual manera fijamos la condicion inicial
f = np.zeros(n)

for s in range(n-1):
    f[s] = eqn(k, c[s])
    c[s+1] = float(c[s]) + (Δt * float(f[s]))


# Hacemos una tabla
print("t     |       c        |      f(t,c)")
print("------+----------------+------------")
for i in range(n):
    print(t[i],'     ',c[i],'          ',f[i])
    print("------+----------------+------------")


plt.scatter(c, t)
plt.show()