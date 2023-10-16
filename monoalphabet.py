import random
def monoalphabetic_encrypt(plaintext, key):

    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            # Find the index of the character in the alphabet and substitute it with the key character
            index = ord(char.upper()) - 65
            ciphertext += key[index]
        else:
            ciphertext += char
    return ciphertext

def monoalphabetic_decrypt(ciphertext, key):

    plaintext = ""
    for char in ciphertext:
        if char.isalpha():

            index = key.index(char.upper())
            plaintext += chr(index + 65)
        else:
            plaintext += char
    return plaintext
plaintext = "KIRTIPATEL"
#alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#key = "".join(random.choice(alphabet) for _ in range(26))
key = "KRTYUIOPASDFGHEJLZXCVBNMWQ"

ciphertext = monoalphabetic_encrypt(plaintext, key)
print("Ciphertext:", ciphertext)

decrypted = monoalphabetic_decrypt(ciphertext, key)
print("Decrypted plaintext:", decrypted)

#print("key ="+key)
