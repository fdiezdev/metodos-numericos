from math import *
import numpy as np

n = int(input("Ingrese dimension del sistema: "))
m = int(input("Ingrese cantidad de ecuaciones: "))

print("La dimension del sistema es ",n,"x",m)

# n -> filas
# m -> columnas

def matrix(n, m):
    
    N = [0]*n # Vector fila
    M = [0]*m # Vector columna

    for i in range(n):
        for j in range(m):
            
            M[j] = float(input("a"+str(i+1)+str(j+1)+"="))
        
        N[i] = M
        M = [0]*m
        

    return N


M = matrix(n, m)
print("M = "+str(M))
print("dim(M)="+str(len(M)*len(M[0])))
 

def reduc(M):

    n =  len(M) # Numero de filas de la matriz
    m = len(M[0])
    print ("n=",n," | m=",m)
    k = 0 # Contador para seleccionar la fila pivote

    for i in range(n-1):
        p = M[k] # Fila pivote

        for j in range(m-1):

            f = M[i+1][j]/float(p[j])
            print("f=",f)
            # M[i+1] = M[i+1] - [i * f for i in p]
            M[i+1] = np.subtract(M[i+1],[i * f for i in p])
        
        k = k+1
        print("F",i+2,"'=",M[i+1])
        print("M=",M)

reduc(M)