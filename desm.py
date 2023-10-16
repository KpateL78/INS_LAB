from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

def des_encrypt(plaintext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_plaintext = pad(plaintext, DES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

def des_decrypt(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_data = cipher.decrypt(ciphertext)
    unpadded_data = unpad(decrypted_data, DES.block_size)
    return unpadded_data

if __name__ == "__main__":
    predefined_key = bytes.fromhex("AABBCCDDEEFF0011")

   
    plaintext = input("Enter the plaintext to encrypt: ").encode('utf-8')

    try:
        encrypted_data = des_encrypt(plaintext, predefined_key)
        decrypted_data = des_decrypt(encrypted_data, predefined_key)
       
        print("Key:", predefined_key)
        print("Encrypted data (in hexadecimal):", encrypted_data.hex())
        print("Decrypted data:", decrypted_data.decode('utf-8'))

    except Exception as e:
        print("Error:", e)
