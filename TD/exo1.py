from math import sqrt
from math import pi

# Exercice 1
def aire_rectangle():
    longueur = int(input('Rentrer la longueur: '))
    largeur = int(input('Rentrer la largeur: '))
    if longueur <= 0 or largeur <= 0:
        print('Saisir des valeurs positives')
    else:
        print(longueur * largeur)

#aire_rectangle()
    
def resteDivision():
    a = int(input('Rentrer un nombre: '))
    b = int(input('Rentrer un autre nombre: '))
    if b <= 0 or a <= 0:
        print('Division par 0 impossible')
    else: 
        print(a % b)

#resteDivision()

def perimetreCercle():
    rayon = float(input('Rentrer le rayon du cercle: '))
    if rayon <= 0:
        print('Saisir une valeur positive')
    else:
        print(2 * pi * rayon)

#perimetreCercle()
    
def lePlusGrand():
    a = int(input('Rentrer un nombre: '))
    b = int(input('Rentrer un autre nombre: '))
    if a > b:
        print(a)
    else:
        print(b)

#lePlusGrand()

def racineCarree(nb):
    if nb < 0:
        print('Saisir un nombre positif')
    else:
        print(sqrt(nb))

def polynomeSecondDegre(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return('Pas de solution')
    elif delta == 0:
        return(-b/(2*a))
    else:
        print("x1 = ", (-b-sqrt(delta))/(2*a))
        print("x2 = ", (-b+sqrt(delta))/(2*a))

#a = float(input('Rentrer un a: '))
#b = float(input('Rentrer un b: '))
#c = float(input('Rentrer un c: '))
#polynomeSecondDegre(a, b, c)


def etoile(ligne):
    for i in range(1, ligne+1):
        print('*' * i)
etoile(5)

        


