import random

def est_premier(n, k=999):
    if n == 2 or n == 3:
        return True
    if n < 2 or n%2 == 0:
        return False
    r, d = 0, n - 1
    while d%2 == 0:
        r += 1
        d //= 2
    
    
    #test de Miller-Rabin pour avoir un nombre premier plus précis que le test de base précédent
    for g in range(k):
        a = random.randrange(2, n - 1) 
        
        #Pow permet de calculer à la puissance d, modulo n
        x = pow(a, d, n)
        if x != 1 and x != n - 1:
            for g in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
    return True

#test de la fonction est_premier
# print(est_premier(33))


def generer_premier(taille):
    while True:
        n = random.getrandbits(taille)
        n != (1 << taille - 1) | 1
        if est_premier(n):
            return n


def inverse_modulaire(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1


#test inverse_modulaire
# print(inverse_modulaire(5, 11))
#Dans ce cas, on calcule l'inverse modulaire de 5 modulo 11. 
# Le résultat est 9 parce que 5 * 9 est égal à 45, et 45 divisé par 11 donne un reste de 1.
# Donc, 9 est bien l'inverse modulaire de 5 modulo 11.


def generer_cles_rsa(taille=2048):
    p = generer_premier(taille // 2)
    q = generer_premier(taille // 2)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    d = inverse_modulaire(e, phi)
    return ((e, n), (d, n))


def chiffrer_rsa(message, cle_publique):
    e, n = cle_publique
    message_int = int.from_bytes(message.encode('utf-8'), 'big')
    chiffre = pow(message_int, e, n)
    return chiffre








        