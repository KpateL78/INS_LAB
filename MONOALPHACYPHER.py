import random

def generate_cipher_key():
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    random.shuffle(alphabet)
    return ''.join(alphabet)

def encrypt(message, key):
    encrypted_message = ''
    for char in message:
        if char.isalpha():
            char = char.upper()
            index = ord(char) - ord('A')
            encrypted_char = key[index]
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(ciphertext, key):
    decrypted_message = ''
    for char in ciphertext:
        if char.isalpha():
            char = char.upper()
            index = key.index(char)
            decrypted_char = chr(index + ord('A'))
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message
message = "smitthakor"
key = generate_cipher_key()
encrypted = encrypt(message, key)
decrypted = decrypt(encrypted, key)

print("Original message:", message)
print("Key:", key)
print("Encrypted message:", encrypted)
print("Decrypted message:", decrypted)
