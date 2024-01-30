def addition(nb1, nb2):
 nb1 = int(input('Rentrer un nombre: '))
 nb2 = int(input('Rentrer un autre nombre: '))
 return nb1 + nb2

def print_segment_arbre(n):
    for size in range(1, n+1, 2):
        print(('*' * size).center(n))

print_segment_arbre(5)