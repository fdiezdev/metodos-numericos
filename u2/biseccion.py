from math import *

eqn = str(input("Ingrese ecuacion: "))

# Definimos la funcion
def f(x):
    return eval(eqn)

# a -> limite inferior
# b -> limite superior
# t -> tolerancia ???
def biseccion(a, b, t):

    k = 0
    m = f(a)*f(b)
    
    if(m>0):
        print("En el intervalo no hay cambio de signo")
    else:

        while abs(a-b) > t:
            xR = (a+b)/2
            
            if(m<0): # Cambia de signo en [a,xR]
                b = xR # El nuevo limite superior es el valor medio
            if(m>0): # Cambia de signo en [xR,b]
                a = xR # El nuevo limite inferior es el valor medio

            print("La raiz esta en el subintervalo [",a,",",b,"] ")
            k = k+1
        
        print("La mejor aproximacion a la raiz es x",k,"=",xR)

xL = float(input("Limite superior: "))
xU = float(input("Limite inferior: "))
xT = float(input("Tolerancia: "))

biseccion(xL, xU, xT)