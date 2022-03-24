import numpy as np

imax = 100

# eqn = input("Ingrese ecuacion: ")

def f(x):
    return (2*x)+1

# a -> limite inferior
# b -> limite superior
# t -> tolerancia
def regfal(a, b, t):

    # Para reducir la evaluacion de funciones
    fa = f(a)
    fb = f(b)

    # Variables
    xl = a
    xu = b
    xr = xu
    xv = 0
    k = 0
    ea = 0

    while ea > t or k >= imax:
        
        xv = xr
        xr = b - ( (fb * (a-b) ) / ( fa-fb ) )

        if xr != 0:
            ea = abs((xr-xv)/xr)

        k = k + 1

        test = f(xl) * f(xr)

        if(test < 0): # Hay un cambio de signo en [a, xl]
            xu = xr
            fu = f(xl)
        else:
            xl = xr
            fl = f(xr)

    print("----------\n","xr: ", xr, "\n", "k: ",k) 

xL = float(input("Ingrese xl: "))
xU = float(input("Ingrese xu: "))
eS = float(input("Ingrese es: "))
regfal(xL, xU, eS)