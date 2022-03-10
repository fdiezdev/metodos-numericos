import matplotlib.pyplot as plt

m = 68.1
c = 12.5
g = 9.8
ti = 0
tf = 12
dt = 2 # Este es el "paso" que yo tomo

n = int(((tf-ti)/dt))
print("n: "+ str(n))

# Creamos dos vectores para v y t con dimension n
# luego en el ciclo for modificamos indice a indice
v = [0.0]*n
t = [0.0]*n

for i in range(n-1):
    print(i)
    t[i+1] = t[i] + dt
    v[i+1] = v[i]+g-(c/m*v[i])*dt
    print(t[i+1], v[i+1])

plt.plot(t, v)
plt.show()