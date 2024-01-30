import random
from math import exp

def TableImpaire(n):
    table = []
    for i in range(1, n+1):
        if i % 2 == 1:
            table.append(i)
    return table

def tableRandom(n):
    table = []
    for i in range(1, n):
        element = random.uniform(-1, 1)
        table.append(element)
    return(table)

#print(tableRandom(5))

L = [random.uniform(-1, 1) for i in range(5)]
#print(L)

def expression(element):
    return 0.83 * exp(-0.04982 * (element - 1))


def bouclier(intensite):
    while intensite <= 0:
        intensite = float(input('Rentrer l\'intensité du laser: '))
    intensite_alter = intensite
    tour = 0
    while intensite_alter > intensite * 0.25:
        intensite_alter = expression(intensite_alter)
        tour += 1

    return(tour)

intensite = float(input('Rentrer l\'intensité du laser: '))
print(bouclier(intensite))   



