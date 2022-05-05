import csv
from re import X
import matplotlib.pyplot as plt
import numpy as np

imax = 60 # nro. max de dias que tiene la tabla

with open('u5\ejercicio_covid.csv') as file:

    r = csv.reader(file)

    k = 0
    date = ['']*imax
    cases = [0.0]*imax

    for i in r:
        print(i)

        date[k] = i[0]
        cases[k] = i[1]

        if k > 60:
            break
        
        k = k + 1
    date.remove(date[0])
    cases.remove(cases[0])

    print(date)
    print(cases)

    plt.scatter(sorted(date),sorted(cases))
    plt.grid(axis='x')
    ax = plt.gca()
    plt.draw()

    ax.set_xticklabels(ax.get_xticks(), rotation = 45)
    plt.show()

    