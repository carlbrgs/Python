from cryptography.hazmat.backends import default_backend        # librairie de cryptographie pour le chiffrement RSA
from cryptography.hazmat.primitives.asymmetric import rsa       # librairie de cryptographie pour le chiffrement RSA
from cryptography.hazmat.primitives import hashes               # librairie de cryptographie pour le hashage
from cryptography.hazmat.primitives.asymmetric import padding   # librairie de cryptographie pour le padding

#----------------------------------------------#

# Chiffrement de substitution (Décalage de César)
def chiffrement_substitution(texte, decalage):
    """
    Chiffre un texte en utilisant le chiffrement de substitution. (Décalage de César ROT)
    texte : str
    decalage : int
    """
    resultat = ""
    for i in range(len(texte)):
        char = texte[i]
        # Si le caractère est une lettre de l'alphabet
        if char.isalpha():
            # On récupère le code ASCII de la lettre et on le ramène entre 0 et 25 
            # en vériiant si la lettre est minuscule ou majuscule (97 = a, 65 = A tableau ASCII)
            ascii_offset = 97 if char.islower() else 65
            # On applique le décalage sur le code ASCII et on ramène le résultat entre 0 et 25
            resultat += chr((ord(char) - ascii_offset + decalage) % 26 + ascii_offset)
        else:
            # Si le caractère n'est pas une lettre de l'alphabet, on le laisse tel quel
            resultat += char
    return resultat

# Déchiffrement de substitution (Décalage de César)
def dechiffrement_substitution(texte, decalage):
    """
    Déchiffre un texte en utilisant le chiffrement de substitution. (Décalage de César ROT)
    texte : str
    decalage : int
    """
    # On utilise un décalage négatif pour déchiffrer le texte
    return chiffrement_substitution(texte, -decalage)

#----------------------------------------------#²²²

# Chiffrement affine (a*x + b)
def chiffrement_affine(texte, a, b):
    """
    Chiffre un texte en utilisant le chiffrement affine. (a*x + b)
    texte : str
    a : int
    b : int
    """
    resultat = ""
    for char in texte:
        # Si le caractère est une lettre de l'alphabet
        if char.isalpha():   
            # On récupère le code ASCII de la lettre et on le ramène entre 0 et 25 
            # en vériiant si la lettre est minuscule ou majuscule (97 = a, 65 = A tableau ASCII)
            ascii_offset = 97 if char.islower() else 65
            char_code = ord(char) - ascii_offset
            # On applique la formule de chiffrement affine et on ramène le résultat entre 0 et 25
            resultat += chr((a * char_code + b) % 26 + ascii_offset)
        else:
            # Si le caractère n'est pas une lettre de l'alphabet, on le laisse tel quel
            resultat += char
    return resultat

# Déchiffrement affine (a*x + b)
def dechiffrement_affine(texte, a, b):
    """
    Déchiffre un texte en utilisant le chiffrement affine. (a*x + b)
    texte : str
    a : int
    b : int
    """
    # On calcule l'inverse de "a" modulo 26
    a_inv = 0
    for i in range(26):
        if (i * a) % 26 == 1:
            a_inv = i
            break
    # On utilise -b*a_inv au lieu de -b
    return chiffrement_affine(texte, a_inv, -b*a_inv % 26)

#----------------------------------------------#
# Chiffrement RSA

# Génération des clés RSA
def generer_cles_rsa():
    """
    Génère une paire de clés RSA.
    """
    cle_privee = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    cle_publique = cle_privee.public_key()
    return cle_privee, cle_publique

# Chiffrement RSA
def chiffrer_rsa(message, cle_publique):
    """
    Chiffre un message en utilisant le chiffrement RSA.
    message : str
    cle_publique : object
    """
    message_chiffre = cle_publique.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return message_chiffre

# Déchiffrement RSA
def dechiffrer_rsa(message_chiffre, cle_privee):
    """
    Déchiffre un message en utilisant le chiffrement RSA.
    message_chiffre : object
    cle_privee : object
    """
    message_clair = cle_privee.decrypt(
        message_chiffre,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return message_clair.decode()

#----------------------------------------------#

print("--------------------------------------------------------------------")

# Déclaration des variables avec le message et le décalage
message = str(input("\t1. Entrez un message pour le chiffrer : "))

# Vérification de la validité du décalage
while True:
    try:
        decalage = int(input("\t2. Entrez un décalage pour le chiffrement substitution : "))
        break
    except ValueError:
        print("Veuillez entrer un nombre entier pour le décalage.")

# Vérification de la validité de a et b
while True:
    try:
        a = int(input("\t3. Entrez un nombre pour le chiffrement affine : "))
        break
    except ValueError:
        print("Veuillez entrer un nombre entier pour 'a'.")

while True:
    try:
        b = int(input("\t4. Entrez un autre nombre pour le chiffrement affine : "))
        break
    except ValueError:
        print("Veuillez entrer un nombre entier pour 'b'.")


print("--------------------------------------------------------------------")

# Utilisation de la fonction chiffrement_substitution
message_chiffre = chiffrement_substitution(message, decalage)
print("\tMessage chiffré (Substitution):\t", message_chiffre)

print("--------------------------------------------------------------------")

# Utilisation de la fonction chiffrement_affine
message_chiffre_affine = chiffrement_affine(message, a, b)
print("\tMessage chiffré (Affine):\t", message_chiffre_affine)

print("--------------------------------------------------------------------")

# Utilisation de la fonction chiffrement_rsa
cle_privee, cle_publique = generer_cles_rsa()
message_chiffre_rsa = chiffrer_rsa(message, cle_publique)
print("\tClé publique (RSA):\t\t", cle_publique)
print("\tClé privée (RSA):\t\t", cle_privee)
print("\tMessage chiffré (RSA):\t", message_chiffre_rsa)

print("--------------------------------------------------------------------")

# Utilisation de la fonction dechiffrement_substitution
message_dechiffre_substitution = dechiffrement_substitution(message_chiffre, decalage)
print("\tMessage déchiffré (Substitution):\t", message_dechiffre_substitution)

# Utilisation de la fonction dechiffrement_affine
message_dechiffre_affine = dechiffrement_affine(message_chiffre_affine, a, b)
print("\tMessage déchiffré (Affine):\t\t", message_dechiffre_affine)

# Utilisation de RSA
cle_privee, cle_publique = generer_cles_rsa()
message_chiffre_rsa = chiffrer_rsa(message, cle_publique)
message_dechiffre_rsa = dechiffrer_rsa(message_chiffre_rsa, cle_privee)
print("\tMessage déchiffré (RSA):\t\t", message_dechiffre_rsa)


assert message_dechiffre_substitution == message 
assert message_dechiffre_affine == message
assert message_dechiffre_rsa == message

print("--------------------------------------------------------------------")


