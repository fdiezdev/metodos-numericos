from math import *

imax = 100 # Condicion de corte

# Definimos la funcion

eqn = str(input("Ingrese ecuacion: "))

def f(x):
    return eval(eqn)

# a -> limite inferior
# b -> limite superior
# t -> error de tolerancia ???
def biseccion(a, b, t):

    n1=a
    n0=b

    k = 0

    if(f(a)*f(b)>0):
        print("En el intervalo no hay cambio de signo")
    else:
        while (abs(n1-n0)>=t or k >= imax):
            n1 = n0
            n0 = (a+b)/2

            if(f(a)*f(n0)<0): # Cambia de signo en [a,n0]
                b = n0 # El nuevo limite superior es el valor medio
            if(f(n0)*f(b)<0): # Cambia de signo en [n0,b]
                a = n0 # El nuevo limite inferior es el valor medio

            print("[",a,",",b,"] ")
            k = k+1
            
        print("La mejor aproximacion a la raiz es x",k,"=",n0)

xL = float(input("Limite superior: "))
xU = float(input("Limite inferior: "))
xT = float(input("Tolerancia: "))

biseccion(xL, xU, xT)