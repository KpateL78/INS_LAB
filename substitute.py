#substitution cipher
import random
import string

def generate_substitution_key():
    alphabet = string.ascii_uppercase
    shuffled_alphabet = list(alphabet)
    random.shuffle(shuffled_alphabet)
    substitution_key = {}
    for i in range(len(alphabet)):
        substitution_key[alphabet[i]] = shuffled_alphabet[i]
    return substitution_key

def encrypt_substitution(plaintext, substitution_key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha() and char.isupper():
            ciphertext += substitution_key[char]
        else:
            ciphertext += char
    return ciphertext

def decrypt_substitution(ciphertext, substitution_key):
    decryption_key = {v: k for k, v in substitution_key.items()}
    plaintext = ""
    for char in ciphertext:
        if char.isalpha() and char.isupper():
            plaintext += decryption_key[char]
        else:
            plaintext += char
    return plaintext

substitution_key = generate_substitution_key()
plaintext = "PATELKIRTI"
ciphertext = encrypt_substitution(plaintext, substitution_key)
decrypted_text = decrypt_substitution(ciphertext, substitution_key)

print("Substitution Key:", substitution_key)
print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted Text:",decrypted_text)