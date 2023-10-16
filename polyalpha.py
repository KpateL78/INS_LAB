def vigenere_encrypt(plain_text, key):
    encrypted_text = ""
    key_index = 0

    for char in plain_text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)].lower()) - ord('a')
            encrypted_char = chr((ord(char.lower()) - ord('a') + shift) % 26 + ord('a'))
            encrypted_text += encrypted_char
            key_index += 1
        else:
            encrypted_text += char

    return encrypted_text


def vigenere_decrypt(encrypted_text, key):
    decrypted_text = ""
    key_index = 0

    for char in encrypted_text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)].lower()) - ord('a')
            decrypted_char = chr((ord(char.lower()) - ord('a') - shift) % 26 + ord('a'))
            decrypted_text += decrypted_char
            key_index += 1
        else:
            decrypted_text += char

    return decrypted_text


plain_text = "Arbaz Malek"
key = "secret"
encrypted_text = vigenere_encrypt(plain_text, key)
decrypted_text = vigenere_decrypt(encrypted_text, key)

print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)