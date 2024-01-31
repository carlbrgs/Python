import random

# Fonction pour tester si un nombre est premier
def est_premier(n, k=128):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def generer_premier(taille):
    while True:
        n = random.getrandbits(taille)
        n |= (1 << taille - 1) | 1
        if est_premier(n):
            return n


def inverse_modulaire(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Fonction pour générer des clés RSA
def generer_cles_rsa(taille=2048):
    p = generer_premier(taille // 2)
    q = generer_premier(taille // 2)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    d = inverse_modulaire(e, phi)
    return ((e, n), (d, n))

# Fonction pour chiffrer un message avec RSA
def chiffrer_rsa(message, cle_publique):
    e, n = cle_publique
    message_int = int.from_bytes(message.encode('utf-8'), 'big')
    chiffre = pow(message_int, e, n)
    return chiffre

# Fonction pour déchiffrer un message avec RSA
def dechiffrer_rsa(chiffre, cle_privee):
    d, n = cle_privee
    message_int = pow(chiffre, d, n)
    message = message_int.to_bytes((message_int.bit_length() + 7) // 8, 'big').decode('utf-8')
    return message

def interface_utilisateur():
    cle_publique, cle_privee = generer_cles_rsa()
    
    while True:
        choix = input("Voulez-vous chiffrer ou déchiffrer un message? (C/D): ").lower()
        if choix == 'c':
            message = input("Entrez le message à chiffrer: ")
            message_chiffre = chiffrer_rsa(message, cle_publique)
            print(f"Message chiffré: {message_chiffre}")
        elif choix == 'd':
            chiffre = int(input("Entrez le message chiffré à déchiffrer (nombre entier): "))
            try:
                message_dechiffre = dechiffrer_rsa(chiffre, cle_privee)
                print(f"Message déchiffré: {message_dechiffre}")
            except ValueError:
                print("Le message chiffré n'est pas valide.")
        else:
            print("Choix invalide.")
        
        continuer = input("Voulez-vous continuer? (Oui/Non): ").lower()
        if continuer != 'oui':
            break

if __name__ == "__main__":
    interface_utilisateur()
